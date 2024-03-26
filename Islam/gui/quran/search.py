from . import quranJsonControl
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class Search(qt.QDialog):
    def __init__(self,p,from_surah,from_ayah,to_surah,to_ayah):
        super().__init__(p)
        self.setWindowTitle(_("quran searcher"))
        self.ayahs=quranJsonControl.getQuran(from_surah,from_ayah,to_surah,to_ayah)
        layout=qt.QVBoxLayout(self)
        self.keyword=qt.QLineEdit()
        self.keyword.setAccessibleName(_("search"))
        layout.addWidget(self.keyword)
        self.searchButton=qt.QPushButton(_("search"))
        self.searchButton.clicked.connect(self.on_search)
        layout.addWidget(self.searchButton)
        self.result=qt.QListWidget()
        self.result.setAccessibleName(_("result"))
        layout.addWidget(self.result)
    def on_search(self):
        self.result.clear()
        self.result.addItems(quranJsonControl.searchinquran(self.keyword.text(),self.ayahs))
        self.result.setFocus()