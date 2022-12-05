import os

path = '../Inputs/5.txt'
with open(os.path.join(os.path.dirname(__file__), path), 'r') as input_file:
    lines = input_file.readlines()
int_list = [int(l) for l in lines[0].split(',')]


def intcode(list, opcode):
    if opcode == 1:
        int_list[int_list[i + 3]] = int_list[int_list[i + 1]] + int_list[int_list[i + 2]]
    elif opcode == 2:
        int_list[int_list[i + 3]] = int_list[int_list[i + 1]] * int_list[int_list[i + 2]]


# Part1
s = 4

int_list[1] = 12
int_list[2] = 2

for i in range(0, len(int_list)-1, s):
    if int_list[i] == 99:
        break
    intcode(int_list, i)


print(int_list[0])

# Part2
output = 19690720
a = 0
b = 0

for g in range(len(int_list)-1):
    for h in range(len(int_list)-1):
        int_list = [int(l) for l in lines[0].split(',')]
        int_list[1] = g
        int_list[2] = h
        for i in range(0, len(int_list)-1, s):
            if int_list[i] == 1:
                int_list[int_list[i + 3]] = int_list[int_list[i + 1]] + int_list[int_list[i + 2]]
            elif int_list[i] == 2:
                int_list[int_list[i + 3]] = int_list[int_list[i + 1]] * int_list[int_list[i + 2]]
            elif int_list[i] == 99:
                break
        if int_list[0] == output:
            a = g
            b = h
            break
    if int_list[0] == output:
        break

print(100 * a + b)
