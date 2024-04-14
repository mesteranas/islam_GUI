import os
import json
import requests
import settings
def  translation(Surah,Ayah):
    with open("data/json/translation/" + settings.settings_handler.get("quran","translation"),"r",encoding="utf-8-sig")as data:
        data=json.load(data)

    for surah in data:
        if surah["id"]==int(Surah):
            for ayah in surah["verses"]:
                if ayah["id"]==Ayah:
                    return ayah["translation"]
def get(from_surah,from_ayah,to_surah,to_ayah,translation):
    with open("data/json/translation/" + translation,"r",encoding="utf-8-sig")as data:
        data=json.load(data)
    result=[]
    for Surah in data:
        if from_surah==int(Surah["id"]):
            for Ayah in Surah["verses"]:
                if from_ayah<=int(Ayah["id"]):
                    result.append(Ayah["translation"])
            if to_surah==int(Surah["id"]):
                if to_ayah==int(Ayah["id"]):
                    break
                elif from_ayah<int(Ayah["id"]):
                    result.append(Ayah["translation"])
            elif from_surah<int(Surah["id"]):
                result.append(Ayah["translation"])
    return "\n".join(result)
translationDict={"english.json":_("english"),
                 "spanish.json":_("spanish"),
                 "french.json":_("french"),
                 "Bengali .json":_("Bengali "),
                 "Chinese.json":_("Chinese"),
                 "Indonesian.json":_("Indonesian"),
                 "Russian.json":_("Russian"),
                 "Swedish.json":_("Swedish"),
                 "Turkish.json":_("Turkish"),
                 "Urdu.json":_("Urdu")}
def getdict():
    result={}
    for trans in os.listdir("data/json/translation"):
        try:
            result[translationDict[trans]]=trans
        except:
            pass
    return result
def on_get(self):
    r=requests.get("https://raw.githubusercontent.com/mesteranas/{}/main/{}/data/json/files/all_translations.json".format(settings.settings_handler.appName,settings.app.appdirname))
    return r.json()