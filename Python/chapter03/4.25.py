j=1

while(j <=3):

    sum=0

    for i in range(1,5):

        print( "Enter NO. {} the score {}:". format(j,i) ,end=' ')

        score =eval( input())

        sum = sum + score

        aver = sum/4.0

print("NO.{}aver={:.2f} \n".format(j,aver))

j +=1
