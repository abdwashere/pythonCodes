def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def mul(x,y):
    return x*y

def divide(x,y):
    if y==0:
        return print("cant divide by 0 ")
    return x/y


while True:

    print(" Calculator ")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. exit")

    choice = input("choice option 1-5: ")

    if choice == "5":
      print("bye")
    break

if choice in ["1","2","3","4"]:
    num1 = int(input("enter first number "))
    num2 = int(input("enter second number "))

if choice == "1":
            print("Result:", add(num1, num2))
elif choice == "2":
            print("Result:", subtract(num1, num2))
elif choice == "3":
            print("Result:", mul(num1, num2))
elif choice == "4":
            print("Result:", divide(num1, num2))
else:
        print("invalid choice, try again.")
