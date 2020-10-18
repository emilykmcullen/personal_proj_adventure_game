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
        display_inventory(inventory)
    elif option == "1":
        in_living_room = True
        look_living_room(living_room_items)
        while in_living_room:
            print_menu_look_living_room(living_room_item_menu)
            lr_option = menu_input_living_room_objects()
            if lr_option == "1":
                print("A wooden hair comb, gifted to you by Emily's mum for your birthday. It has brought you many hours of relaxation.")
                add_item_to_list(inventory, "comb")
                remove_item_from_list(living_room_items, "comb")
                remove_item_from_list(living_room_item_menu, "1. Pick up comb")
                emily_home_in_lr(inventory, money_in_wallet)
            elif lr_option == "2":
                print("It's a picture of you and Emily eating a picnic, you put it in your pocket")
                add_item_to_list(inventory, "a romantic picture of you and Emily")
                remove_item_from_list(living_room_items, "a romantic picture of you and Emily")
                remove_item_from_list(living_room_item_menu, "2. Pick up picture")
                emily_home_in_lr(inventory, money_in_wallet)
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
                        if fr_option == "1" and money_in_wallet >= 6:
                            framers_choice_1_can_afford()
                            remove_item_from_list(framers_menu, "1. I'd like to get this picture framed in your best frame please.")
                            add_item_to_list(inventory, "a romantic picture of you and Emily, beautifully presented in a clip frame")
                            remove_item_from_list(inventory, "a romantic picture of you and Emily")
                            money_in_wallet -= 6
                            update_money_in_inventory(inventory, money_in_wallet)
                            emily_home(inventory, money_in_wallet)
                            in_framers = False
                        elif fr_option == "1" and money_in_wallet < 6:
                            framers_choice_1_cant_afford()
                            in_framers = False
                        elif fr_option == "2":
                            in_framers = False
                    else:
                        print("You enter the framing shop. A plethora of wonderful, exotic frames surround you.")
                        print("A woman comes to the counter")
                        print("Woman: 'May I help you sir?'")
                        print("You: 'No, I have nothing to frame! I'll be on my way.'")
                        in_framers = False 
            elif br_option == "2":
                in_sains = True 
                while in_sains:
                    sainsburys(sainsburys_action_menu)
                    s_option = menu_input_sains()
                    if s_option == "1":
                        sains_choice_1()
                        if money_in_wallet >= 5:
                            print("You buy the regular toothbrush.")
                            add_item_to_list(inventory, "a regular toothbrush")
                            # remove_item_from_list(sainsburys_stock, "1. An electric toothbrush (you can't see the price)")
                            remove_item_from_list(sainsburys_action_menu, "1. Buy toothbrush £5")
                            money_in_wallet -= 5
                            update_money_in_inventory(inventory, money_in_wallet)
                            emily_home(inventory, money_in_wallet)
                        else:
                            cant_afford()
                    elif s_option == "2": 
                        if money_in_wallet >= 2:
                            sains_choice_gen("a nice blue bic pen", "a pen", "2. Buy pen £2")
                            money_in_wallet -= 2
                            update_money_in_inventory(inventory, money_in_wallet)
                            emily_home(inventory, money_in_wallet)
                        else: 
                            cant_afford()
                    elif s_option == "3": 
                        if money_in_wallet >= 4.95:
                            money_in_wallet -= 4.95
                            update_money_in_inventory(inventory, money_in_wallet)
                            sains_choice_gen("a block of post-it notes in every colour of the rainbow","expensive post-it notes", "3. Buy expensive post-it notes £4.95")
                            emily_home(inventory, money_in_wallet)
                        else: 
                            cant_afford()
                    elif s_option == "4":
                        in_sains = False
            elif br_option == "3":
                in_globetrotters = True 
                while in_globetrotters:
                    globetrotters(globetrotters_action_menu)
                    g_option = menu_input_globe()
                    if g_option == "1":
                        if money_in_wallet >= 5:
                            globe_choice_gen(" the classic no frills fish and chips", "fish and chips")
                            money_in_wallet -= 5
                            update_money_in_inventory(inventory, money_in_wallet)
                            emily_home(inventory, money_in_wallet)
                        else:
                            cant_afford()
                    elif g_option == "2":
                        if money_in_wallet >= 7:
                            globe_choice_gen(" fish and chips with a delicious dollop of mushed peas", "fish and chips and mushy peas")
                            money_in_wallet -= 7
                            update_money_in_inventory(inventory, money_in_wallet)
                            emily_home(inventory, money_in_wallet)
                        else:
                            cant_afford()
                    elif g_option == "3":
                        if money_in_wallet >= 9:
                            globe_choice_gen(" fish and chips with a tub of steaming hot curry sauce", "fish and chips with curry sauce")
                            money_in_wallet -= 9
                            update_money_in_inventory(inventory, money_in_wallet)
                            emily_home(inventory, money_in_wallet)
                        else:
                            cant_afford()
                    elif g_option == "4":
                        if money_in_wallet >= 2:
                            globe_choice_gen(" scraps, a great choice if ever there was one", "scraps")
                            money_in_wallet -= 2
                            update_money_in_inventory(inventory, money_in_wallet)
                            emily_home(inventory, money_in_wallet)
                            # print(money_in_wallet)
                        else:
                            cant_afford()
                    elif g_option == "5":
                        in_globetrotters = False
            elif br_option == "4":
                on_brunts_high_street = False
            elif br_option == "5":
                display_inventory(inventory)

                









            

        

    