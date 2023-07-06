a,b,c=input("请输入三角形的三条边长：").split("")
a,b,c=int(a),int(b),int(c)
if(a>0 and b>0 and c>0 and a+b>c and b+c>a and a+c>b):
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print("面积为{0:.2f}".format(area))
else:
    print("不能构成三角形")