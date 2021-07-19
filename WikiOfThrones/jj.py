import requests
import json

message = "/get Samwell Tarly"
name = " ".join(message.split("get")[1::])
print("Getting info for for name:"+name)
response = requests.get("https://anapioficeandfire.com/api/characters?name="+name.strip())

# for item in response.json():
#     print(item.get("name"))

#lst = [item.get("region") for item in response.json()]
print("Response Code: "+str(response.status_code))
if(len(response.json())==0):
    print("No character is in the name of"+name)

details = {}

wantedDetails = ["name","gender","culture","born","died","titles","aliases","father","mother","spouse","tvSeries","playedBy"] 

# lst = {"name":"",
#        "gender":"",
#        "culture":"",
#        "born":"",
#        "died":"",
#        "titles":"",
#        "aliases":"",
#        "father":"",
#        "mother":"",
#        "spouse":"",
#        "tvSeries":"",
#        "playedBy":""}

lst = {}

arr = []

for key in response.json()[0].keys():
    if(key in wantedDetails):
        lst[key] = response.json()[0][key]
    # for item in lst.keys():
    #     print(item+" "+key)
    #     if(item.lower() == key.lower()):
    #         print("Is a match: "+item.lower()+" "+key.lower())
    #         lst[item] == response.json()[0][key]

# for key, value in lst.items():
#     arr.append([key, value])

print(lst)

#print(len(response.json()))