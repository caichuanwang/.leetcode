def test():
    a = [1,2,3,4]
    for i  in range(a.__len__()-1):
        print(i)
    for i  in reversed(range(a.__len__()-1)):
        print(i)

if __name__ == "__main__":
    test()
