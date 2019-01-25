# Autthor:zhang long
import copy
'''
names = ["zhanglong", "long", "cccczl", "dddd", "ccc", "fffff"]
names2 = names.copy()
names[0] = "张龙"
print(names)
print(names2)

# 浅copy，只是name2中的列表只是name中的引用。列表中的子列表被保存在另一个内存地址中，所以copy只是拷贝了第一层，子列表中并不会改变。
names = ["zhanglong", "long", "cccczl", ["zhang", "kill"], "dddd", "ccc", "fffff"]
names2 = names.copy()
names[0] = "张龙"
names[3][0] = "龙"
print(names)
print(names2)
names.clear()
print(names, names2)

names = ["zhanglong", "long", "cccczl", ["zhang", "kill"], "dddd", "ccc", "fffff"]
names2 = copy.deepcopy(names)
names[3][0] = "龙"
print(names,names2)
#循环打印列表中的值
for i in names:
    print(i)

print("----------------------------------------------")
# 间隔打印列表中的值
print(names[::3])
#或者
new_names= names[::3]
for i in new_names:
    print(i)
'''

#浅copy，再次列举,例子联合账号。
person = ["name", ["saving", 100]]
p1 = person[:]
p2 = person[:]
print(p1)
print(p2)

p1[0] = "long"
p2[0] = "luo"

p1[1][1] = 50
print(p1)
print(p2)


'''
p1= copy.copy(person)
p2 = person[:]
p3 = list(person)
'''

'''
print(names)
print(names[:3])
print(names[-3:])

names.append("lily")
print(names)
names.insert(1,"kkkk")
names.append("zhang")
print(names)
names[0] = "zhang"
print(names)
names.remove("zhang")
del names[0]
names.pop(0)
print(names)
print(names.index("fffff"))
names.append("zhang")
print(names.count("zhang"))
#reverse 反正
names.reverse()
print(names)
#sort 排序，符号———>数字————>大写————>小写，优先级安装asc码来的
names.sort()
print(names)
names2 = [1,2,3,4]
names.extend(names2)
del names2
print(names)
'''
