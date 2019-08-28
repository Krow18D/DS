
def quick(A):
	if len(A) == 0:
		return []
	pivot = A.pop(0)
	L, R = [], []
	for e in A:
		if e <= pivot:
			L.append(e)
		else:
			R.append(e)
	return quick(L) + [pivot] + quick(R)

print(quick([3, 7, 4, 1]))