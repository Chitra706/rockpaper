import random
moves = ["rock", "paper", "scissors" ]
keep_playing = "true"

while(keep_playing=="true"):
    cmove = random.choice(moves)
    pmove = input("What is your move? rock, paper, scissors?")

    print("The computer chose", cmove)
    if(cmove==pmove):
        print("Tie")
    elif(pmove=="rock" and cmove=="scissors"):
        print("Player won")
    elif(pmove=="rock" and cmove=="paper"):
        print("Computer won")  
    elif(pmove=="paper" and cmove=="rock"):
        print("Player won")
    elif(pmove=="paper" and cmove=="scissors"):
        print("Computer won") 
    elif(pmove=="scissors" and cmove=="paper"):
        print("Player won")
    elif(pmove=="scissors" and cmove=="rock"):
        print("Computer won")                
    