def bubble(l):
    swap =False
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                swap=True
                l[j],l[j+1] = l[j+1],l[j]
        if not swap: return l 
    return l

def select(l):
    for i in range(len(l)):
        max = l[0]
        ind =0
        for j in range(len(l)-i):
            if l[j]>max:
                max=l[j]
                ind=j
        l[j],l[ind] = l[ind],l[j]        
    return l

def insertion(l):
    for i in range(1,len(l)):    
        for j in range(i,0,-1):
            if l[j]<l[j-1]:
                l[j],l[j-1] = l[j-1],l[j]
            else:
                break
            print(l)
    return l

def shell(l,dIncrement):
    for n in dIncrement:
        for i in range(n,len(l)):
            el = l[i]
            for j in range(i,-1,-n):
                if el <l[j-n] and j>=n:             
                    l[j] = l[j-n]
                else:
                    l[j]=el
                    break
            print(l)
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
    return quick(L) +[pivot]+quick(R)
    
def merge(l):
    if len(l) == 1:
        return l
    mid = len(l)//2
    L = merge(l[:mid])
    R = merge(l[mid:])
    out=[]
    while len(L)!=0 and len(R) !=0:
        if L[0] > R[0]:
            out.append(R.pop(0))
        else:
            out.append(L.pop(0))
    while len(R) != 0:
        out.append(R.pop(0))
    while len(L) != 0:
        out.append(L.pop(0))
    return out

l = [10,11,1,13,2,6,4,12,5,8,7,9,3]

#print(bubble(l))
#print(select(l))
#print(insertion(l))
#print(shell(l,[5,3,1]))
#print(quick(l))
print(merge(l))
