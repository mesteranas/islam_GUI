import os
import guiTools,gui
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class Tafseer(qt.QWidget):
    def __init__(self,p):
        super().__init__()
        self.surah=gui.quran.tafseerJsonControl.getSurah()
        self.from_surah=qt.QComboBox()
        self.from_surah.addItems(self.surah.keys())
        self.from_surah.currentTextChanged.connect(self.change_from)
        self.from_ayah=qt.QSpinBox()
        self.change_from(self.from_surah.currentText())
        self.to_surah=qt.QComboBox()
        self.to_surah.addItems(self.surah.keys())
        self.to_surah.currentTextChanged.connect(self.change_to)
        self.to_ayah=qt.QSpinBox()
        self.change_to(self.to_surah.currentText())
        self.tafseer_book=qt.QComboBox()
        self.tafseer_book.addItems(gui.quran.tafseerJsonControl.getTafseers())
        self.open=qt.QPushButton(_("open"))
        self.open.setDefault(True)
        self.open.clicked.connect(self.on_open)
        layout=qt.QFormLayout(self)
        layout.addRow(_("from surah:"),self.from_surah)
        layout.addRow(_("from ayah:"),self.from_ayah)
        layout.addRow(_("to surah"),self.to_surah)
        layout.addRow(_("to ayah:"),self.to_ayah)
        layout.addRow(_("tafseer book"),self.tafseer_book)
        layout.addWidget(self.open)
        self.content=""
    def change_from(self,text):
        self.from_ayah.setRange(1,self.surah[text][1])
    def change_to(self,text):
        self.to_ayah.setRange(1,self.surah[text][1])
    def on_open(self):
        index=self.tafseer_book.currentIndex()
        from_surah=self.surah[self.from_surah.currentText()][0]
        to_surah=self.surah[self.to_surah.currentText()][0]
        from_ayah=self.from_ayah.value()
        to_ayah=self.to_ayah.value()
        self.content=gui.quran.tafseerJsonControl.all(from_surah,from_ayah,to_surah,to_ayah,gui.quran.tafseerJsonControl.getbook(self.tafseer_book.currentText()))
        guiTools.TextViewer(self,_("tafseer "),self.content).exec()