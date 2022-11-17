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
        "德州": {},
        "青岛": {},
        "济南": {},
    },
    "广东": {
        "东莞": {},
        "常熟": {},
        "佛山": {},

    }
}

for i in company_dict:
    print(i)

while True:
    choice = input("选择输入:")
    if choice in company_dict:
        for j in company_dict[choice]:
            print("\t", j)
    elif choice == "b":
        break

    while True:
        choice_2 = input("选择输入2:")
        if choice_2 in company_dict[choice]:
            for g in company_dict[choice][choice_2]:
                print("\t""\t", g)

        elif choice_2 == "b":
            break

        while True:
            choice_3 = input("选择输入3:")
            if choice_3 in company_dict[choice][choice_2]:
                for h in company_dict[choice][choice_2][choice_3]:
                    print("\t""\t", h)
                print("这是最后一层菜单！")

            elif choice_3 in ["b", ""]:
                break

