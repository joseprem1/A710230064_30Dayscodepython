import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget, QFileDialog

class FileSearchApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("File Search App")
        
        self.label = QLabel("Enter file name to search:")
        self.search_input = QLineEdit()
        
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_file)
        
        self.result_label = QLabel()
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.search_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.result_label)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def search_file(self):
        file_name = self.search_input.text()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(self, "Search File", "", "All Files (*);;Text Files (*.txt)", options=options)
        
        if file_path:
            if file_name in file_path:
                self.result_label.setText(f"File found: {file_path}")
            else:
                self.result_label.setText("File not found.")
        else:
            self.result_label.setText("File not selected.")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileSearchApp()
    window.show()
    sys.exit(app.exec_())
