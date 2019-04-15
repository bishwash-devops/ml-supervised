import gym
from gym.envs.registration import register

from .taxi import *
from .mazeworld import *
from .windy_cliff_walking import *
from .frozen_lake import *

__all__ = ['RewardingFrozenLakeEnv']


register(
    id='FrozenLake4x4-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '4x4'},
)

register(
    id='FrozenLakeNoRewards4x4-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '4x4', 'rewarding': False},
)

register(
    id='FrozenLakeNoSlip4x4-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '4x4', 'is_slippery': False},
)

register(
    id='FrozenLake15x15-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '15x15'}
)

register(
    id='FrozenLakeNoRewards15x15-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '15x15', 'rewarding': False}
)

register(
    id='FrozenLakeNoSlip15x15-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '15x15', 'is_slippery': False}
)


def get_small_frozen_lake_environment():
    return gym.make('FrozenLake4x4-v0')


def get_large_frozen_lake_environment():
    return gym.make('FrozenLake15x15-v0')


def get_small_no_slip_frozen_lake_environment():
    return gym.make('FrozenLakeNoSlip4x4-v0')


def get_large_no_slip_frozen_lake_environment():
    return gym.make('FrozenLakeNoSlip15x15-v0')


def get_small_no_reward_frozen_lake_environment():
    return gym.make('FrozenLakeNoRewards4x4-v0')


def get_large_no_reward_frozen_lake_environment():
    return gym.make('FrozenLakeNoRewards15x15-v0')

