# choices array
choices = ["Rock", "Paper", "Scissors"]

#input
playerChoice = input("Enter your choice (1=Rock, 2=Paper, 3=Scissors): ")
playerChoice = int(playerChoice)

# Validating player input
if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice must be between 1 and 3.")
else:
    # Get computer choice
    computerChoice = input("Enter computer's choice (1-3): ")
    computerChoice = int(computerChoice)

    # Validate computer input
    if computerChoice < 1 or computerChoice > 3:
        print("Error: Choice must be between 1 and 3.")
    else:
        # Array indexing 
        playerPick = choices[playerChoice - 1]
        computerPick = choices[computerChoice - 1]

        print("You chose:", playerPick)
        print("Computer chose:", computerPick)

        # finding the winner
        if playerChoice == computerChoice:
            print("It's a tie!")
        elif playerChoice == 1 and computerChoice == 3:
            print("Rock beats Scissors - You win!")
        elif playerChoice == 2 and computerChoice == 1:
            print("Paper beats Rock - You win!")
        elif playerChoice == 3 and computerChoice == 2:
            print("Scissors beats Paper - You win!")
        else:
            print("You lose!")

        # comparing
        if playerPick != "Rock":
            print("You didn't pick the classic Rock...")
