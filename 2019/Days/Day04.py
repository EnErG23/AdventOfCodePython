import os

path = '../Inputs/4.txt'
with open(os.path.join(os.path.dirname(__file__), path), 'r') as input_file:
    lines = input_file.readlines()

# Part 1

a = int(lines[0].split('-')[0])
b = int(lines[0].split('-')[1])
req2 = [a, b]

i = req2[0]

result1 = 0
result2 = 0

while i < req2[1] + 1:
    asStr = str(i)

    req3 = False
    req4 = True
    req5 = False

    for j in range(1, len(asStr)):
        if asStr[j - 1] > asStr[j]:
            req4 = False
            break

    if req4:
        for j in range(0, len(asStr)-1):
            if asStr.count(asStr[j]) >= 2:
                req3 = True
                if asStr.count(asStr[j]) == 2:
                    req5 = True
        if req3:
            result1 += 1
        if req5:
            result2 += 1

    i += 1

print(result1)
# not 615
# not 750
print(result2)
