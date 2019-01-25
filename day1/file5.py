# Autthor:zhang long
# !/bin/bash/env python
# _*_ coding:utf-8 _*_
# python version:3.6

lock = "D:/project/oldboypy3/day1/lock.txt"
account = "D:/project/oldboypy3/day1/userpassword.txt"

count = 0
flag = 1
lock_user = []

f1 = open(lock, 'r')
lock_file = f1.readlines()
f1.close()
for i in lock_file:
    i = i.strip('\n')
    lock_user.append(i)

f2 = open(account, 'r')
account_file = f2.readlines()
f2.close()

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
            if name == n1 and passwd == p1:
                print("welcome login!!")
                flag = True
            else:
                continue
    if flag is True:
        break
    else:
        if count > 2:
            print("错误三次")
            with open(lock, 'a') as f:
                f.write("\n" + name)
                break
