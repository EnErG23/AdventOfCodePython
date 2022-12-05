file = '../Inputs/1.txt'
#file = '../Inputs/1-test.txt'

Input = [l.strip() for l in open(file)]

elves = (';'.join(Input)).split(';;')

ElfCalories = []

for elf in elves:
    elfCalories = 0
    for snackCalories in elf.split(';'):
        elfCalories += int(snackCalories)
    ElfCalories.append(elfCalories)

ElfCalories = sorted(ElfCalories)

print(ElfCalories[-1])
print(ElfCalories[-1]+ElfCalories[-2]+ElfCalories[-3])