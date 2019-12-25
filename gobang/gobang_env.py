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

from gobang.piece_color import PieceColor


class Gobang_Env(gym.Env):
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 2
    }

    def __init__(self):
        self.screen_width = 1000
        self.pieces = []

        self.screen_height = self.screen_width
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

        if self.viewer is None:
            self.viewer = rendering.Viewer(self.screen_width, self.screen_height)

            # 创建背景颜色,rendering.FilledPolygon为填充一个矩形
            self._init_background_color()
            self._init_background_lines()

        else:
            for piece in self.pieces:
                self.viewer.add_geom(piece)

        return self.viewer.render(return_rgb_array=mode == 'rgb_array')

    def _init_background_lines(self):
        screen_height = self.screen_height
        screen_width = self.screen_width
        margin_size = self.margin_size
        row_max_high = screen_height - margin_size
        for i in range(1, screen_width // self.margin_size + 1):
            self.viewer.add_geom(rendering.Line((margin_size * i, margin_size),
                                                (margin_size * i, row_max_high)))
            self.viewer.add_geom(rendering.Line((margin_size, margin_size * i),
                                                (screen_width - margin_size, margin_size * i)))

    def _init_background_color(self):
        screen_height = self.screen_height
        screen_width = self.screen_width
        background_color = rendering.FilledPolygon(
            [(0, 0), (screen_width, 0), (screen_width, screen_height), (0, screen_height)])
        background_color.set_color(0.8, 0.6, 0.4)
        self.viewer.add_geom(background_color)

    def add_piece(self, pos_xy, piece_color=PieceColor.BLACK):
        piece = rendering.make_circle(self.margin_size / 3)
        piece.add_attr(rendering.Transform(translation=self._convert_2_location(pos_xy)))
        piece.set_color(*piece_color.value)
        self.pieces.append(piece)

    def add_black_piece(self, pos_xy):
        self.add_piece(pos_xy, piece_color=PieceColor.BLACK)

    def add_white_piece(self, pos_xy):
        self.add_piece(pos_xy, piece_color=PieceColor.WHITE)

    def _convert_2_location(self, pos_xy):
        return tuple([(i + 1) * self.margin_size for i in pos_xy])

    def num_convert_2_pos_xy(self, num):
        row_num = self.screen_width // self.margin_size - 1
        return num // row_num, num % row_num

    def close(self):
        if self.viewer:
            self.viewer.close()


if __name__ == '__main__':
    env = Gobang_Env()
    env.reset()
    env.render()
    i = 0
    num = env.screen_width // env.margin_size
    while i < 20:
        p1 = random.randint(0, ((env.screen_width // env.margin_size) - 1) ** 2)
        p2 = env.num_convert_2_pos_xy(p1)
        print(p1, p2)
        time.sleep(0.5)
        i += 1
        if i % 2 == 0:
            env.add_black_piece(p2)
        else:
            env.add_white_piece(p2)

        env.render()
    time.sleep(20)
    pass
