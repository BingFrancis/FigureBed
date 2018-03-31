#!/usr/bin/env python
#coding=utf-8
import os


def writeToFile(paramList, filePath):
    file = open(filePath, 'r+')
    paramLines = file.readlines()
    file.close()
    paramNames = [i.split()[0] for i in paramLines]

    newLines = []
    for i in range(len(paramNames)):
        newLines.append(paramNames[i] + '\t' + str(paramList[i]) + '\n')

    file = open(filePath, 'w+')
    file.writelines(newLines)
    file.close()


def run(paramList, roboType, absPath):
    writeToFile(paramList, '../paramfiles/optimizing.txt')
    command = './sample_start-optimization.sh {0} {1} out'.format(roboType, absPath)
    os.system(command)

    file = open('./out')
    lines = file.readlines()
    file.close()
    rst = lines[-1].split(',')[-1]
    return float(rst)


def main():
    paramList = [0.713957,108.885,59.8033,-20.8189,135.06,81.8352,0.310764,-0.0750521,0.0638539,-66.0305,
    0.0352144,0.0453233,0.0797951,12.4784,114.868,1.54207,1.15373,0.699879,1.13833,-0.113229,
    0.285081,-0.116635,1.45764,0.593476,0.0882758,-0.208468,-0.126124]
    absPath = os.path.abspath('..')+'/paramfiles/optimizing.txt'
    print absPath
    roboType = 2
    rst = run(paramList, roboType, absPath)
    print(rst)


if __name__ == '__main__':
    main()
