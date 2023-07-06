x=eval(input("请输入第一个整数:"))

 # 输入x,并转换为整数

max = x

 # 把x作为max的初值

min =x

 # 把x作为min的初值

for i in range(2, 6, 1):
    x = eval(input("请输入下一个整数:"))  # 输入第2 个数，存放在x中
    if (x > max):
        max = x
    elif (x < min):
        min = x
print("最大值为:{},最小值为:{}".format(max, min))
