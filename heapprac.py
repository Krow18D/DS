def insert(lst,data):
    lst.append(data)
    last = len(lst)-1
    while last > 0:
        if lst[last] < lst[(last-1)//2]:
            lst[last] , lst[(last-1)//2]=lst[(last-1)//2],lst[last]  
            last = (last-1)//2
        else:
            break

def delmin(lst):
    last = len(lst)-1
    temp = lst[-1]
    n = 0
    L = 2*n+1
    R = 2*n+2
    found = False
    while L < last and not found:
        R = L if R>=last else R
        idx_min = L if lst[L] < lst[R] else R
        if lst[idx_min] < temp:
            lst[n]=lst[idx_min]
            n=idx_min
            L = 2*n+1
            R = 2*n+2
        else:
            found = True
    lst[n] = temp
    lst.pop()

    




lst = [5,1,4,9,6,3,8,2,7,0]
l = []
for i in lst:
    insert(l, i)
print(l)

print('-'*15)

for i in range(len(lst)):
    print(l[0], end = ' ')
    delmin(l)