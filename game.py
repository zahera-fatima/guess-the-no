import random

guessestaken=1
name = input("Hello! what is your name?")
number  = random.randint(1,100)
print(name+ " I am thinking of a no b/w 1 & 100.")
print("you have 10 chances.")

while guessestaken <= 10:
    print("Take "+str(guessestaken)+"guess")
    guess = int(input())
    guessestaken += 1
    
    if guess==number:
        break
    elif guess< number:
        print("your guess is too low.")
    else:
        print("your guess is too high.")

if guess == number:
    guessestaken = str(guessestaken)
    print("good job,"+name+"! you guess a number in "+guessestaken+" chances.")

else:
    number = str(number)
    print("TRY AGAIN. Number is " +number)

    