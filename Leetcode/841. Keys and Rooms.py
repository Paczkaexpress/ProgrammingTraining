class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        numOfRooms = len(rooms)
        notVisited = []
        visited = set()
        
        notVisited = rooms[0]
        visited.add(0)
        
        while notVisited:
            visited.add(notVisited[0])
            tmp = set(rooms[notVisited.pop(0)])
            tmp = tmp - visited
            # print(tmp)
            # print(visited)
            for i in tmp:
                notVisited.append(i)
            
        if len(visited) == numOfRooms:
            return True
        return False