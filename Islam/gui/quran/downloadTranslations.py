import json
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
            r=requests.get("https://raw.githubusercontent.com/mesteranas/{}/main/{}/data/json/translation/{}".format(settings.settings_handler.appName,settings.app.appdirname,self.text))
            with open("data/json/translation/{}".format(self.text),"wb") as data:
                data.write(r.content)
            self.objects.finch.emit(True)
        except Exception as e:
            self.objects.finch.emit(False)
class DownloadTranslations(qt.QDialog):
    def __init__(self,p):
        super().__init__(p)
        self.setWindowTitle(_("download  translation"))
        self.tafseers=qt.QComboBox()
        self.tafseers.addItems(gui.quran.translation.on_get(None))
        self.download=qt.QPushButton(_("download"))
        self.download.clicked.connect(self.on_download)
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
            self.close()