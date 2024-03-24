from .downloadTafseer import DownloadTafseer
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class DownloadMore(qt.QDialog):
    def __init__(self,p):
        super().__init__(p)
        self.setWindowTitle(_("download more tools"))
        self.tafseer=qt.QPushButton(_("tafseer "))
        self.tafseer.clicked.connect(lambda:DownloadTafseer(self).exec())
        layout=qt.QVBoxLayout(self)
        layout.addWidget(self.tafseer)