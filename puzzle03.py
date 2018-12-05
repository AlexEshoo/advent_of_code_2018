import re

def place_square(x, y, l, h):
	print(x,y,l,h)

result = re.findall(r"#\d+ @ (\d+),(\d)+: (\d+)x(\d+)", "#1 @ 1,3: 4x4\n#2 @ 2,4: 10x321")

for r in result:
	place_square(*r)
