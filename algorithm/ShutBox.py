import random


def twoDiceSum():
    dice1 = random.randint(1, 7)
    dice2 = random.randint(1, 7)
    return dice1 + dice2

def dfs(start, target, board, nextBoards):
    if target == 0:
        nextBoards.append(board)
        return

    for i in range(start, 9):
        if board[i] == 1:
            if board[i] <= target:
                # flip to zero, recurse to next level
                board[i] = 0
                dfs(i + 1, target - (i + 1), list(board), nextBoards)
                board[i] = 1
            else:
                return

# index is number number on card
board = [1] * 10

# simulate one iteration
target = twoDiceSum()

print("Test:")
print("Target: %i"%target)

nextBoards = []
dfs(0, target, board, nextBoards)
print(nextBoards)

# simulate entire game (no player involved)
currentBoards = [board]
players = ['A', 'B']
i = 0
while currentBoards:
    target = twoDiceSum()

    nextBoards = []
    dfs(0, target, board, nextBoards)
    currentBoards = nextBoards

    if not currentBoards:
        print("Game over")
        break

    # make a "strategic move" here
    currentBoardIdx = random.randint(0, len(currentBoards))
    try:
        board = currentBoards[currentBoardIdx]
    except:
        print(currentBoards)
        break

    # log message:
    print("Player %s rolled dice sum %i, end state %s"%(players[i%2], target, board))

    i += 1