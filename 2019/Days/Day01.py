import os
import math

path = '../Inputs/1.txt'
with open(os.path.join(os.path.dirname(__file__), path), 'r') as input_file:
    lines = input_file.readlines()
int_list = [int(l) for l in lines]

total_fuel1 = 0
total_fuel2 = 0

for i in int_list:
    total_fuel1 += math.floor(i/3)-2
    fuel = i
    while True:
        fuel = math.floor(fuel / 3) - 2
        if fuel < 1:
            break
        total_fuel2 += fuel

print(total_fuel1)
print(total_fuel2)
