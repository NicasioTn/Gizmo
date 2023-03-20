from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
import subprocess

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HTTPS Test")

        # Create text edit widget to display the results
        self.resultsTextEdit = QTextEdit()
        self.resultsTextEdit.setReadOnly(True)

        # Create button widget to run the test
        self.runTestButton = QPushButton("Run Test")
        self.runTestButton.clicked.connect(self.runTest)

        # Add the widgets to a layout
        layout = QVBoxLayout()
        layout.addWidget(self.resultsTextEdit)
        layout.addWidget(self.runTestButton)

        # Create a container widget for the layout and set it as the central widget of the window
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def runTest(self):
        # Run the testssl.sh command and capture the output
        output = subprocess.check_output(['D:/Project/Project 1/Code/testssl.sh/testssl.sh', '-p', '443', 'isanmsu.com'])

        # Parse the output to extract the SSL/TLS configuration information
        results = output.decode().splitlines()

        # Extract the overall grade and detailed SSL/TLS configuration information
        grade = None
        details = []
        for line in results:
            if line.startswith("Overall rating:"):
                grade = line.split(":")[1].strip()
            elif line.startswith("   TLS protocol"):
                details.append(line.strip())

        # Extract any issues or vulnerabilities found in the configuration
        issues = []
        for line in results:
            if line.startswith("[!]"):
                issues.append(line.strip())

        # Display the results in the text edit widget
        self.resultsTextEdit.setPlainText(f"Overall grade: {grade}\n\n")
        self.resultsTextEdit.append("SSL/TLS Configuration Details:\n")
        for detail in details:
            self.resultsTextEdit.append(detail)
        self.resultsTextEdit.append("\n")
        if len(issues) > 0:
            self.resultsTextEdit.append("Issues/Vulnerabilities Found:\n")
            for issue in issues:
                self.resultsTextEdit.append(issue)
        else:
            self.resultsTextEdit.append("No issues/vulnerabilities found.")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
