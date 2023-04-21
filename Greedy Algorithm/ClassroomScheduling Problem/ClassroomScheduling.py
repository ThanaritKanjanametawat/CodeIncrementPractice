import time
n = int(input())
Classes = []
for _ in range(n):
    Classes.append(tuple(map(lambda x: int("".join(x.split(":"))), input().split())))

Classes = list(enumerate(Classes,start=1))



def ClassroomScheduling(n, Classes):
    # Classes.sort(key=lambda x: x[1][1])

    c = 0
    Classrooms = []
    while Classes:
        Classroom = []
        # Always Select the first one
        Classroom.append(Classes[0])

        left = 0
        for right in range(1,len(Classes)):
            if Classes[left][1][1] <= Classes[right][1][0]:
                Classroom.append(Classes[right])
                left = right

        for Class in Classroom:
            Classes.remove(Class)

        Classrooms.append(tuple(map(lambda x: x[0], Classroom)))
        c += 1


    print(c)
    for row in Classrooms:
        print(*row)

st = time.process_time()
ClassroomScheduling(n, Classes)
et = time.process_time()
print(f"Running Time: {et-st}")