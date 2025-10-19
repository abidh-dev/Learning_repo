x = int(input("Enter a number: "))
y = int(input("Enter b number: "))

# sum
print(f"The sum of {x} and {y} is {x + y}")
# difference
print(f"The difference of {x} and {y} is {x - y}")
# product
print(f"The product of {x} and {y} is {x * y}")
# division
if y != 0:
   print(f"The division of {x} and {y} is {x / y}")
else:
   print("Division by zero is not allowed.")