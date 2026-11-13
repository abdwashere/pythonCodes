a = int(input("enter real part of first complex number: "))
b = int(input("enter imaginary part of first complex number: "))

c = int(input("enter real part of second complex number: "))
d = int(input("enter imaginary part of second complex number: "))

#addition
y = a+c
z = b+d
print(f"sum of complex numbers {a}{b:+}i and {c}{d:+}i is: {y:+}{z:+}i")

#multiplication
w = (a*c) - (b*d)
x = (a*d) + (b*c)
print(f"product of complex numbers {a}{b:+}i and {c}{d:+}i is: {w}{x:+}i")

#subtraction
m = a-c
n = b-d
print(f"difference of complex numbers {a}{b:+}i and {c}{d:+}i is: {m}{n:+}i")

#division
if c**2 == 0 and d**2 == 0:
  print("denominator cannot be zero")
else:
  p = ((a*c)+(b*d))/(c**2 + d**2)
  q = ((b*c)-(a*d))/(c**2 + d**2)
  print(f"quotient of complex numbers {a}{b:+}i and {c}{d:+}i is: {p}{q:+}i")
