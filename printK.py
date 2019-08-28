
#printK(5)
    
def printStar(n):
    if n > 0:
        print('*',end=' ')
        printStar(n-1)
    else:
        print()
        

def printK(n):
    if n>0:
        printStar(n)
        printK(n-1)
        printStar(n)



def printArrow(i,j):
    if j != i:
        printStar(j)
        printArrow(i,j+1)
        printStar(j)
    else:
        printStar(i)

printK(5)
printArrow(5,1)




# def printStar(n):
#     if n:
#         print('*',end = '')
#         printStar(n-1)
#     else: return

# def printRightStar(row,i=1):
#     if i==row:
#         printStar(i)
#         print()
#         return
#     printStar(i)
#     print()
#     printRightStar(row,i+1)
#     printStar(i)
#     print()

# def printLeftStar(row,i=1):
#     if i==row:
#         printStar(i)
#         print()
#         return
#     print(' '*(row-i),end='')
#     printStar(i)    
#     print()
#     printLeftStar(row,i+1)
#     print(' '*(row-i),end='')
#     printStar(i)    
#     print()

# def printUpStar(row,i):
#     if i==row:
#         printStar(2*i-1)
#         print()
#         return
#     print(' '*(row-i),end='')
#     printStar(2*i-1) 
#     print()
#     printUpStar(row,i+1)
#     print(' '*(row-i),end='')
#     printStar(2*i-1) 
#     print()

# #printLeftStar(5,1)
# printRightStar(5,1)
# #printUpStar(5,1)