n=input("请输入一个整数：")
n=int(n)
s=1
for i in range(1,n+1):
    s=s*i
print("{0}!={1}".format(n,s))
