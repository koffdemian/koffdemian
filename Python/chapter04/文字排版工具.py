article = input("请输入您需要排版的内容：")
choice = int(input("请选择您想要使用的功能（1.删除空格  2.英文标点替换  3.英文单词大写）："))
if choice == 1:
    article = article.replace(" ", "")

elif choice == 2:
    choice2 = int(input("请选择您想使用的功能（1.英文标点全部替换为中文标点 2.中文标点全部替换为英文标点）："))
    if choice2 == 1:
        article = article.replace(",", "，")
        article = article.replace(".", "。")
        article = article.replace(":", "：")
        article = article.replace(";", "；")
        article = article.replace("!", "！")
        article = article.replace("?", "？")
    elif choice2 == 2:
        article = article.replace("，", ",")
        article = article.replace("。", ".")
        article = article.replace("：", ":")
        article = article.replace("；", ";")
        article = article.replace("！", "!")
        article = article.replace("？", "?")
    else:
        print("输入错误请重新输入！！！")
elif choice == 3:
    choice3 = int(input("请选择您想使用的功能（1.首字母大写，其余字母小写  2.全文英文首字母大写  3.全文单词大写）："))
    if choice3 == 1:
        article = article.capitalize()
    elif choice3 == 2:
        article = article.title()
    elif choice3 == 3:
        article = article.upper()
    else:
        print("输入错误请重新输入！！！")
else:
    print("输入错误请重新输入！！！")
print("排版后的内容：", article)