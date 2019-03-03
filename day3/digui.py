# def coding(y):
#     print(y)
#     if y * 20 < 1000:
#         return coding(y * 20)
#     print("--->", y)
#
#
# coding(1)


def add(a, b, c):
    return c(a) + c(b)


reg = add(5, -10, abs)
print(reg)
