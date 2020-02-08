import sys
import copy

res = []

def packManDFS(pmPosX, pmPosY, fdPosX, fdPosY, visited,tmpRes):
    # print(tmpRes)
    if pmPosX == fdPosX and pmPosY == fdPosY:
        res.append(copy.deepcopy(tmpRes))
        return
    
    if mp[pmPosX][pmPosY+1] != "%" and visited[pmPosX][pmPosY+1] == 0:
        visited[pmPosX][pmPosY+1] = 1
        tmpRes.append([pmPosX, pmPosY+1])
        packManDFS(pmPosX, pmPosY+1, fdPosX, fdPosY, visited,tmpRes)
        tmpRes.pop(-1)
        visited[pmPosX][pmPosY+1] = 0
    
    if mp[pmPosX+1][pmPosY] != "%" and visited[pmPosX+1][pmPosY] == 0:
        visited[pmPosX+1][pmPosY] = 1
        tmpRes.append([pmPosX+1, pmPosY])
        packManDFS(pmPosX+1, pmPosY, fdPosX, fdPosY, visited,tmpRes)
        tmpRes.pop(-1)
        visited[pmPosX+1][pmPosY] = 0
    
    if mp[pmPosX-1][pmPosY] != "%" and visited[pmPosX-1][pmPosY] == 0:
        visited[pmPosX-1][pmPosY] = 1
        tmpRes.append([pmPosX-1, pmPosY])
        packManDFS(pmPosX-1, pmPosY, fdPosX, fdPosY, visited,tmpRes)
        tmpRes.pop(-1)
        visited[pmPosX-1][pmPosY] = 0
    
    if mp[pmPosX][pmPosY-1] != "%" and visited[pmPosX][pmPosY-1] == 0:
        visited[pmPosX][pmPosY-1] = 1
        tmpRes.append([pmPosX, pmPosY-1])    
        packManDFS(pmPosX, pmPosY-1, fdPosX, fdPosY, visited,tmpRes)
        tmpRes.pop(-1)
        visited[pmPosX][pmPosY-1] = 0
        
    # print(res)
    
    return

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
    packManDFS(pmPosX, pmPosY, fdPosX, fdPosY, visited, tmpRes)
    
    # print(len(res))
    # print(res)
    
    minSol = 9999
    minId = 0
    for i in range(len(res)):
        if len(res[i]) < minSol:
            minSol = len(res[i])
            minId = i
    
    print(len(res[minId]))
    for r in res[minId]:
        print("{} {}".format(r[0],r[1]))
    print(len(res[0])-1)
    for r in res[0]:
        print("{} {}".format(r[0],r[1]))