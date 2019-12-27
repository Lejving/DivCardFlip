# DivCardFlip
A python script that gives you the best divination cards to flip in Path of Exile

Quick tutorial:
1. Run "datadl.py" to get prices
2. Run main.py
3. Flip some divcards!

Forbidden.txt are cards that are forbbiden. Some div cards give for example unique "Axe" and the weights for each unique axe that can possible come from this card is unknown. Therefore we cannot determine how much profit we will get from flipping this card. It is possible to make a worst case scenario and consider every card giving you the worst unique Axe and go on from that, but that feature is not yet included. If there are any cards you don't like, you may add them to the forbidden.txt file and they will not show up when you run main.py!

For the newbies:
1. Extract contents somewhere, maybe desktop.
2. Press start in windows and search for "cmd"
3. Type: "cd C:\Users\INSERTYOURUSERNAMEHERE\Desktop\DivCardFlip-master"
4. Type: "python datadl.py"
5. Type: "python main.py"

Be sure to have python 3.5+ installed!





Here's a sample how it will look:
```
----------------------------------------------------------------------------------------------------
A Dab of Ink (2.0):
Type: Unique
Profit: 7.0
Profit per card: 0.78
Chaos needed: 18.0
Sell price: 25.0
Card stack: 9
----------------------------------------------------------------------------------------------------
The Hoarder (10.0):
Type: Currency
Profit: 12.0
Profit per card: 1.0
Chaos needed: 120.0
Sell price: 132.0
Card stack: 12
----------------------------------------------------------------------------------------------------
```
