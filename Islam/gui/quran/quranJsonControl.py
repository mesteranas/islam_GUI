import json
with open("data/json/quran.json","r",encoding="utf-8-sig") as file:
    data=json.load(file)
def getSurahs():
    surahs={}
    for key,value in data.items():
        ayahs={}
        for ayah in value["ayahs"]:
            ayahs["{} ({})".format(ayah["text"],str(ayah["numberInSurah"]))]=ayah["numberInSurah"]
        surahs[str(value["number"])+value["name"]]=[key,"\n".join(ayahs)]
    return surahs