list1=[]
for i in range (1,99999):
    count=0
    for j in range(1,i):
        if(i%j==0):
            count =count +1
    if(count ==2):
        list1.append(i)
print(list1)
