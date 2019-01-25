# Autthor:zhang long

commodity_list = [("iphone", 5000), ("ihone", 500), ("iphne", 50), ("iphon", 5008), ("iphoe", 50000), ]
salary = input("请输入你的工资(you salary)：")
# print(len(commodity_list))
shop_list = []
# 难点解决，方法用commodity_list倒入到i，在打印查询的下标，得到序号，思考无问题，操作时错误，列表全部一样导致index查找失败。
# 加入了新的方法，enumerate获取下标。
for i in commodity_list:
    print(commodity_list.index(i), i)
while True:
    commodity_select = input("请选择你要购买的商品：")
    if commodity_select.isdigit() and int(commodity_select) < len(commodity_list):
        name, jiage = commodity_list[int(commodity_select)]
        if int(salary) < jiage:
            print("钱都不够买个毛线！")
        
        else:
            shop_list.append(commodity_list[int(commodity_select)])
            salary = int(salary) - jiage
            print("你的余额还剩%s。" % salary)
    
    elif int(commodity_select) >= len(commodity_list):
        print("没有这件商品")
    
    elif commodity_select == "q":
        print(shop_list)
        print("结账完成，你的余额还剩%s。" % salary)
        break

'''
print("--------------------------------")
for index, i in enumerate(commodity_list):
    print(index, i)
'''
