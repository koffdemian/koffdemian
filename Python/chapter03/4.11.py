n=1
while(n<=6):
    score=input("请输入一个学生的成绩：")
    score=float(score)
    if score>=60.0:
        print("passed")
    else:
        print("failed")
        n=n+1