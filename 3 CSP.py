def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nq(board, col, n):
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            if solve_nq(board, col + 1, n):
                return True

            board[i][col] = 0

    return False


# -------- USER INPUT --------
n = int(input("Enter number of queens: "))

board = [[0]*n for _ in range(n)]

if solve_nq(board, 0, n):
    print("Solution:")
    for row in board:
        print(row)
else:
    print("No solution")
