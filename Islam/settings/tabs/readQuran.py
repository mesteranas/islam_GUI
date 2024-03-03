import guiTools,update
import zipfile
import sys
import os,shutil
from settings import settings_handler,app
from settings import language
import PyQt6.QtWidgets as qt
import sys
import PyQt6.QtGui as qt1
from PyQt6.QtCore import Qt
language.init_translation()
class ReadQuran(qt.QWidget):
    def __init__(self,p):
        super().__init__()
        self.run=qt.QCheckBox(_("run send random Ayah"))
        self.run.setChecked(p.cbts(settings_handler.get("readQuran","run")))
        self.duration=qt.QSlider()
        self.duration.setRange(1,60)
        self.duration.setValue(int(settings_handler.get("readQuran","duration")))
        layout=qt.QFormLayout(self)
        layout.addWidget(self.run)
        layout.addRow(_("duration using minutes"),self.duration)
