# Autthor:long zhang

age_of_oldboy = "56"

for i in range(3):
    guess_age = input("guess age:")
    if age_of_oldboy == guess_age:
        print("yes,you got it")
        break
    elif guess_age > age_of_oldboy:
        print("think smaller ....")
    else:
        print("think bigger!")
else:
    print("too many times")
