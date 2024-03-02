import settings
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
        self.list.addItems([_("date : {} {}").format(weekday_names[datetime.datetime.now().weekday()],date),_(" hijri date : {} / {} / {}").format(hijriDate[2],hijriDate[1],hijriDate[0]),_("hijri munth name {}").format(hijri[hijriDate[1]])])
