def start_game():
    print("Hello Ross, you are in the living room of your flat, 66B, when you recieve a text from your beloved Emily, it reads:")
    print("'HI BABES, PLEASE BUY ME THE BEST PRESENT, CU SOON XXX'")
    print("You must buy Emily a present but you only have 4 hours before she returns home from her walk.")


def print_menu_living_room(): 
    print("1. Look around the room")
    print("2. Leave the flat and go to the Bruntsfield high street")
    print("3. Go to the bedroom")
    print("i: Display inventory")
    print("Q or q: Quit ")

def look_living_room(lr_items):
    print("It is your living room. Decorated lovingly by the air bnb hosts who are now renting it to you. Amongst the many treasures of this room, a few items in particular catch your eye:")
    print("In the room there is:")
    for item in lr_items:
        print(item)
    # print("A wooden hair comb, gifted to you by Emily's mum for your birthday. It has brought you many hours of relaxation.")
    # print("A picture of you and Emily, in happier times.")
    # print("The charger for your electric toothbrush, you recall how Emily doesn't have an electric toothbrush of her own, it is a source of tension in your relationshop.")

def print_menu_look_living_room(lr_choices):
    for item in lr_choices:
        print(item)
    

def bedroom():
    print("You go to the bedroom and fall asleep. Emily returns 4 hours later to no present.")
    print("Relationship over. GAME OVER")