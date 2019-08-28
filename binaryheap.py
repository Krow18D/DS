def insert(lst, data):
    lst.append(data)
    key_idx = len(lst)-1
    while key_idx > 0:
        if lst[key_idx] < lst[(key_idx-1) //2]:
            lst[(key_idx-1)//2], lst[key_idx] = lst[key_idx], lst[(key_idx-1)//2]
            key_idx = (key_idx-1)//2
        else:
            break

def print90(lst, level=0, n=0):
    L = n*2 + 1
    R = n*2 + 2
    if n < len(lst):
        print90(lst, level+1, R)
        print('   '*level, lst[n])
        print90(lst, level+1, L)

def deleteMin(lst):
    last = len(lst)-1
    temp = lst[-1]
    n = 0
    L = n*2 + 1
    R = n*2 + 2
    found = False

    while L < last and not found:
        R = L if R >= last else R
        idx_min = L if lst[L] <  lst[R] else R
        if lst[idx_min] < temp:
            lst[n] = lst[idx_min]
            n = idx_min
            L = n*2 + 1
            R = n*2 + 2
        else:
            found = True
    lst[n] = temp
    lst.pop()



lst = [5,1,4,9,6,3,8,2,7,0]
l = []
for i in lst:
    insert(l, i)
print(l)
print90(l)
print('-'*15)

for i in range(len(lst)):
    print(l[0], end = ' ')
    deleteMin(l)