from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QListWidgetItem,
    QDesktopWidget,
    QMessageBox,
)
from PyQt5 import QtCore
from google_api_calendar import GoogleCalendar
from calendar_widget import Ui_Calendar
import sys


class CalendarWindow(QWidget, Ui_Calendar):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(840, 460)
        self.centerWidget()

        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
        self.saveButton.clicked.connect(self.deleteEvents)
        self.addButton.clicked.connect(self.addNewEvente)

    def centerWidget(self):
        screenGeometry = QDesktopWidget().availableGeometry()
        widgetGeometry = self.frameGeometry()
        widgetGeometry.moveCenter(screenGeometry.center())
        self.move(widgetGeometry.topLeft())

    # Смена выбранной в календаре даты
    def calendarDateChanged(self):
        self.dateSelected = self.calendarWidget.selectedDate().toPyDate()
        self.updateEventList()

    # Обновление списка календарей
    def updateEventList(self):
        # Обращение к функции, которая возвращает список дел на выбранную дату (находится в другом файле)
        event_list = google_calendar.get_event_by_date(
            calendar_id, str(self.dateSelected)
        )
        self.eventList.clear()
        events = []
        # Поиск нужных нам данных из предоставленного списка (нам нужно название и дата, если токавая имеется)
        for event in event_list:
            append_ = ""
            for key, value in event.items():
                if key == "summary":
                    append_ += value
                    append_ += ": "
                elif key == "start":
                    try:
                        start = value["dateTime"]
                    except KeyError as value:
                        start = ""
                    append_ += start[11:16]
                elif key == "end":
                    try:
                        end = value["dateTime"]
                    except KeyError as value:
                        end = ""
                    append_ += " - "
                    append_ += end[11:16]
            events.append(append_)

        # Добавление всех найденных событий в виджет
        for event in events:
            item = QListWidgetItem(event)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.eventList.addItem(item)

    # Удаление событий
    def deleteEvents(self):
        for i in range(self.eventList.count()):
            item = self.eventList.item(i)

            # Отсечка ненужной мнформации, остается только название
            for i in str(item.text()):
                if i == ":":
                    task = str(item.text())[: str(item.text()).index(i)]
                    break
            # Если событие отмечено, то вызвать функцию удаления
            if item.checkState() == QtCore.Qt.Checked:
                google_calendar.delete_event(calendar_id, task, str(self.dateSelected))

        self.updateEventList()

        # Сообщение об удалении события
        messageBox = QMessageBox()
        messageBox.setText("Выполненные события удалены")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

    # Создание нового события
    def addNewEvente(self):
        # Считывание текста из строки вводы. Это будет название собвтия
        newTask = str(self.eventLine.text())
        date = str(self.dateSelected)

        # На случай, если нам нужно событие на весь день
        if "/allday" in newTask:
            self.updateEventList()
            google_calendar.add_event(calendar_id, newTask, date)

        # СОздание события с указанием времени начала и конца
        else:
            self.updateEventList()
            time_start = self.timeEdit.time()
            hour_start = time_start.hour()
            minute_start = time_start.minute()
            second_start = time_start.second()

            time_end = self.timeEdit_2.time()
            hour_end = time_end.hour()
            minute_end = time_end.minute()
            second_end = time_end.second()

            # Перевод даты и времени в нужный для google api calendar формат
            start_time = (
                date
                + "T"
                + "{:02d}:{:02d}:{:02d}".format(hour_start, minute_start, second_start)
            )
            end_time = (
                date
                + "T"
                + "{:02d}:{:02d}:{:02d}".format(hour_end, minute_end, second_end)
            )
            google_calendar.add_event_with_time(
                calendar_id, newTask, start_time, end_time
            )

        # Сообщение о создании события
        messageBox = QMessageBox()
        messageBox.setText(f"Событие добавлено")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

        self.updateEventList()


if __name__ == "__main__":
    calendar_id = "dima2642007@gmail.com"
    google_calendar = GoogleCalendar()
    google_calendar.add_calendar(calendar_id)

    app = QApplication(sys.argv)
    ex = CalendarWindow()
    ex.show()
    sys.exit(app.exec_())
