from PyQt6.QtCore import QSize, QStringListModel
from PyQt6.QtWidgets import QMainWindow,QDialog,QLabel,QHBoxLayout, QPushButton, QLineEdit, QWidget, QListView, QVBoxLayout
from database import Database

class FormWindow(QDialog):
    def __init__(self, parent = None,object = None):
        super().__init__(parent)
        if object is None:
            self.setWindowTitle("Форма добавления")
            self.button = QPushButton("Добавить")
            self.button.clicked.connect(self.button_click)
        else:
            self.setWindowTitle("Форма изменения")
            self.button = QPushButton("Изменить")
            self.id = object.split(":")[0]
            self.button.clicked.connect(self.button_click)



        label = QLabel("Название:")
        self.name_text = QLineEdit(object)
        self.id = object.split(":")[0]

        if object is None:
            self.name_text.text = QLineEdit()
        else:
            self.name_text = QLineEdit(object.split(":")[1])

        if object is None:
            self.name_text = object

        name_input = QHBoxLayout()
        name_input.addWidget(label)
        name_input.addWidget(self.name_text)
        name_input_widget = QWidget()
        name_input_widget.setLayout(name_input)


        layout = QVBoxLayout()
        layout.addWidget(name_input_widget)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def button_click(self):
         self.done(1)