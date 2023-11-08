from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi
import sys

class CalendarWindow(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('calendar.ui', self)
        self.setFixedSize(840, 400)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)

    def calendarDateChanged(self):
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        print('Date selected:', dateSelected)
        return dateSelected

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = CalendarWindow()
    ex.show()
    sys.exit(app.exec())
