#!/usr/bin python  
# -*- coding=utf-8 -*-
"""
    just study demo
    @version: v1.0 
    @author: xsh
    @license: open
    @contact: xshqhua@foxmail.com
    @software: PyCharm
    @file: gym_01_pong_v0.py
    @time: 2019/12/22 20:48
"""
import time
import gym

env = gym.make('Pong-v4')

for i_episode in range(100):
    env.reset()
    for t in range(100):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        time.sleep(0.1)
        if done:
            print("Episode finished after {} timesteps".format(t + 1))
            break
