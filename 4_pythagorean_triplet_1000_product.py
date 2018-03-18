
flag=False
for a in range(1,1000):
    for b in range(1,1000):
        for c in range(1,1000):
            if((a*a+b*b)==c*c ):
                if (a<b & b<c ):
                    if(a+b+c==1000):
                        print(a,b,c,a*b*c)
                        flag=True
                        break
        if(flag==True):
            break
    if(flag==True):
        break
