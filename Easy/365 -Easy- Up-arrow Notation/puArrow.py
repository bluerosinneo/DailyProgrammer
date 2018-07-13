def upArrow(a,n,b):
    if (n==1):
        return a**b
    elif(b==0):
        return 1
    else:
        return upArrow(a,(n-1),upArrow(a,n,(b-1)))

print("1 ↑ 0")
print(upArrow(1,1,0))

print("1 ↑↑ 0")
print(upArrow(1,2,0))

print("3↑↑↑2")
print(upArrow(3,3,2))

print("4↑↑3")
print("{} digits".format(len(str(upArrow(4,2,3)))))
