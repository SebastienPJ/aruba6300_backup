import time

def saveCurrentScreen(session, server_IP, port_number):
    time.sleep(5)
    screenOutput = session.read_very_eager()
    with open(f'SavedScreens/SavedScreen_{server_IP}_{port_number}.txt', 'w') as savedScreenFile:
        savedScreenFile.write(screenOutput.decode('ascii'))
        savedScreenFile.close()

def getCurrentPrompt(filePath):
    endArray = []
    with open(filePath) as file:
        for line in file:
            endArray.append(line.replace('\n', ''))
        file.close()
    print(f'Length of endArray: {len(endArray)}')
    print(endArray)
    print(f'Current Prompt: {endArray[-1]}')
    return endArray[-1]