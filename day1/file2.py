# Autthor:zhang long

f = open("userpassword.txt", mode="r", encoding="utf-8")
lock = open("lock.txt", mode="r", encoding="utf-8")

count = 0

while count < 3:
    user_input = input("请输入用户名：")
    password_input = input("请输入密码：")
    
    while True:
        hang_du_qu = lock.readline().strip()  # 逐行读取文本中的行
        if hang_du_qu == user_input:  # 和输入进行对比
            print("你的用户名已经被封锁")
            break
        elif not hang_du_qu:  # 否则读取为空行时跳出循环
            break
    
    while True:
        u1, p1 = f.readline().split()
        if u1 == user_input and p1 == password_input:
            print("登录成功")
            break
        elif u1 == user_input or p1 == password_input:
            print("用户名或密码错误")
            break


'''
    
    lock.write(user_input)
    print(user_input)
    lock.close()

    #



while True:
    date, date2 = f.readline().split()
    if user_input == date and password_input == date2:
        print("欢迎登陆{user}".format(user=user_input))
    break
else:
    print("登录错误")
'''
