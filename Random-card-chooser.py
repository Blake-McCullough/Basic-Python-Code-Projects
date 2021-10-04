import random
suit = random.randint(1,4)
number = random.randint(1,12)
if suit == 1:
    suit_name = "spades"
elif suit == 2:
    suit_name = "clubs"
elif suit == 3:
    suit_name = "hearts"
else:
    suit_name = "diamonds"

print("The card is",number,"of",suit_name)


