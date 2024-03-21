import json
with open("data/json/iraab.json","r",encoding="utf-8-sig")as data:
    data=json.load(data)
def Iraab(surah,ayah):
    return data[str(surah)][int(ayah)]["text"]
def get(from_surah,from_ayah,to_surah,to_ayah):
    result=[]
    for t,t1 in data.items():
        if from_surah==int(t):
            for t2 in t1:
                if from_ayah<=int(t1.index(t2))+1:
                    result.append(t2["text"])
            if to_surah==int(t):
                if to_ayah==int(t1.index(t2))+1:
                    break
                elif from_ayah<int(t1.index(t2))+1:
                    result.append(t2["text"])
            elif from_surah<int(t):
                result.append(t2["text"])
    return "\n".join(result)
