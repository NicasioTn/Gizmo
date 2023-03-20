from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QTextEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create the checkboxes
        self.number_cb = QCheckBox('Numbers')
        self.uppercase_cb = QCheckBox('Uppercase')
        self.lowercase_cb = QCheckBox('Lowercase')
        self.special_cb = QCheckBox('Special characters')

        # Create the text edit widget and connect its textChanged signal to a function
        self.text_edit = QTextEdit(self)
        self.text_edit.textChanged.connect(self.update_checkboxes)

        # Create a vertical layout and add the checkboxes and text edit to it
        vbox = QVBoxLayout()
        vbox.addWidget(self.number_cb)
        vbox.addWidget(self.uppercase_cb)
        vbox.addWidget(self.lowercase_cb)
        vbox.addWidget(self.special_cb)
        vbox.addWidget(self.text_edit)

        self.setLayout(vbox)

        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('Password Checker')
        self.show()

    def update_checkboxes(self):
        # Get the current text from the text edit widget
        text = self.text_edit.toPlainText()

        # Reset the checkbox states to unchecked
        self.number_cb.setChecked(False)
        self.uppercase_cb.setChecked(False)
        self.lowercase_cb.setChecked(False)
        self.special_cb.setChecked(False)

        # Check the characters in the text and update the checkboxes accordingly
        for char in text:
            if char.isdigit():
                self.number_cb.setChecked(True)
            elif char.isupper():
                self.uppercase_cb.setChecked(True)
            elif char.islower():
                self.lowercase_cb.setChecked(True)
            else:
                self.special_cb.setChecked(True)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec()
