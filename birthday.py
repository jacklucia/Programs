correctAnswer = False
notFollowing = 0
while(correctAnswer == False):
    birthday = input("Give me your date of birth now!! MM/DD/YYYY: ")
    if(birthday[1] != '0' or birthday[0] != '1'):
        print("MM/DD/YYYY FORMAT PLEASE (YES THE FIRST M COUNTS, AND THE FIRST D)\n")
        notFollowing += 1
        continue
    else:
        correctAnswer = True
if(notFollowing > 0):
    print('BRO IT WAS A SIMPLE FORMAT THAT YOU MESSED UP ', str(notFollowing), ' TIMES!!\n')
    print("ANYWAY, YO BIRTHDAY IS ", birthday)
else:
    print("Yo birthday is ", birthday)