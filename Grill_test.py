import os
from statistics import mean
os.system("cls")

print("Grill 1:")
num = [int(line) for line in open('Grill_1.txt', 'r')]
min_num, max_num, mean_num = min(num), max(num), mean(num)
print("Min: ", min_num)
print("Max: ", max_num)
print("Mean:", mean_num)
print("Standard Deviation of temps is: ", mean_num-min_num)