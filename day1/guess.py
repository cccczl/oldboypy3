# Autthor:long zhang

age_of_oldboy = 56
'''
count = 0
while True:
    if count == 3:
        print("Too many times")
        break
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldboy:
         print("yes,you got it")
         break
    elif guess_age > age_of_oldboy:
         print("think smaller ....")
    else:
         print("think bigger!")
    count += 1
print("-----------------------------------------")
'''
count1 = 0
while count1 < 3:
    guess_age = int(input("guess age:"))
    if guess_age == age_of_oldboy:
         print("yes,you got it")
         break
    elif guess_age > age_of_oldboy:
         print("think smaller ....")
    else:
         print("think bigger!")
    count1 += 1
    if count1 == 3 :
        countinec_confirm = input("do you want to keep guess")
        if countinec_confirm != 'n':
            count1 = 0
''''
else:
    print("Too many times")
'''

