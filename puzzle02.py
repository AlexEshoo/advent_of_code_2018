from collections import Counter

with open("inputs/p02_input.txt") as f:
    box_ids = [b_id.strip() for b_id in f]

three_letter_occurances = 0
two_letter_occurances = 0

for box_id in box_ids:
    top_two = list(dict(Counter(box_id).most_common(2)).values())
    if 2 in top_two:
        two_letter_occurances += 1

    if 3 in top_two:
        three_letter_occurances += 1

print("Checksum: ", three_letter_occurances * two_letter_occurances)


def positional_difference(a, b):
    diffs = {}
    for i in range(len(a)):
        if a[i] != b[i]:
            diffs[i] = (a[i], b[i])

    return diffs


for i, base_id in enumerate(box_ids):
    for b_id in box_ids[i+1:]:
        diff = positional_difference(base_id, b_id)
        if len(diff) == 1:
            ind = list(diff.keys())[0]
            print("shared letters: ", base_id[:ind] + base_id[ind+1:])