
import numpy as np
import heapq


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
    record = 10000000
    for coordinate2 in coordinate_list:
        distance = get_manhanttan_distance(coordinate1, coordinate2)
        if distance < record:
            record = distance
            result = coordinate2
    return result


def get_nearest_uncleaned_coordinate(self):
    passed_by_coordinate_list = get_passed_by_coordinate_list(self)
    return find_nearest_coordinate_by_manhanttan(self.current_coordinate, passed_by_coordinate_list)


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def neighbors(current, robot):
    coordinate_list = robot.coordinate_list
    impassable_coordinate_list = robot.impassable_coordinate_list
    neighbors = []

    x, y = current
    left_coordinate = (x - 1, y)
    right_coordinate = (x + 1, y)
    down_coordinate = (x, y - 1)
    up_coordinate = (x, y + 1)

    if left_coordinate in coordinate_list and left_coordinate not in impassable_coordinate_list:
        neighbors.append(left_coordinate)
    if right_coordinate in coordinate_list and right_coordinate not in impassable_coordinate_list:
        neighbors.append(right_coordinate)
    if down_coordinate in coordinate_list and down_coordinate not in impassable_coordinate_list:
        neighbors.append(down_coordinate)
    if up_coordinate in coordinate_list and up_coordinate not in impassable_coordinate_list:
        neighbors.append(up_coordinate)

    return neighbors


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def a_star_search(robot, goal):
    start = robot.current_coordinate
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    road_map = []

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in neighbors(current, robot):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    current = goal
    while current != start:
        road_map.append(current)
        current = came_from[current]

    return reversed(road_map)


def a_star_result_merge(robot):
    goal = get_nearest_uncleaned_coordinate(robot)
    road_map = a_star_search(robot, goal)
    for coordinate in road_map:
        robot.path_log.append(coordinate)
    robot.current_coordinate = goal


def a_star_back_to_home(robot):
    road_map = a_star_search(robot, robot.start_coordinate)
    for coordinate in road_map:
        robot.path_log.append(coordinate)
    robot.current_coordinate = robot.start_coordinate
