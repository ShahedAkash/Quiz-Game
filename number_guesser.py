import random

random_number_range = input("Type the range of random number. ")

if random_number_range.isdigit():
    random_number_range = int(random_number_range)

    if random_number_range <= 0 :
        print('please type the number avobe 0.')
        quit()

else:
    print('Try next time.')
    quit()

random_number = random.randint(0 ,  random_number_range)
guesses = 0
while True:

    guesses +=1

    number_guess = input('Guess a number-')
    if number_guess.isdigit() :
        number_guess = int(number_guess)
    else:
        print('Try to put a number next time.')
        continue
    if number_guess == random_number:
        print('You guese the correct number.')
        break
    elif number_guess > random_number:
        print('You are avobe the number.')
    else:
        print('you are below the number.')

print('You got the number by trying',guesses,'times.')