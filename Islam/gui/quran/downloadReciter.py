import os
from . import quranJsonControl
import json
import requests
import guiTools,gui,settings
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class downloadObjects(qt2.QObject):
    progress=qt2.pyqtSignal(int)
    downloaded=qt2.pyqtSignal(int)
    pauseDownloading=qt2.pyqtSignal(str)
    finch=qt2.pyqtSignal(bool)
class downloadThread(qt2.QRunnable):
    def __init__(self,p):
        super().__init__()
        self.objects=downloadObjects()
        self.pause=False
        self.objects.pauseDownloading.connect(self.on_pause)
    def on_pause(self,s):
        self.pause=True
    def  run(self):
        try:
            count=0
            for key,value in quranJsonControl.data.items():
                for ayah in value["ayahs"]:
                    if not self.pause:
                        if not os.path.exists(os.path.join("data","reciters")):
                            os.makedirs(os.path.join("data","reciters"))
                        if not os.path.exists(os.path.join("data","reciters",settings.settings_handler.get("quran","reciter"))):
                            os.makedirs(os.path.join("data","reciters",settings.settings_handler.get("quran","reciter")))
                        file=self.on_set(key,ayah["numberInSurah"])
                        if os.path.exists("data/reciters/" + settings.settings_handler.get("quran","reciter") + "/" + file):
                            count+=1
                            self.objects.downloaded.emit(count)
                        else:
                            with requests.get(settings.tabs.quran.quranDict[settings.settings_handler.get("quran","reciter")] + file,stream=True) as r:
                                if r.status_code!=200:
                                    self.objects.finsh.emit(False)
                                    return
                                size=r.headers.get("content-length")
                                try:
                                    size=int(size)
                                except TypeError:
                                    self.objects.finsh.emit(False)
                                    return
                                recieved=0
                                progress=0
                                with open("data/reciters/" + settings.settings_handler.get("quran","reciter") + "/" + file,"wb") as file:
                                    for pk in r.iter_content(1024):
                                        file.write(pk)
                                        recieved+=len(pk)
                                        progress=int((recieved/size)*100)
                                        self.objects.progress.emit(progress)
                            count+=1
                            self.objects.downloaded.emit(count)
            self.objects.finch.emit(True)
        except Exception as e:
            print(e)
            self.objects.finch.emit(False)
    def on_set(self,surah,Ayah):
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

class DownloadReciter(qt.QDialog):
    def __init__(self,p):
        super().__init__(p)
        self.setWindowTitle(_("download tafseer"))
        self.progress=qt.QProgressBar()
        self.downloaded=qt.QSpinBox()
        self.downloaded.setAccessibleName(_("numbrt of ayahs downloaded"))
        self.downloaded.setRange(0,7000)
        self.downloaded.setReadOnly(True)
        self.pause=qt.QPushButton(_("pause"))
        layout=qt.QVBoxLayout(self)
        layout.addWidget(self.progress)
        layout.addWidget(self.downloaded)
        layout.addWidget(self.pause)
        thread=qt2.QThreadPool(self)
        run=downloadThread(self)
        run.objects.finch.connect(self.on)
        run.objects.progress.connect(self.on_progress)
        run.objects.downloaded.connect(self.on_downloaded)
        thread.start(run)
        self.pause.clicked.connect(lambda:run.objects.pauseDownloading.emit("a"))
    def on(self,state):
        if state==True:
            qt.QMessageBox.information(self,_("done"),_("downloaded"))
            self.close()
        else:
            qt.QMessageBox.information(self,_("error"),_("please try later"))
            self.close()
    def on_progress(self,progress):
        self.progress.setValue(progress)
    def on_downloaded(self,count):
        self.downloaded.setValue(count)