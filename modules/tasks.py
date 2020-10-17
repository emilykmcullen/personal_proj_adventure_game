from data.inventory import * 

def add_item_to_list(list, item):
    list.append(item)    

def display_inventory():
    print(inventory)

def remove_item_from_list(list, item):
    list.remove(item)