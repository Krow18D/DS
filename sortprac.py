def bubble(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1-i):
            if l[j]> l[j+1]:
                l[j], l[j+1] = l[j+1],l[j]
    return l

def selection(l):
    for i in range(len(l)):
        max = l[0]
        idx = 0
        for j in range(len(l)-i):
            if l[j] > max:
                max = l[j]
                idx = j
        l[j],l[idx] = l[idx],l[j]
    return l


def insertion(l):
    for i in range(len(l)):
        for j in range(i,0,-1):
            if l[j]<l[j-1]:
                l[j],l[j-1] = l[j-1],l[j]
    return l


def quick(l):
    if l == []:
        return []
    pivot = l.pop(0)
    L,R = [],[]
    for i in l:
        if i < pivot:
            L.append(i)
        else:
            R.append(i)
    return quick(L) + [pivot] +quick(R)

def merge(l):
    if len(l)==1:
        return l
    mid = len(l)//2
    L = merge(l[:mid])
    R = merge(l[mid:])
    out = []
    while len(L)!=0 and len(R)!=0:
        if L[0] < R[0]:
            out.append(L.pop(0))
        else:
            out.append(R.pop(0))
    while len(R)!=0:
        out.append(R.pop(0))
    while len(L)!=0:
        out.append(L.pop(0))
    return out





l = [3,5,4,1,2,7,8]
#print(bubble(l))
#print(selection(l))
#print(insertion(l))
#print(quick(l))
print(merge(l))
#print(shell(l,[5,3,1]))