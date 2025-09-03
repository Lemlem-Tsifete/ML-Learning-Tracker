num = int(input("Put it your number : "))

if(num % 2 == 0):
    print(num,": your number is Even number")
else:
    print(num, ": your number is odd number")

for i in range(1, 11):
    print(num , "X", i, "=", num * i)