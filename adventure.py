from modules.input import *
from modules.menus import *
from modules.tasks import *
from data.inventory import *

start_game()
while True:
    print_menu_living_room()
    option = menu_input_living_room()
    if option.lower() == "q":
        break
    if option.lower() == "i":
        display_inventory()
    elif option == "1":
        in_living_room = True
        look_living_room(living_room_items)
        while in_living_room:
            # look_living_room(living_room_items)
            print_menu_look_living_room(living_room_item_menu)
            lr_option = menu_input_living_room_objects()
            if lr_option == "1":
                #need to test if comb is in living room etc
                print("A wooden hair comb, gifted to you by Emily's mum for your birthday. It has brought you many hours of relaxation.")
                add_item_to_list(inventory, "comb")
                # inventory.append("comb")
                remove_item_from_list(living_room_items, "comb")
                remove_item_from_list(living_room_item_menu, "1. Pick up comb")
                # living_room_items.remove("comb")
                # living_room_item_menu.remove("1. Pick up comb")
            elif lr_option == "2":
                print("It's a picture of you and Emily eating a picnic, you put it in your pocket")
                add_item_to_list(inventory, "a romantic picture of you and Emily")
                remove_item_from_list(living_room_items, "a romantic picture of you and Emily")
                remove_item_from_list(living_room_item_menu, "2. Pick up picture")
            elif lr_option == "3":
                print("The charger for your electric toothbrush, you recall how Emily doesn't have an electric toothbrush of her own, it is a source of tension in your relationshop.")
                print("You: I don't want to pick that up! But perhaps it has given me a good idea for a present....")
            elif lr_option.lower() == "s":
                in_living_room = False
    elif option == "2":
        on_brunts_high_street = True 
        while on_brunts_high_street:
            bruntsfield_high_street()
            br_option = menu_input_brunts()
            if br_option == "1":
                in_framers = True 
                while in_framers:
                    if "a romantic picture of you and Emily" in inventory:
                        framers(framers_menu)
                        fr_option = menu_input_framers()
                        if fr_option == "1":
                            framers_choice_1()
                            remove_item_from_list(framers_menu, "1. I'd like to get this picture framed in your best frame please.")
                            add_item_to_list(inventory, "a romantic picture of you and Emily, beautifully presented in a clip frame")
                            remove_item_from_list(inventory, "a romantic picture of you and Emily")
                            money_in_wallet -= 6
                            in_framers = False
                        elif fr_option == "2":
                            in_framers = False
                    else:
                        print("You enter the framing shop. A plethora of wonderful, exotic frames surround you.")
                        print("A woman comes to the counter")
                        print("Woman: 'May I help you sir?'")
                        print("You: 'No, I have nothing to frame! I'll be on my way.'")
                        in_framers = False 

                        





            

        

    