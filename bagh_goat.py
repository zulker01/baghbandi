# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 11:04:02 2022

@author: User
"""

from tkinter import *
import math


class baghClass():
    possible_moves = {
        0: [1, 5, 6], 1: [2, 0, 6], 2: [3, 1, 7, 6, 8], 3: [4, 2, 8], 4: [3, 9, 8],
        5: [6, 10, 0], 6: [7, 5, 11, 1, 10, 2, 12, 0], 7: [8, 6, 12, 2], 8: [9, 7, 13, 3, 12, 4, 14, 2], 9: [8, 14, 4],
        10: [11, 15, 5, 6, 16], 11: [12, 10, 16, 6], 12: [13, 11, 17, 7, 16, 8, 18, 6], 13: [14, 12, 18, 8],
        14: [13, 19, 9, 18, 8],
        15: [16, 20, 10], 16: [17, 15, 21, 11, 20, 12, 22, 10], 17: [18, 16, 22, 12],
        18: [19, 17, 23, 13, 22, 14, 24, 12], 19: [18, 24, 14],
        20: [21, 15, 16], 21: [22, 20, 16], 22: [23, 21, 17, 18, 16], 23: [24, 22, 18], 24: [23, 19, 18]
    }
    possible_capture_moves = {
        0: [2, 10, 12], 1: [3, 11], 2: [4, 0, 12, 10, 14], 3: [1, 13], 4: [2, 14, 12],
        5: [7, 15], 6: [8, 16, 18], 7: [9, 5, 17], 8: [6, 18, 16], 9: [7, 19],
        10: [12, 20, 0, 2, 22], 11: [13, 21, 1], 12: [14, 10, 22, 2, 20, 4, 24, 0],
        13: [11, 23, 3], 14: [12, 24, 4, 22, 2],
        15: [17, 5], 16: [18, 6, 8], 17: [19, 15, 7], 18: [16, 8, 6], 19: [17, 9],
        20: [22, 10, 12], 21: [23, 11], 22: [24, 20, 12, 14, 10], 23: [21, 13], 24: [22, 14, 12]
    }

    # baghphoto  = PhotoImage(file="bagh.png")
    def __init__(self, x, y, canvas, baghPhoto):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.baghPhoto = baghPhoto

        self.draw_bagh()

    def draw_bagh(self):
        self.baghImg = self.canvas.create_image(self.x, self.y, image=self.baghPhoto)  # bagh image created

    def is_valid_move(self, from_position, to_x, to_y):
        # check weather a move is valid against current state

        for i in self.possible_moves[from_position]:  # gives adjacent nodes against current position
            cur_x, cur_y = coordinate_index_map[i]
            pos = get_index((cur_x, cur_y))
            if (cur_x - to_x) ** 2 + (cur_y - to_y) ** 2 < 16:
                return True, pos
        else:
            return False, -1

    def possible_move_list(self, from_position):
        return self.possible_moves[from_position]


class goatClass():
    # baghphoto  = PhotoImage(file="bagh.png")
    def __init__(self, x, y, canvas, goatPhoto):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.goatPhoto = goatPhoto

        self.draw_goat()

    def draw_goat(self):
        self.goat = self.canvas.create_image(self.x, self.y, image=self.goatPhoto)  # bagh image created


coordinate_index_map = dict()
x_pos = [80, 180, 280, 380, 480]
y_pos = [80, 180, 280, 380, 480]


def coordinate_mapping():
    k = 0
    for j in range(len(y_pos)):
        for i in range(len(x_pos)):
            coordinate_index_map[k] = (x_pos[i], y_pos[j])
            k += 1

    print(coordinate_index_map)


def get_index(coordinate):
    key_list = list(coordinate_index_map.keys())
    val_list = list(coordinate_index_map.values())
    position = val_list.index(coordinate)
    key_dictionary = key_list[position]
    return key_dictionary  # key of value


coordinate_mapping()
