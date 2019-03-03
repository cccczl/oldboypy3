#
# def test(x, y, z):
#     print(x)
#     print(y)
#     print(z)
#
#
# test(5, 6, 7)
#
# test(y=3, x=4, z=9)
#
#
#
# def test2(x, *args):
#     print(x)
#     print(args)
#
#
# test2(4, 8, 9, 0, 6, True)
#
#
# # for i in test2(4, 8, 9, 0, 6, True):
# #   print(i)
#
# def test3(a=3, *args, **kwargs):
#     print(a)
#     print(args)
#     print(kwargs)
#
#
# test3(a=5, b=4, ke="alb")
# import time
#
#
# def log():
#     time_format ="%Y-%m-%d %X"
#     time_current = time.strftime(time_format)
#     with open('a.txt','a+') as f:
#         f.write("%s enlab acticet \n" %time_current)
#
# def test():
#     print("你好世界")
#
#     log()
#
#
# for i in range(10):
#     test()

def test(x, age=18, *args, **kwargs):
    print(x)
    print(age)
    print(args)
    print(kwargs)


test("nane", age=217, r=34, sex="nan", fell="ddd")
