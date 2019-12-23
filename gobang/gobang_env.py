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
from gym.envs.classic_control import rendering


class Gobang_Env(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 2
    }

    def __init__(self):
        self.pieces = []

        self.terminate_states = dict()  # 终止状态为字典格式
        self.margin_size = 50
        self.gamma = 0.8  # 折扣因子
        self.viewer = None
        self.state = None

    def _seed(self, seed=None):
        self.np_random, seed = random.seeding.np_random(seed)
        return [seed]

    def step(self, action):
        pass

    def reset(self):
        pass

    def render(self, mode='human'):

        row_nums = 20
        margin_size = self.margin_size
        screen_width = 800
        screen_height = 800

        if self.viewer is None:
            self.viewer = rendering.Viewer(screen_width, screen_height)

            # 创建cart矩形,rendering.FilledPolygon为填充一个矩形
            background_color = rendering.FilledPolygon(
                [(0, 0), (screen_width, 0), (screen_width, screen_height), (0, screen_height)])
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

            for i in range(len(self.row_lines)):
                self.viewer.add_geom(self.row_lines[i])
                self.viewer.add_geom(self.column_lines[i])
        else:
            for piece in self.pieces:
                self.viewer.add_geom(piece)

        return self.viewer.render(return_rgb_array=mode == 'human')

    def add_piece(self, pos_xy):
        piece = rendering.make_circle(self.margin_size / 3)
        piece.add_attr(rendering.Transform(translation=self._convert_2_location(pos_xy)))
        piece.set_color(0, 0, 0)
        self.pieces.append(piece)

    def _convert_2_location(self, pos_xy):
        return tuple([(i + 1) * self.margin_size for i in pos_xy])

    def close(self):
        if self.viewer:
            self.viewer.close()


if __name__ == '__main__':
    env = Gobang_Env()
    env.reset()
    env.render()
    time.sleep(2)
    env.add_piece((1, 5))
    env.render()
    time.sleep(2)
    env.add_piece((4, 5))
    env.render()
    time.sleep(2)
    env.add_piece((3, 4))
    env.render()
    time.sleep(10)
    # env.render()
    # env.close()
    pass
