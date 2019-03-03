f = open("D:\project\oldboypy3\day1\lock.txt", encoding="utf-8")
print("这里是光标位置", f.tell())
count = 0
for info in f:
    if count > 2 and count % 2 == 1:
        print("------------------")
    count += 1
    print(info.strip("\n"))
print("----------guangbiao-----------")
f.seek(20)
print(info)
print(f.encoding)
print(f.name)
print("这里是新光标位置", f.tell())
print(type(info))
f.close()
