# every interaction the user do with Qt application is an event.
# Qt represents the events using event objects which package up
# information about what happened. Events will be passed to a
# specific event handlers on the widget where the interaction occured.
# e.g.clicking on a widget will cause QMouseEvent to be sent to
# widget.mousePressEvent event handler. event objects contain information
# such as  what triggered the event and where specifically it occurred.

from PyQt5 import QtWidgets, QtCore

import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        self.label = QtWidgets.QLabel()
        self.button = CustomButton()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setCentralWidget(widget)

    # mouse event
    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            press_pos_point = e.globalPos()
            press_pos_x = e.globalX()
            press_pos_y = e.globalY()
            self.label.setText(f"mousePressEvent with left button at ({press_pos_x},{press_pos_y})")
        else:
            self.label.setText("mousePressEvent with right button")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")
    
    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    # context menu event when right click button
    def contextMenuEvent(self, event):
        menu = QtWidgets.QMenu()
        menu.addAction("context action 1")
        menu.addAction("context action 2")
        menu.exec(event.globalPos())


class CustomButton(QtWidgets.QPushButton):
    def __init__(self):
        super().__init__()
    
    def mousePressEvent(self, e):
        # if you want the widget to own event handlers, you can choose
        # to mark an event as handler calling .accept().if you .ignore() it,
        # the event handler will be pass to its parent widget
        if e.button() == QtCore.Qt.LeftButton:
            e.ignore()
            print("left press on the button")
        else:
            e.accept()
            print("right press on the button")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()


# reference:
# https://www.pythonguis.com/tutorials/pyqt-signals-slots-events/