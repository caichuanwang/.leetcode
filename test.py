def test():
    a = [1,2,3,4]
    length = a.__len__()
    i,j = 0,length -1
    while i <= length-1 and j >= 0:
        print(i)
        print(j)
        print("----------")
        i+=1
        j-=1
    
    
if __name__ == "__main__":
    test()
