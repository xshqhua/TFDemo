#!/usr/bin python  
# -*- coding=utf-8 -*-
"""
    just study demo
    @version: v1.0 
    @author: xsh
    @license: open
    @contact: xshqhua@foxmail.com
    @software: PyCharm
    @file: gobang_env.py
    @time: 2019/12/22 22:12
"""
import random
import time

import gym


class Gobang_Env(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 2
    }

    def __init__(self):

        self.states = range(1, 17)  # 状态空间

        self.x = [150, 250, 350, 450] * 4
        self.y = [450] * 4 + [350] * 4 + [250] * 40 + [150] * 4

        self.terminate_states = dict()  # 终止状态为字典格式
        self.terminate_states[11] = 1
        self.terminate_states[12] = 1
        self.terminate_states[15] = 1

        self.actions = ['n', 'e', 's', 'w']

        self.rewards = dict();  # 回报的数据结构为字典
        self.rewards['8_s'] = -1.0
        self.rewards['13_w'] = -1.0
        self.rewards['7_s'] = -1.0
        self.rewards['10_e'] = -1.0
        self.rewards['14_4'] = 1.0

        self.t = dict();  # 状态转移的数据格式为字典
        self.t['1_s'] = 5
        self.t['1_e'] = 2
        self.t['2_w'] = 1
        self.t['2_e'] = 3
        self.t['3_s'] = 6
        self.t['3_w'] = 2
        self.t['3_e'] = 4
        self.t['4_w'] = 3
        self.t['4_s'] = 7
        self.t['5_s'] = 8
        self.t['6_n'] = 3
        self.t['6_s'] = 10
        self.t['6_e'] = 7
        self.t['7_w'] = 6
        self.t['7_n'] = 4
        self.t['7_s'] = 11
        self.t['8_n'] = 5
        self.t['8_e'] = 9
        self.t['8_s'] = 12
        self.t['9_w'] = 8
        self.t['9_e'] = 10
        self.t['9_s'] = 13
        self.t['10_w'] = 9
        self.t['10_n'] = 6
        self.t['10_e'] = 11
        self.t['10_s'] = 14
        self.t['10_w'] = 9
        self.t['13_n'] = 9
        self.t['13_e'] = 14
        self.t['13_w'] = 12
        self.t['14_n'] = 10
        self.t['14_e'] = 15
        self.t['14_w'] = 13

        self.gamma = 0.8  # 折扣因子
        self.viewer = None
        self.state = None

    def _seed(self, seed=None):
        self.np_random, seed = random.seeding.np_random(seed)
        return [seed]

    def getTerminal(self):
        return self.terminate_states

    def getGamma(self):
        return self.gamma

    def getStates(self):
        return self.states

    def getAction(self):
        return self.actions

    def getTerminate_states(self):
        return self.terminate_states

    def setAction(self, s):
        self.state = s

    def step(self, action):
        # 系统当前状态
        state = self.state
        if state in self.terminate_states:
            return state, 0, True, {}
        key = "%d_%s" % (state, action)  # 将状态和动作组成字典的键值

        # 状态转移
        if key in self.t:
            next_state = self.t[key]
        else:
            next_state = state
        self.state = next_state

        is_terminal = False

        if next_state in self.terminate_states:
            is_terminal = True

        if key not in self.rewards:
            r = 0.0
        else:
            r = self.rewards[key]

        return next_state, r, is_terminal, {}

    def reset(self):
        self.state = self.states[int(random.random() * len(self.states))]
        return self.state

    def render(self, mode='human'):
        from gym.envs.classic_control import rendering
        row_nums = 20
        margin_size = 50
        screen_width = 800
        screen_height = 800

        if self.viewer is None:
            self.viewer = rendering.Viewer(screen_width, screen_height)

            # 创建cart矩形,rendering.FilledPolygon为填充一个矩形
            background_color = rendering.FilledPolygon(
                [(0, 0), (screen_width, 0), (screen_width, screen_height), (0, screen_height)])
            # Transform给cart添加平移属性和旋转属性
            self.carttrans = rendering.Transform()
            background_color.add_attr(self.carttrans)
            background_color.set_color(0.8, 0.6, 0.4)

            # 在图上加入几何cart
            self.viewer.add_geom(background_color)

            self.row_lines = []
            self.column_lines = []
            row_max_high = screen_height - margin_size
            for i in range(1, row_nums + 1):
                self.row_lines.append(rendering.Line((margin_size * i, margin_size),
                                                     (margin_size * i, row_max_high)))
                self.column_lines.append(rendering.Line((margin_size, margin_size * i),
                                                        (screen_width - margin_size, margin_size * i)))

            # 创建网格世界
            self.line1 = rendering.Line((margin_size, margin_size),
                                        (screen_width - margin_size, margin_size))
            self.line2 = rendering.Line((margin_size, margin_size * 2),
                                        (screen_width - margin_size, margin_size * 2))

            self.piece = rendering.make_circle(margin_size / 3)
            self.circletrans = rendering.Transform(translation=(250, 350))
            self.piece.add_attr(self.circletrans)
            self.piece.set_color(0, 0, 0)

            for i in range(len(self.row_lines)):
                self.viewer.add_geom(self.row_lines[i])
                self.viewer.add_geom(self.column_lines[i])
            self.viewer.add_geom(self.piece)
            self.viewer.add_geom(self.piece)

        return self.viewer.render(return_rgb_array=mode == 'human')

    def close(self):
        if self.viewer:
            self.viewer.close()


if __name__ == '__main__':
    env = Gobang_Env()
    env.reset()
    env.render()
    time.sleep(10)
    # env.render()
    # env.close()
    pass
