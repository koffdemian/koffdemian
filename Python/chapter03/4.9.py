money=input("请输入购买的款数：")
money=int(money)
if money>=2000:
    money=(1-0.15)*money
elif money>=1000:
    money = (1 - 0.10) * money
elif money >=500:
    money = (1 - 0.075) * money
elif money >=250:
    money = (1 - 0.05) * money
print("实际付款数为：{:.1f}".format(money))
    