# Task5: Store Inventory Update
# create item dictionary
store_item = {"Book": 10, "Pen": 15, "Bag": 12}
# ask user to input their request
item_request = input("Enter item name: ")
# ask user to input their quantity request
quantity_request = int(input("Enter the quantity you want: "))
# print dict before subtraction
print(f"Before purchase: {store_item}")
# minus inputed quantity from former quantity
store_item[item_request.title()] -= quantity_request
#  print items with remaining quantity 
print(f"After purchase: {store_item}")
