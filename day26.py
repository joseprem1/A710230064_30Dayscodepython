import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

class GradeFinder(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Mencari Nilai Seseorang")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.name_label = QLabel("Nama:")
        self.name_input = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        self.find_button = QPushButton("Cari Nilai")
        self.find_button.clicked.connect(self.find_grade)
        layout.addWidget(self.find_button)

        self.table = QTableWidget()
        self.table.setRowCount(5)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Nama"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Nilai"))
        layout.addWidget(self.table)

        self.setLayout(layout)

        self.grades = {
            "Jose": "A",
            "Rasyid": "B",
            "Rahman": "A",
            "Abi": "B",
            "Mahmudi": "A"
        }

    def find_grade(self):
        name = self.name_input.text()
        if name in self.grades:
            self.table.setItem(0, 0, QTableWidgetItem(name))
            self.table.setItem(0, 1, QTableWidgetItem(self.grades[name]))
        else:
            self.table.setItem(0, 0, QTableWidgetItem("Nama tidak ditemukan"))
            self.table.setItem(0, 1, QTableWidgetItem(""))

    def closeEvent(self, event):
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    finder = GradeFinder()
    finder.show()
    sys.exit(app.exec_())