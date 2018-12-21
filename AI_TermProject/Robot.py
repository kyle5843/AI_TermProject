from sensor import *
from motion import *
from aStar import *


class Robot(object):
    def __init__(self) -> object:
        from map_test import coordinate_list, impassable_coordinate_list, coordinate_data
        self.coordinate_data = coordinate_data
        self.coordinate_list = coordinate_list
        self.impassable_coordinate_list = impassable_coordinate_list
        self.start_coordinate = (27, 24)
        self.current_coordinate = self.start_coordinate
        self.path_log = []
        self.path_log.append(self.start_coordinate)

        # motion
        Robot.move_up = move_up
        Robot.move_down = move_down
        Robot.move_left = move_left
        Robot.move_right = move_right
        Robot.u_turn = u_turn
        Robot.u_turn_toward_right = u_turn_toward_right
        Robot.u_turn_toward_left = u_turn_toward_left
        #
        # sensor
        Robot.judge_up_passable = judge_up_passable
        Robot.judge_down_passable = judge_down_passable
        Robot.judge_left_passable = judge_left_passable
        Robot.judge_right_passable = judge_right_passable
        Robot.judge_up_passed = judge_up_passed
        Robot.judge_down_passed = judge_down_passed
        Robot.judge_left_passed = judge_left_passed
        Robot.judge_right_passed = judge_right_passed
        #
        # A*
        Robot.get_uncleaned_coordinate_list = get_uncleaned_coordinate_list
        Robot.a_star_search = a_star_search

    def getPath(self):
        # GO U_TURN
        self.u_turn()

        while len(get_uncleaned_coordinate_list(self)) > 0:
            a_star_result_merge(self)
            self.u_turn()
        a_star_back_to_home(self)





