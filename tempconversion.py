unit = input("is this in celsius or fahrenheit (c/f): ")
temp = float(input("enter the temperature:  "))


if unit == "c" or unit == "C":
    temp = (9 * temp)/5 + 32
    print(f"the temperature in fahrenhiet is: {temp}F")
elif unit == "f" or unit == "F":
    temp = round((temp - 32)* 5/9,2)
    print(f"the temperature in celsius is: {temp}C")
else:
    print("enter a valid unit!")


