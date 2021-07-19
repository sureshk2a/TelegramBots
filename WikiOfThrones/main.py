import json, telebot, requests

API_KEY = json.load(open('keys.json',))['wikiOfThronesBot']
bot = telebot.TeleBot(API_KEY)

characterUrl = "https://anapioficeandfire.com/api/characters?name="
allBooksUrl = "https://www.anapioficeandfire.com/api/books"
allHousesUrl = "https://www.anapioficeandfire.com/api/houses"

def getAllBooks():
  response = requests.get(allBooksUrl)
  allBooks = [item.get("name") for item in response.json()]
  return "\n".join(allBooks)

def getAllHouses():
  response = requests.get(allHousesUrl)
  houses = [item.get("name") for item in response.json()]
  return "\n".join(houses)

def getCharacterDetail(name):
  details = {}
  response = requests.get(characterUrl+name)
  if(len(response.json())==0):
    return "No character is in the name of"+name
  response = response.json()[0]
  wantedDetails = ["name","gender","culture","born","died","titles","aliases","father","mother","spouse","tvSeries","playedBy"] 
  for key in response.keys():
    if(key in wantedDetails):
        details[key] = response[key]
  return "\n".join(json.dumps(details).split(",")).replace("{","").replace("}","")



@bot.message_handler(commands=['help'])
def greet(message):
  bot.reply_to(message, "I sure do help you!\nYou can get the info of a game of Thrones\n character by typing their name prefixed by /get ex:(/get John Snow)")

@bot.message_handler(commands=['get'])
def getCharacterInfo(message):
  modified_message = " ".join(str(message.text).split("get")[1::]).strip()
  print("Searching for: "+modified_message)
  if("books" in str(modified_message).lower()):
    bot.send_message(message.chat.id,str(getAllBooks()))
  elif("houses" in str(modified_message).lower()):
    bot.send_message(message.chat.id,str(getAllHouses()))
  else:
    bot.send_message(message.chat.id,getCharacterDetail(modified_message))
bot.polling()