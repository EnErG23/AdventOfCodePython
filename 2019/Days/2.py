file = open("Inputs/2.txt", "r")
lines = file.readlines()


def intcode(inputs, pointer, noun, verb):
    inputs[1] = noun
    inputs[2] = verb

    for i in range(0,len(inputs) - 1, pointer):
        if inputs[i] == 1:
            inputs[inputs[i + 3]] = inputs[inputs[i + 1]] + inputs[inputs[i + 2]]
        elif inputs[i] == 2:
            inputs[inputs[i + 3]] = inputs[inputs[i + 1]] * inputs[inputs[i + 2]]
        elif inputs[i] == 99:
            break

    return inputs[0]


def intcodewithoutput(program, output):
    for i in range(len(program) - 1):
        for j in range(len(program) - 1):
            program = [int(i) for i in lines[0].split(',')]
            if intcode(program, 4, i, j) == output:
                return 100 * i + j


program = [int(i) for i in lines[0].split(',')]

print(intcode(program, 4, 12, 2))
print(intcodewithoutput(program, 19690720))