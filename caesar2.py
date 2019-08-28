class Queue:
    def __init__(self,list = None):
        if(list == None):
            self.items = []
        else:
            self.items=list
    def enQ(self,x):
        self.items.append(x)
    def deQ(self):
        if(len(self.items)>0):
            return self.items.pop(0)
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return len(self.items) == 0
    def nowData(self):
        return self.items[0]

def resetCode(code):
    code = Queue([2, 5, 6, 1, 8, 3])

def encode(mes,code):
    encodemes=""
    for i in mes:
        if i != " ":
            c = code.deQ()
            code.enQ(c)
            temp = ord(i) + c
            if('a'<=i<='z'):
                if temp > ord('z'):
                    temp-=26
            elif ('A' <=i<= 'Z'):
                if temp > ord('Z'):
                    temp -= 26
            encodemes+=chr(temp)
        else:
            encodemes+=" "
    resetCode(code)
    return encodemes

def decode(mes,code):
    decodemes = ""
    for i in mes:
        if i != " ":
            c = code.deQ()
            code.enQ(c)
            temp = ord(i) - c
            if ('a' <= i<= 'z'):
                if temp < ord('a'):
                    temp += 26
            elif ('A' <=i<= 'Z'):
                if temp < ord('A'):
                    temp += 26
            decodemes += chr(temp)
        else:
            decodemes += " "
    resetCode(code)
    return decodemes



mes = Queue()
code = Queue([2, 5, 6, 1, 8, 3])
print(code.items)
s_in = "Chanyapuk Numprasop"
en = encode(s_in, code)
print(en)
print(code.items)
de = decode(en,code)
print(de)
print(encode(de,code))
