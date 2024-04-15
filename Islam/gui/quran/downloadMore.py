from .downloadTafseer import DownloadTafseer
from .downloadTranslations import DownloadTranslations
from .downloadReciter import DownloadReciter
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class DownloadMore(qt.QDialog):
    def __init__(self,p):
        super().__init__(p)
        self.setWindowTitle(_("download more tools"))
        self.tafseer=qt.QPushButton(_("tafseer "))
        self.tafseer.clicked.connect(lambda:DownloadTafseer(self).exec())
        self.translation=qt.QPushButton(_("translation"))
        self.translation.clicked.connect(lambda:DownloadTranslations(self).exec())
        layout=qt.QVBoxLayout(self)
        self.reciter=qt.QPushButton(_("current reciter"))
        self.reciter.clicked.connect(lambda:DownloadReciter(self).exec())
        layout.addWidget(self.reciter)
        layout.addWidget(self.tafseer)
        layout.addWidget(self.translation)