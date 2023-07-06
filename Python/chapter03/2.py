year=int(input("请输入年份："))
day=28
if(year%4==0 and year%100!=0)or year%400==0:
    day=29
    print("{0}年二月有{1}天".format(year,day))