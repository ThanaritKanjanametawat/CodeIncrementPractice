import time
n = int(input())
Activities = []
for _ in range(n):
    Activities.append(tuple(map(int,input().split())))

Activities = list(enumerate(Activities))


def ActivitySelection(n,Activities):
    Activities.sort(key=lambda x: x[1][1])
    # Always select the first one
    print(Activities[0][0], end=" ")
    left = 0
    for right in range(1, n):
        if Activities[left][1][1] <= Activities[right][1][0]:
            print(Activities[right][0], end=" ")
            left = right


st = time.process_time()
ActivitySelection(n,Activities)
et = time.process_time()
print(f"\nRunning Time: {et-st}")