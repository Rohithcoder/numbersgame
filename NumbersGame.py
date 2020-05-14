import math
num = (int(input("Enter a Number: ")))
if num%2 != 0:
    print(f"{num} is an odd number")
else:
    print(f"{num} is an even number")
root = math.sqrt(num)
if int(root + 0.5) ** 2 == num:
    print(f"{num} is a perfect square")
else:
    print(f"{num} is not a perfect square")
multiple = (input("Would you like the multiplictaion table of this Number yes/no: "))
numbers = (int(input("How much multiples would you like: ")))
if multiple == "yes":
    for i in range(1,numbers+1):
        print(f"{num} x {i} = {num*i}")



