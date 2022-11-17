# Autthor:zhang long
# !/bin/bash/env python
# _*_ coding:utf-8 _*_
# python version:3.6

lock = "D:/project/oldboypy3/day1/lock.txt"
account = "D:/project/oldboypy3/day1/userpassword.txt"

count = 0
flag = 1
lock_user = []

with open(lock, 'r') as f1:
    lock_file = f1.readlines()
for i in lock_file:
    i = i.strip('\n')
    lock_user.append(i)

with open(account, 'r') as f2:
    account_file = f2.readlines()
while True:
    name = input("input your name:")
    passwd = input("input your password:")
    if name in lock_user:
        print("user is lock!")
        break
    else:
        count += 1
        for i in account_file:
            n1, p1 = i.strip().split()
            if name != n1 or passwd != p1:
                continue
            print("welcome login!!")
            flag = True
    if flag is True:
        break
    if count > 2:
        print("错误三次")
        with open(lock, 'a') as f:
            f.write("\n" + name)
            break
