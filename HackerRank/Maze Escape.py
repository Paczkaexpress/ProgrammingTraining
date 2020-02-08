import sys

rawMap = sys.stdin.read().split()
rawMap = rawMap[1:]
initFlag = False
mp = [[0]*len(rawMap[0]) for _ in range(len(rawMap))]
bruteFlag = False

try:
    filename = open("myfile.txt","r+") 
except:
    filename = open("myfile.txt","w+")

# print(filename.read())
try:
    rawRead = filename.read().split()
    prevChoice = rawRead[0]
    # print(rawRead[1])
    if rawRead[1] == "True":
        bruteFlag = True
    else:
        bruteFlag = False
except:
    bruteFlag = False
    prevChoice = ""
    initFlag = True
    
if prevChoice == "UP":
    for j in range(len(rawMap[0])):
        for i in range(len(rawMap)):
            mp[i][j] = rawMap[i][j]
elif prevChoice == "DOWN":
    for j in range(len(rawMap[0])):
        for i in range(len(rawMap)-1,-1,-1):
            mp[i][j] = rawMap[i][j]
elif prevChoice == "RIGHT":
    for j in range(len(rawMap)):
        for i in range(len(rawMap[0])):
            mp[i][j] = rawMap[i][j]
elif prevChoice == "LEFT":
    for j in range(len(rawMap)-1,-1,-1):
        for i in range(len(rawMap[0])):
            mp[i][j] = rawMap[i][j]
else:
    for j in range(len(rawMap[0])):
        for i in range(len(rawMap)):
            mp[i][j] = rawMap[i][j]
# print(rawMap)
# print(mp)    
# print(prevChoice)

choice = ""
# print(initFlag)
# if initFlag == True:
    # choice = "RIGHT"
if bruteFlag == True:
    # print("activated")
    choice = "UP"
elif mp[2][1] ==  "e":
    choice = "DOWN"
elif mp[0][1] == "e":
    choice = "UP"
elif mp[1][2] == "e":
    choice = "RIGHT"
elif mp[1][0] == "e":
    choice = "LEFT"
elif mp[1][0] == "#" and mp[0][1] == "-" and mp[2][1] == "-" and initFlag == True:
    choice = "RIGHT" #left
elif mp[1][2] == "#" and mp[0][1] == "-" and mp[2][1] == "-" and initFlag == True:
    choice = "LEFT" #right
elif mp[0][1] == "#" and mp[1][0] == "-" and mp[1][2] == "-" and initFlag == True:
    choice = "DOWN" #up
elif mp[2][1] == "#" and mp[1][0] == "-" and mp[1][2] == "-" and initFlag == True:
    choice = "UP" #down

elif mp[1][0] == "#" and mp[2][1] == "-":
    # print("{} {}".format(mp[1][0], mp[2][1]))
    choice = "DOWN"
elif mp[1][2] == "#" and mp[0][1] == "-":
    # print("{} {}".format(mp[1][2], mp[0][1]))
    choice = "UP"

elif mp[0][1] == "#" and mp[0][0] == "#" and mp[0][2] == "#" and mp[1][0] == "-":
    # print("{} {}".format(mp[2][1], mp[1][0]))
    choice = "LEFT"
elif mp[2][1] == "#" and mp[1][0] == "-":
    # print("{} {}".format(mp[2][1], mp[1][0]))
    choice = "LEFT"
elif mp[0][1] == "#" and mp[1][2] == "-":
    # print("{} {}".format(mp[0][1], mp[1][2]))
    choice = "RIGHT"
elif mp[2][0] == "#" and mp[1][0] == "-":
    # print("{} {}".format(mp[2][1], mp[1][0]))
    choice = "LEFT"
    bruteFlag = True
elif mp[2][2] == "#" and mp[1][2] == "-":
    # print("{} {}".format(mp[0][1], mp[1][2]))
    choice = "RIGHT"
    bruteFlag = True
elif mp[2][1] == "-":
    # print("{} {}".format(mp[2][1], mp[1][0]))
    choice = "LEFT"
elif mp[0][1] == "-":
    # print("{} {}".format(mp[0][1], mp[1][2]))
    choice = "RIGHT"
else:
    choice = "UP"
    
# bute force algo
# rotate left if you can
# 
# print(mp)
filename.truncate(0)
filename.write(choice)
# print(str(bruteFlag))
filename.write(" ")
filename.write(str(bruteFlag))
print(choice)





