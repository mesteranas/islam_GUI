import guiTools,gui
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class Quran(qt.QWidget):
    def __init__(self,p):
        super().__init__()
        self.brows=qt.QComboBox()
        self.brows.addItems([_("surahs"),_("pages"),_("juzes"),_("Quarters")])
        self.brows.currentIndexChanged.connect(self.change)
        self.select=qt.QComboBox()
        self.go=qt.QPushButton(_("read quran"))
        self.go.setDefault(True)
        self.go.clicked.connect(lambda:guiTools.TextViewer(self,self.select.currentText(),self.content[self.select.currentText()][1]).exec())
        layout=qt.QFormLayout(self)
        layout.addRow(_("brows by"),self.brows)
        layout.addRow(_("select"),self.select)
        layout.addWidget(self.go)
        self.content=[]
        self.change(self.brows.currentIndex())
    def change(self,index):
        if index==0:
            self.content=gui.quran.quranJsonControl.getSurahs()
        elif index==1:
            self.content=gui.quran.quranJsonControl.getPage()
        elif index==2:
            self.content=gui.quran.quranJsonControl.getJuz()
        elif index==3:
            self.content=gui.quran.quranJsonControl.getHezb()
        self.select.clear()
        self.select.addItems(self.content.keys())