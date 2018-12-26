from Load_Map import coordinate_list, impassable_coordinate_list, coordinate_data
from Robot import *
from Motion import *


class CleanSensor(object):
    def __init__(self) -> object:
        self.coordinate_data = coordinate_data
        self.coordinate_list = coordinate_list
        self.impassable_coordinate_list=impassable_coordinate_list
        #self.judge_up_passable = judge_up_passable
        #self.judge_down_passable = judge_down_passable
        #self.judge_left_passable = judge_left_passable
        #self.judge_right_passable = judge_right_passable
        #self.move_up=move_up
        self.area=0
        self.distance=0
    def Area(self):
        self.area=len(self.coordinate_list)-len(self.impassable_coordinate_list)
        return self.area

    def getCleanAreaPercentage(self, robot):
        return len(robot.clearArea) / self.Area()

    #需要掛在astar啟動時?   self.Distance.setText(str(self.CalDis()))
    def CalDis(self):
        self.distance = self.distance + 1
        return self.distance
        """
        if self.judge_up_passable is True:
            distance=distance+1
        if self.judge_down_passable is True:
            distance=distance+1
        if self.judge_left_passable is True:
            distance=distance+1
        if self.judge_right_passable is True:
            distance=distance+1
        if self.move_up is True:
            print("YES")
        """


#CL=CleanSensor()
#print(len(CL.coordinate_data))
#print(len(CL.coordinate_list))
#print(len(CL.impassable_coordinate_list))
#print(CL.coordinate_data[0][1])




