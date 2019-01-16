from Load_Map import coordinate_list, impassable_coordinate_list, coordinate_data
from Robot import *


class CleanSensor(object):
    def __init__(self) -> object:
        self.coordinate_data = coordinate_data
        self.coordinate_list = coordinate_list
        self.impassable_coordinate_list = impassable_coordinate_list
        self.area = 0
        self.distance = 0
        self.clear_distance = 0

    def setRobot(self, robot):
        self.distance = 0
        self.clear_distance = 0
        self.robot = robot

    def Area(self):
        self.area = len(self.coordinate_list) - len(self.impassable_coordinate_list)
        return self.area


    def getCleanAreaPercentage(self):
        return len(self.robot.clearArea) / self.Area()


    def getTotalDirtyCleanPercentage(self):
        return self.clear_distance / self.robot.totalDirty


    def updateDistance(self):
        self.distance = self.distance + 1

    def updateClearDistance(self):
        self.clear_distance = self.clear_distance + 1

    def checkDirtyLevel(self, x, y):
        return self.robot.dirtyData[x][y]['b']





