a=input("请输入十进制整数：")
print("转换成2进制:{:b}".format(int(a,8)))
print("转换成8进制:{:o}".format(int(a,16)))
print("转换成16进制:{:x}".format(int(a,8)))

'''
↓	    2进制	          8进制	          10进制	           16进制
2进制	-	       bin(int(n,8))	bin(int(n,10))	bin(int(n,16))
8进制	oct(int(n,2))	-	        oct(int(n,10))	 oct(int(n,16))
10进制	int(n,2)	 int(n,8)	        -	           int(n,16)
16进制	hex(int(n,2)) hex(int(n,8))	hex(int(n,10))	   -
'''