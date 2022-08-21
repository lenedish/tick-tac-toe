import random
import tkinter 
from tkinter import messagebox

buttons = [[0 for i in range(3)] for j in range(3)]

boardElements = [[0, 0, 0], 
                 [0, 0, 0],
                 [0, 0, 0]]



def main(buttons, boardElements):

    window = tkinter.Tk()
    window.resizable(False, False)
    window.title('tic-tac-toe')

    for row in range(3):
        for column in range(3):
            buttons[row][column] = tkinter.Button(window, text=' ', font=('consolas', 50), width=2,
            command=lambda row=row, column=column: game(row, column, buttons, boardElements))
            buttons[row][column].grid(row=row, column=column)

    window.mainloop()

def game(row, column, buttons, boardElements):

    if playerChoise(row, column, buttons, boardElements) == False:
        return

    if gameState(gameCheck(boardElements)) == True:
        return

    if computerChoise(buttons, boardElements) == False:
        return
    
    if gameState(gameCheck(boardElements)) == True:
        return

    
def playerChoise(row, column, buttons, boardElements):
    # Player choise
    choise = buttons[row][column]

    if boardElements[row][column] != 0:
        return False
    else:
        choise.config(text='X')
        boardElements[row][column] = 1 

# If no cells is left return
def empty(boardElements):
    emptyCounter = 0

    for boardElement in boardElements:
        if 0 not in boardElement:
            emptyCounter += 1

        if emptyCounter == 3:
            return True

def gameCheck(brdEls):

    # Horizontal
    for brdEl in brdEls:
        if brdEl[0] == brdEl[1] == brdEl[2] and brdEl[0] != 0:
            if brdEl[0] == 1:
                return 1
            else:
                return 2
    
    # Vertical
    for column in range(3):
        if brdEls[0][column] == brdEls[1][column] == brdEls[2][column] and brdEls[0][column] != 0:
            if brdEls[0][column] == 1:
                return 1
            else:
                return 2

    # Diagonal
    for column in range(0, 4, 2):
        if brdEls[0][0 + column] == brdEls[1][1] == brdEls[2][2 - column] and brdEls[0][0 + column] != 0:
            if brdEls[0][0 + column] == 1:
                return 1
            else:
                return 2

    if empty(boardElements) == True:
        return 3

    return False


def gameState(state):
    if state != False:
        for row in range(3):
            for column in range(3):
                buttons[row][column]["state"] = "disabled"
        if state == 3:
            messagebox.showinfo('Game State', 'Tie')
        elif state == 1:
            messagebox.showinfo('Game State', 'You win')
        elif state == 2:
            messagebox.showinfo('Game State', 'You lose')
        return True
    
            
def computerChoise(buttons, boardElements):

    move = False

    while move == False:
        row = random.randrange(0, 3)
        column = random.randrange(0, 3) 

        if empty(boardElements) == True:
            return

        choise = buttons[row][column]

        if boardElements[row][column] == 0:
            choise.config(text='O')
            boardElements[row][column] = 2
            move = True
    
main(buttons, boardElements)
