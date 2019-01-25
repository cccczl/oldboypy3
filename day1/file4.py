#!/bin/bash/env python
# _*_ coding:utf-8 _*_
# python version:3.6

'''
编写登录接口：
    1.输入用户名和密码登录
    2.输错三次锁定账户
    3.下次登录还是上次的账户，提示锁定，直接退出（用到文件读写）
    4.成功 后显示登录成功
'''
# lock定义为锁定文件
lock = "D:/project/oldboypy3/day1/lock.txt"
# account定义为账户文件

account = "D:/project/oldboypy3/day1/userpassword.txt"
# 计数器
count = 0
# 标识器
flag = 1
# 定义锁定用户列表为空
lock_user = []

# 打开锁定文件，并读取锁定账户
f1 = open(lock, 'r')
lock_file = f1.readlines()
f1.close()

# 循环锁定账户，将账户追加到lock_user列表中
for i in lock_file:
    i = i.strip('\n')
    lock_user.append(i)
# 打开账户文件，并读取用户和密码
f2 = open(account, 'r')
account_file = f2.readlines()
f2.close()

while True:
    name = input("input your name:")
    passwd = input("input your password:")
    # 如果输入的账户在锁定用户列表中，退出循环；
    if name in lock_user:
        print("user is lock!")
        break
    else:
        # 否则计数器加count+1
        count += 1
        # 如果count大于2，也就是输错三次
        if count > 2:
            print("错误三次")
            # 将账户添加到锁定账户中
            with open(lock, 'a') as f:
                f.write("\n" + name)
            break
        # 如果count小于2,
        else:
            # 循环输入的用户名和密码，是否和账户文件里边的一样
            for i in account_file:
                n1, p1 = i.strip().split()
                if name == n1 and passwd == p1:
                    print("welcome login!!")
                    # 如果账户密码一样，flag标识为True
                    flag = True
                # 如果输入账户密码和文件存储的不一样，则跳出本次循环
                else:
                    # 跳出本次循环
                    continue
        # 如果flag标识为True，退出整个循环
        if flag is True:
            break
# Autthor:zhang long
