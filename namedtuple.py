from collections import namedtuple
card=namedtuple("card",["face","suits"])
card=card(face="ace",suits="spades")
print(card.face)
card.suits