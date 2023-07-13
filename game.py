def printboard():
    print("| {} | {} | {} |".format(1,2,3))
    print("-------------")
    print("| {} | {} | {} |".format(4,5,6))
    print("-------------")
    print("| {} | {} | {} |".format(7,8,9))
    print("-------------")

def state(line):
    print("| {} | {} | {} |".format(line[0],line[1],line[2]))
    print("-------------")
    print("| {} | {} | {} |".format(line[3],line[4],line[5]))
    print("-------------")
    print("| {} | {} | {} |".format(line[6],line[7],line[8]))
    print("-------------")

line=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

def result(a,b,c):
    return a+b+c

def check(X,O):
    condition = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for win in condition:
        if result(X[win[0]],X[win[1]],X[win[2]])==3:
            print("X wins the match")
            return 1
        if result(O[win[0]],O[win[1]],O[win[2]])==3:
            print("O wins the match")
            return 0
    print("Match Tie and over")
    return -1


X=[0,0,0,0,0,0,0,0,0]
O=[0,0,0,0,0,0,0,0,0]
print("Welcome to Tic Tac Toe Game")
printboard()
turn=1
for turn in range(1,10):
    if (turn%2)!=0:
        print("Player X's chance")
        choose=int(input("Please choose (1-9): "))
        line[choose-1]="X"
        X[choose - 1] = 1  # Update X list
        state(line)
        turn=turn-1
    else:
        print("Player O's chance")
        choose=int(input("Please choose (1-9): "))
        line[choose-1]="O"
        O[choose - 1] = 1  # Update O list
        state(line)
        turn=turn-1
    cwin=check(X,O)
    if(cwin!=-1):
        print("Match over")
        break
        