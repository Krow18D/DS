def mul(x,y):
    if(y==0):
        return 0
    elif(y<0):
        return -(x-mul(x,y+1))
    else:
        return x+mul(x,y-1)
print(mul(4,3))
