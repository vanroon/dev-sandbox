#!/bin/python

import os
import csv

directory = 'C:\\Users\\Erik\\stack\\SEGURA\\Rabobank\\csv_processed\\'
masterCsvFileName = 'C:\\Users\\Erik\\stack\\SEGURA\\Rabobank\\masterCsv.csv'
noDuplicatesMasterFile = 'C:\\Users\\Erik\\stack\\SEGURA\\Rabobank\\noDuplicatesMasterCsv.csv'

# get all files in a variable
def listFiles(directory):
	tempArray = os.listdir(directory)
	fileArray = []
	for fileName in tempArray:
		fullPathToFile = '%s%s' % (directory, fileName)
		fileArray.append(fullPathToFile)
	return fileArray

def writeLinesFromSingleFile(fullPathToFile, outputFile):
	with open(fullPathToFile) as f:
		csvMaster = open(outputFile, 'a')
		for line in f:
			csvMaster.write(line)
		csvMaster.close()

def createOutputMasterFile(fileName):
	f = open(fileName, 'w')
	f.close()

def removeDuplicatesFromMasterFile(masterFile):
    line_set = set()
    for line in open(masterFile, 'r'):
        if line not in line_set:
            line_set.add(line.rstrip())
    return line_set

def writeNoDuplicatesSetToFile(noDuplicatesSet, noDuplicatesFile):
    createOutputMasterFile(noDuplicatesFile)
    f = open(noDuplicatesFile, 'a')
    for line in noDuplicatesSet:
        f.write(line+'\n')
    f.close()





		

def main():
    createOutputMasterFile(masterCsvFileName)
    listWithFiles = listFiles(directory)
    #fileNumber = 0
    for fileName in listWithFiles:
        writeLinesFromSingleFile(fileName, masterCsvFileName)
        #print fileName
        #fileNumber += 1
        #print fileNumber
    noDuplicatesSet = removeDuplicatesFromMasterFile(masterCsvFileName)
    writeNoDuplicatesSetToFile(noDuplicatesSet, noDuplicatesMasterFile)

main()




