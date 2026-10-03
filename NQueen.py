N = 4
board = [-1] * N

def safe(row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(row):
    if row == N:
        for i in range(N):
            print("." * board[i] + "Q" + "." * (N - board[i] - 1))
        print()
        return

    for col in range(N):
        if safe(row, col):
            board[row] = col
            solve(row + 1)
            board[row] = -1

solve(0)