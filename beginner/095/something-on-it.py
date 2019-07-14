topping_list = [x for x in input()]
price = 700
for topping_item in topping_list:
    if topping_item == 'o':
        price += 100
print(price)
