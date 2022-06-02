def readfile(filename):
    letterDict = {}
    fileobj = open(filename, "r")
    for line in fileobj:
        line = line.strip()
        for char in line:
            char = char.lower()
            if char.isalpha():
                if char not in letterDict:
                    letterDict[char]=1
                else:
                    letterDict[char] += 1

    fileobj.close()
    return letterDict
def sortkeys(dictionary):
    dictkeys = dictionary.keys()
    keyList = list(dictkeys)
    keyList.sort()
    return keyList
def main ():
    alhphaDict =  readfile("speech.txt")
    sortedletters = sortkeys(alhphaDict)
    print("The frequency of letters are: ")
    for key in sortedletters:
        value = alhphaDict[key]
        print(key, ":", value)
main()
