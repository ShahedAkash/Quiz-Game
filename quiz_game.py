print('Hello.Welcome to quiz game.')
askUser = input('Do you want to start the game? ')

score = 0

if askUser.lower() == "yes":
    print('The game is started.')
    
    ans = input('What is the name of the PM of Bangladesh? ')
    if ans.lower() == "seuli bu":
        print('correct')
        score += 1
    else:
        print('incorrect')

    ans = input('How many days are celebrated in Bangladesh? ')
    if ans.lower() == "no one can say":
        print('correct')
        score += 1
    else:
        print('incorrect')

    ans = input('Which language is more important in Bangladesh is Bagla or English? ')
    if ans.lower() == "english":
        print('correct')
        score += 1
    else:
        print('incorrect')

    ans = input('Are you happy in here? ')
    if ans.lower() == "no":
        print('correct')
        score += 1
    else:
        print('incorrect')

    print('You got '+ str(score) + ' point.')
    print('You got correct '+ str((score/4)*100) +'%')

else:
    quit()