from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QCheckBox
from math import log2

class PasswordEvaluator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create the widgets
        self.password_label = QLabel('Password:')
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.number_cb = QCheckBox('Numbers')
        self.uppercase_cb = QCheckBox('Uppercase')
        self.lowercase_cb = QCheckBox('Lowercase')
        self.special_cb = QCheckBox('Special characters')
        self.warning_label = QLabel()
        self.entropy_label = QLabel()

        # Connect the textChanged signal of the password edit widget to the update function
        self.password_edit.textChanged.connect(self.update)

        # Create a vertical layout and add the widgets to it
        vbox = QVBoxLayout()
        vbox.addWidget(self.password_label)
        vbox.addWidget(self.password_edit)
        vbox.addWidget(self.number_cb)
        vbox.addWidget(self.uppercase_cb)
        vbox.addWidget(self.lowercase_cb)
        vbox.addWidget(self.special_cb)
        vbox.addWidget(self.warning_label)
        vbox.addWidget(self.entropy_label)

        self.setLayout(vbox)

        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('Password Evaluator')
        self.show()

    def update(self):
        # Get the current password from the password edit widget
        password = self.password_edit.text()

        # Reset the checkbox states to unchecked
        self.number_cb.setChecked(False)
        self.uppercase_cb.setChecked(False)
        self.lowercase_cb.setChecked(False)
        self.special_cb.setChecked(False)

        # Check the characters in the password and update the checkboxes accordingly
        for char in password:
            if char.isdigit():
                self.number_cb.setChecked(True)
            elif char.isupper():
                self.uppercase_cb.setChecked(True)
            elif char.islower():
                self.lowercase_cb.setChecked(True)
            else:
                self.special_cb.setChecked(True)

        # Calculate the entropy of the password
        entropy = self.calculate_entropy(password)
        self.entropy_label.setText(f'Entropy: {entropy:.2f} bits')

        # Check if the password meets the length and complexity requirements and display a warning if it doesn't
        length = len(password)
        if length < 8:
            self.warning_label.setText('Password length should be at least 8 characters')
        elif not (self.number_cb.isChecked() and self.uppercase_cb.isChecked() and self.lowercase_cb.isChecked() and self.special_cb.isChecked()):
            self.warning_label.setText('Password should contain at least one of each: Number, Uppercase, Lowercase, Special Character')
        else:
            self.warning_label.setText('')

    def calculate_entropy(self, password):
        # Get the number of possible characters in the password
        if password == '':
            return 0
        possible_characters = 0
        if self.number_cb.isChecked():
            possible_characters += 10
        if self.uppercase_cb.isChecked():
            possible_characters += 26
        if self.lowercase_cb.isChecked():
            possible_characters += 26
        if self.special_cb.isChecked():
            possible_characters += 32
        # Calculate the entropy using the formula log2(possible_characters^password_length)
        return log2(possible_characters) * len(password)
    
if __name__ == '__main__':
    app = QApplication([])
    evaluator = PasswordEvaluator()
    app.exec()
