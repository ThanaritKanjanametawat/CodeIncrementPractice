#Time used: 1 Hour 40 Minutes
import sys
import time
N, H = map(int,input().split())
S = []
for _ in range(N):
    S.append(int(input()))

def Drone_TH(N, H, S):
    OptimalSolution = sys.maxsize
    HitLayer = []
    for h in range(1, H+1):
        hits = 0
        for i in range(N):
            if (i%2 == 0 and S[i] >= h) or (i%2 == 1 and S[i] >= H-h+1):
                hits += 1

        HitLayer.append(hits)
        if hits < OptimalSolution:
            OptimalSolution = hits

    return OptimalSolution, HitLayer.count(OptimalSolution)

st = time.process_time()
print(*Drone_TH(N, H ,S))
et = time.process_time()
print(f"Running Time: {et-st}")