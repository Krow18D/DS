def bubblesort(a):
    for last in range(len(a)-1,-1,-1):
        swaped = False
        for walk in range(last):
            if a[walk]>a[walk+1]:
                a[walk],a[walk+1]=a[walk+1],a[walk]
                swaped = True
        if swaped == False:
            break
    
def selectionsort(l):
    for last in range(len(l)-1,-1,-1):
        big = l[0]
        big_pos = 0
        for walk in range(1,last+1):
            if l[walk] > big :
                big = l[walk]
                big_pos = walk
        l[last],l[big_pos] = l[big_pos],l[last]

def Insertionsort(l):
    for i in range(1,len(l)):
        ele = l[i]
        for j in range(i,-1,-1):
            if ele < l[j-1] and l[j]>0:
                l[j] = l[j-1]
            else :
                l[j] = ele
                break
def shellsort(l):
    for i in range(inc):
        for j in range(0,len(l)-1,inc):
            if l[j]>l[j+inc] and (j+inc)<=len(l) :
                l[j+inc],l[j] = l[j],l[j+inc]
                



# lst = [] # method 1
# for row in range(7):
#     in_row = []
#     for col in range(7):
#         in_row.append(0)
#     lst.append(in_row)

# lst = [] # method 2
# for row in range(7):
#     in_row = [0 for _ in range(7)]
#     lst.append(in_row)




graph = [ [0 for _ in range(7)] for _ in range(7)] # method 3
graph[0][1] = 1
graph[0][3] = 1
graph[1][3] = 1
graph[1][4] = 1
graph[2][0] = 1
graph[2][5] = 1
graph[3][2] = 1
graph[3][4] = 1
graph[3][5] = 1
graph[3][6] = 1
graph[4][6] = 1
graph[6][5] = 1

weights = [ [0 for _ in range(7)] for _ in range(7)]
weights[0][1] = 2
weights[0][3] = 1
weights[1][3] = 3
weights[1][4] = 10
weights[2][0] = 4
weights[2][5] = 5
weights[3][2] = 2
weights[3][4] = 2
weights[3][5] = 8
weights[3][6] = 4
weights[4][6] = 6
weights[6][5] = 1


shortest = [ float('inf') for _ in range(7) ]
visited = [ False for _ in range(7)]
comefrom = [ None for _ in range(7)]

def findMin():
    idx = None
    mini = float('inf')
    for i in range(7):
        if shortest[i] < mini and visited[i] == False:
            idx = i
            mini = shortest[i]
    return idx

def shortestPath(start):
    shortest[start] = 0
    while 1:
        from_ = findMin()
        if from_ == None:
            break
        visited[from_] = True
        for to_ in range(7):
            # graph[from_][to_] เช็คว่ามีเส้นจาก from_ ไป to_ หรือเปล่า ถ้ามี จะมีค่าเท่ากับ 1
            if graph[from_][to_] == 1 and shortest[to_] > shortest[from_] + weights[from_][to_]:
                shortest[to_] = shortest[from_] + weights[from_][to_]
    print(shortest)

shortestPath(0)
# display
# for i in range(7):
#     for j in range(7):
#         print(graph[i][j], end='\t')
#     print()

# class rec:
#     def __init__(self, key, data):
#         self.key = key
#         self.data = data


# class Hash:
#     def __init__(self):
#         self.size = 3
#         self.table = [None] * self.size
#         self.total = 0

#     def isPrime(self, v):
#         for i in range(2, v**0.5):
#             if v%i == 0:
#                 return False
#         return True

#     def resize(self):
#         while not self.isPrime(self.size):
#             self.size += 1
        
#         t_table = self.table
#         self.table = [None]*self.size
#         self.total = 0

#         for i in range(t_table):
#             if t_table[i]:
#                 self.put(t_table[i].key, t_table[i].data)


#     def put(self, key, data):
#         if self.total >= self.size:
#             self.resize()
import math

class Heap:
    def __init__(self):
        self.container = []

    def get_parent(self, idx):
        if (idx-1)//2 < 0:
            return None
        return (idx-1)//2

    def update(self, idx):
        par_idx = self.get_parent(idx)
        now = idx
        while par_idx != None:
            if self.container[par_idx] > self.container[now]:
                self.container[par_idx], self.container[now] = self.container[now], self.container[par_idx]
                now = par_idx
                par_idx = self.get_parent(par_idx)
            else:
                break

    def insert(self, data):
        self.container.append(data)
        self.update(len(self.container)-1)

    def display(self, i=0):
        if i < len(self.container):
            indent = int(math.log2(i+1))
            self.display(i*2+2)
            print(' '*indent, self.container[i])
            self.display(i*2+1)

    def delete(self, now = 0):
        L = now*2+1
        R = now*2+2
        if L >= len(self.container) or R >= len(self.container):
            self.container[now] = self.container.pop()
        elif self.container[L] > self.container[R]:
            self.container[now], self.container[R] = self.container[R], self.container[now]
            self.delete(R)
        else:
            self.container[now], self.container[L] = self.container[L], self.container[now]
            self.delete(L)

# H = Heap()
# H.insert(5)
# H.insert(10)
# H.insert(11)
# H.insert(3)
# # print(H.container)
# H.display()
# H.delete()
# # print(H.container)
# H.display()






inc = [5,3,1]
x = [1,6,9,8,16,3,2,4]
# bubblesort(x)
# selectionsort(x)
# Insertionsort(x)
# print(x)
            


