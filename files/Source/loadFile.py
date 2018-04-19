def loadFile(file): 
    file  = open(file, 'r')
    string = ''
    for line in file: 
        string = string + line
    return string