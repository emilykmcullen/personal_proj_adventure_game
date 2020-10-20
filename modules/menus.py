from modules.tasks import *
from data.inventory import *
from modules.input import *
# for look around living room, sainsburys and globetrotters, edit menu so 
# if invalid number chosen loop begins again
# create these menus as dictionaries
# if number in dictionary its ok

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
        print(item['number'], item['desc'])
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
    print("i. Display inventory")

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
        print(action["number"], action["desc"])

def sains_choice_1():
    print("You buy a toothbrush")

def sains_choice_gen(desc, stock_item, action):
    print(f"You buy {desc}")
    add_item_to_list(my_inventory, stock_item)
    remove_item_from_list(sainsburys_action_menu, action)
    # rev_item_from_list2(sainsburys_action_menu, action)



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
    add_item_to_list(my_inventory, stock_item)

def emily_home(inv, cash):
    if len(inv)> 8 or cash < 3:
        print("It's 7pm, Emily is back from her walk!")
        print("You meet her in the living room at home")
        print("Emily: 'Where is my present?'")
        print("You look at your inventory:")
        display_inventory(inv)
        print('Which item should you give Emily?')
        for i in range(1, len(my_inventory)+1):
            print(f"{i}. {my_inventory[i-1]['desc']}")
        choice = my_inventory[int(input("Which num? "))-1]
        print(f"You give Emily {choice['desc']}")
        print("You search her face for a response")
        print("After what seems like hours she looks at you and says:")
        print(f"'{choice['emily response']}''")
        if choice["rating"]>= 7: 
            print("You both hug and have the best relationship for ever and ever")
            print("GAME OVER")
        elif 7> choice["rating"]>= 4:
            print("You get a lukewarm hug, there is a underlying tension in your relationship until the next year when you break up")
            print(f"Emily cites the time you bought her {choice['desc']} as the reason")
            print("GAME OVER")
        elif choice["rating"]< 4:
            print("You immediately break up")
            print("GAME OVER")

def emily_home_in_lr(inv, cash):
    if len(inv)> 8 or cash <3:
        print("It's 7pm, Emily returns from her walk!")
        print("Emily: 'Where is my present?'")
        print("You look at your inventory:")
        display_inventory(inv)
        print('Which item should you give Emily?')
        for i in range(1, len(my_inventory)+1):
            print(f"{i}. {my_inventory[i-1]['desc']}")
        choice = my_inventory[int(input("Which num? "))-1]
        print(f"You give Emily {choice['desc']}")
        print("You search her face for a response")
        print("After what seems like hours she looks at you and says:")
        print(f"'{choice['emily response']}''")
        if choice["rating"]>= 7: 
            print("You both hug and have the best relationship for ever and ever")
            print("GAME OVER")
        elif 7> choice["rating"]>= 4:
            print("You get a lukewarm hug, there is a underlying tension in your relationship until the next year when you break up")
            print(f"Emily cites the time you bought her {choice['desc']} as the reason")
            print("GAME OVER")
        elif choice["rating"]< 4:
            print("You immediately break up")
            print("GAME OVER")
        

def game_over(inv, cash):
    if len(inv)> 8 or cash <3:
        return False
    return True
        






        
