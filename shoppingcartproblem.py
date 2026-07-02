foods = []
prices = []
total = 0

while True:
    food = input("enter a food to buy (q to quit) ") 
    if food == "q" or food == "Q":
        break
    else:
        price = int(input(f"enter the price of {food} $: "))
        foods.append(food)
        prices.append(price)

print("-----your cart-----")

for food in foods:
    print(food, end= " ")

for price in prices:
    total +=price

print()
print(f"your total is {total}$ ")