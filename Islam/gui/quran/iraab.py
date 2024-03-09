import json
with open("data/json/iraab.json","r",encoding="utf-8-sig")as data:
    data=json.load(data)
def Iraab(surah,ayah):
    return data[str(surah)][int(ayah)]["text"]