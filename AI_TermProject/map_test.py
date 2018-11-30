import csv

# map
file = "map.csv"
map = []
with open(file, newline='') as csv_file:
    f = csv.reader(csv_file)
    for row in f:
        map.append(row)

coordinate_list = []
impassable_coordinate_list = []
for x in range(len(map)):
    for y in range(len(map[x])):
        coordinate_list.append((y, x))
        if map[x][y] == '#':
            # reverse_x, reverse_y = y, len(map) - x - 1
            impassable_coordinate_list.append((y, x))
