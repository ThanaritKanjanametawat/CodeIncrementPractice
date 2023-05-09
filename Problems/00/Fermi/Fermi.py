#Time used: 5 minutes
import time
Answer = list(map(int,input().split()))
Guess = list(map(int,input().split()))

def Fermi(Answer, Guess):
    Hint = []
    for i in range(3):
        if Guess[i] == Answer[i]:
            Hint.append("Fermi")
        elif Guess[i] in Answer:
            Hint.append("Pico")
        else:
            Hint.append("Nano")

    return sorted(Hint)

st = time.process_time()
print(*Fermi(Answer, Guess))
et = time.process_time()
print(f"Running Time: {et-st}")