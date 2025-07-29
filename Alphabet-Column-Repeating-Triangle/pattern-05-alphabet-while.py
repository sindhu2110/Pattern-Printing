# A 
# A B 
# A B C
# A B C D
# A B C D E

n=5
row=0
while row<n:
    #print(row,end="  ")
    row+=1
    col=0
    while col<row:
        print(chr(65+col), end=" ")
        col+=1
    print()



