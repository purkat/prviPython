'''
items = ["milk", "bread", "eggs", "juice", "salami", "joghurt"]

prices = [2.25, 1.68, 3.15, 1.22, 1.43, 2.87]

chosen_item = raw_input("What item would you like to buy? ")

if chosen_item in items:
    item_index = items.index(chosen_item)
    item_price = prices[item_index]
    print "Item price is %s" % (item_price)
else:
    print "Item is not available."
'''
items_prices = {
    "milk": 2.25,
    "bread": 1.68,
    "eggs": 3.15,
    "juice": 1.22,
    "salami": 1.43,
    "joghurt": 2.87
}

print items_prices.keys()
print items_prices.values()

chosen_item = raw_input("Izberi izdelek: ")

if chosen_item in items_prices.keys():
    price = items_prices[chosen_item]
    print "Item price is %s" % (price)
else:
    print "Item is not available."
cars = {
    "clio": ["renault", ["red", "blue"]],
    "golf": {"znamka": "volkswagen", "barve": ["red", "blue"], "vrata": 4},
    "laguna": "renault",
    "m3": "bmw",
    "cordoba": "seat"
}
print cars["golf"]["barve"][1]



