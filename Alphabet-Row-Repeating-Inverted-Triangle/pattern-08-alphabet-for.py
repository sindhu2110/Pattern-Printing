n=5
for row in range(n,0,-1):
    #print("row:",row,end="  ")
    for col in range(row):        
        #print(row,end="")
        print(chr(65 + n-row), end=" ")
    print()
    
