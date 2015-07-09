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
    file = open(outputFile,'w')
    file.write("#column1: Log file name \n"
               +"#column2: Reduced Chi-Square\n"
               +"#column3: Star Time\n"
               +"#column4: End Time\n"
               +"#column5: Time used\n"
               )
    for fileName in logFileList:

        for line in reversed(open(fileName).readlines()):
            match = re.search(r'(.*)Reduced chisqu: (.*)', line)
            if match:
                reducedChiSquare = re.findall("\d+.\d+",match.group(2))[0]
                endTime = 0
                startTime, endTime, usedTime = getTimeUsed(fileName, line)
                file.write(fileName + "\t"
                           + str(reducedChiSquare)+ "\t"
                           + startTime + "\t"
                           + endTime + "\t"
                           + usedTime + "\t"
                           +"\n")
                break
    file.close()

def getTimeUsed(fileName, lineWithEndTime):
    startTimeMatch = re.search(r'.*(2015.*).log',fileName)
    startTime =  startTimeMatch.group(1)

    endTimeMatch = re.findall("\d+.\d+",lineWithEndTime)
    endTime = ""
    for i in range(3):
        endTime += str(endTimeMatch[i]).replace(":","").replace("/","").replace(" ","_")

    usedTime = "0"
    return startTime, endTime, usedTime


def main():
    outputFile = "output.txt"
    DirectoryName= "/Users/cheng109/work/J1430_4150_Golden_gravitational_lensing"
    logFileList = getLogFileList(DirectoryName)
    getReducedChiSquare(logFileList, outputFile)


if __name__=="__main__":
    main()