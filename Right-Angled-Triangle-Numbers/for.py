
# Pattern 03: Right-Angled Triangle of Numbers
# Example (n = 5):
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


n = 5
for row in range(n):
    #row=0
    #row=1
    #row=2
    #row = 3
    #row = 4
    #exit
    for col in range(row+1):
        # col in range row=0 => col=0
        #exit

        # col in range row=1 => col=0,1
        #exit

        # col in range row=2 => col=0,1,2
        #exit

        # col in range row=3 => col=0,1,2,3 
        #exit
        
        # col in range row=4 => col=0,1,2,3,4 
        #exit
        
        #print(row,col,";") 
        
              
        #0,0
        #1,0    1,1
        #2,0    2,1    2,2
        #3,0    3,1    3,2    3,3  
        #4,0    4,1    4,2    4,3   4,4 
        print(col+1,end=" ")
            # 1
            # 1  #2
            # 1  #2  #3
            # 1  #2  #3  #4
            # 1  #2  #3  #4  #5

    print(" ")
    #next line
    #next line
    #next line
    #next line
    #next line
    #next line


        

