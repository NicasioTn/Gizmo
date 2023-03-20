from PyQt6.QtCore import Qt, QAbstractTableModel, QVariant
from PyQt6.QtWidgets import QApplication, QTableView

class MyTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
        self._headers = list(data.keys())

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return 2

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(["Tools Name", "Detected"][section])
            else:
                return str(section + 1)
        return QVariant()

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            row = index.row()
            column = index.column()
            if column == 0:
                return str(self._headers[row])
            elif column == 1:
                value = self._data[self._headers[row]]["result"]
                return str(value)
        return QVariant()

if __name__ == '__main__':
    app = QApplication([])
    response = {
        "Bkav":{
            "detected":"false",
            "result":"unrated site"
        },
        "OpenPhish":{
            "detected":"false",
            "result":"clean site"
        },
        "VX Vault":{
            "detected":"false",
            "result":"clean site"
        },
        "Feodo Tracker":{
            "detected":"false",
            "result":"clean site"
        },
        "Web Security Guard":{
            "detected":"false",
            "result":"clean site"
        },
        "Scantitan":{
            "detected":"false",
            "result":"clean site"
        },
        "AlienVault":{
            "detected":"false",
            "result":"clean site"
        },
        "Sophos":{
            "detected":"false",
            "result":"clean site"
        },
        "Phishtank":{
            "detected":"false",
            "result":"clean site"
        },
        "CyberCrime":{
            "detected":"false",
            "result":"clean site"
        },
    }
    model = MyTableModel(response)
    view = QTableView()
    view.setModel(model)
    view.show()
    app.exec()
