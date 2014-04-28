def removeLetters(letterList, toRemoveList):
    # convert the string to a mutable object
    newList = list(letterList)

    for i, currentChar in enumerate(newList):
        for charToRemove in toRemoveList:
            # we still want the spaces
            if charToRemove is currentChar:
                # cannot actually delete the element, since we depend on the iterator
                newList[i] = ""

    # before returning, we convert back into an immutable form
    return "".join(newList)


if __name__ == '__main__':
    letterList = raw_input("List A: ")
    toRemoveList = raw_input("List B: ")

    newList = removeLetters(letterList, toRemoveList)
    print newList
