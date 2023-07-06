import time
scale = 50

start = time.perf_counter()
#返回性能计数器的值（以小数秒为单位）作为浮点数，
# 即具有最高可用分辨率的时钟，以测量短持续时间
#perf_counter()适合小一点的程序测试，会计算sleep()时间。

print("开始下载".center(scale//2,'-'))
for i in range(scale+1):
    a = '*'*i
    b = '.'*(scale - i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
    time.sleep(0.1)
print("\n"+"下载完成".center(scale//2,'-'))