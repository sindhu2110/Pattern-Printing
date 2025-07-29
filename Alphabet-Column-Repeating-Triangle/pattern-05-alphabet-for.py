n=5
for row in range(n):
    #print("row:",row,end="  ")
    for col in range(row+1):
        print(chr(65 + col), end=" ")
    print()
    
