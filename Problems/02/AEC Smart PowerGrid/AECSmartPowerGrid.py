import time
N, C = list(map(int,input().split()))
S, T = list(map(int,input().split()))
Edges = []
for _ in range(C):
    c = list(map(int, input().split()))
    for e in Edges:
        if set(c[:2]) == set(e[:2]):
            e[2] += c[2]
            break
    else:
        Edges.append(c)

print(Edges)
def AECSmartPowergrid():
    return

st = time.process_time()
print()
et = time.process_time()
print(f"Running Time: {et-st}")