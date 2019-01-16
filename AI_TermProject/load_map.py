import json

# map
with open('mapData.json') as f:
    data = json.load(f)
mapData = data['MapData']

coordinate_list = []
impassable_coordinate_list = []
coordinate_data = [[0 for x in range(50)] for y in range(50)]
totalDirty = 0
for x in range(len(mapData)):
    for y in range(len(mapData[x])):
        posX = mapData[x][y]['x']
        posY = mapData[x][y]['y']
        posY = abs(30 - posY)
        coordinate_data[posX][posY] = mapData[x][y]
        coordinate_list.append((posX, posY))
        coordinate_type = coordinate_data[posX][posY]['a']
        if coordinate_type == 1 or coordinate_type == 5 or coordinate_type == 6:
            impassable_coordinate_list.append((posX, posY))
        else:
            totalDirty = totalDirty + coordinate_data[posX][posY]['b']
