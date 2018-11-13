
import numpy as np


def move_up(self):
    self.current_coordinate = tuple(np.array(self.current_coordinate) + np.array([0, 1]))
    # print('up')
    self.path_log.append(self.current_coordinate)


def move_down(self):
    self.current_coordinate = tuple(np.array(self.current_coordinate) + np.array([0, -1]))
    # print('down')
    self.path_log.append(self.current_coordinate)


def move_left(self):
    self.current_coordinate = tuple(np.array(self.current_coordinate) + np.array([-1, 0]))
    # print('left')
    self.path_log.append(self.current_coordinate)


def move_right(self):
    self.current_coordinate = tuple(np.array(self.current_coordinate) + np.array([1, 0]))
    # print('right')
    self.path_log.append(self.current_coordinate)


def u_turn_toward_right(self):
    rollback = False
    while True:
        if (self.judge_up_passable() is False) \
                and (self.judge_down_passable() is False) \
                and (self.judge_right_passable() is True):
            self.move_right()

        if rollback is False:
            while self.judge_up_passable() is True and self.judge_up_passed() is False:
                self.move_up()
            if self.judge_right_passable() is True and self.judge_right_passed() is False:
                self.move_right()
                rollback = True
            else:
                rollback = True

        if rollback is True:
            while self.judge_down_passable() is True and self.judge_down_passed() is False:
                self.move_down()
            if self.judge_right_passable() is True and self.judge_right_passed() is False:
                self.move_right()
                rollback = False
            else:
                rollback = False
                break


def u_turn_toward_left(self):
    rollback = False
    while True:
        if (self.judge_up_passable() is False) \
                and (self.judge_down_passable() is False) \
                and (self.judge_left_passable() is True):
            self.move_left()

        if rollback is False:
            while self.judge_up_passable() is True and self.judge_up_passed() is False:
                self.move_up()
            if self.judge_left_passable() is True and self.judge_left_passed() is False:
                self.move_left()
                rollback = True
            else:
                rollback = True

        if rollback is True:
            while self.judge_down_passable() is True and self.judge_down_passed() is False:
                self.move_down()
            if self.judge_left_passable() is True and self.judge_left_passed() is False:
                self.move_left()
                rollback = False
            else:
                rollback = False
                break
