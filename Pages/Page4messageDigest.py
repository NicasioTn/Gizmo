import os
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QGridLayout,QLineEdit,QPushButton, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from pathlib import Path

import hashlib
import qrcode

class MessageDigest:
    def md5(self, data):
        return hashlib.md5(data.encode()).hexdigest()

    def sha1(self, data):
        return hashlib.sha1(data.encode()).hexdigest()

    def sha256(self, data):
        return hashlib.sha256(data.encode()).hexdigest()

    def sha3_256(self, data):
        return hashlib.sha3_256(data.encode()).hexdigest()
    

class MainWindow(QWidget):
    # Properties
    state_browse_file = False
    state = ""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Message Digest Generator')
        self.resize(400, 350)
        
        layout = QGridLayout()
        self.setLayout(layout)

        # file selection
        file_browse = QPushButton('Browse')
        file_browse.clicked.connect(self.open_file_dialog)
        self.filename_edit = QLineEdit()
        self.filename_edit.setFixedWidth(150)
        
        layout.addWidget(QLabel('File:'), 0, 0)
        layout.addWidget(self.filename_edit, 0, 1)
        layout.addWidget(file_browse, 0 ,5)
        layout.addWidget(QLabel('QR-Code'), 0, 8)
        
        # Buttons
        self.button_md5 = QPushButton('MD5')
        self.button_sha1 = QPushButton('SHA1')
        self.button_sha2 = QPushButton('SHA2')
        self.button_sha3 = QPushButton('SHA3')
        self.button_clear = QPushButton('Clear')
        self.button_save = QPushButton('Save')
        layout.addWidget(self.button_md5, 1, 0)
        layout.addWidget(self.button_sha1, 1, 1)
        layout.addWidget(self.button_sha2, 1, 2)
        layout.addWidget(self.button_sha3, 1, 3)
        layout.addWidget(self.button_clear, 1, 5)
        layout.addWidget(self.button_save, 2, 5)
        
        # Labels
        self.label_QR = QLabel('QR-Code')
        self.label_Hash_text = QLabel('Result: ')
        self.label_Hash_text.setStyleSheet("color: #000000")
        layout.addWidget(self.label_QR, 1, 8)
        layout.addWidget(self.label_Hash_text, 2, 8)
     
        # Events button
        self.button_md5.clicked.connect(self.Md5)
        self.button_sha1.clicked.connect(self.Sha1)
        self.button_sha2.clicked.connect(self.Sha2)
        self.button_sha3.clicked.connect(self.Sha3) 
        self.button_clear.clicked.connect(self.filename_edit.clear)
        self.button_clear.clicked.connect(self.clearResult)
        self.button_save.clicked.connect(self.saveQR)
        
        self.show()
    
    # Save QR-Code Section ---------------------------------------------
    def saveQR(self,):
        pathfile, _ = QFileDialog.getSaveFileName(
            self,
            "Save File",
            "",
            "Images (*.png *.jpg)")
        if pathfile:
            print("Save at: ", pathfile)
            
        # Save QR-Code with pixmap at pathfile
        if self.state == "md5":
            self.label_QR.pixmap().save(pathfile, 'PNG')
        elif self.state == "sha1":
            self.label_QR.pixmap().save(pathfile, 'PNG')
        elif self.state == "sha2":
            self.label_QR.pixmap().save(pathfile, 'PNG')
        elif self.state == "sha3":
            self.label_QR.pixmap().save(pathfile, 'PNG')
        else:
            print("Error: QR-Code is Not Generated")
    
    # Clear Section ---------------------------------------------
    def clearResult(self):
        self.label_Hash_text.setText('Result: ')
        self.label_QR.setText('QR-Code')
    
    
    # Hash Algorithms Section ---------------------------------------------
    def Md5(self):
        if os.path.isfile(self.filename_edit.text()):
            path_direct = self.getPath()
            init_hash = hashlib.md5()
            file = path_direct 
            BLOCK_SIZE = 65536 
            with open(file, 'rb') as f: 
                fb = f.read(BLOCK_SIZE) 
                while len(fb) > 0: 
                    init_hash.update(fb) 
                    fb = f.read(BLOCK_SIZE) 
            file_hashed =  init_hash.hexdigest()
            print (f"This is file hash MD5: {file_hashed}") 
            self.label_Hash_text.setText(f'Result: {file_hashed}')
            self.qrCodeGenerator(file_hashed)
        else:
            if(self.filename_edit.text() == ''):
                print("Error: Text is Empty")
            else:
                md5 = MessageDigest.md5(self, self.filename_edit.text())
                print(f'MD5: {md5}')
                self.label_Hash_text.setText(f'Result: {md5}')
                self.qrCodeGenerator(md5)
                
    
    def Sha1(self):
        if os.path.isfile(self.filename_edit.text()):
            path_direct = self.getPath()
            init_hash = hashlib.sha1()
            file = path_direct 
            BLOCK_SIZE = 65536 
            with open(file, 'rb') as f: 
                fb = f.read(BLOCK_SIZE) 
                while len(fb) > 0: 
                    init_hash.update(fb) 
                    fb = f.read(BLOCK_SIZE) 
            file_hashed =  init_hash.hexdigest()
            print (f"This is file hash SHA1: {file_hashed}") 
            self.label_Hash_text.setText(f'Result: {file_hashed}')
            self.qrCodeGenerator(file_hashed)
        else:
            if(self.filename_edit.text() == ''):
                print("Error: Text is Empty")
            else:
                sha1 = MessageDigest.sha1(self, self.filename_edit.text())
                print(f"SHA1: {sha1}")
                self.label_Hash_text.setText(f'Result: {sha1}')
                self.qrCodeGenerator(sha1)
            
        
    def Sha2(self):
        if os.path.isfile(self.filename_edit.text()):
            init_hash = hashlib.sha256()
            path_direct = self.getPath()
            file = path_direct 
            BLOCK_SIZE = 65536 
            with open(file, 'rb') as f: 
                fb = f.read(BLOCK_SIZE) 
                while len(fb) > 0: 
                    init_hash.update(fb) 
                    fb = f.read(BLOCK_SIZE) 
            file_hashed =  init_hash.hexdigest()
            print (f"This is file hash SHA2: {file_hashed}") 
            self.label_Hash_text.setText(f'Result: {file_hashed}')
            self.qrCodeGenerator(file_hashed)
        else:
            if(self.filename_edit.text() == ''):
                print("Error: Text is Empty")
            else:
                sha2 = MessageDigest.sha256(self, self.filename_edit.text())
                print(f'SHA2: {sha2}')
                self.label_Hash_text.setText(f'Result: {sha2}')
                self.qrCodeGenerator(sha2)
            
    
    def Sha3(self):
        if os.path.isfile(self.filename_edit.text()):
            init_hash = hashlib.sha3_256()
            path_direct = self.getPath()
            file = path_direct 
            BLOCK_SIZE = 65536 
            with open(file, 'rb') as f: 
                fb = f.read(BLOCK_SIZE) 
                while len(fb) > 0: 
                    init_hash.update(fb) 
                    fb = f.read(BLOCK_SIZE) 
            file_hashed =  init_hash.hexdigest()
            print (f"This is file hash SHA3: {file_hashed}") 
            self.label_Hash_text.setText(f'Result: {file_hashed}')
            self.qrCodeGenerator(file_hashed)
        else:
            if(self.filename_edit.text() == ''):
                print("Error: Text is Empty")
            else:
                sha3 = MessageDigest.sha3_256(self, self.filename_edit.text())
                print(f'SHA3: {sha3}')
                self.label_Hash_text.setText(f'Result: {sha3}')
                self.qrCodeGenerator(sha3)
            
    
    # QR-Code Section ---------------------------------------------
    def qrCodeGenerator(self, hash):
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        qr.add_data(hash)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("./SaveQR/MessageDigest-QRCode.png")
        self.ShowImage_QR() # show image
        
    
    # Browse File Section ---------------------------------------------
    def open_file_dialog(self):
        filename, ok = QFileDialog.getOpenFileName(
            self,
            "Select a File", 
            "D:\\icons\\avatar\\", 
            "Images (*.png *.jpg)"
        )
        if filename:
            path = Path(filename)
            self.filename_edit.setText(str(path))
            if path.exists(): # check if file exists 
                print("File exists")
            print(path) 
            # set and show image from browse file
            # imagePath = f"{path}"
            # pixmap = QPixmap(imagePath)
            # self.label_QR.setPixmap(pixmap)
            # self.resize(pixmap.width(), pixmap.height())
            
            self.state_browse_file = True # browsed file 
            if(self.state_browse_file == True):
                #hashfile = self.hash_file(path, self.state)
                self.setPath(path)
            
    def setPath(self, path):
        self.path = path
    
    def getPath(self):
        return self.path
    
    # Show Image Section ---------------------------------------------
    def ShowImage_QR(self):
        imagePath = "./SaveQR/MessageDigest-QRCode.png"
        pixmap = QPixmap(imagePath)
        pixmap = pixmap.scaledToWidth(200)
        pixmap = pixmap.scaledToHeight(200)
        self.label_QR.setPixmap(pixmap)
        #self.resize(pixmap.width(), pixmap.height())
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec()) 