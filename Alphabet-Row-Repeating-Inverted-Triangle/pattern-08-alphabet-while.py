#A A A A A 
#B B B B 
#C C C
#D D
#E
n=5
row=n
while row>0:
    #print(row, end=" ")
    row-=1
    col=0
    while col<row+1:
        print(chr(65+n-row-1), end=" ")
        col+=1
    print()
