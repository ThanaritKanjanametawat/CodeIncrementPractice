# Time used: 2 hours 34 minutes
import time
Chord = input().split()
def Harmonics_TH(Chord):
    Notes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    Major_Pattern = (0, 4, 7)
    Minor_Pattern = (0, 3, 7)

    # Turn flat into Sharp
    for i in range(len(Chord)):
        if "b" in Chord[i]:
            Chord[i] = Notes[Notes.index(Chord[i][0])-1]

    for rootnote in Chord:
        idx = Notes.index(rootnote)
        Minor = list(map(lambda x: Notes[x%12],[idx + p for p in Minor_Pattern]))
        Major = list(map(lambda x: Notes[x%12],[idx + p for p in Major_Pattern]))

        if set(Chord) == set(Minor):
            return f"{rootnote} Minor"

        elif set(Chord) == set(Major):
            return f"{rootnote} Major"

    return "Not valid chord"



st = time.process_time()
print(Harmonics_TH(Chord))
et = time.process_time()
print(f"Running Time: {et-st}")