import  json,os
import settings
settings.language.init_translation()
with open("data/json/quran.json","r",encoding="utf-8-sig") as file:
    qdata=json.load(file)

def getSurah():
    surahs={}
    for key,value in qdata.items():
        surahs[str(value["number"])+value["name"]]=[int(key),value["numberOfAyahs"]]
    return surahs
def all (from_surah,from_ayah,to_surah,to_ayah,tafseer_file):
    with open("data/json/tafseer/{}".format(tafseer_file),"r",encoding="utf-8-sig") as file:
        data=json.load(file)
    result=[]
    for t in data:
        if from_surah==int(t["number"]):
            if from_ayah<=int(t["aya"]):
                result.append(t["text"])
        if to_surah==int(t["number"]):
            if to_ayah==int(t["aya"]):
                break
            elif from_ayah<int(t["aya"]):
                result.append(t["text"])
        elif from_surah<int(t["number"]):
            result.append(t["text"])
    return "\n".join(result)
tafseers={"al-baghawi.json":_("al-baghawi"),"al-qurtubi.json":_("al-qurtubi"),"al-saddi.json":_("al-saddi"),"al-tabari.json":_("al-tabari"),"al-wasit.json":_("al-wasit"),"el-moisr.json":_("el-moisr"),"ibn-kathir.json":_("ibn-kathir"),"tanwir-al-miqbas.json":_("tanwir-al-miqbas")}
def getTafseers():
    result=[]
    for item in os.listdir("data/json/tafseer"):
        try:
            result.append(tafseers[item])
        except:
            pass
    return result
def getbook(text):
    r={}
    for key,value in tafseers.items():
        r[value]=key
    return r[text]