from math.integer import gcd
n=int(input("Enter a number:"));
print("\n\nPYTHAGORAS THEOREM\n\n")
for i in range(1,n+1):
    for j in range(1,i):
        for k in range(1,j):
             flag=0
             if(k*k) + (j*j) == (i*i) and gcd(gcd(i,j),k)==1:
                 print("a =",k,"b =",j,"c =",i)