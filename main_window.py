import sys

from PyQt6.QtCore import QSize, QStringListModel
from PyQt6.QtWidgets import QMainWindow, QWidget, QListView, QVBoxLayout
from database import Database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Главная")

        list_model = QStringListModel()
        list_model.setStringList(self.get_animals())

        list_widget = QWidget()
        list_view = QListView(list_widget)
        list_view.setModel(list_model)

        layout = QVBoxLayout()
        layout.addWidget(QListView())

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def get_animals(self):
        db = Database()
        result_raw = db.get_animals()
        result = []
        for r in result_raw:
            result.append(str(r["id"])+ ":"+ r["name"])
        return result
        
