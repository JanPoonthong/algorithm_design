N = int(input())

def main(N):
    col = set()
    posDiag = set() # (r-c)
    negDiag = set() # (r+c)

    res = []
    board = [["."] * N for i in range(N)]

    def backtrack(r):
        if r == N:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        for c in range(N):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    backtrack(0)

    return res


arr = main(N)
for board in arr:
    for row in board:
        print(row)
    print()
