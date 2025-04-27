def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

num = int(input("Enter number:"))
if isEven(num):
    print("Even!")
else:
    print("Odd!")