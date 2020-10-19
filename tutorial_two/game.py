game = [[0,0,0,],
        [0,0,0],
        [0,0,0],]


def game_board(player=0, row=0, column=0, just_display=False):
    # print(type(game))
    print("   0  1  2")
    if not just_display:
        game[row][column]= player
    # count = 0
    for count, row in enumerate(game):
        print(count, row)
        # count= count+1
        # for item in row:
        #     print(item)   



game_board(just_display=True)
print("  ---------")
game_board(player=1, row=2, column=1)
# game[0][1] = 1
# game_board()

# def addition(x, y):
#     return x+y


# z = addition("hey"," there")
# print(z)


