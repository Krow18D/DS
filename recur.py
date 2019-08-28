def printStar(n):
    if n>0:
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
    if i!=j:
        printStar(j)
        printArrow(i,j+1)
        printStar(j)
    else:
        printStar(j)


printK(5)
printArrow(5,1)




















# def sumEven(l,n):
#     if n == 0:
#         return l[n]
#     if l[n]%2==0:
#         print(' + ',l[n],end='',sep = '')
#         return l[n]+sumEven(l,n-1)
#     else:
#         return sumEven(l,n-1)

# def printStar(n):
#     if n==0:
#         print()
#     else:
#         print('*',end=' ')
#         printStar(n-1)

# def printK(n):
#     if n>0:
#         printStar(n)
#         printK(n-1)
#         printStar(n)

# def printArrow(i,j):
#     if j!=i:
#         printStar(j)
#         printArrow(i,j+1)
#         printStar(j)
#     else:
#         printStar(j)


# l = [14,556,2,4,1,3,7,3]
# print(' +',sumEven(l,len(l)-1))
# printArrow(5,1)    