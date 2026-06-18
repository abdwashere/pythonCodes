princple = 0
rate = 0 
time = 0

while True:
    princple = int(input("enter principle amount:"))
    if princple <0:
        print("principle cannot be less than zero or zero")
    else:
        break

while True:
    rate = int(input("enter rate rate:"))
    if rate <0:
        print("rate cannot be less than zero or zero")
    else:
        break

while True:
    time = int(input("enter time in years:"))
    if time <0:
        print("time cannot be less than zero or zero")
    else:
        break

interest = princple * pow((1 + (rate/100)),time)
print(f"final amount after {time} years will be ${interest}")
    