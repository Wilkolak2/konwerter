import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class myForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.cmValue.textChanged.connect(self.cmToCal)
        self.ui.calValue.textChanged.connect(self.calToCm)

        self.ui.mValue.textChanged.connect(self.mToFeet)
        self.ui.sValue.textChanged.connect(self.feetToM)

        self.ui.kmValue.textChanged.connect(self.kmToMile)
        self.ui.milValue.textChanged.connect(self.mileToKm)

        self.show()

    def cmToCal(self):
        toConvert = self.ui.cmValue.text()
        try:
            toConvert = float(toConvert)
            convert = toConvert/2.54
            self.ui.calValue.setText(f'{convert}')
        except ValueError:
            self.ui.cmValue.setText('')

    def calToCm(self):
        toConvert = self.ui.calValue.text()
        try:
            toConvert = float(toConvert)
            convert = toConvert*2.54
            self.ui.cmValue.setText(f'{convert}')
        except ValueError:
            self.ui.calValue.setText('')

    def mToFeet(self):
        toConvert = self.ui.mValue.text()
        try:
            toConvert = float(toConvert)
            convert = toConvert*3.37
            self.ui.sValue.setText(f'{convert}')
        except ValueError:
            self.ui.mValue.setText('')

    def feetToM(self):
        toConvert = self.ui.sValue.text()
        try:
            toConvert = float(toConvert)
            convert = toConvert/3.37
            self.ui.mValue.setText(f'{convert}')
        except ValueError:
            self.ui.sValue.setText('')

    def kmToMile(self):
        toConvert = self.ui.kmValue.text()
        try:
            toConvert = float(toConvert)
            convert = toConvert/1.6
            self.ui.milValue.setText(f'{convert}')
        except ValueError:
            self.ui.kmValue.setText('')

    def mileToKm(self):
        toConvert = self.ui.milValue.text()
        try:
            toConvert = float(toConvert)
            convert = toConvert*1.6
            self.ui.kmValue.setText(f'{convert}')
        except ValueError:
            self.ui.milValue.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = myForm()
    sys.exit(app.exec())