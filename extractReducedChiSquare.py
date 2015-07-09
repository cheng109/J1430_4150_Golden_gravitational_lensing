# Edit by Jun Cheng

import os.path
import re

def getLogFileList(DirectoryName):
    filenames = next(os.walk(DirectoryName))[2]
    logFileList = []
    for name in filenames:
        if name.startswith('lv_parameter'):
            logFileList.append(name)
    return logFileList


def getReducedChiSquare(logFileList, outputFile):
    #reducedChiSquare = []
    file = open(outputFile,'w')
    file.write("#column1: Log file name \n#cloumn2: Reduced Chi-Square\n")
    for fileName in logFileList:
        for line in reversed(open(fileName).readlines()):
            match = re.search(r'(.*)Reduced chisqu: (.*)', line)
            #

            if match:
                reducedChiSquare = re.findall("\d+.\d+",match.group(2))[0]
                file.write(fileName + "\t" + str(reducedChiSquare) +"\n")
                break
    file.close()

def main():
    outputFile = "output.txt"
    DirectoryName= "/Users/cheng109/work/J1430_4150_Golden_gravitational_lensing"
    logFileList = getLogFileList(DirectoryName)
    getReducedChiSquare(logFileList, outputFile)






if __name__=="__main__":
    main()