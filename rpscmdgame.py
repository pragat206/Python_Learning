import random

#taking player input and defining computer's input

computer = ['rock','paper','scissor']
x = random.randrange(len(computer))
computerinput = computer[x]

playerinput = input("Choose rock,paper or scissor: ").lower()

#Events where player won

def playerwin(playerinput,computerinput):
    playerwon = False
    if playerinput == "rock" and computerinput == "scissor":
        playerwon = True
    elif playerinput == "scissor" and computerinput == "paper":
        playerwon = True
    elif playerinput == "paper" and computerinput == "rock":
        playerwon = True
    else:
        playerwon = False
    return playerwon

#Game body

while True:
    
    if playerwin(playerinput,computerinput):
        print("Player has won the game")
        print("Players Choice:",playerinput,"\nComputer selection:",computerinput)
    elif playerinput == computerinput:
        print("Its a TIE!")
        print("Players Choice:",playerinput,"\nComputer selection:",computerinput)
    else:
        print("Computer won")
        print("Players Choice:",playerinput,"\nComputer selection:",computerinput)
    break
