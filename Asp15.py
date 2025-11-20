n = int(input("Enter number of rows: "))

for i in range(n):
    num = 1
    row = []
    for j in range(i + 1):
        row.append(str(num))
        num = num * (i - j) // (j + 1)
    print(" ".join(row))