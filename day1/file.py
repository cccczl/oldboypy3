# Autthor:zhang long


f = open("userpassword.txt", mode='r', encoding='utf-8')

while True:
    user_input = input("用户名:")
    password_input = input("密码:")
    while True:
        data = f.readline().strip()
        if data == user_input and  data==password_input:
            print("用户名正常")
            print("密码正常")
