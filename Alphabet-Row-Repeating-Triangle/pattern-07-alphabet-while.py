#A 
#B B 
#C C C 
#D D D D 
#E E E E E 

n=5
row=0
while row<n:
    #print(row,end="")
    row+=1
    col=0
    while col<row:
        print(chr(65+row-1), end=" ")
        col+=1
    print()
