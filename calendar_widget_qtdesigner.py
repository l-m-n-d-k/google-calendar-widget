from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem
from PyQt5.uic import loadUi
from PyQt5 import QtCore
from google_api_calendar import GoogleCalendar
import sys


class CalendarWindow(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("calendar.ui", self)
        self.setFixedSize(840, 460)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)

    def calendarDateChanged(self):
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        event_list = google_calendar.get_event_by_date(
            calendar_id, 
            str(dateSelected)
        )
        events = []
        
        for event in event_list:
            events.append(event["summary"])

        self.updateEventList(events)

    def updateEventList(self, events):
        self.eventList.clear()
        for event in events:
            item = QListWidgetItem(event)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.eventList.addItem(item)


if __name__ == "__main__":
    calendar_id = "dima2642007@gmail.com"
    google_calendar = GoogleCalendar()
    google_calendar.add_calendar(calendar_id)
    app = QApplication(sys.argv)
    ex = CalendarWindow()
    ex.show()
    sys.exit(app.exec_())