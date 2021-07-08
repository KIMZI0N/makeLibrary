a = int(input("Enter a integer: "))
b = int(input("Enter another: "))

if a > b:
    print(f"{a} is greater than {b}.")
elif b > a:
    print(f"{b} is greater than {a}.")
elif a == b:
    print(f"{a} is equal to {b}.")
