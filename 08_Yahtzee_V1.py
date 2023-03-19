import easygui
import random

players = []

player1 = easygui.enterbox(f"Enter the name of player 1: ", "Player 1")
player2 = easygui.enterbox(f"Enter the name of player 2: ", "Player 2")

# Add player names to player list with a score of -
players.append([player1, 0])
players.append([player2, 0])

# Loop until the player does not want to continue playing the game
while True:
    for player in players:
        dice_rolls = 0
        score = 0

        while dice_rolls < 3:
        # list to record the numbers on the 5 dice each roll
        dice = []

        dice_rolls += 1
        for dice_roll in range(5):
            dice.append(random.randint(1, 6))

        # sort dice to make it easy to compare results
        dice.sort()

        # check and shoe results
        # 5 dice are the same if 1st dice matches last dice
        if dice[0] == dice[4]:
            results = "Yahtzee!"
            score += 50

        elif dice[0] == dice[2] or dice[1] == dice[3] or dice[2] \
            == dice[4]:
            result = "Three of a kind!"
            score += 10

            # otherwise
        else:
            result = "Better luck next time"
            roll_again = easygui.buttonbox(f"{player[0]}: dice roll"
                                           f"{dice_rolls} (Current score is "
                                           f"{score})\n\You rolled: "
                                           f"{str(dice).strip('[]')}\n\n"
                                           f"Choose:", "Random draw"
                                           , choices=["Roll again"])

        if roll_again == "Stick":
            easygui.button(f"{str(dice).strip('[]')}\n\n"
                           f"{result} \nScore: {score}", "Result")
            # change player score - 2nd element of player list
            player[1] = score
            dice_rolls = 3

        else:
            # set value to append to score if player doesn't 'stick' any
            player[1] = 0

    # show results for end of round
    # In case of a draw
    if players[0][1] == players[1][1]:
        result = f"This is a draw!\n{players[0][0]} scored {players[0][1]}" \
        f"and {players[1][0]} also scored {players[1][1]}"
    # If player 1 wins
    elif players[0][1] > players[1][1]:
        result = f"The winner is {players[0][0]} with a score of" \
        f" {players[0][1]}\n\n{players[0][0]} scored {players[1][1]}"
        # Or, it will be a player 2 win
        

