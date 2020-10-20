from data.inventory import * 

def add_item_to_list(listt, item):
    listt.append(item)    

def display_inventory(inv):
    for item in inv:
        print(item["desc"])

def remove_item_from_list(listt, item):
    listt.remove(item)

def update_money_in_inventory(listt, current_amount):
    listt[0]["desc"] = "£" + str(current_amount)
