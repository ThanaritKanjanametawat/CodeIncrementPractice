import time
n = int(input())
X = list(map(int,input().split()))
def LISConcept2(n, X):
    pass

st = time.process_time()
optimalValue, optimalSolution = LISConcept2(n, X)
print(optimalValue)
print(*optimalSolution)
et = time.process_time()
print(f"Running Time: {et-st}")