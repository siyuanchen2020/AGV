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
input_var = numpy.array([2, 3, 2, 2, 6, 7, 3])
numpy.savetxt('input.txt', input_var)

os.system("xsim-runner.exe --model LawMcComasMOPs.xml --input input.txt --output_txt output_Law2.txt")

#xsim-runner.exe --model LawMcComasMOPs.xml --input input.txt --output_txt output_Law.txt

# check the output array
with open('output_Law2.txt') as my_file:
    # Throughput, Work-In-Process, Parts-Produced, and Lead-Time
    output_array = my_file.readlines()

print(output_array)