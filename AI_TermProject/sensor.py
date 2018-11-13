

def judge_up_passable(self):
    x, y = self.current_coordinate
    up_coordinate = (x, y + 1)
    if up_coordinate not in self.coordinate_list or (up_coordinate in self.impassable_coordinate_list):
        return False
    else:
        return True


def judge_down_passable(self):
    x, y = self.current_coordinate
    down_coordinate = (x, y - 1)
    if down_coordinate not in self.coordinate_list or (down_coordinate in self.impassable_coordinate_list):
        return False
    else:
        return True


def judge_left_passable(self):
    x, y = self.current_coordinate
    left_coordinate = (x - 1, y)
    if left_coordinate not in self.coordinate_list or (left_coordinate in self.impassable_coordinate_list):
        return False
    else:
        return True


def judge_right_passable(self):
    x, y = self.current_coordinate
    right_coordinate = (x + 1, y)
    if right_coordinate not in self.coordinate_list or (right_coordinate in self.impassable_coordinate_list):
        return False
    else:
        return True


def judge_up_passed(self):
    x, y = self.current_coordinate
    up_coordinate = (x, y + 1)
    if up_coordinate in self.path_log:
        return True
    else:
        return False


def judge_down_passed(self):
    x, y = self.current_coordinate
    down_coordinate = (x, y - 1)
    if down_coordinate in self.path_log:
        return True
    else:
        return False


def judge_right_passed(self):
    x, y = self.current_coordinate
    right_coordinate = (x + 1, y)
    if right_coordinate in self.path_log:
        return True
    else:
        return False


def judge_left_passed(self):
    x, y = self.current_coordinate
    left_coordinate = (x - 1, y)
    if left_coordinate in self.path_log:
        return True
    else:
        return False

