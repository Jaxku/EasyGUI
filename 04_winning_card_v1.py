import easygui
import random

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

# Loop until the player doesn't want to continue playing.
while True:
    # Choose card and suit for player, and then repeat for computer
    player = [random.choice(cards), random.choice(suits)]
    computer = [random.choice(cards), random.choice(suits)]

    # Calulate winner acording to position of cards
    if cards.index(player[0]) == cards.index(computer[0]):
            result = "This is a draw!"

    # Player wins if their card has bigger index number
    elif cards.index(player[0]) > cards.index(computer[0]):
        result = "You Win!"

    # Otherwise the computer wins
    else:
        result = "You lose!"

    # Show results and ask if player wants another game
    play_again = easygui.buttonbox(f"You have the {player[0]} of {player[1]}\n"
                                   f"and I have the {computer[0]} of "
                                   f"{computer[1]}\n\n"f"*** {result} ***\n\n"
                                   f"Do you want to play again?", "Game result"
                                   , choices=["Yes", "No"])

    # Ends the loop if the gamer doesn't want to game this swag game anymore
    if play_again == "No":
        break

easygui.msgbox(f"Goodbye,"
               f"Thanks for playing")

