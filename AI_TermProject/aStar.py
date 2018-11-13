
import numpy as np


def multi_dim_diff(coordinate_list_1, coordinate_list_2):
    coordinate_list_1, coordinate_list_2 = np.array(coordinate_list_1), np.array(coordinate_list_2)
    arr1_view = coordinate_list_1.view([('', coordinate_list_1.dtype)] * coordinate_list_1.shape[1])
    arr2_view = coordinate_list_2.view([('', coordinate_list_2.dtype)] * coordinate_list_2.shape[1])
    intersected = np.setdiff1d(arr1_view, arr2_view)
    return np.ndarray.tolist(intersected)


def get_uncleaned_coordinate_list(self):
    passable_coordinate_list = multi_dim_diff(self.coordinate_list, self.impassable_coordinate_list)
    uncleaned_coordinate_list = multi_dim_diff(passable_coordinate_list, self.path_log)
    return uncleaned_coordinate_list


def multi_dim_intersect(coordinate_list_1, coordinate_list_2):  # 两个坐标集的交集
    coordinate_list_1, coordinate_list_2 = np.array(coordinate_list_1), np.array(coordinate_list_2)
    arr1_view = coordinate_list_1.view([('', coordinate_list_1.dtype)] * coordinate_list_1.shape[1])
    arr2_view = coordinate_list_2.view([('', coordinate_list_2.dtype)] * coordinate_list_2.shape[1])
    intersected = np.intersect1d(arr1_view, arr2_view)
    return np.ndarray.tolist(intersected)


def get_passed_by_coordinate_list(self):
    passed_by_coordinate_list = []
    for coordinate in self.path_log:
        x, y = coordinate
        up = (x, y + 1)
        down = (x, y - 1)
        left = (x - 1, y)
        right = (x + 1, y)
        passed_by_coordinate_list.append(up)
        passed_by_coordinate_list.append(down)
        passed_by_coordinate_list.append(left)
        passed_by_coordinate_list.append(right)
    passed_by_coordinate_list = list(set(passed_by_coordinate_list))
    passed_by_coordinate_list = multi_dim_intersect(passed_by_coordinate_list, self.coordinate_list)
    passed_by_coordinate_list = multi_dim_intersect(passed_by_coordinate_list, self.get_uncleaned_coordinate_list())
    return passed_by_coordinate_list


def get_manhanttan_distance(coordinate1, coordinate2):
    return np.abs(np.array(coordinate1) - np.array(coordinate2)).sum()


def find_nearest_coordinate_by_manhanttan(coordinate1, coordinate_list):
    record = 50000
    for coordinate2 in coordinate_list:
        distance = get_manhanttan_distance(coordinate1, coordinate2)
        if distance < record:
            record = distance
            result = coordinate2
    return result


def get_nearest_uncleaned_coordinate(self):
    passed_by_coordinate_list = get_passed_by_coordinate_list(self)
    return find_nearest_coordinate_by_manhanttan(self.current_coordinate, passed_by_coordinate_list)
