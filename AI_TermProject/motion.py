
import numpy as np
import random


def move_up(self):
    self.current_coordinate = tuple(np.array(self.current_coordinate) + np.array([0, 1]))
    self.path_log.append(self.current_coordinate)


def move_down(self):
    self.current_coordinate = tuple(np.array(self.current_coordinate) + np.array([0, -1]))
    self.path_log.append(self.current_coordinate)


def move_left(self):
    self.current_coordinate = tuple(np.array(self.current_coordinate) + np.array([-1, 0]))
    self.path_log.append(self.current_coordinate)


def move_right(self):
    self.current_coordinate = tuple(np.array(self.current_coordinate) + np.array([1, 0]))
    self.path_log.append(self.current_coordinate)


def u_turn(self):
    if random.randint(1, 2) == 1:
        if self.judge_up_passable() is True or self.judge_right_passable() is True or self.judge_down_passable():
            self.u_turn_toward_right()
        elif self.judge_up_passable() is True or self.judge_left_passable() is True or self.judge_down_passable():
            self.u_turn_toward_left()
    else:
        if self.judge_up_passable() is True or self.judge_left_passable() is True or self.judge_down_passable():
            self.u_turn_toward_left()
        elif self.judge_up_passable() is True or self.judge_right_passable() is True or self.judge_down_passable():
            self.u_turn_toward_right()


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

        if rollback is True:
            while self.judge_down_passable() is True and self.judge_down_passed() is False:
                self.move_down()
            if self.judge_left_passable() is True and self.judge_left_passed() is False:
                self.move_left()
                rollback = False
            else:
                rollback = False
                break


def doClean(self, x, y):
    self.dirtyData[x][y]['b'] = self.dirtyData[x][y]['b'] - 1
