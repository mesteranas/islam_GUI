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
class Sibha(qt.QWidget):
    def __init__(self,p):
        super().__init__()
        self.run=qt.QCheckBox(_("run sibha"))
        self.run.setChecked(p.cbts(settings_handler.get("sibha","run")))
        self.duration=qt.QSlider()
        self.duration.setRange(1,60)
        self.duration.setValue(int(settings_handler.get("sibha","duration")))
        self.type=qt.QComboBox()
        self.type.addItems([_("notification message"),_("sound")])
        self.type.setCurrentIndex(int(settings_handler.get("sibha","type")))
        layout=qt.QFormLayout(self)
        layout.addWidget(self.run)
        layout.addRow(_("duration using minutes"),self.duration)
        layout.addRow(_("type"),self.type)