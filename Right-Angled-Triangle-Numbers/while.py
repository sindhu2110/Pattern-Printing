# Pattern 03: Right-Angled Triangle of Numbers
# Example (n = 5):
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n=5
row=0
while row<n:
   # print(row,":" , end="")
    row+=1
    col=0
    while col<row:
        print(col+1, end=" ")
        col+=1
    print()