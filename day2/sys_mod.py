# Autthor:zhang long
#import sys

'''
print(sys.path)
print(sys.argv)
print(sys.argv[0])
'''

'''
import os

#os.system("dir")  # 只能够执行
cmd_res = os.popen("dir").read()
print("-----", cmd_res)
os.mkdir("new")
'''

china_who = '我爱北京'
china_one = '我爱北京天安门'
china = ""

china = china_one if len(china_who) < len(china_one) else china_who #三元运算,根据条件判断该写变量。

print(china)
print(china.encode())
print(china.encode().decode())