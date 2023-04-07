import sys
import serial
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Připojení k sériovému portu
        self.ser = serial.Serial('COM1', 9600)

        # Vytvoření GUI
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('COM port monitor')
        self.com_label = QLabel('COM port:', self)
        self.com_label.move(50, 50)
        self.combo_box = QComboBox(self)
        self.combo_box.addItems(['COM1', 'COM2', 'COM3'])
        self.combo_box.move(120, 50)
        self.button = QPushButton('Connect', self)
        self.button.move(120, 100)
        self.button.clicked.connect(self.connect_clicked)

    def connect_clicked(self):
        # Připojení k nově vybranému portu
        port = self.combo_box.currentText()
        self.ser.port = port
        self.ser.open()

        # Spuštění smyčky pro čtení dat ze sériového portu
        while True:
            data = self.ser.read()
            if data:
                key = chr(data[0])
                self.press_key(key)

    def press_key(self, key):
        # Simulace stisku klávesy
        print(f'Pressed key {key}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
