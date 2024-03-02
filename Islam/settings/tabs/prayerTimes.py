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
class PrayerTimes(qt.QWidget):
    def __init__(self,p):
        super().__init__()
        self.country=qt.QComboBox()
        self.country.addItems(guiTools.dictionarys.countries.values())
        self.country.setCurrentText(guiTools.dictionarys.countries[settings_handler.get("prayerTimes","country")])
        self.city=qt.QLineEdit()
        self.city.setText(settings_handler.get("prayerTimes","city"))
        layout=qt.QFormLayout(self)
        layout.addRow(_("country"),self.country)
        layout.addRow(_("city"),self.city)