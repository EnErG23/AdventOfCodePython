file = open("Inputs/3-1.txt", "r")
lines = file.readlines()

coords = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

r = 31

totaltrees = 1

for coord in coords:
    trees = 0

    c = coord[0]
    skip = False

    for line in lines[coord[1]:]:
        if skip:
            skip = False
            continue
        if line[c] == "#":
            trees += 1
        c += coord[0]
        if c > r-1:
            c -= r
        if coord[1] > 1:
            skip = True

    totaltrees = totaltrees * trees

print(totaltrees)