

def createUnfilteredArray(path):
    endArray = []

    with open(path) as file:
        for line in file:
            endArray.append(line.split())

    return endArray



def createDesiredArray(rawArray, beginCase, endCase):
    if beginCase not in rawArray:
        return
    
    startIndex = rawArray.index(beginCase)
    arrayLength = len(rawArray)
    finishedArray = []

    for index in range(startIndex, arrayLength):

        if isinstance(endCase, list):
            if rawArray[index] == endCase:
                break
        elif isinstance(endCase, str):
            if endCase in rawArray[index]:
                break
        else:
            print('check your endPoint type')

            
        if len(rawArray[index]) == 0:
            continue
        
        currentLine = rawArray[index]
        finishedArray.append(currentLine)

    return finishedArray




def createDataOnlyArray(filteredArray, linesUntilData):
    lenArray = len(filteredArray)
    dataArray = []

    for number in range(linesUntilData, lenArray):
        dataArray.append(filteredArray[number])

    return dataArray


def getHostname(unprocessedArray):
    # print(unprocessedArray)

    for line in unprocessedArray:
        for element in line:
            if '#' in element:
                return element

    pass