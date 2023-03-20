# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton
# from datetime import datetime
# import nmap
# import os
# os.environ["PATH"] += os.pathsep + r"C:\Program Files (x86)\Nmap"

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Malware Scanner")

#         # Create widgets
#         self.input_edit = QLineEdit(self)
#         self.input_edit.setPlaceholderText("Enter target IP address or domain name")
#         self.input_edit.setGeometry(20, 20, 200, 30)

#         self.output_label = QLabel(self)
#         self.output_label.setGeometry(20, 80, 400, 300)

#         self.mode_button = QPushButton("Stealth", self)
#         self.mode_button.setGeometry(20, 400, 100, 30)
#         self.mode_button.clicked.connect(self.switch_mode)

#         self.scan_button = QPushButton("Start Scan", self)
#         self.scan_button.setGeometry(150, 400, 100, 30)
#         self.scan_button.clicked.connect(self.scan)

#     def switch_mode(self):
#         if self.mode_button.text() == "Stealth":
#             self.mode_button.setText("Aggressive")
#         elif self.mode_button.text() == "Aggressive":
#             self.mode_button.setText("Adaptive")
#         else:
#             self.mode_button.setText("Stealth")

#     def scan(self):
#         # Get target from input edit
#         target = self.input_edit.text()

#         # Get current date and time
#         now = datetime.now()
#         date_time = now.strftime("%m/%d/%Y %H:%M:%S")

#         # Perform Nmap scan based on current mode
#         nm = nmap.PortScanner()
#         if self.mode_button.text() == "Stealth":
#             # Perform scan in stealth mode
#             nm.scan(hosts=target, arguments="-sS")
#         elif self.mode_button.text() == "Aggressive":
#             # Perform scan in aggressive mode
#             nm.scan(hosts=target, arguments="-A")
#         else:
#             # Perform scan in adaptive mode
#             nm.scan(hosts=target, arguments="-sS -A --version-all")

#         # Display scan results in output label
#         scan_results = f"Scan results for {target} at {date_time}:\n\n"
#         for host in nm.all_hosts():
#             scan_results += f"Host : {host} ({nm[host].hostname()})\n"
#             scan_results += f"State : {nm[host].state()}\n"
#             for proto in nm[host].all_protocols():
#                 scan_results += "----------\n"
#                 scan_results += f"Protocol : {proto}\n"
#                 lport = nm[host][proto].keys()
#                 for port in sorted(lport):
#                     scan_results += f"port : {port}\n"
#                     scan_results += f"state : {nm[host][proto][port]['state']}\n"
#                     scan_results += f"service : {nm[host][proto][port]['name']}\n"
#                     scan_results += f"version : {nm[host][proto][port]['version']}\n"
#                     if 'cpe' in nm[host][proto][port]:
#                         scan_results += f"CPE : {nm[host][proto][port]['cpe']}\n"
#                     if 'cve' in nm[host][proto][port]:
#                         scan_results += f"CVE : {nm[host][proto][port]['cve'][0]['id']}\n"
#                     scan_results += "----------\n"
#             scan_results += "\n"

#         self.output_label.setText(scan_results)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.setGeometry(100, 100, 400, 200)
#     window.show()
#     sys.exit(app.exec())


import sys
import nmap
from datetime import datetime
from tabulate import tabulate
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem

# Add the path to nmap executable to the PATH environment variable
import os
os.environ["PATH"] += os.pathsep + r"C:\Program Files (x86)\Nmap"

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Nmap Scanner"
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        # Labels
        targetLabel = QLabel("Target:")
        optionsLabel = QLabel("Options:")
        self.resultLabel = QLabel()

        # LineEdits
        self.targetLineEdit = QLineEdit()
        self.optionsLineEdit = QLineEdit()

        # Button
        self.scanButton = QPushButton("Scan")
        self.scanButton.clicked.connect(self.scan)

        # Table
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["Port", "State", "Service", "Version", "CVE"])

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(targetLabel)
        layout.addWidget(self.targetLineEdit)
        layout.addWidget(optionsLabel)
        layout.addWidget(self.optionsLineEdit)
        layout.addWidget(self.scanButton)
        layout.addWidget(self.resultLabel)
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        # Window
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, self.width, self.height)
        self.show()

    def scan(self):
        target = self.targetLineEdit.text()
        options = self.optionsLineEdit.text()
        nm = nmap.PortScanner()
        nm.scan(target, arguments=options)
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
        self.resultLabel.setText(f"Target: {target}\nDate-Time: {date_time}")
        self.tableWidget.setRowCount(len(result))
        for i, row in enumerate(result):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i, j, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())
