# Autthor:zhang long

import os, sys, itertools

path = "D:\project\oldboypy3\day1"
print(path)
fd = os.chdir("D:\project\oldboypy3\day2")
print(os.getcwd())

# 简单设想，透过input命令改变目录。并列出目录中的所有文件。

while True:
    current_directory = os.getcwd()
    print("============================")
    print("上方为当前所在的目录%s" % current_directory)
    chdir_directory = input("请在这里输入你想要到达的目录：")
    

    if chdir_directory == "q" or chdir_directory =="Q":
        break
    else:
        movie_dir = os.chdir(chdir_directory)
        list_dir = os.listdir(chdir_directory)
        print(list_dir)
