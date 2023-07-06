num=0

str = "student"

while num< len( str) :

    if str[num] == 'u':

        break

#当读到字符u时，强行退出循环

    print( "循环进行中:" + str[num])
    num=num+1

else:

    str="循环正常结束"

#循环强行退出，该语句不执行

print( str)
