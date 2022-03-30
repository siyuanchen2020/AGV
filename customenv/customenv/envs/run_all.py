from stable_baselines3 import dqn
import numpy
import gym
import matplotlib.pyplot as plt
import os
import pandas as pd
# author: Siyuan Chen


'''
runner = "xsim-runner.exe"
model = "LawMcComasMOPs.xml"
input = "input.txt"
output = "output_Law.txt"
'''

i = 0
dic = {}

for a in range(1, 4):
    for b in range(1, 4):
        for c in range(1, 4):
            for d in range(1, 4):
                for e in range(1, 11):
                    for f in range(1, 11):
                        for g in range(1, 11):
                            i += 1
                            dic[i] = numpy.array([a, b, c, d, e, f, g])

# a simple test
'''
for a in range(1, 4):
    for b in range(1, 4):
        for c in range(1, 4):
            i += 1
            dic[i] = numpy.array([a, b, c, 1, 1, 1, 1])
'''


profit_list = []
input = []
#function for changing the input variable
for action in range(1,81001):
    input_var = dic[action]
    #input_var = numpy.array([a, b, c, d, e, f, g])
    #input = input_var.tolist()
    #print(input_var[0])

    numpy.savetxt('input.txt', input_var)

    os.system("xsim-runner.exe --model LawMcComasMOPs.xml --input input.txt --output_txt output_Law4.txt")

    #xsim-runner.exe --model LawMcComasMOPs.xml --input input.txt --output_txt output_Law.txt

    # check the output array
    with open('output_Law4.txt') as my_file:
        # Throughput, Work-In-Process, Parts-Produced, and Lead-Time
        output_array = my_file.readlines()

    parts_produced = float(output_array[2])
    #print(parts_produced)
    #print(output_array)

    #calculate the maximum profit
    profit = (200 * parts_produced) - 25000 * (input_var[0]+input_var[1]+input_var[2]+input_var[3]) - 1000 * (input_var[4]+input_var[5]+input_var[6])
    #print(profit)
    input.append(input_var)
    profit_list.append(profit)
    print(action)

#print(input)
#print(profit_list)

dataframe = pd.DataFrame({'input_variable':input,'profit':profit_list})
dataframe.to_csv("test.csv",index=False,sep=',')