from modules.input import *
from modules.menus import *
from modules.tasks import *
from data.inventory import *

start_game()
while True:
    print_menu_living_room()
    option = menu_input_living_room()
    print(option)
    if option.lower() == "q":
        break
    if option.lower() == "i":
        display_inventory()
    elif option == "1":
        in_living_room = True
        while in_living_room:
            look_living_room(living_room_items)
            print_menu_look_living_room(living_room_item_menu)
            lr_option = menu_input_living_room_objects()
            if lr_option == "1":
                #need to test if comb is in living room etc
                print("A wooden hair comb, gifted to you by Emily's mum for your birthday. It has brought you many hours of relaxation.")
                inventory.append("comb")
                living_room_items.remove("comb")
            elif lr_option == "2":
                inventory.append("picture of you and Emily in happier times")
                living_room_items.remove("picture of you and Emily in happier times")
            elif lr_option == "3":
                print("The charger for your electric toothbrush, you recall how Emily doesn't have an electric toothbrush of her own, it is a source of tension in your relationshop.")
                inventory.append("electric toothbrush charger")
                living_room_items.remove("electric toothbrush charger")
            elif lr_option.lower() == "s":
                in_living_room = False
        

    