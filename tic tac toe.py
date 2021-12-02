import random


def printboard(board):
    print(board[0][0] + '|' + board[0][1] + '|' + board[0][2])
    print("-----")
    print(board[1][0] + '|' + board[1][1] + '|' + board[1][2])
    print("-----")
    print(board[2][0] + '|' + board[2][1] + '|' + board[2][2])


def getSquare(num):
    if num >= 1 and num <=3:
        num1 = 0
        if num == 1:
            num2 = 0
            return num1, num2
        elif num == 2:
            num2 = 1
            return num1, num2
        elif num == 3:
            num2 = 2
            return num1, num2
    elif num >= 4 and num <= 6:
        num1 = 1
        if num == 4:
            num2 = 0
            return num1, num2
        elif num == 5:
            num2 = 1
            return num1, num2
        elif num == 6:
            num2 = 2
            return num1, num2
    elif num >= 7 and num <= 9:
        num1 = 2
        if num == 7:
            num2 = 0
            return num1, num2
        elif num == 8:
            num2 = 1
            return num1, num2
        elif num == 9:
            num2 = 2
            return num1, num2


def getNum(num1, num2):
    if num1 == 0 and num2 == 0:
        return 1
    elif num1 == 0 and num2 == 1:
        return 2
    elif num1 == 0 and num2 == 2:
        return 3
    elif num1 == 1 and num2 == 0:
        return 4
    elif num1 == 1 and num2 == 1:
        return 5
    elif num1 == 1 and num2 == 2:
        return 6
    elif num1 == 2 and num2 == 0:
        return 7
    elif num1 == 2 and num2 == 1:
        return 8
    elif num1 == 2 and num2 == 2:
        return 9


def checkSpace(board, square1, square2):
    if board[square1][square2] == ' ':
        return True
    else:
        return False


def setMark(board, mark, square1, square2):
    if checkSpace(board, square1, square2):
        board[square1][square2] = mark
        printboard(board)
        return True
    else:
        return False


def playerTurn(board, mark):
    while True:
        while True:
            try:
                num = int(input("Enter a square: "))
                if num > 0 and num < 10:
                    break
                else:
                    print("Invalid square!")
            except:
                print("Input is not a number, try again.")
        num1, num2 = getSquare(num)
        if setMark(board, mark, num1, num2):
            return
        else:
            print("Invalid square. Try again.")


def aiRandTurn(board, mark):
    while True:
        num1, num2 = random.randint(0, 2), random.randint(0, 2)
        if setMark(board, mark, num1, num2):
            return


def aiTurn(board, mark):
    possibleMoves = []
    for i in range(0, 3):
        for j in range(0, 3):
            if checkSpace(board, i, j):
                move = getNum(i, j)
                possibleMoves.append(move)
    for let in ['O', 'X']:
        for k in possibleMoves:
            i, j = getSquare(k)
            board[i][j] = let
            if checkWin(board):
                board[i][j] = mark
                printboard(board)
                return
            else:
                board[i][j] = ' '

    if 5 in possibleMoves:
        if setMark(board, mark, 1, 1):
            return

    possibleCorners = []
    for k in possibleMoves:
        if k in [1, 3, 7, 9]:
            possibleCorners.append(k)
    if len(possibleCorners) > 0:
        move = random.choice(possibleCorners)
        i, j = getSquare(move)
        if setMark(board, mark, i, j):
            return

    possibleEdges = []
    for k in possibleMoves:
        if k in [2, 4, 6, 8]:
            possibleEdges.append(k)
    if len(possibleEdges) > 0:
        move = random.choice(possibleEdges)
        i, j = getSquare(move)
        if setMark(board, mark, i, j):
            return


def checkTie(board):
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == ' ':
                return False
    return True


def checkWin(board):
    if board[0][0] == board[0][1] == board[0][2] != ' ':
        return True
    elif board[1][0] == board[1][1] == board[1][2] != ' ':
        return True
    elif board[2][0] == board[2][1] == board[2][2] != ' ':
        return True
    elif board[0][0] == board[1][0] == board[2][0] != ' ':
        return True
    elif board[0][1] == board[1][1] == board[2][1] != ' ':
        return True
    elif board[0][2] == board[1][2] == board[2][2] != ' ':
        return True
    elif board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    elif board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    else:
        return False


def game(board):
    printboard(board)
    player = 'O'
    while True:
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        print("Player", player, "turn.")
        playerTurn(board, player)
        tie = checkTie(board)
        win = checkWin(board)
        if win:
            print("Game Over.")
            print(player, "Wins.")
            return
        if tie:
            print("Game Over.")
            print("Tie.")
            return


def easy(board):
    printboard(board)
    marks = ['X', 'O']
    player = random.choice(marks)
    first = False
    while True:
        if player == 'O' or first:
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
            print("Player", player, "turn.")
            playerTurn(board, player)
            tie = checkTie(board)
            win = checkWin(board)
            if tie:
                print("Game Over.")
                print("Tie.")
                return
            if win:
                print("Game Over.")
                print(player, "Wins.")
                return
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
#human turn /\ ----- ai turn \/
        print("Player", player, "turn.")
        aiRandTurn(board, player)
        first = True
        tie = checkTie(board)
        win = checkWin(board)
        if tie:
            print("Game Over.")
            print("Tie.")
            return
        if win:
            print("Game Over.")
            print(player, "Wins.")
            return


def medium(board):
    printboard(board)
    marks = ['X', 'O']
    player = random.choice(marks)
    first = False
    hard = False
    while True:
        if player == 'O' or first:
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
            print("Player", player, "turn.")
            playerTurn(board, player)
            tie = checkTie(board)
            win = checkWin(board)
            if tie:
                print("Game Over.")
                print("Tie.")
                return
            if win:
                print("Game Over.")
                print(player, "Wins.")
                return
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
        # human turn /\ ----- ai turn \/
        print("Player", player, "turn.")
        first = True
        if hard:
            aiTurn(board, player)
            hard = False
        else:
            aiRandTurn(board, player)
            hard = True
        tie = checkTie(board)
        win = checkWin(board)
        if tie:
            print("Game Over.")
            print("Tie.")
            return
        if win:
            print("Game Over.")
            print(player, "Wins.")
            return


def hard(board):
    printboard(board)
    marks = ['X', 'O']
    player = random.choice(marks)
    first = False
    while True:
        if player == 'O' or first:
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
            print("Player", player, "turn.")
            playerTurn(board, player)
            tie = checkTie(board)
            win = checkWin(board)
            if tie:
                print("Game Over.")
                print("Tie.")
                return
            if win:
                print("Game Over.")
                print(player, "Wins.")
                return
            if player == 'X':
                player = 'O'
            else:
                player = 'X'
        # human turn /\ ----- ai turn \/
        print("Player", player, "turn.")
        aiTurn(board, player)
        first = True
        tie = checkTie(board)
        win = checkWin(board)
        if tie:
            print("Game Over.")
            print("Tie.")
            return
        if win:
            print("Game Over.")
            print(player, "Wins.")
            return


def instructions():
    print("Tic Tac Toe Instructions:")
    print("Take turns marking the grid and try to get 3 in a row.")
    print("Marks are assigned randomly and X always goes first.")
    print("The squares are as follows:\n1. 2. 3.\n4. 5. 6.\n7. 8. 9.")
    print("Try and beat the AI! There are 3 difficulties ranging from simple to impossible.")


def Menu(options):
    print(options)
    choice = input("Enter your choice: ")
    return choice


def main():
    print("Tic Tac Toe")
    cont = "y"
    while cont.lower() == "y" or cont.lower() == "yes":
        board = [[' ' for j in range(3)] for i in range(3)]
        selection = Menu("1. Instructions\n2. 2 Player\n3. Easy\n4. Medium\n5. Hard\nE. Exit")
        if selection == "1":
            instructions()
        elif selection == "2":
            game(board)
        elif selection == "3":
            easy(board)
        elif selection == "4":
            medium(board)
        elif selection == "5":
            hard(board)
        elif selection == "e" or selection == "E":
            cont = "n"
        else:
            print("Wrong choice, try again.")


main()