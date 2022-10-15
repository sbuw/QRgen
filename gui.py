import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from ui import Ui_MainWindow
import main
from config import PATH


class QRgen(QtWidgets.QMainWindow):
    def __init__(self):
        super(QRgen, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QRgen')
        self.ui.pushButton.clicked.connect(self.generate_qr)

    def generate_qr(self):
        name = self.ui.lineEdit.text()
        text = self.ui.lineEdit_2.text()
        main.generate(name, text)
        self.ui.label.setPixmap(QPixmap(f"{PATH}{name}.png"))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = QRgen()
    application.show()

    sys.exit(app.exec())
