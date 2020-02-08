import sys
import copy

res = []
stack = []

def packManDFS(pmPosX, pmPosY, fdPosX, fdPosY, visited,tmpRes):
    while(True):
        if pmPosX == fdPosX and pmPosY == fdPosY:
            res.append(copy.deepcopy(tmpRes))
            break

        if mp[pmPosX-1][pmPosY] != "%" and visited[pmPosX-1][pmPosY] == 0:
            stack.append([pmPosX - 1, pmPosY])
            visited[pmPosX - 1][pmPosY] = 1
            
        if mp[pmPosX][pmPosY-1] != "%" and visited[pmPosX][pmPosY-1] == 0:
            stack.append([pmPosX, pmPosY - 1])
            visited[pmPosX][pmPosY - 1] = 1



        if mp[pmPosX+1][pmPosY] != "%" and visited[pmPosX+1][pmPosY] == 0:
            stack.append([pmPosX + 1, pmPosY])
            visited[pmPosX + 1][pmPosY] = 1

        if mp[pmPosX][pmPosY+1] != "%" and visited[pmPosX][pmPosY+1] == 0:
            stack.append([pmPosX, pmPosY + 1])
            visited[pmPosX][pmPosY + 1] = 1

        if stack:
            pos = stack.pop(0)
            pmPosX = pos[0]
            pmPosY = pos[1]
            tmpRes.append([pmPosX, pmPosY])

def findMinRoute(pmPosX, pmPosY, fdPosX, fdPosY, stack):
    newStack = []
    oldVal = stack.pop(-1)
    # print(oldVal)
    newStack.append(oldVal)
    while stack:
        val = stack.pop(-1)
        # print("{} {}: {} {}".format(val, oldVal,val[0]+1, val[0]-1))
        
        if val[0] == oldVal[0] and (val[1] + 1) == oldVal[1]:
            oldVal = val 
            newStack.append(val)
        elif val[0] == oldVal[0] and (val[1] - 1) == oldVal[1]:
            oldVal = val
            newStack.append(val)
        elif (val[0] + 1)== oldVal[0] and (val[1]) == oldVal[1]:
            oldVal = val
            newStack.append(val)
        elif (val[0] - 1) == oldVal[0] and (val[1]) == oldVal[1]:
            oldVal = val
            newStack.append(val)
            
    return newStack

if __name__ == "__main__":
    rawTxt = sys.stdin.read()
    
    rawTxt = rawTxt.split()
    
    pmPosX = int(rawTxt[0])
    pmPosY = int(rawTxt[1])
    fdPosX = int(rawTxt[2])
    fdPosY = int(rawTxt[3])
    
    rawMap = rawTxt[6:]
    
    mp = [[0]*len(rawMap[0]) for _ in range(len(rawMap))]
    visited = [[0]*len(rawMap[0]) for _ in range(len(rawMap))]
    for i in range(len(rawMap)):
        for j in range(len(rawMap[0])):
            mp[i][j] = rawMap[i][j]

    tmpRes = []
    tmpRes.append([pmPosX, pmPosY])
    visited[pmPosX][pmPosY] = 1
    packManDFS(pmPosX, pmPosY, fdPosX, fdPosY, visited, tmpRes)
    
    stack = tmpRes.copy()
    res = findMinRoute(pmPosX, pmPosY, fdPosX, fdPosY, stack)
    
    res.reverse()
    
    print(len(tmpRes))
    for r in tmpRes:
        print("{} {}".format(r[0],r[1]))
        
    print(len(res)-1)
    for r in res:
        print("{} {}".format(r[0],r[1]))
    