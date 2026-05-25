import sys

print("Welcome To TicTac Toe \n")
gameState = True
isWinner0 = False
isWinner1 = False

board = [" "," "," ",
         " "," "," ",
         " "," "," "]

def print_board():
    print("+---+---+---+")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |" + "    "  + "1|2|3")
    print("+---+---+---+")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |" + "    "  + "4|5|6")
    print("+---+---+---+")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |" + "    "  + "7|8|9")
    print("+---+---+---+")
    print("\n")
    
player = [" ", " "]
    
def players():
    print("\nPlayer 1 name: ")
    player[0] = input()
    
    print("\nPlayer2 name: ")
    player[1] = input()

# players()
# print_board()

def turn(turn_num):
    
    if turn_num % 2 == 0:
        while True:
            pos = int(input(f"{player[1]} Enter your position: "))
            if 1 <= pos <= 9:
                if board[pos-1] == " ":
                    board[pos-1] = "O"
                    break
                else:
                    print("Position is already taken try again.")
            else:
                print("Position out of range Try again!")
    else:
        while True:
            pos = int(input(f"{player[0]} Enter your position: "))
            if 1 <= pos <= 9:
                if board[pos-1] == " ":
                    board[pos-1] = "X"
                    break
                else:
                    print("Position is already taken try again.")
            else:
                print("Position out of range Try again!")
    
    
    check_board()
    print_board()
    
def check_board():
    
    
    win_combo = [
        [0,1,2],[3,4,5],[6,7,8], # rows
        [0,3,6],[1,4,7],[2,5,8], # columns
        [0,4,8], [2,4,6] # diagonal
        ]
    
    
    def find_X():
        val = "X"
        idx = []
        
        for i in range(len(board)):
            if(board[i] == val):
                idx.append(i)
                
        if idx:
           # print(f"X found at indices: {idx}.")
          
          
            for i in range(len(win_combo)):
                if len(idx) >= 3:
                    if set(win_combo[i]).issubset(idx):
                        global gameState
                        global isWinner0
                        isWinner0 = True
                        gameState = False  
            
    def find_O():
        val = "O"
        idx = []
        
        for i in range(len(board)):
            if(board[i] == val):
                idx.append(i)
                
        if idx:
           # print(f"O found at indices: {idx}.")
            
            for i in range(len(win_combo)):
                if len(idx) >= 3:
                    if set(win_combo[i]).issubset(idx):
                        global gameState
                        global isWinner1
                        isWinner1 = True
                        gameState = False        
            
    find_X()
    find_O()


def clearGame():
    global gameState
    gameState = True
    global board
    global isWinner0
    global isWinner1

    
    board = [" "," "," ",
         " "," "," ",
         " "," "," "]
    
    isWinner0 = False
    isWinner1 = False
    
def playAgain():
    again = str(input("Do you want to play again (type yes or no): "))
    if again == "yes":
        clearGame()
        game()
    else:
        sys.exit(0)


def game():
    global gameState
    turn_num = 1
    players()
    print_board()

    print(player[0] + " Starts the game! \n")
    
    while gameState == True :
        turn(turn_num)
        turn_num += 1
        if turn_num == 10 and isWinner0 == False and isWinner1 == False:
            print("Game ended with no winners!")
            gameState = False
    
    if isWinner0:
        print(f"Game ended with {player[0]} as the Winner!")
    elif isWinner1:
        print(f"Game ended with {player[1]} as the Winner!")
        
    playAgain()
        
    
    
game()
