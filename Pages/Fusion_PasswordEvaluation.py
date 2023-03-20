import sys
import os
from math import log2
from PyQt6.QtWidgets import ( QApplication, QLineEdit,  QWidget, QLabel, QDialog, )
from PyQt6.QtCore import Qt
from math import log2
from PyQt6.QtGui import QIcon
from PyQt6.uic import loadUi
from PyQt6.QtGui import QPixmap

class PasswordEvaluation(QDialog):
    
    # Initialize the properties of the class
    hide = True
    
    number = False
    lower = False
    upper = False
    symbol = False
    shift = False
    
    
    passwd_2021 = [
        "password",
        "123456",
        "qwerty",
        "123456789",
        "admin",
        "letmein",
        "welcome",
        "monkey",
        "dragon",
        "football",
        "iloveyou",
        "abc123",
        "admin123",
        "password123",
        "1234567890",
        "qwertyuiop",
        "123123",
        "superman",
        "batman",
        "trustno1",
        "1234567",
        "12345678",
        "12345",
        "111111",
        "login",
        "starwars",
        "letmein"
        "zaq1zaq1"
    ]
    

    def __init__(self):
        super(PasswordEvaluation, self).__init__()
        loadUi("./Files/Password_Evaluation.ui", self)
        self.setWindowTitle("Password Evaluation")
        
        # Icons Init
        self.warning_icon = QIcon("./Images/warning.png")
        self.check_icon = QIcon("./Images/Checked.png")
        self.hide_icon = QIcon("./Images/hide.png")
        self.unhid_icon = QIcon("./Images/unhide.png")
        self.logo = QPixmap("./Images/logo.png")
        
        self.logo_Label.setPixmap(self.logo)
        # Hide Input
        self.show_Button.setIcon(self.hide_icon)
        
        self.show_Button.setStyleSheet("background-color: transparent; border: none;")
        self.input_Text.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_Text.setMaxLength(100)
        self.show_Button.clicked.connect(self.showPasswd)
        # redirec to update input
        self.input_Text.textChanged.connect(self.update)
        
        
        
        # Initial hide checkboxes
        self.length8_check.setIcon(self.warning_icon)
        self.number_check.setIcon(self.warning_icon)
        self.upper_check.setIcon(self.warning_icon)
        self.lower_check.setIcon(self.warning_icon)
        self.symbol_check.setIcon(self.warning_icon)
       
        
    def showPasswd(self):
        if self.hide:
            self.input_Text.setEchoMode(QLineEdit.EchoMode.Normal)
            self.hide = False
            self.show_Button.setIcon(self.unhid_icon)
        else:
            self.input_Text.setEchoMode(QLineEdit.EchoMode.Password)
            self.hide = True
            self.show_Button.setIcon(self.hide_icon)
        
    def update(self):
        # Get the current password from the password edit widget
        password = self.input_Text.text()

        # Reset the checkbox states to unchecked
        self.length8_check.setChecked(False)
        self.number_check.setChecked(False)
        self.upper_check.setChecked(False)
        self.lower_check.setChecked(False)
        self.symbol_check.setChecked(False)
        

        # Find the password in the list of weak passwords
        
            
        if password == '':
            self.entropy_Label.setText('')
            self.warning_Start.setText('Start typing to see the entropy score')
            self.quality_Label.setText('')
        else:
            if password in self.passwd_2021:
                self.warning_Start.setText('Found in the top 10 million passwords! "2021" ')
            else:
                self.warning_Start.setText('Not found in the list')
        
        
        for char in password:
            if char.isdigit():
                self.number_check.setChecked(True)
                self.number_check.setIcon(self.check_icon)
            elif char.isupper():
                self.upper_check.setChecked(True)
                self.upper_check.setIcon(self.check_icon)
            elif char.islower():
                self.lower_check.setChecked(True)
                self.lower_check.setIcon(self.check_icon)
            else:
                self.symbol_check.setChecked(True)
                self.symbol_check.setIcon(self.check_icon)
                
            if len(self.input_Text.text()) >= 8:
                self.length8_check.setChecked(True)
                self.length8_check.setIcon(self.check_icon)
        
        # Calculate the entropy of the password
        entropy = self.calculate_entropy(password)
        if entropy == 0:
            self.entropy_Label.setText(f'-- Bits')
            self.quality_Label.setText('')
        elif entropy > 999:
            self.entropy_Label.setText(f'~NaN Bits')
        else:
            self.entropy_Label.setText(f'~{entropy:.0f} Bits')

        # Check if the password meets the length and complexity requirements and display a warning if it doesn't
        length = len(password)        
        if length < 8:
            self.quality_Label.setText('So very, very bad')
            if length == 0:
                self.quality_Label.setText('')
        else : 
            if entropy < 35 :
                self.quality_Label.setText('Not good enough')
            elif entropy < 50 :
                self.quality_Label.setText('You could do better')
            elif entropy < 75:
                self.quality_Label.setText('That\'ll do nicely!')
            elif entropy < 100:
                self.quality_Label.setText('You\'re a genius! ')
            else:
                self.quality_Label.setText('Good luck cracking that, H4x0r')
        
        # Update the input length label
        self.charLength8_Label.setText(f'{length} Chars')
        
        
    def calculate_entropy(self, password):
        # Get the number of possible characters in the password
        if password == '':
            self.length8_check.setIcon(self.warning_icon)
            self.number_check.setIcon(self.warning_icon)
            self.upper_check.setIcon(self.warning_icon)
            self.lower_check.setIcon(self.warning_icon)
            self.symbol_check.setIcon(self.warning_icon)
            return 0
        
        possible_characters = 0
        if self.number_check.isChecked(): # 0-9
            possible_characters += 10
        if self.upper_check.isChecked(): # A-Z
            possible_characters += 26
        if self.lower_check.isChecked(): # a-z
            possible_characters += 26
        if self.symbol_check.isChecked(): # !@#$%^&*()_+-=
            possible_characters += 32
        # Calculate the entropy using the formula log2(possible_characters^password_length)
        self.total_Label.setText(f'Total {possible_characters} Chars')
        return log2(possible_characters) * len(password)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordEvaluation()
    window.setFixedHeight(700)
    window.setFixedWidth(1200)
    window.show()
    sys.exit(app.exec())     
    