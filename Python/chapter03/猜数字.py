a=float(input("有两次机会，第一次输入数字："))
b=55
if a==b :
    print("恭喜，猜数成功")
    if a == b:
        print("恭喜，猜数成功")
    elif a > b:
        print("很遗憾，你猜大了")

    else:
        print("很遗憾，你猜小了")

elif a>b:
    print("很遗憾，你猜大了")
    a = float(input("最后机会，输入数字："))
    if a == b:
        print("恭喜，猜数成功")
    elif a > b:
        print("很遗憾，你猜大了")
    else:
        print("很遗憾，你猜小了")

else:
    print("很遗憾，你猜小了")
    a = float(input("最后机会，输入数字："))
    if a == b:
        print("恭喜，猜数成功")
    elif a > b:
        print("很遗憾，你猜大了")
    else:
        print("很遗憾，你猜小了")