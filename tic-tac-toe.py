import random

def main():
    game = True
    boardElements = [' ', ' ', ' ', 
                     ' ', ' ', ' ',
                     ' ', ' ', ' ',]

    print('0 | 1 | 2')
    print('---------')
    print('3 | 4 | 5')
    print('---------')
    print('6 | 7 | 8\n')

    while game == True:
        playerTurn(boardElements)
        game = gameCheck(boardElements)
        if game == False:
            break

        computerTurn(boardElements)
        game = gameCheck(boardElements)

# Draw the play board
def drawBoard(el):
    print(f'{el[0]} | {el[1]} | {el[2]}')
    print('---------')
    print(f'{el[3]} | {el[4]} | {el[5]}')
    print('---------')
    print(f'{el[6]} | {el[7]} | {el[8]}\n')

def computerChoise():
    return random.randint(0, 8)

def playerChoise():
    print("Your turn:")

    while True:

        while True:
            choise = input('Enter cell number (0 - 8): ')
            if choise.isnumeric() == False:
                print('You must provide number\n')
            else:
                break
        
        choise = int(choise)

        if choise >= 0 and choise <= 8:
            return choise
            break
        print('Number between 0 and 8\n')
        

def playerTurn(boardElements):
    move = False 
    while move == False:
        choise = playerChoise()
        if boardElements[choise] == ' ':
            boardElements[choise] = 'X'
            drawBoard(boardElements)
            move = True
        else:
            print("This cell is not free. Try again\n")

def computerTurn(boardElements):
    move = False 
    print("Computer's turn:")
    while move == False:
        choise = computerChoise()
        if boardElements[choise] == ' ':
            boardElements[choise] = 'O'
            drawBoard(boardElements)
            move = True

# Check if game is win, lose or tie 
def gameCheck(el):
    if ' ' not in el:
        print('Tie!')
        return False
    else:    
        # Columns
        for i in range(3):
            if el[0 + i] == el[3 + i] == el[6 + i] and el[0 + i] != ' ':
                if el[0 + i] == 'X':
                    print("You win!")
                else:
                    print('You lose')
                return False
        # Rows
        for i in range(0, 9, 3):
            if el[0 + i] == el[1 + i] == el[2 + i] and el[0 + i] != ' ':
                if el[0 + i] == 'X':
                    print("You win!!")
                else:
                    print('You lose')
                return False
        # Diagonals
        for i in range(0, 4, 2):
            if el[0 + i] == el[4] == el[8 - i] and el[0 + i] != ' ':
                if el[0 + i] == 'X':
                    print("You win!!")
                else:
                    print('You lose')
                return False
    return True
main()