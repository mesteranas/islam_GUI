import  json
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
