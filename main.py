import termcolor
import os
os.system('color')
ans = input("Answer: ").strip().upper()
chance = int(input("Input Chance: "))
keep_ans = ""
first = True
print()
while (chance > 0):
    print("You have chance: " + str(chance))
    if (first):
        for i in range(len(ans)):
            if (i == len(ans)-1):
                print("_")
                print()
            else:
                print("_", end=" ")
            keep_ans += "_"
    word = input("Your letter to Guess: ").strip().upper()
    check = ans.find(word)
    if (check != -1):
        print("Correct!")
        for i in range(len(ans)):
            if (check == i):
                keep_ans = keep_ans[:i] + ans[i] + keep_ans[i + 1:]
            if (i == len(keep_ans) - 1):
                print(keep_ans[i])
                print()
                print()
            else:
                print(keep_ans[i], end=" ")
        first = False
        chance -= 1
    else:
        print("Incorrect")
        print()
        print()
        chance -= 1
if (ans == keep_ans):
    print(termcolor.colored("Exellent!", 'green'))
    print("The answer is " + ans)
else:
    print(termcolor.colored("Sorry~", 'red'))
    print("The answer is " + ans)