import random,copy

def drawBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['bot-L'] + '|' + board['bot-M'] + '|' + board['bot-R'])
    print('-----')

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O ?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O' , 'X']
    
def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeBoard(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    return ((bo['top-L'] == le and bo['top-M'] == le and bo['top-R'] == le) or
            (bo['mid-L'] == le and bo['mid-M'] == le and bo['mid-R'] == le) or
            (bo['bot-L'] == le and bo['bot-M'] == le and bo['bot-R'] == le) or
            (bo['top-L'] == le and bo['mid-M'] == le and bo['bot-R'] == le) or
            (bo['top-M'] == le and bo['mid-M'] == le and bo['bot-M'] == le) or
            (bo['top-R'] == le and bo['mid-R'] == le and bo['bot-R'] == le) or
            (bo['top-L'] == le and bo['mid-M'] == le and bo['bot-R'] == le) or
            (bo['top-R'] == le and bo['mid-M'] == le and bo['bot-L'] == le) )

def isSpaceFree(board,move):
    return board[move] == ''

def getPlayerMove(board):
    move = ''
    while move not in 'top-L top-M top-R mid-L mid-M mid-R bot-L bot-M bot-R'.split() or not isSpaceFree(board,move):
        print('What is your next move? (top-, mid-, bot- & L, M, R)')
        move = input()
    return move

def makeMove(board, letter, move):
    board[move] = letter

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None
        
def getComputerMove(board, computerLetter):
    if computerLetter == "X":
        playerLetter = "O"
    else:
        playerLetter = 'X'

    for i in 'top-L top-M top-R mid-L mid-M mid-R bot-L bot-M bot-R'.split():
        dupe = copy.copy(board)
        if isSpaceFree(dupe, i):
            makeMove(dupe, computerLetter, i)
            if isWinner(dupe, computerLetter):
                return i
            
    for i in 'top-L top-M top-R mid-L mid-M mid-R bot-L bot-M bot-R'.split():
        dupe = copy.copy(board)
        if isSpaceFree(dupe, i):
            makeMove(dupe, playerLetter, i)
            if isWinner(dupe, playerLetter):
                return i
    
    move = chooseRandomMoveFromList(board, ['top-L', 'top-R', 'bot-L', 'bot-R'])
    if move != None:
        return move
    
    return chooseRandomMoveFromList(board, ['top-M', 'low-M', 'mid-L' ,'mid-R'])

def isboardFull(board):
    for i in 'top-L top-M top-R mid-L mid-M mid-R bot-L bot-M bot-R'.split():
        if isSpaceFree(board, i):
            return False  # Ako postoji prazno polje, tabla nije puna, pa vratite False
    return True  # Ako nijedno polje nije prazno, tabla je puna, pa vratite True

    
print("Welcome to Tic Tac Toe!")

while True:
        theBoard =  {'top-L': '','top-M': '', 'top-R': '',
                    'mid-L': '','mid-M': '', 'mid-R': '',
                    'bot-L': '','bot-M': '', 'bot-R': ''}
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print('The ' + turn + ' will go first')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard,playerLetter):
                    drawBoard(theBoard)
                    print("Hooray! You won the game!")
                    gameIsPlaying = False
                else:
                    if isboardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'computer'
            
            else:
                move = getComputerMove(theBoard,computerLetter)
                makeMove (theBoard, computerLetter, move)

                if isWinner(theBoard,computerLetter):
                    drawBoard(theBoard)
                    print("You Lost! Computer won this game")
                    gameIsPlaying = False
                else:
                    if isboardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'
                    
        if not playAgain():
            break

