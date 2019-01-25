# Autthor:zhang long

# 定义常量指定文件路径
LOCK = "lock.txt"
USERPASSWORD = "userpassword.txt"

flag = 0

for count in range(3):
    username = input("请输入用户名（input you username）:")
    password = input("请输入密码（input you password）:")
    
    f = open(LOCK, 'r', encoding='utf-8')
    for i in f.readlines():
        if username == i.strip("\n"):
            print("你的用户已经被锁定")
            flag = True
    
    f1 = open(USERPASSWORD, 'r', encoding='utf-8')
    user_password = f1.readlines()
    
    for userlist in user_password:
        u1, p1 = userlist.strip('\n').split()
        if u1 == username and p1 == password:
            print("欢迎%s登录" % username)
            flag = True
        else:
            continue
    
    if flag == True:
        break
    
    if count == 2:
        file_writh = open(LOCK, 'a', encoding='utf-8')
        file_writh.write('\n' + username)
        print("已经重试3次，将你用户名输入锁定")
        
f.close()
f1.close()
