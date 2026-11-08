n=int(input("Enter a number:"));
a=0
b=1
for i in range (1,n+1):
    print(a,end=" ")
    sum=a+b
    a=b
    b=sum