# Autthor:long zhang
import getpass

_user = "long"
_password = "791026"

username = input("username:")
password = getpass.getpass("password:")

if _user == username and _password == password:
    print("Welcome user {name} login...".format(name=username))
else:
    print("Invalid username or password")

#特殊的格式化拼接。
info = '''
---------info of {_username}------

Username:{_username}
Password:{_passowrd}

''' .format(_username=username,_passowrd=password)


print(info)