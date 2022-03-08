from gym.envs.registration import register

register(
    id='customenv',
    entry_point='customenv.envs:customenv',
)

"""
register(
    id='basic-v2',
    entry_point='gym_basic.envs:BasicEnv2',
)
"""