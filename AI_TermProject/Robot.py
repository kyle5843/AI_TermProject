from Sensor import *
from Motion import *
from A_Star import *
from CleanSensor import *
import copy

MOVE_COST = 0.1
CLEAN_COST = 0.05

class Robot(object):
    def __init__(self) -> object:
        from Load_Map import coordinate_list, impassable_coordinate_list, coordinate_data, totalDirty

        # coordinate_data include all map information
        self.coordinate_data = coordinate_data

        # coordinate_list only include all (x,y) coordinates
        self.coordinate_list = coordinate_list

        # impassable_coordinate_list include all impassable passed (x,y) coordinates
        self.impassable_coordinate_list = impassable_coordinate_list

        # temp dirty data, reset every term
        self.dirtyData = copy.deepcopy(self.coordinate_data)

        # totalDirty = all dirty level's sum
        self.totalDirty = totalDirty

        # sensor instance
        self.clearArea = []
        self.cleanSensor = CleanSensor()
        self.cleanSensor.setRobot(self)

        # initial
        self.start_coordinate = (27, 24)
        self.current_coordinate = self.start_coordinate
        self.path_log = []
        self.power = 100

        # motion
        Robot.move_up = move_up
        Robot.move_down = move_down
        Robot.move_left = move_left
        Robot.move_right = move_right
        Robot.u_turn = u_turn
        Robot.u_turn_toward_right = u_turn_toward_right
        Robot.u_turn_toward_left = u_turn_toward_left
        Robot.doClean = doClean
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
        Robot.detectObstructionType = detectObstructionType
        #
        # A*
        Robot.get_uncleaned_coordinate_list = get_uncleaned_coordinate_list
        Robot.a_star_search = a_star_search

    def getPath(self):
        self.path_log.append(self.current_coordinate)
        # GO U_TURN
        self.u_turn()

        while len(get_uncleaned_coordinate_list(self)) > 0:
            a_star_result_merge(self)
            self.u_turn()
        a_star_back_to_home(self)

    def reset(self):
        self.path_log = []
        self.current_coordinate = self.start_coordinate
        self.clearArea = []
        self.dirtyData = copy.deepcopy(self.coordinate_data)
        self.power = 100
        self.cleanSensor.setRobot(self)

    def check_down(self):
        return self.judge_up_passable()

    def check_up(self):
        return self.judge_down_passable()

    def check_right(self):
        return self.judge_right_passable()

    def check_left(self):
        return self.judge_left_passable()

    def clean(self, x, y):
        self.power = self.power - CLEAN_COST
        self.cleanSensor.updateClearDistance()
        self.doClean(x, y)

    def move(self):
        self.power = self.power - MOVE_COST
        self.cleanSensor.updateDistance()

    def detectObstructionType(self, x, y):
        return self.detectObstructionType(x, y)
