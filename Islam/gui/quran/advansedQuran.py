from . import quranJsonControl,tafseerJsonControl,iraab,translation
import guiTools,gui,settings
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
from PyQt6.QtMultimedia import QMediaPlayer,QAudioOutput
class AdvansedQuran (qt.QDialog):
    def __init__(self,p,List,content,index):
        super().__init__(p)
        self.setWindowTitle(_("quran"))
        self.is_playing=False
        self.playToEnd=False
        self.index=index
        self.content=content
        self.ayah=List[1].split("\n")
        self.currentAyah=qt.QLabel(self.ayah[0])
        self.media=QMediaPlayer()
        self.audio=QAudioOutput()
        self.media.setAudioOutput(self.audio)
        self.media.mediaStatusChanged.connect(self.on_state)
        self.showFullScreen()
        self.currentAyahIndex=0
        self.tafseer=qt.QPushButton(_("tafseer"))
        self.tafseer.clicked.connect(self.on_tafseer)
        self.previous=qt.QPushButton(_("previous ayah"))
        self.previous.clicked.connect(self.on_previous)
        qt1.QShortcut("up",self).activated.connect(self.on_previous)
        self.play=qt.QPushButton(_("play ayah"))
        self.play.clicked.connect(self.on_play)
        qt1.QShortcut("space",self).activated.connect(self.on_play)
        self.next=qt.QPushButton(_("next ayah"))
        self.next.clicked.connect(self.on_next)
        qt1.QShortcut("down",self).activated.connect(self.on_next)
        qt1.QShortcut("left",self).activated.connect(lambda:guiTools.speak(self.currentAyah.text()))
        self.next_page=qt.QPushButton(_("next"))
        self.next_page.clicked.connect(self.on_pagenext)
        qt1.QShortcut("alt+right",self).activated.connect(self.on_pagenext)
        self.previous_page=qt.QPushButton(_("previous"))
        self.previous_page.clicked.connect(self.on_pageprevious)
        qt1.QShortcut("alt+left",self).activated.connect(self.on_pageprevious)
        self.gotoayah=qt.QPushButton(_("go to ayah"))
        self.gotoayah.clicked.connect(self.goToAyah)
        qt1.QShortcut("ctrl+shift+g",self).activated.connect(self.goToAyah)
        self.goto=qt.QPushButton(_("Go To"))
        self.goto.clicked.connect(self.goToPage)
        qt1.QShortcut("ctrl+g",self).activated.connect(self.goToPage)
        self.playAll=qt.QPushButton(_("play to the end"))
        self.playAll.clicked.connect(self.on_play_all)
        qt1.QShortcut("ctrl+space",self).activated.connect(self.on_play_all)
        self.iraab=qt.QPushButton(_("Grammar "))
        self.iraab.clicked.connect(self.on_iraab)
        self.translation=qt.QPushButton(_("translation"))
        self.translation.clicked.connect(self.on_translation)
        self.ayahinfo=qt.QPushButton(_("get information for current ayah"))
        self.ayahinfo.clicked.connect(self.on_info)
        layout=qt.QVBoxLayout(self)
        layout.addWidget(self.currentAyah)
        layout.addWidget(self.tafseer)
        layout.addWidget(self.previous)
        layout.addWidget(self.play)
        layout.addWidget(self.next)
        layout.addWidget(self.next_page)
        layout.addWidget(self.previous_page)
        layout.addWidget(self.gotoayah)
        layout.addWidget(self.goto)
        layout.addWidget(self.playAll)
        layout.addWidget(self.iraab)
        layout.addWidget(self.translation)
        layout.addWidget(self.ayahinfo)
    def on_next(self):
        if self.currentAyahIndex==len(self.ayah)-1:
            self.currentAyahIndex=0
        else:
            self.currentAyahIndex+=1
        self.currentAyah.setText(self.ayah[self.currentAyahIndex])
        guiTools.speak(self.currentAyah.text())
    def on_previous(self):
        if self.currentAyahIndex==0:
            self.currentAyahIndex=len(self.ayah)-1
        else:
            self.currentAyahIndex-=1
        self.currentAyah.setText(self.ayah[self.currentAyahIndex])
        guiTools.speak(self.currentAyah.text())
    def on_set(self):
        Ayah,surah,juz,page=quranJsonControl.getAyah(self.currentAyah.text())
        if int(surah)<10:
            surah="00" + surah
        elif int(surah)<100:
            surah="0" + surah
        else:
            surah=str(surah)
        if Ayah<10:
            Ayah="00" + str(Ayah)
        elif Ayah<100:
            Ayah="0" + str(Ayah)
        else:
            Ayah=str(Ayah)
        return surah+Ayah+".mp3"
    def on_play(self):
        if not self.is_playing:
            self.media.setSource(qt2.QUrl(settings.tabs.quran.quranDict[settings.settings_handler.get("quran","reciter")] + self.on_set()))
            self.media.play()
            self.is_playing=True
        else:
            self.media.stop()
            self.is_playing=False
            self.playToEnd=False
    def on_tafseer(self):
        Ayah,surah,juz,page=quranJsonControl.getAyah(self.currentAyah.text())
        guiTools.TextViewer(self,_("tafseer"),tafseerJsonControl.all(int(surah),int(Ayah),int(surah),int(Ayah),settings.settings_handler.get("quran","tafseer"))).exec()
    def on_pagenext(self):
        if self.index==len(self.content)-1:
            self.index=0
        else:
            self.index+=1
        self.ayah=list(self.content)[self.index][1].split("\n")
        self.currentAyah.setText((self.ayah[0]))
        self.currentAyahIndex=0
        guiTools.speak(str(self.index+1))
    def on_pageprevious(self):
        if self.index==0:
            self.index=len(self.content)-1
        else:
            self.index-=1
        self.ayah=list(self.content)[self.index][1].split("\n")
        self.currentAyah.setText((self.ayah[0]))
        self.currentAyahIndex=0
        guiTools.speak(str(self.index+1))
    def on_state(self,state):
        if state==QMediaPlayer.MediaStatus.EndOfMedia:
            self.is_playing=False
            if self.playToEnd:
                self.on_next()
                if not self.currentAyahIndex==0:
                    self.on_play_all()
                else:
                    self.playToEnd=False
    def goToAyah(self):
        text,ok=qt.QInputDialog.getInt(self,_("go to ayah"),_("type ayah number"),self.currentAyahIndex+1,1,len(self.ayah))
        if ok:
            self.currentAyahIndex=text-1
            self.currentAyah.setText(self.ayah[self.currentAyahIndex])
            guiTools.speak(self.currentAyah.text())
    def goToPage(self):
        text,ok=qt.QInputDialog.getInt(self,_("go to "),_("type number"),self.index+1,1,len(self.content))
        if ok:
            self.index=text-1
            self.ayah=list(self.content)[self.index][1].split("\n")
            self.currentAyah.setText((self.ayah[0]))
            self.currentAyahIndex=0
            guiTools.speak(str(self.index+1))
    def on_iraab(self):
        Ayah,surah,juz,page=quranJsonControl.getAyah(self.currentAyah.text())
        guiTools.TextViewer(self,_("Grammar "),iraab.Iraab(surah,int(Ayah)-1)).exec()
    def on_play_all(self):
        if not self.is_playing:
            self.media.setSource(qt2.QUrl(settings.tabs.quran.quranDict[settings.settings_handler.get("quran","reciter")] + self.on_set()))
            self.media.play()
            self.is_playing=True
            self.playToEnd=True
        else:
            self.media.stop()
            self.is_playing=False
            self.playToEnd=False
    def on_translation(self):
        Ayah,surah,juz,page=quranJsonControl.getAyah(self.currentAyah.text())
        guiTools.TextViewer(self,_("translation"),translation.translation(surah,int(Ayah))).exec()
    def on_info(self):
        ayah,surah,juz,page,hizb,sajda=getAyah(self.currentAyah.text())
        qt.QMessageBox.information(self,_("info"),_("ayah {} surah {} juz {} page {} quarter {} sajda: {}".format(ayah,surah,juz,page,hizb,sajda)))

def getAyah(text):
    for key,value in quranJsonControl.data.items():
        for ayah in value["ayahs"]:
            t="{} ({})".format(ayah["text"],str(ayah["numberInSurah"]))
            if t==text:
                return str(ayah["numberInSurah"]),str(key + value["name"]),str(ayah["juz"]),str(ayah["page"]),str(ayah["hizbQuarter"]),str(ayah["sajda"])
    return "1","1","1","1","1","False"