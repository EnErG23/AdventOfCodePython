import os

path = '../Inputs/3.txt'
with open(os.path.join(os.path.dirname(__file__), path), 'r') as input_file:
    lines = input_file.readlines()

# Part 1
allcoords = []

for wire in lines:
    coords = [(0, 0)]

    straights = wire.split(',')
    i = 0

    for straight in straights:
        direction = straight[0]
        value = int(straight[1:])

        for v in range(value):
            if direction == "R":
                coords.append((coords[i][0] + 1, coords[i][1]))
            elif direction == "D":
                coords.append((coords[i][0], coords[i][1] - 1))
            elif direction == "L":
                coords.append((coords[i][0] - 1, coords[i][1]))
            else:
                coords.append((coords[i][0], coords[i][1] + 1))

            i += 1

    allcoords.append(coords[1:])

similarcoords = list(set(allcoords[0]) & set(allcoords[1]))

distances = []

for coord in similarcoords:
    distances.append(abs(coord[0]) + abs(coord[1]))

distances.sort()

print(distances[0])

# Part 2
allcoords = []

for wire in lines:
    coords = [(0, 0)]

    straights = wire.split(',')
    i = 0

    for straight in straights:
        direction = straight[0]
        value = int(straight[1:])

        for v in range(value):
            if direction == "R":
                coords.append((coords[i][0] + 1, coords[i][1]))
            elif direction == "D":
                coords.append((coords[i][0], coords[i][1] - 1))
            elif direction == "L":
                coords.append((coords[i][0] - 1, coords[i][1]))
            else:
                coords.append((coords[i][0], coords[i][1] + 1))

            i += 1

    allcoords.append(coords[1:])

similarcoords = list(set(allcoords[0]) & set(allcoords[1]))

steps = []

for coord in similarcoords:
    steps.append(allcoords[0].index(coord) + allcoords[1].index(coord))

steps.sort()

print(steps[0]+2)