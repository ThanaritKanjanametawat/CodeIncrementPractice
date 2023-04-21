import time
n = int(input())
Tasks = []
for _ in range(n):
    Tasks.append(tuple(map(int, input().split())))

Tasks = list(enumerate(Tasks))


def MinTheMaxLateness(n,Tasks):
    Tasks.sort(key=lambda x: x[1][1])

    time = 0
    maxLateness = -1
    for i, T in Tasks:
        time += T[0]
        Lateness = time - T[1]
        if Lateness > maxLateness and Lateness > 0:
            maxLateness = Lateness
        print(i,end= " ")

    print(f"\n{maxLateness}")

st = time.process_time()
MinTheMaxLateness(n,Tasks)
et = time.process_time()
print(f"Running Time: {et-st}")