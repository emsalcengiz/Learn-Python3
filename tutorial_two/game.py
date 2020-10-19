# game = [[0,0,0,],
#         [0,0,0],
#         [0,0,0],]


# def game_board(player=0, row=0, column=0, just_display=False):
#     # print(type(game))
#     print("   0  1  2")
#     if not just_display:
#         game[row][column]= player
#     # count = 0
#     for count, row in enumerate(game):
#         print(count, row)
#         # count= count+1
#         # for item in row:
#         #     print(item)   



# game_board(just_display=True)
# print("  ---------")
# game_board(player=1, row=2, column=1)
# # game[0][1] = 1
# # game_board()

# # def addition(x, y):
# #     return x+y


# # z = addition("hey"," there")
# # print(z)





import itertools


def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # Horizontal
    for row in game:
        print(row)
        if all_same(row):
            print(f" {row[0]} yatay olarak kazanan oyuncu!")
            return True

    # Diagonal
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f" {diags[0]} çapraz olarak kazanan (/)!")
        return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f" {diags[0]} çapraz olarak kazanan (\\)!")
        return True

    # Vertical
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])

        if all_same(check):
            print(f" {check[0]} dikey olarak kazanan (|)!")
            return True

    return False


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("Başka birini seç!")
            return game_map, False
        print("    " + "  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True

    except IndexError as e:
        print("Error: 0 1 veya 2 olarak satır / sütun girdiğinizden emin olun", e)
        return game_map, False

    except Exception as e:
        print("bi şeyler  ters gitti!", e)
        return game_map, False


play = True
players = [1, 2]
while play:

    game_size = int(input("Oyun büyüklüğü ne kadar? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Mevcut oyuncu {current_player}")
        played = False

        while not played:
            column_choice = int(input("Hangi sütunu oynamak istiyorsun? (0, 1, 2): "))
            row_choice = int(input("Hangi satırı oynamak istiyorsun? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("Oyun bitti. Tekrar oynamak ister misin? (e/h) ")
            if again.lower() == "e":
                print("yeniden başlıyor")
            elif again.lower() == "h":
                print("Byeeeeeee")
                play = False
            else:
                print("Geçerli bir cevap değil..")
                play = False

