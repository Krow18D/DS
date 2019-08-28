class Queue:
    def __init__(self,list =None):
        if list==None:
            self.items = []
        else:
            self.items = list
    def enQ(self,x):
        self.items.append(x)
    def deQ(self):
        if self.items != []:
            return self.items.pop(0)
    def size(self):
        return len(self.items)
    def isEmpty(self):
        if len(self.items)==0:
            return True
        else:
            return False

def encode(s_in,code):
    encoded_str =''
    for s in s_in:
        if s != ' ':
            num = code.deQ()
            code.enQ(num)
            temp = ord(s)+num
            if 'a'<=s<='z':
                if temp>ord('z'):
                    temp = ord('a')-ord('z')+temp-1
            if 'A'<=s<='Z':
                if temp>ord('Z'):
                    temp = ord('A') - ord('Z') + temp - 1
            temp2 = chr(temp)
        else:
            temp2 = s
        encoded_str+=temp2
    return encoded_str


code=Queue([2,5,6,1,8,3])
print(code.items)
s_in = "Chanyapuk Numprasop"
en = encode(s_in,code)
print(en)
