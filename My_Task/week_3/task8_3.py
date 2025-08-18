# Task3: Online Store Cart Calculator

# create item list
item_list = ["Book", "Pen", "Bag"]
# create item price
item_price = [500,100,800]
cart_total = 0
# create onluine price calculator
cart_total += item_price[0] + item_price[1] + item_price[2]
# print updated list with f-string
print(f"Items : {item_list}\nTotal Price: {cart_total}")

