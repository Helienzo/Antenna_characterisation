#from src import *

#def __init__():
    # myfile = open(str("setup.txt"), "r")
    # fileVec = line.split(" ")
    # for item in myfile.split(" "):
    #     if "centerFrequency" in item:
    #         print "hello"
    #         print item.strip()


def main():
    setupLen = setup_size()
    myfile = open(str("setup.txt"), "r")
    lineNo = 0
    centerFrequency = 0
    vectorRec = False

    for line in myfile:
        fileVec = line.split(" ")
        #print line
        print fileVec[0]
        while lineNo < setupLen+2:
            lineNo += 1
            if fileVec[0] == "centerFrequency":
                centerFrequency = str(fileVec[2])

            elif "vectorRec" in line:
                vectorRec = bool(fileVec[2])


    print centerFrequency
def setup_size():
    with open("setup.txt") as f:
        for i, l in enumerate(f):
            pass
    return i + 1

main()
