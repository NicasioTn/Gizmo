import os
import re
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QGridLayout,QLineEdit,QPushButton, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from pathlib import Path
import configparser
import json
import requests
import asyncio
url = ""
api_key = 'e8cf03a48915da2f70adfb45ae906ce940e837c47ba572bb30a8f1b8573df8e8'

class MainWindow(QWidget):
    
    # Properties
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Malware Scanning')
        self.resize(400, 50)
        
        layout = QGridLayout()
        self.setLayout(layout)

        # file selection
        file_browse = QPushButton('Browse')
        button_scan = QPushButton('Scan')
        button_scan.clicked.connect(self.scan_file_url)
        file_browse.clicked.connect(self.open_file_dialog)
        
        self.filename_edit = QLineEdit()
        self.filename_edit.setFixedWidth(300)

        layout.addWidget(QLabel('File:'), 0, 0)
        layout.addWidget(self.filename_edit, 0, 1)
        layout.addWidget(file_browse, 0 ,5)
        layout.addWidget(button_scan, 0 ,6)
        
        # Buttons
        self.button_clear = QPushButton('Clear')
        layout.addWidget(self.button_clear, 0, 7)
     
        # Events button
        self.button_clear.clicked.connect(self.filename_edit.clear)
        self.button_clear.clicked.connect(self.clearState)
        self.show()
    
    # clear section ----------------------------------------------------------
    def clearState(self):
        print('clear input')
        
    # report section --------------------------------------------------------
    def create_report(self): # create report PDF
        pass
    
    
    # scan file or url section -----------------------------------------------
    def scan_file_url(self):
        # malicous_sites = ["https://trycracksetup.com", "https://www.cracksetup.com", "https://idmcrackeys.com"]
        
        # Define the pattern to match the URL or file 
        url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        file_pattern = re.compile(r'^[A-Za-z]:|^(\/[A-Za-z0-9_]+)+\/?$')
        
        input = self.filename_edit.text()
        print(input)
        
        if url_pattern.match(input):
            #print('URL')
            print(f"URL, scanning...")
            # scan url
            url = 'https://www.virustotal.com/vtapi/v2/url/scan'
            params = {'apikey': api_key, 'url': url}
            response = requests.post(url, data=params)
            date = response.json().get("scan_date")
            print(f"Date: {date}")
            
            #get report after scaned form url
            url = 'https://www.virustotal.com/vtapi/v2/url/report'
            params = {'apikey': api_key, 'resource': self.filename_edit.text()}  # url
            response = requests.get(url, params=params)
            #print(response.json())
            
            for i in response.json().get("scans"):
                print(f"Name: {i} - {response.json().get('scans').get(i).get('detected')} \t | \t Result:{response.json().get('scans').get(i).get('result')}")
            
            print(f"Scan ID: {response.json().get('scan_id')} Success........")
        elif file_pattern.match(input):
            #print('File')
            try:
                print(f"File, scanning...")
                url = 'https://www.virustotal.com/vtapi/v2/file/scan'
                params = {'apikey': api_key}
                files = {'file': (input, open(input, 'rb'))}
                response = requests.post(url, files=files, params=params)
                resource = response.json().get("resource")
                print(f"Resource: {resource}")
                # get report from file scaned
                url = 'https://www.virustotal.com/vtapi/v2/file/report'
                params = {'apikey': api_key, 'resource': resource}
                response = requests.get(url, params=params)
                #print(response.json().get("scans"))
                
                for i in response.json().get("scans"):
                    print(f"Name: {i} - {response.json().get('scans').get(i).get('detected')} \t | \t Result: - {response.json().get('scans').get(i).get('result')}")
                    
                print(f"Scan ID: {response.json().get('scan_id')} Success........")
            except:
                print("Invalid input")
        else:
            print('Invalid input')
            
        # if not file_path : # check if input path is empty
        #     print("File or URL exists")

        # elif file_path.split(":", 1)[0] == "https" or file_path.split(":", 1)[0] == "http":  # check if text is url by checking if it has http or https
        #     print(f"URL, scanning...")
        #     # scan url
        #     url = 'https://www.virustotal.com/vtapi/v2/url/scan'
        #     params = {'apikey': api_key, 'url': url}
        #     response = requests.post(url, data=params)
        #     date = response.json().get("scan_date")
        #     print(f"Date: {date}")
            
        #     #get report after scaned form url
        #     url = 'https://www.virustotal.com/vtapi/v2/url/report'
        #     params = {'apikey': api_key, 'resource': self.filename_edit.text()}  # url
        #     response = requests.get(url, params=params)
        #     #print(response.json())
            
        #     for i in response.json().get("scans"):
        #         print(f"Name: {i} - {response.json().get('scans').get(i).get('detected')} \t | \t Result:{response.json().get('scans').get(i).get('result')}")
            
        #     print(f"Scan ID: {response.json().get('scan_id')} Success........")
            
            
        # elif file_path.split(":", 1)[0] != "https" and file_path.split(":", 1)[0] != "http": # if not url then it is a file
        #     try:
        #         print(f"File, scanning...")
        #         url = 'https://www.virustotal.com/vtapi/v2/file/scan'
        #         params = {'apikey': api_key}
        #         files = {'file': (file_path, open(file_path, 'rb'))}
        #         response = requests.post(url, files=files, params=params)
        #         resource = response.json().get("resource")
        #         print(f"Resource: {resource}")
        #         # get report from file scaned
        #         url = 'https://www.virustotal.com/vtapi/v2/file/report'
        #         params = {'apikey': api_key, 'resource': resource}
        #         response = requests.get(url, params=params)
        #         #print(response.json().get("scans"))
                
        #         for i in response.json().get("scans"):
        #             print(f"Name: {i} - {response.json().get('scans').get(i).get('detected')} \t | \t Result: - {response.json().get('scans').get(i).get('result')}")
                    
        #         print(f"Scan ID: {response.json().get('scan_id')} Success........")
        #     except:
        #         print("Invalid input")
        # else:
        #     print("Invalid input")
        
    
    
    # Browse File Section ---------------------------------------------
    def open_file_dialog(self):
        current_dir = os.getcwd()
        filename, ok = QFileDialog.getOpenFileName(
            self,
            "Select a File", 
            current_dir, 
            "All Files (*)"
        )
        if filename:
            path = Path(filename)
            self.filename_edit.setText(str(path))
            if path.exists(): # check if file exists 
                print(path) 
                
            else:
                print("File exists")
            
            # set and show image from browse file
            # imagePath = f"{path}"
            # pixmap = QPixmap(imagePath)
            # self.label_QR.setPixmap(pixmap)
            # self.resize(pixmap.width(), pixmap.height())
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec()) 