#! /usr/bin/env python 
import re

correspondances = {
    ",":[0,1],
    ".":[0,1],
    ":":[1,1],
    ";":[1,1],
    "!":[1,1],
    "?":[1,1]
}

def betterSpaceCorrection(oldStr, corres):
    punc = [",", ".", ":", ";", "!"]
    res = ""
    for item in punc:
        #the "." case is tricky, re also has "." keyword
        patOld = r"\s*" + "\\" + item + r"\s*"
        patNew = " "*corres[item][0] + item + " "*corres[item][1]
        res = re.sub(patOld, patNew, oldStr)
        oldStr = res
    return res

#each list is a string
def enhancedSpaceCorrelation(lists, corres):
    res = []
    for idx, line in enumerate(lists):
        tmp = betterSpaceCorrection(line, corres)
        end = tmp[-1]
        #tackle the last line
        if idx == len(lists) - 1:
            #check the ending character
            if end == "," or end == ".":
                tmp = tmp[:-2] + "."
            else:
                tmp = tmp[:-3] + "."
        #tackle the other lines
        else:
            if end == "," or end == ".":
                #before ";" add a space
                tmp = tmp[:-2] + " ;"
            else:
                tmp = tmp[:-2] +";"
        res.append(tmp)
    return res

def SpaceCorrection(oldStr):
    #split the original string by space
    #oldStr is a list type now
    oldStr = oldStr.split(" ")
    #remove the redundant space in the list
    newStr = []
    for item in oldStr:
        if item != "":
            newStr.append(item)
    #now consider the punctuations
    for idx in xrange(len(newStr)):
        #tackle "," and "." cases, can not in the head
        if newStr[idx] == "," or newStr[idx] == ".":
            newStr[idx-1] += newStr[idx]
            newStr[idx] = []
        for alpha in newStr[idx]:
            #tackle ":",";","!","?" cases 
            if alpha == ":" or alpha == ";" or alpha == "!" or alpha == "?":
                # add a space before this alpha
                newStr[idx].replace(alpha, " "+alpha)
    ret = []
    for item in newStr:
        if len(item) != 0:
            ret.append(item)
    return " ".join(ret)

if __name__ == "__main__":
    oldString = "M.   Charles Granger ,     Mr . Right  !"
    newString = betterSpaceCorrection(oldString, correspondances)
    print newString
    lists = ["M.   Charles Granger ,     Mr . Right  !", "Hello . world, hello France;   "]
    res = enhancedSpaceCorrelation(lists, correspondances)
    for item in res:
        print item
