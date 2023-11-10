from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem
from PyQt5.uic import loadUi
from PyQt5 import QtCore
import sys

class CalendarWindow(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('calendar.ui', self)
        self.setFixedSize(840, 460)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.updateEventList()

    def calendarDateChanged(self):
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        return dateSelected

    def updateEventList(self, events=["Write email", 'LMS']):
        for event in events:
            item = QListWidgetItem(event)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.eventList.addItem(item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = CalendarWindow()
    ex.show()
    sys.exit(app.exec_())