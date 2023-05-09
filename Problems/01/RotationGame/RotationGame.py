import time
N, M = list(map(int,input().split()))
Movements = []
for _ in range(M):
    Movements.append(list(map(int,input().split())))

def rowRotate(Board, N, row):
    Board[row] = Board[row][N-1:] + Board[row][:N-1]

def columnRotate(Board, N, column):
    prev = Board[0][column]
    for i in range(N):
        prev, Board[i][column] = Board[i][column], prev

    Board[0][column] = prev



def RotationGame(N, M, Movements):
    Board = []
    i = 1
    while i <= N**2:
        b = []
        for _ in range(N):
            b.append(i)
            i += 1
        Board.append(b)


    for movement in Movements:
        cord = [0,0]
        for row in Board:
            if movement[0] in row:
                cord = [Board.index(row), row.index(movement[0])]
        count = 0
        while movement[0] not in Board[movement[1]-1]:
            columnRotate(Board, N, cord[1])
            cord[0] = (cord[0]+1) % N
            count += 1

        while Board[movement[1]-1][movement[2]-1] != movement[0]:
            rowRotate(Board, N, cord[0])
            count += 1


        print(count)





st = time.process_time()
RotationGame(N, M, Movements)
et = time.process_time()
print(f"Running Time: {et-st}")