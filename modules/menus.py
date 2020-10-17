def start_game():
    print("Hello Ross, you are in the living room of your flat, 66B, when you recieve a text from your beloved Emily, it reads:")
    print("'HI BABES, PLEASE BUY ME THE BEST PRESENT, CU SOON XXX'")
    print("You must buy Emily a present but you only have 4 hours before she returns home from her walk.")


def print_menu_living_room(): 
    print("You are in your living room at home.")
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
    
def print_menu_look_living_room(lr_choices):
    for item in lr_choices:
        print(item)
    # remove item if chosen
    

def bedroom():
    print("You go to the bedroom and fall asleep. Emily returns 4 hours later to no present.")
    print("Relationship over. GAME OVER")

def bruntsfield_high_street():
    print("You are on Bruntsfield high street, shopping mecca, 'notable street' on Google Maps. It is 5pm and only three shops are open:")
    print("The framing shop and Sainsbury's local and Globetrotter's fish and chip shop")
    print("Where will you go?")
    print("1. The framing shop")
    print("2. Sainsbury's")
    print("3. Globetrotter's")
    print("4. Return home")

def framers(fr_choices):
    print("You enter the framing shop. A plethora of wonderful, exotic frames surround you.")
    print("A woman comes to the counter")
    print("Woman: 'May I help you sir?'")
    for item in fr_choices:
        print(item)

def framers_choice_1():
    print("Woman: 'That will be £170 and it will be ready in two weeks.")
    print("You: 'What?? OK what can you do immediately for £20?")
    print("Woman: 'We have these gorgeous clip frames for £6 a pop.")
    print("You: 'Okay, I'll take it.")
    print("You now have a beautifully presented romantic picture of you and Emily")
    print("You exit the shop")