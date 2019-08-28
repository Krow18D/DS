class rec:
    def __init__(self,key,data):
        self.key = key
        self.data = data
    def __str__(self):
        return self.key+","+str(self.data)
class Hashtable:
    def __init__(self):
        self.size = 3
        self.table = [None]*self.size
        self.total = 0
    def printTable(self):
        n = 0
        while n < self.size:
            if self.table[n] != None:
                print(n,' : ',self.table[n])
            n+=1 
    def hash(self,str1):
        sum = 0
        for i in str1:
            sum+=ord(i)
        return sum%self.size
    def rehash(self,count,inx):
        return (count+inx)%self.size
    def resize(self):
        old = self.size 
        oldtable = self.table
        self.total = 0
        self.size*=2
        while not primeNum(self.size):
            self.size+=1
        self.table = [None]*self.size
        for i in oldtable:
            if i != None:
                self.put(i.key,i.data)


    def put(self,key,data):
        if self.total/self.size==1.0:
            self.resize()
        fcol = inx = self.hash(key)
        print(key,inx)
        if self.table[inx]==None:
            self.table[inx]=rec(key,data)
        else:
            count = 0
            index = self.rehash(count,fcol)
            while self.table[index]!= None:
                count+=1
                if self.table[index].key == key:
                    self.total-=1
                    break
                if index == self.size:
                    fcol = count = 0
                index = self.rehash(count,fcol)
            self.table[index] = rec(key,data)
        self.total+=1


def primeNum(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

h = Hashtable()
print(h.table)

h.put('a',7)
h.put('b',555)
h.put('d',766)
h.put('d',7662)

h.printTable()

