def hn(n,from_,to_):
    if(n==1):
        print(from_," to ",to_)
    else:
        #print("1")
        free = 6-from_-to_
        hn(n-1,from_,free)
        #print("2")
        hn(1,from_,to_)
        #print("3")
        hn(n-1,free,to_)
        #print("4")
hn(3,1,3)
