import numpy as np
from leds import numOfLeds


bottomRightIndex = 50
topRightIndex = 86
topLeftIndex = 148
bottomLeftIndex = 185
endIndex = 249

numOfLedsRight = topRightIndex - bottomRightIndex
numOfLedsTop = topLeftIndex - topRightIndex
numOfLedsLeft = bottomLeftIndex - topLeftIndex
numOfLedsBottom = endIndex - bottomLeftIndex 
depth = 0.1 # percentage


def getSize(arr2d):
    return (len(arr2d[0]), len(arr2d))

def getAverageRowsColors(rows):
    rowsArray = np.array(rows, dtype=np.int32)
    averageColors = np.mean(rowsArray, axis=0).astype(int)
    return averageColors.tolist()

def getAverageColumnsColors(columns):
    columnsArray = np.array(columns, dtype=np.int32)
    averageColors = np.mean(columnsArray, axis=1).astype(int)
    return averageColors.tolist()

def getMappedRows(arr, newWidth):
    oldWidth, height = getSize(arr)
    newArr = [ [ None for _ in range(newWidth) ] for _ in range(height) ]

    for newIndex in range(newWidth):
        oldIndex = (newIndex * oldWidth) // newWidth
        for heightIndex in range(height):
            newArr[heightIndex][newIndex] = arr[heightIndex][oldIndex]

    return newArr

def getMappedColumns(arr, newHeight):
    width, oldHeight = getSize(arr)
    newArr = [ None for _ in range(newHeight) ]

    for newIndex in range(newHeight):
        oldIndex = (newIndex * oldHeight) // newHeight
        newArr[newIndex] = arr[oldIndex]

    return newArr

def getColors(frame):
    colors = [ (0, 0, 0) for _ in range(numOfLeds) ]
    width, height = getSize(frame)
    depthWidth = round(width * depth)
    depthHeight = round(height * depth)

    #* TOP
    topRows = frame[:depthHeight]
    mappedTopRows = getMappedRows(topRows, numOfLedsTop)
    topAverageColors = getAverageRowsColors(mappedTopRows)
    topAverageColors = topAverageColors[::-1]

    for index in range(numOfLedsTop):
        colors[topRightIndex + index] = topAverageColors[index]

    #* BOTTOM
    bottomRows = frame[-depthHeight:]
    mappedBottomRows = getMappedRows(bottomRows, numOfLedsBottom)
    bottomAverageColors = getAverageRowsColors(mappedBottomRows)

    for index in range(numOfLedsBottom):
        colors[bottomLeftIndex + index] = bottomAverageColors[index]

    #* RIGHT
    rightRows = frame[:, -depthWidth:]
    mappedRightRows = getMappedColumns(rightRows, numOfLedsRight)
    rightAverageColors = getAverageColumnsColors(mappedRightRows)
    rightAverageColors = rightAverageColors[::-1]

    for index in range(numOfLedsRight):
        colors[bottomRightIndex + index] = rightAverageColors[index]

    #* LEFT
    leftRows = frame[:, :depthWidth]
    mappedLeftRows = getMappedColumns(leftRows, numOfLedsLeft)
    leftAverageColors = getAverageColumnsColors(mappedLeftRows)

    for index in range(numOfLedsLeft):
        colors[topLeftIndex + index] = leftAverageColors[index]

    return colors
