def first():
    prime_list = [1, 2, 3]
    prime_inp = int(input("Input your integer:"))

    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, x):
            if not x % i:
                return False
        return True

    def next_prime(y):
        if is_prime(y):
            return y
        z = 0
        while True:
            if is_prime(z):
                prime_list.append(z)
            if prime_list[len(prime_list) - 1] > y:
                return prime_list[len(prime_list) - 1]
            else:
                z = z + 1

    print(next_prime(prime_inp))


def second():
    num = input("num : ")
    num_int = int(num)
    num_part = num_int
    num_for_sum = 0
    sum = 0
    for x in range(len(num), 0, -1):
        num_for_sum = num_part % 10
        sum += num_for_sum ** (x)
        num_part = num_part // 10

    if sum == num_int:
        print("It's a Disarium number")
    else:
        print("Sorry but no")

def tic_tac_toe():

    grid = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    turn = 0
    won = False
    grid_used = [[False, False, False], [False, False, False], [False, False, False]]
    X_wins = 0
    O_wins = 0

    def Turner():
        global turn
        if (turn%2) == 0:
            print("It's X's turn")
            row = int(input("row you choose(1-3):"))-1
            column = int(input("column you choose(1-3):"))-1
            if not grid_used[row][column] :
                grid_used[row][column] = True
                grid[row][column] = 'X'
                turn += 1
                ifWon()
            else :
                Turner()
        else :
            print("It's O's turn")
            row = int(input("row you choose(1-3):"))-1
            column = int(input("column you choose(1-3):"))-1
            if not grid_used[row][column]:
                grid_used[row][column] = True
                grid[row][column] = 'O'
                turn += 1
                ifWon()
            else:
                Turner()

    def ifWon():
        global won, X_wins , O_wins
        if grid[0][0] != '_':
            if grid[0][0] == grid[0][1]:
                if grid[0][0] == grid[0][2]:
                    won = True
                    if grid[0][0] == 'X':
                        X_wins += 1
                        New_Game()
                    elif grid[0][0] == 'O':
                        O_wins += 1
                        New_Game()
        if grid[0][0] != '_':
            if grid[0][0] == grid[1][1]:
                if grid[0][0] == grid[2][2]:
                    won = True
                    if grid[0][0] == 'X':
                        X_wins += 1
                        New_Game()
                    elif grid[0][0] == 'O':
                        O_wins += 1
                        New_Game()
        if grid[0][0] != '_':
            if grid[0][0] == grid[1][0]:
                if grid[0][0] == grid[2][0]:
                    won = True
                    if grid[0][0] == 'X':
                        X_wins += 1
                        New_Game()
                    elif grid[0][0] == 'O':
                        O_wins += 1
                        New_Game()
        if grid[1][1] != '_':
            if grid[1][1] == grid[0][2]:
                if grid[1][1] == grid[2][0]:
                    won = True
                    if grid[1][1] == 'X':
                        X_wins += 1
                        New_Game()
                    elif grid[1][1] == 'O':
                        O_wins += 1
                        New_Game()
        if grid[1][1] != '_':
            if grid[1][1] == grid[1][0]:
                if grid[1][1] == grid[1][2]:
                    won = True
                    if grid[1][1] == 'X':
                        X_wins += 1
                        New_Game()
                    elif grid[1][1] == 'O':
                        O_wins += 1
                        New_Game()
        if grid[1][1] != '_':
            if grid[1][1] == grid[0][1]:
                if grid[1][1] == grid[2][1]:
                    won = True
                    if grid[1][1] == 'X':
                        X_wins += 1
                        New_Game()
                    elif grid[1][1] == 'O':
                        O_wins += 1
                        New_Game()
        if grid[2][2] != '_':
            if grid[2][2] == grid[0][2]:
                if grid[2][2] == grid[1][2]:
                    won = True
                    if grid[2][2] == 'X':
                        X_wins += 1
                        New_Game()
                    elif grid[2][2] == 'O':
                        O_wins += 1
                        New_Game()
        if grid[2][2] != '_':
            if grid[2][2] == grid[2][0]:
                if grid[2][2] == grid[2][1]:
                    won = True
                    if grid[2][2] == 'X':
                        X_wins += 1
                        New_Game()
                    elif grid[2][2] == 'O':
                        O_wins += 1
                        New_Game()
        if grid_used[0][0]:
            if grid_used[0][1]:
                if grid_used[0][2]:

                    if grid_used[1][0]:
                        if grid_used[1][1]:
                            if grid_used[1][2]:

                                if grid_used[2][0]:
                                    if grid_used[2][1]:
                                        if grid_used[2][2]:

                                            if not won:
                                                X_wins += 1
                                                O_wins += 1
                                                New_Game()
        print_grid()
        Turner()



    def print_grid():
        for i in range(0, 3):
            for y in range(0, 3):
                print("|", end=" ")
                print(grid[i][y], end=" ")
            print("| ")

    def New_Game():
        print("X Wins : ", X_wins)
        print("O Wins : ", O_wins)
        answer = input("You want to continue(Y/N) :")
        if answer == "Y" or answer == "y":
            ifWon()
        else:
            exit()

    ifWon()
print("First exercise")
first()
print("Second exercise")
second()
print("Tic Tac Toe")
tic_tac_toe()