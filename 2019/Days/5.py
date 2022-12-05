file = open("Inputs/5.txt", "r")
lines = file.readlines()


# def intcode(inputs, pointer, noun, verb, input):
#     inputs[1] = noun
#     inputs[2] = verb
def intcode(inputs, pointer, input):
    for i in range(0, len(inputs) - 1, 2):
        if inputs[i] == 3:
            inputs[inputs[i + 1]] = input

    skip = pointer
    for i in range(0, len(inputs) - 1, skip):
        if inputs[i] == 1:
            inputs[inputs[i + 3]] = inputs[inputs[i + 1]] + inputs[inputs[i + 2]]
            skip = 4
        elif inputs[i] == 2:
            inputs[inputs[i + 3]] = inputs[inputs[i + 1]] * inputs[inputs[i + 2]]
            skip = 4
        elif inputs[i] == 4:
            print(inputs[inputs[i + 1]])
        elif inputs[i] == 99:
            return inputs[0]


def intcodewithoutput(program, output):
    for i in range(len(program) - 1):
        for j in range(len(program) - 1):
            program = [int(i) for i in lines[0].split(',')]
            if intcode(program, 4, i, j) == output:
                return 100 * i + j


program = [int(i) for i in lines[0].split(',')]

print(intcode(program, 4, 1))
# print(intcodewithoutput(program, 19690720))