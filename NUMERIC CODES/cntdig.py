a=int(input("Enter a number:"))
copy=a
count =0
while(copy!=0):
    b=copy%10
    count=count+1
    copy=copy//10
print("The number of digits is :",count)
