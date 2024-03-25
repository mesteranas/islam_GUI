import guiTools,update,gui
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
translations = {
    "ibrahim_alakhdar": _("Ibrahim Al-Akhdar"),
    "shaik_abu_baker_alshatri": _("Shaik Abu Baker Al-Shatri"),
    "ahmed_alajmy": _("Ahmed Al-Ajmy"),
    "ahmed_neana": _("Ahmed Neana"),
    "akram_alalaqmy": _("Akram Al-Alaqmy"),
    "warsh": _("Warsh"),
    "khalid_alqahtani": _("Khalid Al-Qahtani"),
    "khalefa_altunaiji": _("Khalefa Al-Tunaiji"),
    "saud_alshuraim": _("Saud Al-Shuraim"),
    "sahl_yassin": _("Sahl Yassin"),
    "salah_albudair": _("Salah Albudair"),
    "salaah_bukhatir": _("Salaah Bukhatir"),
    "data": _("Data"),
    "abdulbasit_abdulsamad_mujawwad": _("Abdulbasit Abdulsamad Mujawwad"),
    "abdurrahmaan_alsudais": _("Abdurrahmaan Al-Sudais"),
    "abdullah_almatroud": _("Abdullah Al-Matroud"),
    "abdullah_basfar": _("Abdullah Basfar"),
    "abdullaah_aljohani": _("Abdullaah Al-Johani"),
    "abdulmohsin_alqasim": _("Abdulmohsin Al-Qasim"),
    "ali_alhuthaify": _("Ali Al-Huthaify"),
    "ali_jaber": _("Ali Jaber"),
    "ali_hajjaj": _("Ali Hajjaj"),
    "fares_abbad": _("Fares Abbad"),
    "nasser_alqatami": _("Nasser Al-Qatami"),
    "hani_alrifai": _("Hani Al-Rifai"),
    "yasser_aldossary": _("Yasser Aldossary"),
    "maher_almuaiqly": _("Maher Al-Muaiqly"),
    "mohammad_altablaway": _("Mohammad Al-Tablaway"),
    "mohammad_ayyoub": _("Mohammad Ayyoub"),
    "mohammad_jibreel": _("Mohammad Jibreel"),
    "mohammad_alminshawi": _("Mohammad Al-Minshawi"),
    "mohammad_alminshawi_mujawwd": _("Mohammad Al-Minshawi Mujawwad"),
    "mohammad_abdulkarim": _("Mohammad Abdulkarim"),
    "mahmood_alhusary": _("Mahmood Al-Husary"),
    "mahmood_alhusary_mujawwd": _("Mahmood Al-Husary Mujawwad"),
    "mahmoud_ali_albanna": _("Mahmoud Ali Albanna"),
    "mishary_alafasy": _("Mishary Al-Afasy"),
    "yaser_salamah": _("Yaser Salamah"),
    "mahmood_alhusary_muallim": _("Mahmood Al-Husary Muallim")
}
quranDict={"ibrahim_alakhdar": "https://verse.mp3quran.net/arabic/ibrahim_alakhdar/32/", "shaik_abu_baker_alshatri": "https://verse.mp3quran.net/arabic/shaik_abu_baker_alshatri/128/", "ahmed_alajmy": "https://verse.mp3quran.net/arabic/ahmed_alajmy/128/", "ahmed_neana": "https://verse.mp3quran.net/arabic/ahmed_neana/128/", "akram_alalaqmy": "https://verse.mp3quran.net/arabic/akram_alalaqmy/128/", "warsh": "http://www.everyayah.com/data/warsh/warsh_ibrahim_aldosary_128kbps/", "khalid_alqahtani": "https://verse.mp3quran.net/arabic/khalid_alqahtani/128/", "khalefa_altunaiji": "https://verse.mp3quran.net/arabic/khalefa_altunaiji/64/", "saud_alshuraim": "https://verse.mp3quran.net/arabic/saud_alshuraim/128/", "sahl_yassin": "https://verse.mp3quran.net/arabic/sahl_yassin/128/", "salah_albudair": "https://verse.mp3quran.net/arabic/salah_albudair/128/", "salaah_bukhatir": "https://verse.mp3quran.net/arabic/salaah_bukhatir/128/", "data": "http://www.everyayah.com/data/Karim_Mansoori_40kbps/", "abdulbasit_abdulsamad_mujawwad": "https://verse.mp3quran.net/arabic/abdulbasit_abdulsamad_mujawwad/128/", "abdurrahmaan_alsudais": "https://verse.mp3quran.net/arabic/abdurrahmaan_alsudais/128/", "abdullah_almatroud": "https://verse.mp3quran.net/arabic/abdullah_almatroud/128/", "abdullah_basfar": "https://verse.mp3quran.net/arabic/abdullah_basfar/128/", "abdullaah_aljohani": "https://verse.mp3quran.net/arabic/abdullaah_aljohani/128/", "abdulmohsin_alqasim": "https://verse.mp3quran.net/arabic/abdulmohsin_alqasim/128/", "ali_alhuthaify": "https://verse.mp3quran.net/arabic/ali_alhuthaify/128/", "ali_jaber": "https://verse.mp3quran.net/arabic/ali_jaber/64/", "ali_hajjaj": "https://verse.mp3quran.net/arabic/ali_hajjaj/128/", "fares_abbad": "https://verse.mp3quran.net/arabic/fares_abbad/64/", "nasser_alqatami": "https://verse.mp3quran.net/arabic/nasser_alqatami/128/", "hani_alrifai": "https://verse.mp3quran.net/arabic/hani_alrifai/128/", "yasser_aldossary": "https://verse.mp3quran.net/arabic/yasser_aldossary/128/", "maher_almuaiqly": "https://verse.mp3quran.net/arabic/maher_almuaiqly/128/", "mohammad_altablaway": "https://verse.mp3quran.net/arabic/mohammad_altablaway/128/", "mohammad_ayyoub": "https://verse.mp3quran.net/arabic/mohammad_ayyoub/128/", "mohammad_jibreel": "https://verse.mp3quran.net/arabic/mohammad_jibreel/128/", "mohammad_alminshawi": "https://verse.mp3quran.net/arabic/mohammad_alminshawi/128/", "mohammad_alminshawi_mujawwd": "https://verse.mp3quran.net/arabic/mohammad_alminshawi_mujawwd/128/", "mohammad_abdulkarim": "https://verse.mp3quran.net/arabic/mohammad_abdulkarim/64/", "mahmood_alhusary": "https://verse.mp3quran.net/arabic/mahmood_alhusary/128/", "mahmood_alhusary_mujawwd": "https://verse.mp3quran.net/arabic/mahmood_alhusary_mujawwd/128/", "mahmoud_ali_albanna": "https://verse.mp3quran.net/arabic/mahmoud_ali_albanna/32/", "mishary_alafasy": "https://verse.mp3quran.net/arabic/mishary_alafasy/128/", "yaser_salamah": "https://verse.mp3quran.net/arabic/yaser_salamah/128/", "mahmood_alhusary_muallim": "https://verse.mp3quran.net/arabic/mahmood_alhusary_muallim/128/"}

class Quran(qt.QWidget):
    def __init__(self,p):
        super().__init__()
        self.reciter=qt.QComboBox()
        self.reciter.addItems(translations.values())
        self.tafseer=qt.QComboBox()
        self.tafseer.addItems(gui.quran.tafseerJsonControl.getTafseers())
        self.trans=qt.QComboBox()
        self.trans.addItems(gui.quran.translation.getdict())
        self.reciter.setCurrentText(translations[settings_handler.get("quran","reciter")])
        self.tafseer.setCurrentText(gui.quran.tafseerJsonControl.tafseers[settings_handler.get("quran","tafseer")])
        transD={}
        for key,value in gui.quran.translation.getdict().items():
            transD[value]=key
        self.trans.setCurrentText(transD[settings_handler.get("quran","translation")])
        layout=qt.QFormLayout(self)
        layout.addRow(_("select reciter"),self.reciter)
        layout.addRow(_("select tafseer"),self.tafseer)
        layout.addRow(_("select translation"),self.trans)
    def get(self):
        d={}
        for key,value in translations.items():
            d[value]=key
        return d[self.reciter.currentText()]