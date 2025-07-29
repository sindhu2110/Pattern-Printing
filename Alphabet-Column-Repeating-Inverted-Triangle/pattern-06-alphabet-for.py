# A B C D E 
# A B C D 
# A B C
# A B
# A
n=5
for row in range(n, 0, -1):
    #print(row, end=" ")

    for col in range(row):    
        print(chr(65+col), end=" ")
    print()
