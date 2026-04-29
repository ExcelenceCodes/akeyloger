import sys
import os
import configparser
import subprocess
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt

class ALogUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('ALog - Control Dashboard')
        self.setFixedSize(300, 200)

        layout = QVBoxLayout()

        self.status_label = QLabel("Status: STANDBY", self)
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setStyleSheet("font-size: 18px; font-weight: bold; color: gray;")
        
        self.btn_on = QPushButton('START SERVICE', self)
        self.btn_on.setStyleSheet("background-color: #2ecc71; color: white; padding: 10px;")
        self.btn_on.clicked.connect(self.turn_on)

        self.btn_off = QPushButton('STOP SERVICE', self)
        self.btn_off.setStyleSheet("background-color: #e74c3c; color: white; padding: 10px;")
        self.btn_off.clicked.connect(self.turn_off)

        layout.addWidget(self.status_label)
        layout.addWidget(self.btn_on)
        layout.addWidget(self.btn_off)

        self.setLayout(layout)

    def set_state(self, status):
        config = configparser.ConfigParser()
        config['Status'] = {'active': status}
        with open('state.ini', 'w') as configfile:
            config.write(configfile)

    def turn_on(self):
        self.set_state('on')
        self.status_label.setText("Status: ACTIVE")
        self.status_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #2ecc71;")
        # Launch the hidden background logger
        subprocess.Popen(['python', 'logger.py'], 
                         creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)

    def turn_off(self):
        self.set_state('off')
        self.status_label.setText("Status: STOPPING...")
        self.status_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #e74c3c;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ALogUI()
    ex.show()
    sys.exit(app.exec())