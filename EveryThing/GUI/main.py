
import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QWidget, QDialog
from PyQt6 import QtWidgets, uic



class HomeScreen(QDialog):
    def __init__(self):
        super(HomeScreen, self).__init__()
        loadUi("HomeScreen.ui", self)
        self.Start_Button.clicked.connect(self.gotomenu)

    def gotomenu(self):
        Start_Button = menu()
        widget.addWidget(Start_Button)
        widget.setCurrentIndex(widget.currentIndex()+1)

    
        
class menu(QDialog):
    def __init__(self):
        super(menu, self).__init__()
        loadUi("menu.ui", self)
        self.advance_Button.clicked.connect(self.gotoadvancemenu)
        self.network_Button.clicked.connect(self.gotonetworkmenu)
      

    def gotoadvancemenu(self):
        advance_Button = advancemenuScreen()
        widget.addWidget(advance_Button)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotonetworkmenu(self):
        network_Button = networkmenuScreen()
        widget.addWidget(network_Button)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    
class advancemenuScreen(QDialog):
    def __init__(self):
        super(advancemenuScreen, self).__init__()
        loadUi("advance_menu.ui", self)
        self.password_Button.clicked.connect(self.gotopassword)
        self.malware_Button.clicked.connect(self.gotomalware)
        self.message_Button.clicked.connect(self.gotomessage)
        self.back_Button.clicked.connect(self.gotomenu)

    def gotopassword(self):
        password_Button = passwordScreen()
        widget.addWidget(password_Button)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotomalware(self):
        malware_Button = malwareScreen()
        widget.addWidget(malware_Button)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotomessage(self):
        message_Button = DigestScreen()
        widget.addWidget(message_Button)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotomenu(self):
        Start_Button = menu()
        widget.addWidget(Start_Button)
        widget.setCurrentIndex(widget.currentIndex()+1)
    

class passwordScreen(QDialog):
    def __init__(self):
        super(passwordScreen, self).__init__()
        loadUi("password.ui", self)
        self.back_Button.clicked.connect(self.gotoadvancemenu)
    
    def gotoadvancemenu(self):
        back_Button = advancemenuScreen()
        widget.addWidget(back_Button)
        widget.setCurrentIndex(widget.currentIndex()+1)
    

class malwareScreen(QDialog):
    def __init__(self):
        super(malwareScreen, self).__init__()
        loadUi("Malware.ui", self)
        self.back_Button.clicked.connect(self.gotoadvancemenu)
    
    def gotoadvancemenu(self):
        back_Button = advancemenuScreen()
        widget.addWidget(back_Button)
        widget.setCurrentIndex(widget.currentIndex()+1)

class DigestScreen(QDialog):
    def __init__(self):
        super(DigestScreen, self).__init__()
        loadUi("message.ui", self)
        self.back_Button.clicked.connect(self.gotoadvancemenu)
    
    def gotoadvancemenu(self):
        back_Button = advancemenuScreen()
        widget.addWidget(back_Button)
        widget.setCurrentIndex(widget.currentIndex()+1)


#network menu


class networkmenuScreen(QDialog):
    def __init__(self):
        super(networkmenuScreen, self).__init__()
        loadUi("network_menu.ui", self)
        self.vulnerability_Button.clicked.connect(self.gotovulnerability)
        self.https_Button.clicked.connect(self.gotohttps)
        self.back_Button.clicked.connect(self.gotomenu)   

    def gotovulnerability(self):
        vulnerability_Button = vulnerabilityScreen()
        widget.addWidget(vulnerability_Button)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotohttps(self):
        https_Button = httpsScreen()
        widget.addWidget(https_Button)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotomenu(self):
        Start_Button = menu()
        widget.addWidget(Start_Button)
        widget.setCurrentIndex(widget.currentIndex()+1)

  


class vulnerabilityScreen(QDialog):
    def __init__(self):
        super(vulnerabilityScreen, self).__init__()
        loadUi("vulnerability.ui", self)
        self.back_Button.clicked.connect(self.gotonetworkmenu)
    
    def gotonetworkmenu(self):
        back_Button = networkmenuScreen()
        widget.addWidget(back_Button)
        widget.setCurrentIndex(widget.currentIndex()+1)


class httpsScreen(QDialog):
    def __init__(self):
        super(httpsScreen, self).__init__()
        loadUi("HTTPS.ui", self)
        self.back_Button.clicked.connect(self.gotonetworkmenu)

    def gotonetworkmenu(self):
        back_Button = networkmenuScreen()
        widget.addWidget(back_Button)
        widget.setCurrentIndex(widget.currentIndex()+1)


     
     

#main
app = QApplication(sys.argv)
welcome = HomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(700)
widget.setFixedWidth(1200)
widget.show()
app.exec()


