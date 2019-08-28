def mergeSort(A):
    if len(A) == 1:
        return A
    mid = len(A)//2
    L = mergeSort(A[:mid])
    R = mergeSort(A[mid:])
    result = []
    while len(L) != 0 and len(R) != 0:
        if L[0] > R[0]:
            result.append(R.pop(0))
        else:
            result.append(L.pop(0))
    while len(L) != 0:
        result.append(L.pop(0))
    while len(R) != 0:
        result.append(R.pop(0))
    return result

def shell(lst, dIncrement):
    for inc in [5, 2, 1]:
        for start in range(len(lst)):
            for walk in range(start+inc, len(lst), inc):
                if lst[walk-inc] > lst[walk] and walk-inc >= 0:
                    lst[walk-inc], lst[walk] = lst[walk], lst[walk-inc]
    return lst



# A = [3, 2 ,56, 1, 9]
# print(A)
# print(mergeSort(A))
A = [1,5,2,4,3,7,6,8]
print(A)
#print(shell(A, [5, 2, 1]))
print(mergeSort(A))

