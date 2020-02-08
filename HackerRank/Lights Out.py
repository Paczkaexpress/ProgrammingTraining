import sys
import copy

def checkIfAllSwitchedOff(mp):
    for i in range(len(mp)):
        for j in range(len(mp)):
            if mp[i][j] == "1":
                return False
    return True
    

def countRemainingSwitched(mp,y,x):
    counter = 0
    for i in range(y,len(mp)):
        for j in range(x,len(mp)):
            if mp[i][j] == "1":
                counter += 1
    return counter

def simulateToggle(mp,x,y):
    mp[y][x] = "1"
    
    try:
        if mp[y-1][x] == "1":
            mp[y-1][x] = "0"
        else:
            mp[y-1][x] = "1"
    except:
        pass
    
    
    try:
        if mp[y][x-1] == "1":
            mp[y][x-1] = "0"
        else:
            mp[y][x-1] = "1"
    except:
        pass
    
    return mp
    
def bruteForce(mp):
    tmpMap = copy.deepcopy(mp)
    for i in range(len(mp)):
        for j in range(len(mp)-1):
            if mp[i][j] == "1":
                y,x = i,j
                tmpMap = simulateToggle(tmpMap,x,y)
                if checkIfAllSwitchedOff(tmpMap) == True:
                    if countRemainingSwitched(mp, i, j) > 1:
                        continue
                return i,j

    for i in range(len(mp)):
        if mp[i][len(mp)-1] == "1":
            y,x = i,len(mp)-1
            tmpMap = simulateToggle(tmpMap,x,y)
            if checkIfAllSwitchedOff(tmpMap) == True:
                if countRemainingSwitched(mp, i, len(mp)-1) > 1:
                    continue
            return i,len(mp)-1
def tieMaster(mp):
    for i in range(len(mp)-1,-1,-1):
        for j in range(len(mp)-1,-1,-1):
            if mp[i][j] == "1":
                return i,j
            
if __name__ == "__main__":
    rawTxt = sys.stdin.read().split()
    
    rawTxt = rawTxt[1:]
    
    mp = [[0]*len(rawTxt) for _ in range(len(rawTxt))]
    
    for i in range(len(mp)):
        for j in range(len(mp)):
            mp[i][j] = rawTxt[i][j]

    x,y = bruteForce(mp)
    # x, y = tieMaster(mp)
    
    print("{} {}".format(x,y))