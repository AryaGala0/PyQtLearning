# QMainWindow is pre-made window which provides a lot of 
# standard window features such as toolbars, menus, statusbar
# dockable widgets and more

import sys
from PyQt5 import QtWidgets, QtCore


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # remember, QMainWindow is a widget
    window = QtWidgets.QMainWindow()
    window.setWindowTitle("First QMainWindow")

    # add menu bar and menu to QMainWindow
    menu_bar = QtWidgets.QMenuBar()
    menu = menu_bar.addMenu("First Menu")
    menu.addAction("menu1")
    menu.addAction("menu2")
    window.setMenuBar(menu_bar)

    # add toolbar to QMainWindow
    toolbar = QtWidgets.QToolBar("I am toobar 1")
    toolbar.addAction("toolbar1-1")
    toolbar.addAction("toolbar1-2")
    window.addToolBar(QtCore.Qt.TopToolBarArea, toolbar)
    toolbar2 = QtWidgets.QToolBar("I am toolbar 2")
    toolbar2.addAction("toolbar2-1")
    toolbar2.addAction("toolbar2-2")
    window.addToolBar(QtCore.Qt.TopToolBarArea, toolbar2)
    window.addToolBarBreak(QtCore.Qt.TopToolBarArea)    # to change a line
    toolbar3 = QtWidgets.QToolBar("I am toolbar 3")
    toolbar3.addAction("toolbar3-1")
    toolbar3.addAction("toolbar3-2")
    window.addToolBar(QtCore.Qt.TopToolBarArea, toolbar3)

    # add dockwidget to QMainWindow
    dock_widget = QtWidgets.QDockWidget("I am a dock widget")
    dock_widget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
    dock_widget.setWidget(QtWidgets.QPushButton("click me and drag me"))
    window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock_widget)
    
    status_bar = QtWidgets.QStatusBar()
    status_bar.showMessage("I am a status bar")
    window.setStatusBar(status_bar)

    window.show()

    app.exec()