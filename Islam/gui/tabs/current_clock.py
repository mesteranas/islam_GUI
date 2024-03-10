import random,os,json
import winsound
import settings,guiTools
import datetime
import aladhan
import hijri_converter
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class CurrentClock(qt.QWidget):
    def __init__(self,p):
        super().__init__()
        self.list=qt.QListWidget()
        self.change()
        layout=qt.QVBoxLayout(self)
        layout.addWidget(self.list)
        self.sibha=qt2.QTimer(self)
        self.sibha.timeout.connect(self.sibhaTimer)
        if settings.settings_handler.get("sibha","run")=="True":
            i=int(settings.settings_handler.get("sibha","duration"))
            self.sibha.start(i*60000)
        self.readQuranTimer=qt2.QTimer(self)
        self.readQuranTimer.timeout.connect(self.readQuran)
        if settings.settings_handler.get("readQuran","run")=="True":
            i=int(settings.settings_handler.get("readQuran","duration"))
            self.readQuranTimer.start(i*60000)
        self.nextPrayer=self.getPrayer()
        self.prayerTimer=qt2.QTimer(self)
        self.prayerTimer.timeout.connect(self.on_prayerTimer)
        self.prayerTimer.start(60000)
        self.on_prayerTimer()
    def Change(self,key):
        prayersDect={"Fajr":_("Fajr"),"Dhuhr":_("Dhuhr"),"Asr":_("Asr"),"Maghrib":_("Maghrib"),"Isha":_("Isha")}
        try:
            return prayersDect[key]
        except:
            return key

    def change(self):
        self.list.clear()
        try:
            client=aladhan.Client(aladhan.City(settings.settings_handler.get("prayerTimes","city"),settings.settings_handler.get("prayerTimes","country")))
            adhans = client.get_today_times()
            for adhan in adhans:
                self.list.addItem(self.Change(adhan.get_en_name()) + _(" at ") + adhan.readable_timing(show_date=False))
        except Exception as e:
            qt.QMessageBox.information(self,_("error"),_("please try later"))
        date = datetime.datetime.now().strftime("%d/%m/%Y")
        hijriDate=str(hijri_converter.Hijri.today()).split("-")
        weekday_names = [_("Monday"), _("Tuesday"), _("Wednesday"), _("Thursday"), _("Friday"), _("Saturday"), _("Sunday")]
        hijri={"1": _("Muharram"),"2": _("Safar"),"3": _("Rabi' al-awwal"),"4": _("Rabi' al-thani"),"5": _("Jumada al-awwal"),"6": _("Jumada al-thani"),"7": _("Rajab"),"8": _("Sha'ban"),"9": _("Ramadan"),"10": _("Shawwal"),"11": _("Dhu al-Qi'dah"),"12": _("Dhu al-Hijjah")}
        if hijriDate[1].startswith("0"):
            hijriDate[1]=hijriDate[1][1]
        self.list.addItems([_("date : {} {}").format(weekday_names[datetime.datetime.now().weekday()],date),_(" hijri date : {}  {}  {}").format(hijriDate[2],hijri[hijriDate[1]],hijriDate[0])])
    def sibhaTimer(self):
        getType=settings.settings_handler.get("sibha","type")
        if getType=="0":
            with open("data/json/azkar.json","r",encoding="utf-8")as json_file:
                r=random.choice(json.load(json_file)["azkar"])
            guiTools.speak(_("alazkar") + r)
        elif getType=="1":
            path="data/sounds/sibha"
            r=random.choice(os.listdir(path))
            winsound.PlaySound(path + "/" + r,1)
    def readQuran(self):
        with open("data/json/quran.json","r",encoding="utf-8-sig") as json_file:
            content=json.load(json_file)
        soura=random.choice(list(content.keys()))
        ayah=random.choice(content[soura]["ayahs"])
        guiTools.speak(content[soura]["name"] + ayah["text"] + str(ayah["numberInSurah"]))
    def getNextPrayer(self):
        try:
            client=aladhan.Client(aladhan.City(settings.settings_handler.get("prayerTimes","city"),settings.settings_handler.get("prayerTimes","country")))
            adhans = client.get_today_times()
            for adhan in adhans:
                time=str(datetime.datetime.strptime(str(adhan.readable_timing(show_date=False)),"%I:%M (%p)").strftime("%H : %M")).split(" : ")
                now=str(datetime.datetime.now().strftime("%H:%M:%p")).split(":")
                hour=int(time[0])
                NowHour=int(now[0])
                minute=int(time[1])
                nowMinute=int(now[1])
                if hour > NowHour:
                    return self.Change(adhan.get_en_name()) + _(" at ") +  adhan.readable_timing(show_date=False)
                if hour==NowHour:
                    if minute>=nowMinute:
                        return self.Change(adhan.get_en_name()) + _(" at ") +  adhan.readable_timing(show_date=False)
                    else:
                        continue
            return self.Change(adhans[0].get_en_name()) + _(" at ") +  adhans[0].readable_timing(show_date=False)
        except:
            return _("error")
    def getPrayer(self):
        text=self.getNextPrayer().split(" at ")
        time=str(datetime.datetime.strptime(str(text[1]),"%I:%M (%p)").strftime("%H : %M")).split(" : ")
        hour=int(time[0])
        minute=int(time[1])
        return hour*3600000 + minute*60000
    def on_prayerTimer(self):
        now=str(datetime.datetime.now().strftime("%H:%M")).split(":")
        NowHour=int(now[0])
        nowMinute=int(now[1])
        time=NowHour*3600000 + nowMinute*60000
        if time==self.nextPrayer:
            if settings.settings_handler.get("prayerReminders","adaan")=="True":
                winsound.PlaySound("data/sounds/adaan/{}".format(settings.settings_handler.get("prayerReminders","adaanVoice")),1)
            self.getPrayer()
        elif self.nextPrayer==time+int(settings.settings_handler.get("prayerReminders","beforDuration"))*60000:
            if settings.settings_handler.get("prayerReminders","beforAdaan")=="True":
                guiTools.speak("Prayer approached")