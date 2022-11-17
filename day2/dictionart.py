# Autthor:zhang long


dict1 = {
    '贵州': {
        '贵阳': ['花溪', '白云', '小河'],
        '黔西南': ['兴义', '册亨', "望谟"]
    },
    '甘肃':{
        '兰州':[""]
    }

}

b = {
    1:3,
    2:3
}

'''
print(dict)
# 字典是无序的
dict["海南"]["三亚"] = "崖州区 "
#dict.pop('贵州')
#print(dict)
print(dict.get('贵阳'))
print(dict)
#print(dict["海南"])aa
print('贵阳' in dict)

dict["海南"]['屯昌'] = "鬼地方"
#print(dict['屯昌'])
print(dict.values())
dict.setdefault("台湾",{"台北":["仙桃"]})

p = dict1.get("贵州").get("贵阳")
print(dict1)
print(dict1["贵州"]["贵阳"][0])
print(dict1["甘肃"])
dict1.update(b)#合并字典
print(dict1)
print("-----------------------------------")

for i in dict1:  #推荐使用这种方法查
    print(i,dict1[i])

for k,v in dict1.items(): #这种方法会把字典转成list
    print(k,v)
'''
print(dict1.get("贵阳"))