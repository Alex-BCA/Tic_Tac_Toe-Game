print("**Tic Tac Toe**")
board=[1,2,3,4,5,6,7,8,9]
def display():
    for i in range(9):
        print(board[i],end="|")
        if(i+1)%3==0:
            print()
            print("------")
display()
def winner():
    win=[
        [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]
        ]
    for a,b,c in win:
        if board[a]==board[b]==board[c]:
            return True
    return False
while True:
    print("Player X turn!")
    position=int(input("player X enter position:"))
    if board[position-1]not in ["X","O"]:
        board[position-1]="X"
        display()
        if winner():
            print("player X wins!")
            break
    else:
        print("position already taken!")
        position=int(input("Enter another position:"))
        board[position-1]="X"
        display()
    if all(i not in board for i in range(1,10)):
        print("Match Draw!")
        break
    print("Player O turn!")
    position=int(input("player O enter position:"))
    if board[position-1]not in ["X","O"]:
        board[position-1]="O"
        display()
        if winner():
            print("Player O wins!")
            break
    else:
        print("position already taken!")
        position=int(input("Enter another position:"))
        board[position-1]="O"
        display()
