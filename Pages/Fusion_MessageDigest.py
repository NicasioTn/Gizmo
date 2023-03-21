import os
import sys
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox
from PyQt6.QtGui import QPixmap, QIcon
from pathlib import Path
from PyQt6.QtGui import QIcon
import hashlib
import qrcode

class Hashing:
    def md5(self, data):
        return hashlib.md5(data.encode('utf-8')).hexdigest()

    def sha1(self, data):
        return hashlib.sha1(data.encode('utf-8')).hexdigest()

    def sha256(self, data):
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def sha3_256(self, data):
        return hashlib.sha3_256(data.encode('utf-8')).hexdigest()

class MessageDigest(QDialog):
    # properties
    state_browse_file = False
    
    def __init__(self):
        super(MessageDigest, self).__init__()
        loadUi("./Files/Message_Digest.ui", self)
        self.setWindowTitle("Message Digest")
        self.window_icon = QIcon("./Images/logo.png")
        self.logo = QPixmap("./Images/logo.png")
        
        self.setWindowIcon(self.window_icon)
        self.logo_Label.setPixmap(self.logo)
        
        # Event Clicked
        self.MD5_Button.clicked.connect(self.Md5)
        self.SHA1_Button.clicked.connect(self.Sha1)
        self.SHA2_Button.clicked.connect(self.Sha2)
        self.SHA3_Button.clicked.connect(self.Sha3) 
        self.clear_Button.clicked.connect(self.input.clear)
        self.clear_Button.clicked.connect(self.clearResult)
        self.save_Button.clicked.connect(self.saveQR)
        self.browse_Button.clicked.connect(self.open_file_dialog)
    
    # Save QR-Code Section ---------------------------------------------
    def saveQR(self,):
        pathfile, ok = QFileDialog.getSaveFileName(
            self,
            "Save File",
            "",
            "Images (*.png *.jpg)")
        
        # Check if a filename was provided
        if pathfile: # show place to save
            print("Save at: ", pathfile)
            # Save QR-Code with pixmap at pathfile
            if not self.output_QR_Label.pixmap().isNull():
                # Save the pixmap to the specified file path
                self.output_QR_Label.pixmap().save(pathfile, 'PNG')
                # Set the text of the save button to "SAVED!" to indicate successful save
                self.save_Button.setText("SAVED!")
            else:
                print("Error: QR-Code is Not Generated")
        else:
            print("Error: No file name specified")
    
    # Clear Section ---------------------------------------------
    def clearResult(self):
        self.output_hash_Label.setText('')
        self.output_QR_Label.setText(' ')
        self.save_Button.setText("SAVE")
    
    
    # Hash Algorithms Section ---------------------------------------------
    def Md5(self):
        if os.path.isfile(self.input.text()):
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
            self.output_hash_Label.setText(f'{file_hashed}')
            self.qrCodeGenerator(file_hashed)
        else:
            if(self.input.text() == ''):
                print("Error: Text is Empty")
            else:
                md5 = Hashing.md5(self, self.input.text())
                print(f'MD5: {md5}')
                self.output_hash_Label.setText(f'{md5}')
                self.qrCodeGenerator(md5)
                
    
    def Sha1(self):
        if os.path.isfile(self.input.text()):
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
            self.output_hash_Label.setText(f'{file_hashed}')
            self.qrCodeGenerator(file_hashed)
        else:
            if(self.input.text() == ''):
                print("Error: Text is Empty")
            else:
                sha1 = Hashing.sha1(self, self.input.text())
                print(f"SHA1: {sha1}")
                self.output_hash_Label.setText(f'Result: {sha1}')
                self.qrCodeGenerator(sha1)
            
        
    def Sha2(self):
        if os.path.isfile(self.input.text()):
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
            self.output_hash_Label.setText(f'{file_hashed}')
            self.qrCodeGenerator(file_hashed)
        else:
            if(self.input.text() == ''):
                print("Error: Text is Empty")
            else:
                sha2 = Hashing.sha256(self, self.input.text())
                print(f'SHA2: {sha2}')
                self.output_hash_Label.setText(f'{sha2}')
                self.qrCodeGenerator(sha2)
            
    
    def Sha3(self):
        if os.path.isfile(self.input.text()):
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
            self.output_hash_Label.setText(f'{file_hashed}')
            self.qrCodeGenerator(file_hashed)
        else:
            if(self.input.text() == ''):
                print("Error: Text is Empty")
            else:
                sha3 = Hashing.sha3_256(self, self.input.text())
                print(f'SHA3: {sha3}')
                self.output_hash_Label.setText(f'{sha3}')
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
            self.input.setText(str(path))
            if path.exists(): # check if file exists 
                print("File exists")
            print(path) 
            
            self.state_browse_file = True # browsed file 
            if(self.state_browse_file == True):
                #hashfile = self.hash_file(path, self.state)
                self.setPath(path)
                
    # Show Image Section ---------------------------------------------
    def ShowImage_QR(self):
        imagePath = "./SaveQR/MessageDigest-QRCode.png"
        pixmap = QPixmap(imagePath)
        pixmap = pixmap.scaledToWidth(200)
        pixmap = pixmap.scaledToHeight(200)
        self.output_QR_Label.setPixmap(pixmap)
        #self.resize(pixmap.width(), pixmap.height())
            
    def setPath(self, path):
        self.path = path
    
    def getPath(self):
        return self.path
    
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MessageDigest()
    window.setFixedHeight(700)
    window.setFixedWidth(1200)
    window.setMinimumSize(1200, 700)
    window.setMaximumSize(1200, 700)
    window.show()
    sys.exit(app.exec())     
    
