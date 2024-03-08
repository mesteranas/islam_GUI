import json,os
import requests
import guiTools,gui,settings
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class downloadObjects(qt2.QObject):
    finch=qt2.pyqtSignal(bool)
class downloadThread(qt2.QRunnable):
    def __init__(self,p,text):
        super().__init__()
        self.objects=downloadObjects()
        self.text=text
    def  run(self):
        try:
            r=requests.get("https://raw.githubusercontent.com/mesteranas/{}/main/{}/data/json/tafseer/{}".format(settings.settings_handler.appName,settings.app.appdirname,self.text))
            with open("data/json/tafseer/{}".format(self.text),"w",encoding="utf-8-sig") as data:
                json.dump(r.json(),data,ensure_ascii=False,indent=4)
            self.objects.finch.emit(True)
        except Exception as e:
            print(e)
            self.objects.finch.emit(False)
class DownloadTafseer(qt.QDialog):
    def __init__(self,p):
        super().__init__(p)
        self.setWindowTitle(_("download tafseer"))
        List=["al-baghawi.json","al-qurtubi.json","al-saddi.json","al-tabari.json","al-wasit.json","el-moisr.json","ibn-kathir.json","tanwir-al-miqbas.json"]
        for item in os.listdir("data/json/tafseer"):
            List.remove(item)
        self.tafseers=qt.QComboBox()
        self.tafseers.addItems(List)
        self.download=qt.QPushButton(_("download"))
        self.download.clicked.connect(self.on_download)
        if list==[]:
            qt.QMessageBox.warning(self,_("error"),_("all tafseers have been downloaded"))
            self.download.setDisabled(True)
        layout=qt.QVBoxLayout(self)
        layout.addWidget(self.tafseers)
        layout.addWidget(self.download)
    def on_download(self):
        thread=qt2.QThreadPool(self)
        run=downloadThread(self,self.tafseers.currentText())
        run.objects.finch.connect(self.on)
        self.download.setDisabled(True)
        thread.start(run)
    def on(self,state):
        if state==True:
            qt.QMessageBox.information(self,_("done"),_("downloaded"))
            self.close()
        else:
            qt.QMessageBox.information(self,_("error"),_("please try later"))