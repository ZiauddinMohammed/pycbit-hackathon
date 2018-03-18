string=input()
l=len(string)
mid=int((l+1)/2)
flag=False
for i in range(0,mid+1):
    if(string[i]==string[l-i-1]):
        flag=True
    else:
        flag=False
        break
if(flag==True):
    if(i==mid):
        print(string+" is a palindrome")
    else:
        print(string+" is not a palindrome") 
else:
        print(string+" is not a palindrome") 
