# Hello World program in Python

correct_word = "skill"

length = len(correct_word)
found = False
tries = 0


def check_word(correct,choice):
    flag = 0
    
    for i in range(0,length):
        if correct[i] == choice[i]:
            flag = flag + 1
            print(" letter {0} exists and is in CORRECT position".format(correct[i]))
        else:
            if choice[i] in correct:
                print("letter {0} EXISTS but it is in WRONG position".format(choice[i]))
            else:
                print("letter {0} does NOT EXISTS".format(choice[i]))
    
    return flag
                
            
while(found == False and tries < 5):
    tries = tries+1
    print("Enter a word of {0} characters".format(length))
    word = input()
    flag = check_word(correct_word,word)
    if flag == length:
        found = True

if found == True:
    print("You have WON!")
else:
    print("Sorry, Please try again")
    
    
    
    
    
