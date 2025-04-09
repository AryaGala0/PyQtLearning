# Signals are notifications emitted by widgets when something happens,
# such as pressing a button or the text changed,slots is the name Qt
# uses for the receivers of signals, if the signal sends data then the 
# receiving function will receive the data with same type.

from PyQt5 import QtWidgets
import sys
import random


class MainWindow(QtWidgets.QMainWindow):
    window_title = [
        "title 1",
        "title 2",
        "title 3",
        "title 4"
    ]
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signal and Slot Win")
        # signal directly recieved by a build-in slot
        self.label = QtWidgets.QLabel()
        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.textChanged.connect(self.label.setText)
        # signal recieved by a custum slot(function)
        self.button = QtWidgets.QPushButton("press me to change title")
        self.button.clicked.connect(self.change_title)
        # data transfer by signal, and connect one signal with multiple slots
        self.button.setCheckable(True)
        self.button.clicked.connect(self.print_status)

        self.widget = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout(self.widget)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.button)

        self.setCentralWidget(self.widget)

    def change_title(self):
        title = random.choice(self.window_title)
        self.setWindowTitle(title)
    
    def print_status(self, check):
        print(f"button status is {check}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()
        

# Reference:
# https://www.pythonguis.com/tutorials/pyqt-signals-slots-events/

