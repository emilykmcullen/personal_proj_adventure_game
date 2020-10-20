
possible_inventory_items = [
    {"desc": "a wooden comb",
     "location" : "living room",
     "rating" : 1},
     {"desc": "a romantic picture of you and Emily",
     "location" : "living room",
     "rating" : 5},
     {"desc": "a romantic picture of you and Emily beautifully presented in a clip frame",
     "location" : "framers",
     "rating" : 4},
     {"desc": "a regular toothbrush",
     "location" : "sainsburys",
     "rating" : 1},
     {"desc": "a blue bic pen",
     "location" : "sainsburys",
     "rating" : 2},
     {"desc": "a pad of expensive post-it notes",
     "location" : "sainsburys",
     "rating" : 6},
     {"desc": "fish and chips",
     "location" : "globetrotters",
     "rating" : 5},
     {"desc": "fish and chips and mushy peas",
     "location" : "globetrotters",
     "rating" : 6},
     {"desc": "fish and chips and curry sauce",
     "location" : "globetrotters",
     "rating" : 8},
     {"desc": "scraps",
     "location" : "globetrotters",
     "rating" : 2},
]


# inv = ["The comb", "Fish and chips with egg", "Deoderant with a pube", "Golden necklace"]

print('Which item should you give Emily?')
for i in range(1, len(possible_inventory_items)+1):
    print(f"{i}. {possible_inventory_items[i-1]['desc']}")


choice = possible_inventory_items[int(input("Which num? "))-1]

print(choice)





