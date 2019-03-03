f = open("gequ", "r",encoding="utf-8")
link = f.readline(5)
print(link)
print(f.tell())

'''
count = 0
for i in f:
    print(i.strip("\n"))
    count += 1
    if count % 2 == 0:
        print("--------------------------------")

f.seek(0, 0)
print(f.tell())

w = open("gequ", "a", encoding="utf-8")
print(w.write("你好世界"))
w.close()
'''
