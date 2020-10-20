money_in_wallet = 15 

living_room_items = ["comb", "a romantic picture of you and Emily", "electric toothbrush charger"]

living_room_item_menu = [
    {"number":1,
    "desc": ": Pick up comb"},
    {"number":2,
    "desc": ": Pick up picture",
    },
    {"number": 3,
    "desc": ": Pick up electric toothbrush charger"},
    {"number": "S",
    "desc":": Stop looking around room"}
]

framers_menu = ["1. I'd like to get this picture framed in your best frame please.", "2. No, thanks, I'll just be on my way."]


sainsburys_action_menu = [
    {"number":1,
    "desc": ": Buy toothbrush £5"},
    {"number":2,
    "desc": ": Buy pen £2"},
    {"number":3,
    "desc": ": Buy expensive post-it notes £4"},
    {"number":4,
    "desc": ": Leave Sainbury's"}
]

globetrotters_action_menu = ["1. Fish and chips £5", "2. Fish and chips and mushy peas £7", "3. Fish and chips and curry sauce £9", "4. Scraps £2", "5. Nothing, leave Globetrotter's"]

# globetrotters_action_menu = [
#     {"number":1,
#     "desc": ": Fish and chips £5"},
#     {"number":2,
#     "desc": ": Fish and chips and mushy peas £7"},
#     {"number":3,
#     "desc": ": Fish and chips and curry sauce £9"},
#     {"number":4,
#     "desc": ": Scraps"},
#     {"number":5,
#     "desc": ": Leave Globetrotter's"}
# ]

possible_inventory_items = [
    {"desc": "a wooden comb",
     "location" : "living room",
     "rating" : 2,
     "emily response" : "I hate it!!"},
     {"desc": "a romantic picture of you and Emily",
     "location" : "living room",
     "rating" : 5,
     "emily response" : "Aw.. cute I suppose"},
     {"desc": "a romantic picture of you and Emily beautifully presented in a clip frame",
     "location" : "framers",
     "rating" : 4,
     "emily response" : "EWWWWW! A CLIP FRAME!"},
     {"desc": "a regular toothbrush",
     "location" : "sainsburys",
     "rating" : 1,
     "emily response": "what!!!!!"},
     {"desc": "a blue bic pen",
     "location" : "sainsburys",
     "rating" : 2,
     "emily response": "erm...."},
     {"desc": "a pad of expensive post-it notes",
     "location" : "sainsburys",
     "rating" : 6,
     "emily response": "soooo cute!"},
     {"desc": "fish and chips",
     "location" : "globetrotters",
     "rating" : 5,
     "emily response": "no sides?"},
     {"desc": "fish and chips and mushy peas",
     "location" : "globetrotters",
     "rating" : 6,
     "emily response" : "....mushy peas? Ok, I guess..."},
     {"desc": "fish and chips and curry sauce",
     "location" : "globetrotters",
     "rating" : 8,
     "emily response": "My favourite combination!"},
     {"desc": "scraps",
     "location" : "globetrotters",
     "rating" : 2,
     "emily response": "I like these but it's not a great present on it's own..."},

]

my_inventory = [
    {"desc":f"£{money_in_wallet}",
    "location": "pocket",
    "rating" : 1,
    "emily response": "sooooo insulting"},
    {"desc" : "a notebook of facts about Emily",
    "location": "pocket",
    "rating" : -5,
    "emily response" : "erm, this is really creepy!!"}
]