import os
from PyQt6.QtWidgets import QApplication, QMessageBox
import time

app = QApplication([])

# create the message box
msg_box = QMessageBox()
msg_box.setIcon(QMessageBox.Icon.Question)
msg_box.setText("Do you want to shutdown? Any program is running now.")
msg_box.setWindowTitle("Shutdown")

# add the "Yes" and "No" buttons
yes_button = msg_box.addButton(QMessageBox.StandardButton.Yes)
no_button = msg_box.addButton(QMessageBox.StandardButton.No)

# show the message box and wait for user input
msg_box.exec()

# check which button was clicked
if msg_box.clickedButton() == yes_button:
    # shutdown the OS if "Yes" was clicked
    os.system("shutdown /s /t 10")  # in linux, use "shutdown -h 10"
    msg_box.setText("cancel shutdown")
    msg_box.show()
    os.system("shutdown /a") # in linux, use "shutdown -c"
    
else:
    # close the message box if "No" was clicked
    msg_box.close()

# start the event loop
app.exec()
