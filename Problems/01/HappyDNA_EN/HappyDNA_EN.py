#Time used: 2 Hours 14 Minutes
import time
import math
DNA = input()
def HappyDNA(DNA):
    LHS = {}
    i = 0.0
    while i < len(DNA)-0.5:
        if i.is_integer():
            LHS[i] = 1
        else:
            LHS[i] = 0

        i += 0.5

    for i in LHS:
        count = 0
        j = i
        while math.ceil(j-count-1) in range(len(DNA)) and math.floor(j+count+1) in range(len(DNA)) and DNA[math.ceil(j-count-1)] == DNA[math.floor(j+count+1)]:
            count += 1

        LHS[i] += 2*count

    solution = list(LHS.values())
    return max(solution), solution.count(max(solution))

st = time.process_time()
Longest, Count = HappyDNA(DNA)
print(Longest)
print(Count)
et = time.process_time()
print(f"Running Time: {et-st}")