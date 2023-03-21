import asyncio
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QProgressBar, QLabel


class IpLookupThread(QThread):
    progress_updated = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ip_address = '8.8.8.8'

    async def lookup_ip(self):
        # Simulate an asynchronous IP lookup
        for i in range(1, 11):
            await asyncio.sleep(1)
            self.progress_updated.emit(i * 10)
        self.progress_updated.emit(100)

    def run(self):
        asyncio.run(self.lookup_ip())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('IP Lookup')
        self.setGeometry(100, 100, 300, 100)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(10, 10, 280, 30)

        self.success_label = QLabel('Success!', self)
        self.success_label.setGeometry(10, 50, 280, 30)
        self.success_label.hide()

        self.ip_lookup_thread = IpLookupThread()
        self.ip_lookup_thread.progress_updated.connect(self.update_progress_bar)
        self.ip_lookup_thread.start()

    def update_progress_bar(self, value):
        self.progress_bar.setValue(value)
        if value == 100:
            self.progress_bar.hide()
            self.success_label.show()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
