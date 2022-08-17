import random
number=random.randint(1,10)
player_name= input("hello,what is your name?")
number_of_guesses=0
print("okay "+player_name+' i am going to guess the number between 1 to 10:')
print("please guess the number:")
while number_of_guesses<5:
    guess= int(input())
    number_of_guesses +=1
    if guess<number:
        print('your guess is too low')
    if guess>number:
        print("your guess is too high")
    if guess==number:
        break
if guess ==number:
        print("you have guessed the correct number in "+str(number_of_guesses)+ " tries")     
else:
        print("you have not guessed the right number,the correct number is: "+str(number))       