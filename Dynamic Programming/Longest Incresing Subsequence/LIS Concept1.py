import time
n = int(input())
X = list(map(int,input().split()))

def LISConcept1(n, X):
    LIS = [1 for _ in range(n)]
    solution = [[] for i in range(n)]

    for i in range(1,n):
        for j in range(i):
            if X[i] > X[j] and LIS[i] < LIS[j] + 1:
                sol = [X[j]]
                sol.extend(solution[j])

                LIS[i] = LIS[j] + 1
                solution[i] = sol

    for i in range(n):
        solution[i].reverse()
        solution[i].append(X[i])

    return max(LIS), solution[LIS.index(max(LIS))]


st = time.process_time()

optimalValue, optimalSolution = LISConcept1(n, X)
print(optimalValue)
print(*optimalSolution)

et = time.process_time()
print(f"Running Time: {et-st}")