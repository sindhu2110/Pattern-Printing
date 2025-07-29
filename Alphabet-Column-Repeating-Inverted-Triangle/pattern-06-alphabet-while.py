# A B C D E 
# A B C D 
# A B C
# A B
# A
n=5
row=n+1
while 0<row:
    print(row, end="")
    col=0
    row-=1
    while col<row:
        print(chr(65+col),end=" ")
        col+=1
    print()





