num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
if num_2 > num_1:
    print(f"{num_2} is bigger")
elif num_1 > num_2:
    print(f"{num_1} is bigger")
else:
    print("Both are equal")