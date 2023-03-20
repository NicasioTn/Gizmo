import sys
import os
import math
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QLabel
    
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon


class Window(QWidget):
    # properties
    hide = True
    maskEye = "🔒"
    result = "-- Bits"
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Evaluation")
        self.resize(250, 250)
        
        # Create an outer layout
        outerLayout = QVBoxLayout()
        # Create a form layout for the label and line edit
        
        self.label = QLabel("TYPE A PASSWORD", self)
        outerLayout.addWidget(self.label, alignment= Qt.AlignmentFlag.AlignCenter)
        # Input
        self.input = QLineEdit()
        self.input.setFixedWidth(150)
        outerLayout.addWidget(self.input, alignment= Qt.AlignmentFlag.AlignCenter)
        
        # Eye Icon
        self.label_eye = QLabel(self.maskEye, self)
        outerLayout.addWidget(self.label_eye, alignment= Qt.AlignmentFlag.AlignCenter)
        
        # show Bits
        self.label_result = QLabel(self.result, self)
        outerLayout.addWidget(self.label_result, alignment= Qt.AlignmentFlag.AlignCenter)
        
        # Hide Input
        self.input.setEchoMode(QLineEdit.EchoMode.Password)
        
        # Component Button
        button1 = QPushButton("Get Text")
        button1.clicked.connect(self.get)
        
        button2 = QPushButton("Show Password")
        button2.clicked.connect(self.showPasswd)
    
        button3 = QPushButton("Clear Text")
        # clear input
        button3.clicked.connect(self.input.clear)
        button3.clicked.connect(self.clearCheckBox) # clear checkbox
        
        outerLayout.addWidget(button1)
        outerLayout.addWidget(button2)
        outerLayout.addWidget(button3)
        
        
        self.check1 = QCheckBox("Number")
        self.check2 = QCheckBox("Alphabet")
        self.check3 = QCheckBox("Special Character")
        self.check4 = QCheckBox("UpperCase")
        self.check5 = QCheckBox("LowerCase")
        
        outerLayout.addWidget(self.check1)
        outerLayout.addWidget(self.check2)
        outerLayout.addWidget(self.check3)
        outerLayout.addWidget(self.check4)
        outerLayout.addWidget(self.check5)
        
        
        '''
        topLayout = QFormLayout()
        # Add a label and a line edit to the form layout
        topLayout.addRow("Enter Password:", QLineEdit())
        # Create a layout for the checkboxes
        optionsLayout = QVBoxLayout()
        # Add some checkboxes to the layout
        optionsLayout.addWidget(QCheckBox("Option one"))
        optionsLayout.addWidget(QCheckBox("Option two"))
        optionsLayout.addWidget(QCheckBox("Option three"))
        # Nest the inner layouts into the outer layout
        outerLayout.addLayout(topLayout)
        outerLayout.addLayout(optionsLayout)
        '''
        
        # Set the window's main layout
        self.setLayout(outerLayout)
        self.check1.clicked.connect(self.print1)
        self.fistStart()
    
    # Show Os Username
    def fistStart(self):
        print(f"Hello, {os.getlogin()}")
    
    # Print State of Checkbox
    def print1(self):
        print(self.check1.checkState())
    
    # Get Password
    def get(self):
        text = self.input.text()
        # Check if text is empty
        if text == "":
            print("No Input !!")
            self.clearCheckBox()
        # Check if text is not empty
        else:
            print(f"Your Input: {text} ") # Show Input Password
            
            if len(text) < 8:
                print("Password is too short")
                
            elif text.isalpha() and len(text) >= 8 and not text.isupper():
                print("Password is all alphabets Not Uppercase")
                self.checkBox(alphabet = True)

            elif text.isalnum() and len(text) >= 8:
                print("Password is all numbers")
                self.checkBox(number = True)
            
            # Not complete yet!
            elif len(text) >= 8 and text.isupper() and text.islower() and text.isdigit() and text.isalpha():
                print("Password is Strong")
                self.checkBox(number = True, alphabet = True, special = True)
                
            # Prepare for Entropy Calculation
            length = len(text)
            print(length)
            list_of_type = self.type_cutting(length, text)
            print(list_of_type)
            self.entropy(length, list_of_type)
            self.label_result.setText(self.result)
        
    
    
    #Sub Process of Entropy Calculation
    def type_cutting(self, length, text):
        
        limit_of_Digits = 0
        limit_of_lower_case = 0
        limit_of_Upper_case = 0
        limit_of_Special = 0
        
        list_of_type = []
        # Check Type
        Passwd_cutting = list(text)
        print(Passwd_cutting)
        for i in Passwd_cutting:
            if i.isdigit():
                print("Number")
                self.checkBox(number = True)
                if limit_of_Digits  == 0:
                    list_of_type.append("Digits")
                    limit_of_Digits = 1
                
                
            elif i.isalpha() and i.islower():
                print("Alphabet")
                self.checkBox(alphabet = True)
                self.checkBox(Lower_case = True)
                if limit_of_lower_case == 0:
                    list_of_type.append("Lower_case")
                    limit_of_lower_case = 1
                
                
            elif i.isalpha() and i.isupper():
                print("Uppercase") 
                self.checkBox(Upper_case = True)
                if limit_of_Upper_case == 0:
                    list_of_type.append("Upper_case")
                    limit_of_Upper_case = 1
                
            else:
                print("Special")
                self.checkBox(special = True)
                if limit_of_Special == 0:
                    list_of_type.append("Special_symbols_US")
                    limit_of_Special = 1
                
        return list_of_type

    
    #Entropy Calculation   
    def entropy(self, length, list_of_type):
        pool_char = {
            "Digits": 10,
            "Lower_case": 26,
            "Upper_case": 26,
            "Special_symbols_US": 32,
        }
        total_chars = sum(pool_char.get(t, 0) for t in list_of_type)
        if total_chars == 0:
            self.result = "Password contains no characters"
        else:
            bits = length * math.log(total_chars, 2)
            self.result = f"~{int(bits)} Bits"
     
    # def entropy(self, length, list_of_type):
        
    #     base = 2
    #     value_of_type = 0
    #     Digits = 10 # 0-9
    #     Lower_case = 26 # a-z
    #     Upper_case = 26 # A-Z
    #     Latin_letter = 52 # a-z + A-Z
    #     Alphanumeric = 62 # 0-9 + a-z + A-Z
    #     Special_symbols_US = 32 #`~!@#$%^&*()-=_+[{]}\|;:'",<.>/?
        
    #     # check type for calculate entropy
    #     for i in list_of_type:
    #         if i == "Digits":
    #             value_of_type += Digits
    #         elif i == "Lower_case":
    #             value_of_type += Lower_case
    #         elif i == "Upper_case":
    #             value_of_type += Upper_case
    #         elif i == "Special_symbols_US":
    #             value_of_type += Special_symbols_US
    #         else : 
    #             pass
            
    #         # if i == "Digits" and i == "Lower_case" and i == "Upper_case": # 0-9 + a-z + A-Z
    #         #     value_of_type = Alphanumeric
    #         # elif i == "Digits" and i == "Lower_case": # 0-9 + a-z
    #         #     value_of_type = Alphanumeric - Upper_case
    #         # elif i == "Digits" and i == "Upper_case": # 0-9 + A-Z
    #         #     value_of_type = Alphanumeric - Lower_case
    #         # elif i == "Lower_case" and i == "Upper_case": # a-z + A-Z
    #         #     value_of_type = Latin_letter
    #         # elif i == "Digits": # 0-9
    #         #     value_of_type = Digits
    #         # elif i == "Special_symbols_US": # `~!@#$%^&*()-=_+[{]}\|;:'",<.>/?
    #         #     value_of_type = Special_symbols_US
    #         # elif i == "Lower_case":
    #         #     value_of_type = 0
        
    #     print(value_of_type)
    #     E = str(length * math.log(value_of_type, base)).split(".") # toString for get only 1 index of list
    #     self.result = (f"~{E[0]} Bits")
    
    # Show Password
    def showPasswd(self):
        if self.hide:
            self.input.setEchoMode(QLineEdit.EchoMode.Normal)
            self.hide = False
            self.label_eye.setText("👁️")
        else:
            self.input.setEchoMode(QLineEdit.EchoMode.Password)
            self.hide = True
            self.label_eye.setText("🔒")
    
    # Check Box
    def checkBox(self, number = False, alphabet = False, special = False, Upper_case = False, Lower_case = False):
        
        if number:
            self.check1.setChecked(True)
        elif alphabet:
            self.check2.setChecked(True)
        elif special:
            self.check3.setChecked(True)
        elif Upper_case:
            self.check4.setChecked(True)
        elif Lower_case:
            self.check5.setChecked(True)
        else:
            print("No Input")
            self.check1.setChecked(False)
            self.check2.setChecked(False)
            self.check3.setChecked(False)
            self.check4.setChecked(False)
            self.check5.setChecked(False)
            
    def clearCheckBox(self):
        # Clear Check Box
        self.check1.setChecked(False)
        self.check2.setChecked(False)
        self.check3.setChecked(False)
        self.check4.setChecked(False)
        self.check5.setChecked(False)
        self.label_result.setText("-- Bits")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # set icon app
    app.setWindowIcon(QIcon("./Files/icon.png"));
    window = Window()
    window.show()
    sys.exit(app.exec())