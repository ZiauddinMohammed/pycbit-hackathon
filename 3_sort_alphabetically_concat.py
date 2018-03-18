
list1=["Ron","Hermione","Harry","Professor","Dobby","List Items 2","The House Elf","Potter","Granger","Lockhart","Weasley"]
list2=["Potter","Fred","Greg","George","Voldemort","Sirius","Dumbledore"]
for i in range(0,len(list1)):
    for j in range(0,len(list1)-i-1):
        if list1[j]>list1[j+1]:
            mini=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=mini
for i in range(0,len(list2)):
   for j in range(0,len(list2)-i-1):
        if list2[j]>list2[j+1]:
            mini=list2[j]
            list2[j]=list2[j+1]
            list2[j+1]=mini
    
list1=list1+list2
print(list1)
