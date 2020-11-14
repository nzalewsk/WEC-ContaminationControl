import numpy as np

def numRobots(columns, startFuel):
    return 2*columns/(startFuel-2)

def topStationXCoords(columns,fuel):
    robotInstance = 1;
    robots = numRobots(columns, fuel)
    topXCoordList = np.array[robots]
    while(robotInstance < robots)
        topXCoordList[robotInstance - 1] = int(columns*(2*robotInstance-1)/(2*robots))
        robotInstace++
    return topXCoordList

def botStationXCoords(columns, fuel):
    robotInstance = 1;
    robots = numRobots(columns, fuel)
    bottomXCoordList = np.array[robots]
    while(robotInstance <= robots)
        bottomXCoordList[robotInstance - 1] = int(columns*(robotInstance)/(robots))
        robotInstace++
    return bottomXCoordList

def sideStationYCoords(rows, fuel):
    robotInstance = 1;
    width = int(fuel/4)
    robots = numRobots(columns, fuel) - 1
    sideXCoordList = np.array[robots]
    while(robotInstance <= robots)
        sideXCoordList[robotInstance - 1] = int(width + ((2*robotInstance - 1)*(rows - 2*width)/(2*robots)))
        robotInstance++
    return sideXCoordList

def main():
    columns = 
    rows =
    fuel =
    inst = 0
    topRobots = np.array[numRobots(columns, fuel)]
    while(inst < numRobots(columns, fuel))
        topRobots[inst].x = topStationXCoords[inst]
        topRobots[inst].y = -1
        topRobots[inst].home.x = topRobots[inst].x
        topRobots[inst].home.y = topRobots[inst].y 
        topRobots[inst].
        topRobots[inst]
        inst++
    inst = 0

    botRobots = np.array[numRobots(columns, fuel)]
    while(inst < numRobots(columns, fuel)
          botRobots[inst].x = botStationXCoords[inst]
          botRobots[inst].y = rows
          botRobots[inst].home.x = botRobots[inst].x
          botRobots[inst].home.y = botRobots[inst].y
          inst++
    inst = 0

    leftRobots = np.array[numRobots(rows, fuel)]
    while(inst < numRobots(rows, fuel) - 1)
        leftRobots[inst].y = sideStationYCoords[inst]
        inst++
    inst = 0

    rightRobots = np.array[numRobots(rows, fuel
    while(inst < numRobots(rows, fuel) - 1)
        rightRobots[inst].y = sideStationYCoords[inst]
        rightRobots[inst].x = 
        inst++
    inst = 0
    
    
