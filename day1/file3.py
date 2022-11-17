import sys, os, getpass

os.system('clear')  # 把终端代码页面清空,提供个干净的视觉
for i in range(3):
    username = input("请输入用户名:")

    lock_file = open('lock.txt', 'r+')  # 当用户输入用户名后，打开LOCK 文件 以检查是否此用户已经LOCK了
    lock_list = lock_file.readlines()

    for lock_line in lock_list:  # 循环LOCK文件
        lock_line = lock_line.strip('\n')  # 去掉换行符
        if username == lock_line:  # 如果LOCK了就直接退出
            sys.exit(f'=======WARNING:该账号 {username} 已经被冻结========')

    user_file = open('userpassword.txt', 'r')  # 打开帐号文件
    user_list = user_file.readlines()
    for user_line in user_list:
        (user, password) = user_line.strip('\n').split()  # 分别获取帐号和密码信息
        if username == user:  # 如用户名正常匹配
            for m in range(3):
                passwd = getpass.getpass('请输入密码:')  # 输入密码,相对安全
                if passwd == password:  # 密码正确，提示欢迎登录
                    print(f'HI,{username},欢迎登录系统')
                    sys.exit(0)  # 正常退出
                elif m != 2:  # m=2时，是最后一次机会，不用在提示还剩余0次机会了
                    print('用户 %s 密码错误，请重新输入，还有 %d 次机会' % (username, 2 - m))
            lock_file.write(username + '\n')  # 密码输入三次错误后，将该用户追加到LOCK文件
            sys.exit(f'用户 {username} 达到最大登录次数，请联系管理员!!')
    if i != 2:  # i=2时，是最后一次机会，不用在提示还剩余0次机会了
        print('用户 %s 不存在，请重新输入，还有 %d 次机会' % (username, 2 - i))
sys.exit(f'用户 {username} 不存在，退出')

lock_file.close()  # 关闭lock文件
user_file.close()  # 关闭user_id文件
# Autthor:zhang long
