from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calendar(object):
    def setupUi(self, Calendar):
        Calendar.setObjectName("Calendar")
        Calendar.setEnabled(True)
        Calendar.setGeometry(QtCore.QRect(0, 0, 831, 456))
        Calendar.setWindowTitle("Calendar")
        Calendar.setWindowIcon(QtGui.QIcon("google_calendar_new_logo_icon_159141.ico"))

        self.calendarWidget = QtWidgets.QCalendarWidget(Calendar)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 10, 421, 311))
        self.calendarWidget.setStyleSheet("font:12pt;")

        self.eventList = QtWidgets.QListWidget(Calendar)
        self.eventList.setGeometry(QtCore.QRect(450, 10, 361, 401))
        self.eventList.setStyleSheet("font:12pt;")

        self.saveButton = QtWidgets.QPushButton(Calendar)
        self.saveButton.setGeometry(QtCore.QRect(450, 420, 361, 28))
        self.saveButton.setStyleSheet(
            "border-radius:10px; background-color: #01BFFF; color:white; font:11pt;"
        )
        self.saveButton.setText("Удалить выполненное")

        self.addButton = QtWidgets.QPushButton(Calendar)
        self.addButton.setGeometry(QtCore.QRect(20, 420, 421, 28))
        self.addButton.setStyleSheet(
            "border-radius:10px; background-color: #01BFFF; color:white; font:11pt;"
        )
        self.addButton.setText("Добавить событие")

        self.eventLine = QtWidgets.QLineEdit(Calendar)
        self.eventLine.setGeometry(QtCore.QRect(20, 350, 421, 31))
        self.eventLine.setStyleSheet("font:12pt;")

        self.label = QtWidgets.QLabel(Calendar)
        self.label.setGeometry(QtCore.QRect(30, 330, 121, 16))
        self.label.setText("Введите событие:")

        self.timeEdit = QtWidgets.QTimeEdit(Calendar)
        self.timeEdit.setGeometry(QtCore.QRect(100, 390, 118, 22))

        self.label_2 = QtWidgets.QLabel(Calendar)
        self.label_2.setGeometry(QtCore.QRect(30, 390, 47, 13))
        self.label_2.setText("Начало:")

        self.label_3 = QtWidgets.QLabel(Calendar)
        self.label_3.setGeometry(QtCore.QRect(260, 390, 47, 13))
        self.label_3.setText("Конец:")

        self.timeEdit_2 = QtWidgets.QTimeEdit(Calendar)
        self.timeEdit_2.setGeometry(QtCore.QRect(320, 390, 121, 22))

        self.retranslateUi(Calendar)
        QtCore.QMetaObject.connectSlotsByName(Calendar)

    def retranslateUi(self, Calendar):
        _translate = QtCore.QCoreApplication.translate
        self.saveButton.setText(_translate("Calendar", "Удалить выполненные"))
        self.addButton.setText(_translate("Calendar", "Добавить событие"))
        self.label.setText(_translate("Calendar", "Введите событие:"))
        self.label_2.setText(_translate("Calendar", "Начало:"))
        self.label_3.setText(_translate("Calendar", "Конец:"))
