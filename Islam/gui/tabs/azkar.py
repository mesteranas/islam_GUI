import json
import gui
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class Azkar(qt.QWidget):
    def __init__(self,p):
        super().__init__()
        self.dict={
            _("azkar el-masaa"):"azkar-masaa.json",
            _("azkar el-sabah"):"azkar-sabah.json"
        }
        self.select=qt.QComboBox()
        self.select.addItems(self.dict.keys())
        self.open=qt.QPushButton(_("open"))
        self.open.setDefault(True)
        self.open.clicked.connect(self.on_open)
        layout=qt.QFormLayout(self)
        layout.addRow(_("select"),self.select)
        layout.addWidget(self.open)
    def on_open(self):
        with open("data/json/doaa/{}".format(self.dict[self.select.currentText()]),"r",encoding="utf-8-sig") as data:
            gui.quran.Azkar(self,json.load(data)).exec()