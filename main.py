import json, re, os
from collections import OrderedDict

highscores = {}
currency = {}
uniques_quick = {}
proph_quick = {}
divcard_quick = {}

with open("Data\\DivinationCard.json", "r") as read_file:
	DivCard = json.load(read_file)

with open("Data\\Currency.json", "r") as read_file:
	Curr = json.load(read_file)

with open("Data\\Prophecy.json", "r") as read_file:
	Proph = json.load(read_file)
	
with open("forbidden.txt", "r") as read_file:
	forbidden = read_file.readlines()
forbidden = [x.strip() for x in forbidden] 
	
currency["Chaos Orb"] = 1
for item in Curr["lines"]:
	currency[item["currencyTypeName"]] = item["receive"]["value"]

for file in os.listdir("Uniquedata"):
	file_loc = "Uniquedata" + "\\" + file
	with open(file_loc, "r") as read_file:
		data = json.load(read_file)
		
	for item in data["lines"]:
		uniques_quick[item["name"]] = item["chaosValue"]

for item in Proph["lines"]:
	proph_quick[item["name"]] = item["chaosValue"]
	
for item in DivCard["lines"]:
	divcard_quick[item["name"]] = item["chaosValue"]

def name_pass(name):
	if name in forbidden:
		return True
	else:
		return False	
		
for item in DivCard["lines"]:
	name = item["name"]
	if name_pass(name):
		continue
	chaos_value = item["chaosValue"]
	stack = item["stackSize"]
	total_cost = item["chaosValue"] * item["stackSize"]
	type_what = item["explicitModifiers"][0]["text"]
	match = re.match("<(.*)>{(.*)}", type_what)
	if match:
		if (match.group(1) == "currencyitem"):
			reward_type = "Currency"
			items = match.group(2).split("x ")
			if len(items) == 1:
				items.insert(0, "1")
			if (items[1] == "Master Cartographer's Sextant"):
				items[1] = "Awakened Sextant"
			
			try:
				reward_value = currency[items[1]] * float(items[0])
			except KeyError:
				print(name)
				
			profit = round((reward_value - total_cost), 2)
			if stack == 0:
				stack = 1
			highscores[name] = {"Type": reward_type, "Profit": profit, "Cost": chaos_value, "Stack": stack, "Profitpercard": round(profit/stack, 2), "Total": total_cost, "Sellprice": reward_value}
		
		if (match.group(1) == "uniqueitem"):
			reward_type = "Unique"
			item_reward = match.group(2)
			if item_reward == "Charan's Sword":
				item_reward = "Oni-Goroshi"
			if name == "Azyran's Reward":
				item_reward = "The Anima Stone"
			
			try:
				reward_value = uniques_quick[item_reward]
			except KeyError:
				print(name)
			
			profit = round((reward_value - total_cost), 2)
			highscores[name] = {"Type": reward_type, "Profit": profit, "Cost": chaos_value, "Stack": stack, "Profitpercard": round(profit/stack, 2), "Total": total_cost, "Sellprice": reward_value}
		
		if (match.group(1) == "prophecy"):
			reward_type = "Prophecy"	
			item_reward = match.group(2)
			if item_reward == "Queen's Sacrifice":
				item_reward = "The Queen's Sacrifice"
			
			try:
				reward_value = proph_quick[item_reward]
			except KeyError:
				print(name)
				
			profit = round((reward_value - total_cost), 2)
			highscores[name] = {"Type": reward_type, "Profit": profit, "Cost": chaos_value, "Stack": stack, "Profitpercard": round(profit/stack, 2), "Total": total_cost, "Sellprice": reward_value}
		
		if (match.group(1) == "divination"):
			reward_type = "Divination"	
			item_reward = match.group(2)
			
			try:
				reward_value = divcard_quick[item_reward]
			except KeyError:
				print(name)
				
			profit = round((reward_value - total_cost), 2)
			highscores[name] = {"Type": reward_type, "Profit": profit, "Cost": chaos_value, "Stack": stack, "Profitpercard": round(profit/stack, 2), "Total": total_cost, "Sellprice": reward_value}
		
highscores_sorted = OrderedDict(sorted(highscores.items(), key=lambda x: x[1]["Profitpercard"]))
print_true = True
if print_true:
	for item in highscores_sorted:
		print(item + " (" + str(highscores_sorted[item]["Cost"]) + "): ")
		print("Type: " + str(highscores_sorted[item]["Type"]))
		print("Profit: " + str(highscores_sorted[item]["Profit"]))
		print("Profit per card: " + str(highscores_sorted[item]["Profitpercard"]))
		print("Chaos needed: " + str(highscores_sorted[item]["Total"]))
		print("Sell price: " + str(highscores_sorted[item]["Sellprice"]))
		print("Card stack: " + str(highscores_sorted[item]["Stack"]))
		print("-"*100)