n=input("请输入一个整数：")
n=int(n)
i=1
s=1
while(i<=n):
    s=s*i
    i=i+1
print("{0}!={1}".format(n,s))