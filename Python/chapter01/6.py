color=input("请选择蓝色，黄色其中一种颜色:")

color2=input("请选择红色，黄色其中一种颜色:")

if color=="蓝色"and color2=="红色":
    print("蓝色+红色=紫色")
elif color=="蓝色"and color2=="黄色":print("蓝色+黄色=绿色")
elif color=="黄色"and color2=="红色":print("黄色+红色=橙色")
elif color=="黄色"and color2=="黄色":print("黄色")
else:print("输入错误，请重新输入")