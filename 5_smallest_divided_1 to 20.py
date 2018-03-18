for i in range(2520,20*19*17*13*11*9*7*3*8):
    flag=True
    for j in range(1,20):
        if(i%j==0):
            if(flag==True):
                flag=True
        else:
            flag=False
            break
    if(flag==True):
        if(j>10):
           break
print(i)
