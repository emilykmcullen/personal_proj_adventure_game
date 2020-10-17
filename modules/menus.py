from modules.tasks import *
from data.inventory import *
from modules.input import menu_input_globe

def start_game():
    print("Hello Ross, you are in the living room of your gorgeous basement flat when you recieve a text from your beloved Emily, it reads:")
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
    print("5. Display inventory")

def framers(fr_choices):
    print("You enter the framing shop. A plethora of wonderful, exotic frames surround you.")
    print("A woman comes to the counter")
    print("Woman: 'May I help you sir?'")
    for item in fr_choices:
        print(item)

def framers_choice_1_can_afford():
    print("Woman: 'That will be £170 and it will be ready in two weeks.")
    print("You: 'What?? OK what can you do immediately for £20?")
    print("Woman: 'We have these gorgeous clip frames for £6 a pop.'")
    print("You: 'Okay, I'll take one.'")
    print("You now have a beautifully presented romantic picture of you and Emily")
    print("You exit the shop")

def framers_choice_1_cant_afford():
    print("Woman: 'That will be £170 and it will be ready in two weeks.")
    print("You: 'What?? OK what can you do immediately for a couple of bucks?")
    print("Woman: 'We have these gorgeous clip frames for £6 a pop.'")
    print("You: 'I can't afford that.. ")
    print("You exit the shop")

def sainsburys(actions):
    print("You are in Sainsbury's")
    print("A quick scan of the shelves reveal a few potential choices:")
    for action in actions:
        print(action)

def sains_choice_1():
    print("You bring the electric toothbrush to the till.")
    print("Checkout assistant: 'That will be £60 please.'")
    print("You: 'How embarassing, I don't have enough money, is there a cheaper option?'")
    print("The checkout assistant disappears for 10 minutes and reappears with a regular toothbrush")
    print("Checkout assistant: 'This will be £5 please.'")

def sains_choice_gen(desc, stock_item, action):
    print(f"You buy {desc}")
    add_item_to_list(inventory, stock_item)
    # remove_item_from_list(sainsburys_stock, action)
    remove_item_from_list(sainsburys_action_menu, action)



def cant_afford():
    print("You can't afford that")

def globetrotters(choices):
    print("You are in Globetrotter's chippy")
    print("Succulent greasy smells fill your flared nostrils and you inhale deeply")
    print("The woman behind the counter says 'Next please'")
    print("You look at the menu:")
    for action in choices:
        print(action)
    

def globe_choice_gen(desc, stock_item):
    print(f"You buy {desc}")
    add_item_to_list(inventory, stock_item)
    # remove_item_from_list(sainsburys_stock, action)
    
