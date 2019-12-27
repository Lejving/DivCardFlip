import urllib.request, json, os
from urllib.request import Request, urlopen

if not os.path.exists("Data"):
    os.makedirs("Data")

if not os.path.exists("Uniquedata"):
    os.makedirs("Uniquedata")
    
Leaguename = "Metamorph"

currency_url = 'https://poe.ninja/api/data/currencyoverview?league=' + Leaguename + '&type=Currency'
div_url = 'https://poe.ninja/api/data/itemoverview?league=' + Leaguename + '&type=DivinationCard'


uniques = [
'https://poe.ninja/api/data/itemoverview?league=' + Leaguename +'&type=UniqueMap',
'https://poe.ninja/api/data/itemoverview?league=' + Leaguename +'&type=UniqueJewel',
'https://poe.ninja/api/data/itemoverview?league=' + Leaguename +'&type=UniqueFlask',
'https://poe.ninja/api/data/itemoverview?league=' + Leaguename +'&type=UniqueWeapon',
'https://poe.ninja/api/data/itemoverview?league=' + Leaguename +'&type=UniqueArmour',
'https://poe.ninja/api/data/itemoverview?league=' + Leaguename +'&type=UniqueAccessory',
]

prophecies_url = 'https://poe.ninja/api/data/itemoverview?league=' + Leaguename + '&type=Prophecy'

##CURRENCY
temp = currency_url.split("/")
temp = temp[5].split("=")
name = temp[2]

req = Request(currency_url, headers={'User-Agent': 'Mozilla/5.0'})
web_byte = urlopen(req).read()
data = json.loads(web_byte.decode())

with open("Data//" + name + ".json", 'w+') as outfile:  
	json.dump(data, outfile)
	

##DIV
temp = div_url.split("/")
temp = temp[5].split("=")
name = temp[2]

req = Request(div_url, headers={'User-Agent': 'Mozilla/5.0'})
web_byte = urlopen(req).read()
data = json.loads(web_byte.decode())

with open("Data//" + name + ".json", 'w+') as outfile:  
	json.dump(data, outfile)

##Prophecies
temp = prophecies_url.split("/")
temp = temp[5].split("=")
name = temp[2]

req = Request(prophecies_url, headers={'User-Agent': 'Mozilla/5.0'})
web_byte = urlopen(req).read()
data = json.loads(web_byte.decode())

with open("Data//" + name + ".json", 'w+') as outfile:  
	json.dump(data, outfile)
	
##UNIQUES 
for url in uniques:
	temp = url.split("/")
	temp = temp[5].split("=")
	name = temp[2]
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	web_byte = urlopen(req).read()
	data = json.loads(web_byte.decode())
	
	with open("Uniquedata//" + name + ".json", 'w') as outfile:  
		json.dump(data, outfile)