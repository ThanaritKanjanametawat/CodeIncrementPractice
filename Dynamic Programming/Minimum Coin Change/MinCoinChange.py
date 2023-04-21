import time
import sys
n = int(input())
_ = int(input())
C = list(map(int,input().split()))


def MinChange(n, C):
    minCoin = [sys.maxsize for _ in range(n + 1)]
    solution = [[] for _ in range(n + 1)]
    minCoin[0] = 0

    for m in range(1,n+1):
        for c in C:
            # minCoin[a] is number of min coins required to make a
            if c <= m and minCoin[m-c] + 1 < minCoin[m]:
                # Temporary solution, will be replace if more optimal solution exist
                sol = []
                sol.append(c)
                sol.extend(solution[m-c])

                minCoin[m] = minCoin[m-c] + 1
                solution[m] = sol


    return minCoin[n], solution[n]



st = time.process_time()

optimalValue, optimalSolution = MinChange(n, C)
print(optimalValue)
print(*optimalSolution)

et = time.process_time()
print(f"Running Time: {et-st}")