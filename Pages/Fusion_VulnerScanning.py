import os
import sys
import nmap
from PyQt6.uic import loadUi
from datetime import datetime
from tabulate import tabulate
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,  QDialog, QFileDialog

# Reference Tool path for Nmap
os.environ["PATH"] += os.pathsep + r"C:\Program Files (x86)\Nmap"

class VulnerabilityScan(QDialog):
    # properties
    
    
    def __init__(self):
        super(VulnerabilityScan, self).__init__()
        loadUi("./Files/Vulnerability_Scanning.ui", self)
        self.setWindowTitle("Vulnerability Scan")
        
        # Events Click
        self.scan_Button.clicked.connect(self.scan)
        
        self.result_tabWidget.setColumnCount(5)
        self.result_tabWidget.setHorizontalHeaderLabels(["Port", "State", "Service", "Version", "CVE"])
        self.result_tabWidget.setStyleSheet("""
            QTableWidget {
                background-color: #FFFFFF;
                alternate-background-color: #F2F2F2;
                selection-background-color: #BBD8E9;
                selection-color: #000000;
            }
            QTableWidget::item {
                padding: 5px;
            }
            QHeaderView::section {
                background-color: #D9E5EF;
                color: #000000;
                padding: 5px;
                border: 1px solid #CCCCCC;   
            }
        """)
        self.clear_Button.clicked.connect(self.clear)
        self.stealth_Button.clicked.connect(self.stealth)
        self.aggressive_Button.clicked.connect(self.aggressive)
        self.adaptive_Button.clicked.connect(self.adaptive)
        self.vulner_Button.clicked.connect(self.vulner)
    
    def stealth(self):
        self.options_LineEdit.setText("-sS -sV -O -T4 -A -v")
    
    def aggressive(self):
        self.options_LineEdit.setText("-sS -sV -O -T4 -A -v -p-")
    
    def adaptive(self):
        self.options_LineEdit.setText("-sS -sV -O -T4 -A -v -p- --script vuln")
    
    def vulner(self):
        self.options_LineEdit.setText("-sS -sV -O -T4 -A -v -p- --script vuln --script-args vulscandb=scipvuldb.csv")
    
    def clear(self):
        self.result_tabWidget.clear()
        self.date_Label.clear()
        self.OS_Label.clear()
        self.target_LineEdit.clear()
        self.options_LineEdit.clear()

    def scan(self):
        target = self.target_LineEdit.text()
        options = self.options_LineEdit.text()
        nm = nmap.PortScanner()
        nm.scan(target, arguments=options)
        
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.date_Label.setText(f"Date-Time: {date_time}")
        
        result = []
        for host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                for port in lport:
                    state = nm[host][proto][port]['state']
                    service = nm[host][proto][port]['name']
                    version = nm[host][proto][port]['version']
                    cve = nm[host][proto][port]['cpe']
                    result.append([port, state, service, version, cve])
                    
        table = tabulate(result, headers=["Port", "State", "Service", "Version", "CVE"])
        self.OS_Label.setText(f"Target: {target}\nDate-Time: {date_time}")
        self.result_tabWidget.setRowCount(len(result))
        for i, row in enumerate(result):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.result_tabWidget.setItem(i, j, item)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VulnerabilityScan()
    window.setFixedHeight(700)
    window.setFixedWidth(1200)
    window.setMinimumSize(1200, 700)
    window.setMaximumSize(1200, 700)
    window.show()
    sys.exit(app.exec())     
    