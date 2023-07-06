n=input("请输入一个大于3的整数")
n=int(n)
flag=1
i=2
while(i<=n**0.5 and flag):
    if(n%i==0):
        flag=0
    else:
        i+=1
if flag:
    print("%d is prime number."%n)
else:
    print("%d is not prime number."%n)