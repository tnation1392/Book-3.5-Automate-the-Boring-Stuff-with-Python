stuff = {'rope': 1, 'torch': 6, 'gold': 42,
         'dagger': 1, 'arrows': 12}

#A function that displays the inventory
def display_inventory(inventory):
    print("Inventory:")
    #Create the item_total
    item_total = 0
    for k, v in inventory.items():
        #Print out each line of the dictionary
        print(k.title() + ': ' + str(v))
        #Add the quantity to the item_total
        item_total += v
    print("Total Number of Items: " + str(item_total))

print(display_inventory(stuff))