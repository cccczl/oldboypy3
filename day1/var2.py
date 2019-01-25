# Autthor:long zhang

#asc ii 码 8位表示一个字节，1KB = 1024个字节，127个用来放置西方的字母等符号。

#gb2312 是表格，用来存放汉字。

#unicode 2个字节来表示，16位来表示。这个基础上，做出了utf-8，可变长，英文模式保存为8位，汉字占3个字节
# -*- coding: utf-8 -*-
#python2 必须使用上面的标识，告诉编译器，使用utf8来处理字符

name = input("name:")
print(name)

username = input("username:")
password = int(input("password:"))

print(username,password)

#特殊的格式化拼接。
info = '''
---------info of {_username}------

Username:{_username}
Password:{_passowrd}

''' .format(_username=username,_passowrd=password)

print(info)
#尽量使用这种拼接方式。
info2 = '''
---------info of %s -------
Username:%s
Password:%d

''' % (name, username, password)

print(info2)

info3 = '''
---------info of {0} -------
Username:{0}
Password:{1}

''' .format(username, password)

print(info3)