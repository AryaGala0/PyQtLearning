from PyQt5 import QtWidgets
import sys


class Main_Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.create_dialog()
        self.call_message_dialog()
    
    def create_dialog(self):
        """create a custom dialog using QDialogButtonBox
        """
        custom_dialog = Custom_Dialog(self)
        custom_dialog.exec()

    def call_message_dialog(self):
        """This function show how we can use QMessageBox
        to show a message with 3 buttons: Ok, Cancel and Ignore.
        """
        msg_box = QtWidgets.QMessageBox.critical(
            self,
            "Message Dialog",
            "This is a message dialog.",
            buttons=QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Ignore,
            defaultButton=QtWidgets.QMessageBox.Ok
        )
        if msg_box == QtWidgets.QMessageBox.accept:
            print("accept")
        else:
            print("cancel")


class Custom_Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Custom Dialog")
        # can use stardard QButton, but this below ensures that the dialog
        # respects the host desktop's standard,e.g. OK button on the
        # right or left. Messing the button style can be annoying to users
        dialog_btn = QtWidgets.QDialogButtonBox.Ok |QtWidgets.QDialogButtonBox.Ignore|QtWidgets.QDialogButtonBox.Cancel
        button_box = QtWidgets.QDialogButtonBox(dialog_btn)

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QtWidgets.QVBoxLayout()
        message = QtWidgets.QLabel("This is a custom dialog.")
        layout.addWidget(message)
        layout.addWidget(button_box)
        self.setLayout(layout)

    def accept(self):
        print("accept")

    def reject(self):
        print("reject")
        super().reject()

if __name__ == "__main__":
    # run a window with a dialog box and a messge box
    app = QtWidgets.QApplication(sys.argv)
    main_window = Main_Window()
    main_window.show()
    app.exec()