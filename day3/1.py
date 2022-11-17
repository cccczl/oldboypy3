list1 = [1, 4, 6, 7, 3, 5, 2, 8, 38, 3, 46, 78]
list1 = set(list1)

list2 = {2, 4, 5, 6, 7, 9, 10, 11, 22}
print(list1, list2)
# 交集
print(list1.intersection(list2))
# 并集
print(list1.union(list2))
# 差集
print(list1.difference(list2))

print(type(list1))
