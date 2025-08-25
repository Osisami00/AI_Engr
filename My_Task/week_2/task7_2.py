
# Task2: super Market PRice list
item_list=["bama", "butter", "oil"]

# request items
first_item_price = int(input("Enter the price of Bama: "))
second_item_price = int(input("Enter the price of Butter: "))
third_item_price = int(input("Enter the price of Oil: "))

dict_of_items = {}
dict_of_items[item_list[0]] =first_item_price
dict_of_items[item_list[1]] = second_item_price
dict_of_items[item_list[2]] = third_item_price

print(dict_of_items)
name_update = input("Enter the name of item you want to change: ")
price_update = input("Enter the updated price of the item you entered: ")

# print(name_update in dict_of_items.keys())

dict_of_items.update({name_update : price_update})
print(dict_of_items)