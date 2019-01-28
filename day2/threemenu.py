# Autthor:zhang long

company_dict = {
    "北京": {
        "昌平": {
            "沙河": ["oldbay", "noatin"],
            "天通苑": ["我爱我家", "链家地产"]
        },
        "朝阳": {
            "望京": ["奔驰", "宝马"],
            "国贸": ["cicc", "Hp", "CISCO"],
            "国贸": ["cicc", "Hp", "CISCO"]
        },
        "海淀": {},
    },
    "山东": {
        "德州":{},
        "青岛":{},
        "济南":{},
    },
    "广东": {
        "东莞":{},
        "常熟":{},
        "佛山":{},
        
    }
}

while True:
    for i in company_dict:
        print(i)
        
    choice = input("选择输入:")
    if choice in company_dict:
        while True:
            for j in  company_dict[choice]:
                print("\t",j)
            while True:
                choice_2 = input("选择输入2:")
                for g in company_dict[choice][choice_2]:
                    print("\t""\t",g)
                while True:
                    choice_3 = input("选择输入3:")
                    for h in company_dict[choice][choice_2][choice_3]:
                        print("\t""\t",h)
