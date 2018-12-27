import csv
import json

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


with open('mapData.json') as f:
    data = json.load(f)
mapData = data['MapData']

coordinate_data = [[0 for x in range(50)] for y in range(50)]
for x in range(len(mapData)):
    for y in range(len(mapData[x])):
        posX = mapData[x][y]['x']
        posY = mapData[x][y]['y']
        posY = abs(30 - posY - 1)
        coordinate_data[posX][posY] = mapData[x][y]

