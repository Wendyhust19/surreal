import sys
from surreal.agent.ddpg_agent import DDPGAgent
from surreal.env import *
from surreal.main.ddpg.configs import *
from surreal.main.basic_boilerplate import run_agent_main


env = gym.make('HalfCheetah-v1')
env._max_episode_steps = 100
env = GymAdapter(env)

run_agent_main(
    agent_class=DDPGAgent,
    env=env,
    learn_config=learn_config,
    env_config=env_config,
    session_config=session_config,
    fetch_parameter_mode='episode',
)

