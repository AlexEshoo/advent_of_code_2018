import re

def get_square_set(c_id, x, y, w, h):
	area = []

	for i in range(w):
		for j in range(h):
			area.append((x + i, y + j))

	return c_id, set(area)


with open("inputs/p03_input.txt") as f:
	result = re.findall(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", f.read())

sets = [get_square_set(*(int(i) for i in r)) for r in result]
overlap = set()
unique_plots = {s[0]: s[1] for s in sets}

for i, s in enumerate(sets):
	count = 0
	the_set = s[1]
	the_id = s[0]
	for s2 in sets[i+1:]:
		common = the_set.intersection(s2[1])
		if len(common) > 0:
			unique_plots.pop(the_id, None)
			unique_plots.pop(s2[0], None)
		overlap.update(common)

print("Total Shared Area: ", len(overlap))
print("The only unique claim is: ", list(unique_plots.keys())[0])