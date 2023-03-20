''' Dynamic Layout the Layout '''
# import sys

# from PyQt6.QtWidgets import (
#     QApplication,
#     QHBoxLayout,
#     QPushButton,
#     QWidget,
# )

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("QHBoxLayout Example")
#         # Create a QHBoxLayout instance
#         layout = QHBoxLayout()
#         # Add widgets to the layout
#         layout.addWidget(QPushButton("Left-Most"))
#         layout.addWidget(QPushButton("Center"), 1)
#         layout.addWidget(QPushButton("Right-Most"), 2)
#         # Set the layout on the application's window
#         self.setLayout(layout)
#         print(self.children())

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec())

''' QGridLayout Example '''
# import sys

# from PyQt6.QtWidgets import (
#     QApplication,
#     QGridLayout,
#     QPushButton,
#     QWidget,
# )

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("QGridLayout Example")
#         # Create a QGridLayout instance
#         layout = QGridLayout()
#         # Add widgets to the layout
#         layout.addWidget(QPushButton("Button at (0, 0)"), 0, 0)
#         layout.addWidget(QPushButton("Button at (0, 1)"), 0, 1)
#         layout.addWidget(QPushButton("Button at (0, 2)"), 0, 2)
#         layout.addWidget(QPushButton("Button at (1, 0)"), 1, 0)
#         layout.addWidget(QPushButton("Button at (1, 1)"), 1, 1)
#         layout.addWidget(QPushButton("Button at (1, 2)"), 1, 2)
#         layout.addWidget(QPushButton("Button at (2, 0)"), 2, 0)
#         layout.addWidget(QPushButton("Button at (2, 1)"), 2, 1)
#         layout.addWidget(QPushButton("Button at (2, 2)"), 2, 2)
#         # Set the layout on the application's window
#         self.setLayout(layout)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec())

''' QStackedLayout Example'''
# import sys

# from PyQt6.QtWidgets import (
#     QApplication,
#     QComboBox,
#     QFormLayout,
#     QLineEdit,
#     QStackedLayout,
#     QVBoxLayout,
#     QWidget,
# )

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("QStackedLayout Example")
#         # Create a top-level layout
#         layout = QVBoxLayout()
#         self.setLayout(layout)
#         # Create and connect the combo box to switch between pages
#         self.pageCombo = QComboBox()
#         self.pageCombo.addItems(["Page 1", "Page 2"])
#         self.pageCombo.activated.connect(self.switchPage)
#         # Create the stacked layout
#         self.stackedLayout = QStackedLayout()
#         # Create the first page
#         self.page1 = QWidget()
#         self.page1Layout = QFormLayout()
#         self.page1Layout.addRow("Name:", QLineEdit())
#         self.page1Layout.addRow("Address:", QLineEdit())
#         self.page1.setLayout(self.page1Layout)
#         self.stackedLayout.addWidget(self.page1)
#         # Create the second page
#         self.page2 = QWidget()
#         self.page2Layout = QFormLayout()
#         self.page2Layout.addRow("Job:", QLineEdit())
#         self.page2Layout.addRow("Department:", QLineEdit())
#         self.page2.setLayout(self.page2Layout)
#         self.stackedLayout.addWidget(self.page2)
#         # Add the combo box and the stacked layout to the top-level layout
#         layout.addWidget(self.pageCombo)
#         layout.addLayout(self.stackedLayout)

#     def switchPage(self):
#         self.stackedLayout.setCurrentIndex(self.pageCombo.currentIndex())

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec())

''''''
# import sys

# from PyQt6.QtWidgets import (
#     QApplication,
#     QCheckBox,
#     QTabWidget,
#     QVBoxLayout,
#     QWidget,
# )

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("QTabWidget Example")
#         self.resize(270, 110)
#         # Create a top-level layout
#         layout = QVBoxLayout()
#         self.setLayout(layout)
#         # Create the tab widget with two tabs
#         tabs = QTabWidget()
#         tabs.addTab(self.generalTabUI(), "General")
#         tabs.addTab(self.networkTabUI(), "Network")
#         layout.addWidget(tabs)

#     def generalTabUI(self):
#         """Create the General page UI."""
#         generalTab = QWidget()
#         layout = QVBoxLayout()
#         layout.addWidget(QCheckBox("General Option 1"))
#         layout.addWidget(QCheckBox("General Option 2"))
#         layout.addWidget(QCheckBox("General Option 3"))
#         generalTab.setLayout(layout)
#         return generalTab

#     def networkTabUI(self):
#         """Create the Network page UI."""
#         networkTab = QWidget()
#         layout = QVBoxLayout()
#         layout.addWidget(QCheckBox("Network Option 1"))
#         layout.addWidget(QCheckBox("Network Option 2"))
#         networkTab.setLayout(layout)
#         return networkTab

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec())
    
    
# from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox
# import sys
 
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.resize(300, 250)
#         self.setWindowTitle("CodersLegacy")
 
#         self.radio = QCheckBox("Option 1", self)
#         self.radio.toggled.connect(self.showDetails)
#         self.radio.move(100, 100)
 
#     def showDetails(self):
#         print("Selected: ", self.sender().isChecked(),
#               "  Name: ", self.sender().text())
#         # self.sender() gives ref to widget that emitted signal
 
# app = QApplication(sys.argv)
# window = Window()
# window.show()
# sys.exit(app.exec())

from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox
import sys
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 250)
        self.setWindowTitle("CodersLegacy")
 
        self.radio = QCheckBox("Option 1", self)
        self.radio.toggled.connect(self.showDetails)
        self.radio.move(100, 100)
 
    def showDetails(self):
        print("Selected: ", self.sender().setChecked(False),
              "  Name: ", self.sender().text())
        # self.sender() gives ref to widget that emitted signal
 
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())