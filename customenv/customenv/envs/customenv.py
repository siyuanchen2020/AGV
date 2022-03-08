import gym
from gym import Env
from gym.spaces import Discrete, Box
import numpy
import os
import gym
from stable_baselines3 import DQN
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common import results_plotter
from stable_baselines3.common.results_plotter import load_results, ts2xy
from stable_baselines3.common.evaluation import evaluate_policy
import matplotlib.pyplot as plt
from stable_baselines3.common.callbacks import BaseCallback

#author: Siyuan Chen
#This code is aimed to create a custom gym environment for Facts Analyzer XML model.



def custom_input(action):
    input_file = []
    input_var = []
    for n in action:
        input_var = [n,1,1,1,1,1,1]
        input_file.append(input_var)
    return input_file

#action = range(1,4)
#input_file = custom_input(action)
#print(input_file)


class customenv(Env):
    def __init__(self):
        # Actions we can take, down, stay, up
        self.action_space = Discrete(3)
        # Temperature array
        self.observation_space = Discrete(2)

    def step(self, action):
        # set the input file
        input_file = custom_input(action)
        # write in the decision variables
        for decision_var in input_file:
            input_var = numpy.array(decision_var)
            numpy.savetxt('input.txt', input_var)
        # execute the runner
        os.system("xsim-runner.exe --model LawMcComasMOPs.xml --input input.txt --output_txt output_Law.txt")
        # write in the output
        with open('output_Law.txt') as my_file:
            # Throughput, Work-In-Process, Parts-Produced, and Lead-Time
            output_array = my_file.readlines()
        # get the throughput
        throughput = float(output_array[0])
        # state?
        state = 1
        # calculate profit as reward
        reward = (200 * throughput * 720) - 25000 * (input[0] + 1 + 1 + 1) - 1000 * (
                    1 + 1 + 1)
        done = True
        info = {}

        # Return step information
        return state, reward, done, info

    def render(self):
        pass

    def reset(self):
        state = 0
        return state

    def close(self):
        pass


env = customenv()

action = range(1,4)

log_dir = "/tmp/gym/"
#os.makedirs(log_dir, exist_ok=True)

'''
if not os.path.exists(models_dir):
    os.makedirs(models_dir)
'''

if not os.path.exists(log_dir):
    os.makedirs(log_dir)


env = Monitor(env, log_dir)

model = DQN("MlpPolicy", env, verbose=1)
#model.learn(total_timesteps=100000, log_interval=4)

'''
episodes = 10
for episode in range(1, episodes + 1):
    state = env.reset()
    done = False
    score = 0

    while not done:
        # env.render()
        action = env.action_space.sample()
        n_state, reward, done, info = env.step(action)
        score += reward
    print('Episode:{} Score:{}'.format(episode, score))

'''
