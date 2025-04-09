import sys
from PyQt5.QtWidgets import QApplication, QPushButton

if __name__ == "__main__":
    # can use app=QApplication([]) if there're no input args from cmd line
    # need one and only one QApplication instance per application
    # QApplication object holds the event loop of your application
    # the event loop will governs all user interaction with the GUI
    # every interaction generate an event, and these events will
    # be placed on the event queue and waiting for being checked
    # on each iteration of event loop.In every iteration, there're a
    # specific handler to deal with the event,and when it's finished,
    # it will go to the next event.
    app = QApplication(sys.argv)        
    # in Qt, all top level widget are windows, so you can just create a widget
    # without creating a QMainwindow, and by defualt it's hidden, so
    # we need to use show method to show it
    button = QPushButton("click me")
    button.show()
    # start the event loop
    app.exec()


# Reference:
# https://www.pythonguis.com/tutorials/creating-your-first-pyqt-window/