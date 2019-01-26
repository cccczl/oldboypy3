# Autthor:zhang long

name = "long\t,myname is too"

'''
print(name.capitalize()) #大写
print(name.count("l")) #统计字符

print(name.center(50,"-")) #用来补全空的字符
print(name.endswith("g")) #用什么结尾
print(name.expandtabs(tabsize=30))
print(name.format(name="long",year=23))

'''


print(name.expandtabs(tabsize=30))#加入空格
p1 = "-"
p2 = ""
string = ("l","2","3","4")
print(p1.join(string))
print(p2.join(string))

print("long".replace("l","z",1))