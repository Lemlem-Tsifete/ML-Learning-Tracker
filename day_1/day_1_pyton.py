num = int(input("Put it your number : "))

if(num % 2 == 0):
    print(num,": your number is Even number")
else:
    print(num, ": your number is odd number")

for i in range(1, 11):
    print(num , "X", i, "=", num * i)

# exercise on manualy dot product catch up matrix and vector 

# a function to do a manualy dot product 
def dot_product_manualy(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must be the same lenght")
    
    result = 0 

    for i in range(len(v1)):
        result += v1[i] * v2[i]
    return result

v1 = [1, 2, 3]
v2 = [4, 5, 6]

manual_result = dot_product_manualy(v1, v2)
print("Manual Dot Product: ", manual_result)