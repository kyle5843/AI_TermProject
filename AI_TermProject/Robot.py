from sensor import *
from motion import *
from view import *
from aStar import *


class Robot(object):
    def __init__(self):
        from map_test import coordinate_list, impassable_coordinate_list
        from view import rootWindow
        self.coordinate_list = coordinate_list
        self.impassable_coordinate_list = impassable_coordinate_list
        self.start_coordinate = (0, 0)
        self.current_coordinate = self.start_coordinate
        self.path_log = []
        self.path_log.append(self.start_coordinate)
        self.rootWindow = rootWindow


robot = Robot()

if __name__ == '__main__':
    pass

# motion
Robot.move_up = move_up
Robot.move_down = move_down
Robot.move_left = move_left
Robot.move_right = move_right
Robot.u_turn_toward_right = u_turn_toward_right
Robot.u_turn_toward_left = u_turn_toward_left

# sensor
Robot.judge_up_passable = judge_up_passable
Robot.judge_down_passable = judge_down_passable
Robot.judge_left_passable = judge_left_passable
Robot.judge_right_passable = judge_right_passable
Robot.judge_up_passed = judge_up_passed
Robot.judge_down_passed = judge_down_passed
Robot.judge_left_passed = judge_left_passed
Robot.judge_right_passed = judge_right_passed

# A*
Robot.get_uncleaned_coordinate_list = get_uncleaned_coordinate_list

# GO U_TURN
robot.u_turn_toward_right()

# print(robot.path_log)
# print(len(robot.path_log))


# find unclear area
# uncleaned_coordinate_list = get_uncleaned_coordinate_list(robot)
robot.path_log.append((2, 0))
robot.current_coordinate = (2, 0)
result = get_nearest_uncleaned_coordinate(robot)
print(result)

# UI
show_window(robot.impassable_coordinate_list, robot.path_log)



