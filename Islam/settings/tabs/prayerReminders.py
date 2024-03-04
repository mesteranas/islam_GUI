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
class PrayerReminders(qt.QWidget):
    def __init__(self,p):
        super().__init__()
        self.adaan=qt.QCheckBox(_("run adaan"))
        self.adaan.setChecked(p.cbts(settings_handler.get("prayerReminders","adaan")))
        self.beforAdaan=qt.QCheckBox(_("get reminder befor adaan"))
        self.beforAdaan.setChecked(p.cbts(settings_handler.get("prayerReminders","beforAdaan")))
        self.beforDuration=qt.QSlider()
        self.beforDuration.setRange(10,30)
        self.beforDuration.setValue(int(settings_handler.get("prayerReminders","beforDuration")))
        self.adaanVoice=qt.QComboBox()
        self.adaanVoice.addItems(os.listdir("data/sounds/adaan"))
        self.adaanVoice.setCurrentText(settings_handler.get("prayerReminders","adaanVoice"))
        layout=qt.QFormLayout(self)
        layout.addWidget(self.adaan)
        layout.addWidget(self.beforAdaan)
        layout.addRow(_("duration using minutes"),self.beforDuration)
        layout.addRow(_("select adaan voice"),self.adaanVoice)