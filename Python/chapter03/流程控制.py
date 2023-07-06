#多分支条件语句if-elif-else。
"""if 判断条件1:
    代码段1
elif 判断条件2:
    代码段2
elif 判断条件3:
    代码段3
...
else:
    代码段n
"""
#if嵌套
'''if 判断条件1:               # 外层条件                    
       代码段1
       if 判断条件2:        # 内层条件
              代码段2
       ...
'''
#循环语句
'''
while语句
while 条件表达式:
    代码块
for 语句
for 临时变量 in 目标对象:
    代码块
循环嵌套
while 循环条件1：        	# 外层循环
    代码段1
    while 循环条件2：   	# 内层循环
        代码段2
        ......
for 临时变量 in 目标对象：        	# 外层循环
    代码段1
    for 临时变量 in 目标对象：   	# 内层循环
        代码段2
        ......
'''
'''
#跳转语句
for word in "Python":
    if (word == 'o'):
        break
    print(word, end="  ")
结果P y t h
    
for word in "Python":
    if (word == 'o'):
        continue
print(word, end="  ")
结果P y t h n



'''