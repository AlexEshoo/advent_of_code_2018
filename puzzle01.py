from itertools import cycle

input_file = "inputs/p01_input.txt"

shifts = []
with open(input_file) as f:
    for line in f:
        if line[0] == '-':
            shifts.append(-1 * int(line[1:]))
        else:
            shifts.append(int(line[1:]))

print("Final frequency: ", sum(shifts))

f = 0
unique_f = set()
shift_gen = cycle(shifts)
while not f in unique_f:
    unique_f.add(f)
    f += next(shift_gen)

print("First Repeated Frequency: ", f)