# Edit by Jun Cheng

# usage:
#   python extractReducedChiSquare.py <DirectoryName>

import os.path
import sys
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
               +"#column5: Time used (Minutes)\n"
               +"\n"
               )
    minChi = 10000
    minFileName = ""
    for fileName in logFileList:
        for line in os.popen('tail -n 10 ' + fileName).readlines():
            match = re.search(r'(.*)Reduced chisqu: (.*)', line)
            if match:
                reducedChiSquare = float(re.findall("\d+.\d+",match.group(2))[0])
                if reducedChiSquare < minChi: 
                    minChi = reducedChiSquare
                    minFileName = fileName
                endTime = 0
                startTime, endTime, usedTime = getTimeUsed(fileName, line)
                file.write(fileName + "\t\t"
                           + str(reducedChiSquare)+ "\t\t"
                           + startTime + "\t\t"
                           + endTime + "\t\t"
                           + usedTime + "\t\t"
                           +"\n")
                break
    file.write("\nThe minimum Reduced Chi-Square:\n"+minFileName + "\t\t" + str(minChi)+"\n")
    file.close()

def getTimeUsed(fileName, lineWithEndTime):
    startTimeMatch = re.search(r'.*(2015.*).log',fileName)
    startTime =  startTimeMatch.group(1)

    endTimeMatch = re.findall("\d+.\d+",lineWithEndTime)
    endTime = ""
    for i in range(3):
        endTime += str(endTimeMatch[i]).replace(":","").replace("/","").replace(" ","_")

    DayDiff = float(endTime[0:8]) - float(startTime[0:8])
    HourDiff = DayDiff*24 + float(endTime[9:11])-float(startTime[9:11])
    MinDiff = HourDiff*60 + float(endTime[11:13])-float(startTime[11:13])

    # Time Format:  YYYYMMDD_HHMMSS


    usedTime = str(round(MinDiff/60,2))
    return startTime, endTime, usedTime


def main():
    outputFile = "output.txt"
    #DirectoryName= "/Users/cheng109/work/J1430_4150_Golden_gravitational_lensing/logFileDirectory_test/"
    DirectoryName= os.getcwd() + "/" + sys.argv[1]
    os.chdir( DirectoryName)
    logFileList = getLogFileList(DirectoryName)
    getReducedChiSquare(logFileList, outputFile)


if __name__=="__main__":
    main()
