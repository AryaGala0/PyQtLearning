import sys
from PyQt5 import QtWidgets


class Window_2(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window 2")
        self.setGeometry(100, 100, 300, 200)
        self.label = QtWidgets.QLabel("This is Window 2", self)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


class Window_1(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window 1")
        self.setGeometry(100, 100, 400, 300)
        self.button = QtWidgets.QPushButton("Open Window 2")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.toggle_window_2)
        self.setCentralWidget(self.button)
        self.window_2 = None

    def toggle_window_2(self):
        if self.window_2 is None:
            self.window_2 = Window_2()
            self.window_2.show()
        else:
            self.window_2.close()
            self.window_2 = None


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window_1 = Window_1()
    window_1.show()
    sys.exit(app.exec_())
