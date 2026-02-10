# ui/main_view.py
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget

class ProfessorView(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Bienvenido profesor")
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

    def set_user(self, username: str):
        self.label.setText(f" Bienvenido profesor: {username}")
