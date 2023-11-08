from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
        QHBoxLayout, QPushButton, QRadioButton, QTextEdit, QVBoxLayout,
        QWidget, QLabel)


class PreviewWindow(QWidget):
    def __init__(self, parent=None):
        super(PreviewWindow, self).__init__(parent)

        self.setWindowFlags(
            Qt.Window                      
            | Qt.WindowStaysOnBottomHint     # <<<=====<
            | Qt.CustomizeWindowHint         # Отключает подсказки заголовка окна по умолчанию.
            | Qt.WindowTitleHint             # Придает окну строку заголовка.
        )

        self.textEdit = QTextEdit()
        self.textEdit.setReadOnly(True)
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)
        text = '''
        Qt.Window
        | Qt.WindowStaysOnBottomHint         <<<=======<
        | Qt.CustomizeWindowHint
        | Qt.WindowTitleHint
        '''
        self.textEdit.setPlainText(text)

        closeButton = QPushButton("&Close")
        closeButton.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Приложение, которое можно свернуть в трей"))
        layout.addWidget(self.textEdit)
        layout.addWidget(closeButton)
        self.setLayout(layout)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = PreviewWindow()
    w.setWindowTitle("Preview - Qt.WindowStaysOnBottomHint")
    w.setGeometry(900, 100, 350, 200) 
    w.show()
    sys.exit(app.exec_())