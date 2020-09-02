import random

print("Hi,Please enter your name : ",end = "")
name = input()
print("Hi "+name+".Lets play a number guessing name")
secretNumber=random.randint(1,20)

print("I am thinking of a number between 1 to 20")

for guessTaken in range (1,6):
    print("Take a guess")
    inputNumber = int(input())
    if inputNumber > secretNumber:
        print("Too high")
    elif inputNumber < secretNumber:
        print("Too low")
    else :
        break

if inputNumber == secretNumber :
    print("Good job.You guessed the correct number in "+ str(guessTaken) + ' chances')
else :
    print("Opps all chances are over.The number I was thinking of was",secretNumber)




if inputNumber == secretNumber:
    print("Congrats")
else :
    print("Opps your number is not correct.The correct number is : ",secretNumber)