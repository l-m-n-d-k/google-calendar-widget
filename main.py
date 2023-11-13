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
        self.saveButton.clicked.connect(self.saveChanges)
        self.addButton.clicked.connect(self.addNewEvente)
        

    def centerWidget(self):
        screenGeometry = QDesktopWidget().availableGeometry()
        widgetGeometry = self.frameGeometry()
        widgetGeometry.moveCenter(screenGeometry.center())
        self.move(widgetGeometry.topLeft())

    def calendarDateChanged(self):
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        event_list = google_calendar.get_event_by_date(
            calendar_id, str(dateSelected))
        events = []
        for event in event_list:
            events.append(event["summary"])
        self.updateEventList(events)
        return str(dateSelected)

    def updateEventList(self, events):
        self.eventList.clear()
        for event in events:
            item = QListWidgetItem(event)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.eventList.addItem(item)

    def saveChanges(self):
        for i in range(self.eventList.count()):
            item = self.eventList.item(i)
            task = str(item.text())
            if item.checkState() == QtCore.Qt.Checked:
                google_calendar.delete_evente(calendar_id, task)

        self.calendarDateChanged()

        massageBox = QMessageBox()
        massageBox.setText("Выполненые задачи удалены")
        massageBox.setStandardButtons(QMessageBox.Ok)
        massageBox.exec()

    def addNewEvente(self):
        newTask = str(self.eventLine.text())
        date = self.calendarDateChanged()
        google_calendar.add_event(
            calendar_id, newTask, None, None, date, date)

        self.calendarDateChanged()


if __name__ == "__main__":
    calendar_id = "dima2642007@gmail.com"
    google_calendar = GoogleCalendar()
    google_calendar.add_calendar(calendar_id)

    app = QApplication(sys.argv)
    ex = CalendarWindow()
    # ex.setWindowFlags(ex.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
    ex.show()
    sys.exit(app.exec_())
