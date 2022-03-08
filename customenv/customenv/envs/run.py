from stable_baselines3 import dqn
import numpy
import gym
import matplotlib.pyplot as plt
import os
# author: Siyuan Chen


'''
runner = "xsim-runner.exe"
model = "LawMcComasMOPs.xml"
input = "input.txt"
output = "output_Law.txt"
'''

#function for changing the input variable
input_var = numpy.array([2, 3, 2, 3, 7, 7, 3])
input = input_var.tolist()
#print(input_var[0])

numpy.savetxt('input.txt', input_var)

os.system("xsim-runner.exe --model LawMcComasMOPs.xml --input input.txt --output_txt output_Law3.txt")

#xsim-runner.exe --model LawMcComasMOPs.xml --input input.txt --output_txt output_Law.txt

# check the output array
with open('output_Law3.txt') as my_file:
    # Throughput, Work-In-Process, Parts-Produced, and Lead-Time
    output_array = my_file.readlines()

throughput = float(output_array[0])
print(throughput)
print(output_array)

#calculate the maximum profit
profit = (200 * throughput * 720) - 25000 * (input[0]+input[1]+input[2]+input[3]) - 1000 * (input[4]+input[5]+input[6])
print(profit)
