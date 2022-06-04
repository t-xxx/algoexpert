def runLengthEncoding(string):
    encodeStrigCharactors = []
    currentRunLength = 1

    for i in range(1, len(string)):
        currentCharactor = string[i]
        previousCharactor = string[i - 1]

        if previousCharactor != currentCharactor or currentRunLength == 9:
            encodeStrigCharactors.append(str(currentRunLength))
            encodeStrigCharactors.append(str(previousCharactor))
            currentRunLength = 0

        currentRunLength += 1

    encodeStrigCharactors.append(str(currentRunLength))
    encodeStrigCharactors.append(string[len(string) - 1])

    return "".join(encodeStrigCharactors)
