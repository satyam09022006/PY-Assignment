a=int(input("Enter first no of ap:"))
n=int(input("Enter the nth term needed to calculate:"))
d=int(input("Enter the common difference of the ap:"))
term = a + (n-1) * d
total = n * (2 * a + (n-1) * d) // 2
print(term)
print(total)
