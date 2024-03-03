import guiTools
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class ElectronicSibha(qt.QWidget):
    def __init__(self,p):
        super().__init__()
        layout=qt.QVBoxLayout(self)
        self.count=qt.QLabel("0")
        layout.addWidget(self.count)
        self.plus=qt.QPushButton(_("+"))
        self.plus.clicked.connect(self.on_plus)
        self.plus.setDefault(True)
        layout.addWidget(self.plus)
        self.reset=qt.QPushButton(_("reset"))
        self.reset.setDefault(True)
        self.reset.clicked.connect(lambda: self.count.setText("0"))
        layout.addWidget(self.reset)
        qt1.QShortcut("c",self).activated.connect(lambda:guiTools.speak(self.count.text()))
    def on_plus(self):
        num=int(self.count.text())
        self.count.setText(str(num+1))
        guiTools.speak(self.count.text())