def find_max(a, b, c):
    max_num = a if (a >= b and a >= c) else b if (b >= c) else c
    return max_num


num1 = 10
num2 = 77
num3 = 45

max_number = find_max(num1, num2, num3)
print("The maximum number is:", max_number)
