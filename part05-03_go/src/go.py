# Write your solution here
def who_won(game_board: list) -> int:
    player_1 = 0
    player_2 = 0
    for game in game_board:
        for number in game:
            if number == 1:
                player_1 +=1
            if number == 2:
                player_2 +=1
    if player_1 > player_2:
        return 1
    elif player_2 > player_1:
        return 2
    else:
        return 0


if __name__ == "__main__":

    winner = who_won([
             [1,1,0,2,1,0],
             [2,1,0,0,1,2],
             [1,2,0,2,1,2],
             [0,2,2,2,2,0]])

    print(winner)