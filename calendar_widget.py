import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QHBoxLayout, QVBoxLayout, QLabel


class TableManager(QWidget):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.setFixedSize(400, 300)
        self.initUI()

    def initUI(self):
        self.calendar_widget = QCalendarWidget(self)
        main_layout = QHBoxLayout(self)
        left_sidebar_layout = QVBoxLayout()
        main_layout.addLayout(left_sidebar_layout)
        left_sidebar_layout.addWidget(QLabel("Календарь"))
        left_sidebar_layout.addWidget(self.calendar_widget)
        self.calendar_widget.clicked.connect(self.show_day)

    def show_day(self):
        self.model.select()
        self.query.exec(f"""SELECT * FROM {self.user} WHERE 
        calendar_date = '{self.calendar_widget.selectedDate().toString("yyyy-MM-dd")}'
        ORDER BY dateline ASC, deadline ASC""")
        self.model.setQuery(self.query)
        self.task_tableview.resizeColumnsToContents()
        self.task_tableview.resizeRowsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TableManager("user")
    ex.show()
    sys.exit(app.exec_())