import sys
import csv

class GraphNode(object):
    def __init__(self, node_id):
        self.node_id = node_id
        self.connections = []
        self.parent = None
        self.onStack = False

    def addConnection(self, connection_node):
        self.connections.append(connection_node)

    def __str__(self):
        connectionList = [x.node_id for x in self.connections]
        return "node id: {}, connections id: {}".format(self.node_id, connectionList)

def loadData(path: str) -> dict:
    movies = {}
    actors = {}
    rolesInMovies = {}
    mooviesForActors = {}

    with open(path+"movies.csv", newline='', encoding="utf-8") as f:
        csvFile = csv.reader(f, delimiter = ',')
        for row in csvFile:
            try:
                movies[int(row[0])] = row[1]
            except ValueError:
                # need to remove cases with the first line
                pass

    with open(path+"people.csv", newline='', encoding="utf-8") as f:
        csvFile = csv.reader(f, delimiter = ',')
        for row in csvFile:
            try:
                actors[int(row[0])] = row[1]
            except ValueError:
                # need to remove cases with the first line
                pass

    with open(path+"stars.csv", newline='', encoding="utf-8") as f:
        csvFile = csv.reader(f, delimiter = ',')
        for row in csvFile:
            try:
                if int(row[0]) in rolesInMovies:
                    rolesInMovies[int(row[0])].append(int(row[1]))
                else:
                    rolesInMovies[int(row[0])] = [int(row[1])]
            except ValueError:
                pass

            try:
                if int(row[1]) in mooviesForActors:
                    mooviesForActors[int(row[1])].append(int(row[0]))
                else:
                    mooviesForActors[int(row[1])] = [int(row[0])]
            except ValueError:
                pass
    
    return movies, actors, rolesInMovies, mooviesForActors

def createBaconDependency(actorsInMovies, moviesForActors):    
    graphCreationDict = dict()
    stack = list()
    counter = 0

    for item in actorsInMovies:
        stack = actorsInMovies[item]
        # print("actor: {}, movie stack: {}".format(item, stack))
        actors = list()
        
        if(item not in graphCreationDict): # if node for that actor is not existing
            node = GraphNode(item)
            graphCreationDict[item] = node
            counter += 1
        else: # if the node exists
            node = graphCreationDict[item]

        for x in stack:
            # find actors in a given films list
            actors.extend(moviesForActors[x])     

        for a in actors:
            # actors cannot point to himself
            if a is not item and a not in graphCreationDict:
                graph = GraphNode(a)
                counter += 1
                graphCreationDict[a] = graph
                node.connections.append(graph)
            elif a is not item:
                node.connections.append(graphCreationDict[a])

    print("Total number of nodes: {}".format(counter))
    return graphCreationDict

def findKavinBaconPath(startNode: GraphNode, targetNode: GraphNode):
    startNode.parent = None
    stack = list()
    startNode.onStack = True
    stack.append(startNode)
    counter = 0

    while stack:
        counter += 1
        print(counter,end="\r")
        node = stack.pop(0)
        if(node.node_id == targetNode.node_id):
            print("Destination found")
            targetNode = node
            break

        for x in node.connections:
            if(x.parent is None and x.onStack == False):
                x.parent = node
                # print("id: {}, parent: {}".format(x.node_id,x.parent))
                x.onStack = True
                stack.append(x)
    path = []
    node = targetNode
    path.append(node)
    while node.parent:
        # print("node id: {}".format(node.node_id))
        node = node.parent
        path.append(node)

    # print("node id: {}".format(node.node_id))
    return path

if __name__ == "__main__":
    print("The software will try find the Kevin Bacon number for the provided actors")
    # get argument
    if (len(sys.argv) < 4):
        sys.exit("Usage: python degrees.py [directory] [1st name] [2nd name]")
    
    
    folderName = sys.argv[1]
    actor1Name = sys.argv[2]
    actor2Name = sys.argv[3]
    
    # load data 
    path = folderName + '/'

    print("Start loading data")    
    moviesList, actors, rolesInMovies, mooviesForActors = loadData(path)
    print("Data loaded. Check if provided actors are existing in the database")

    
# finding fits for the first name
    fittingActorNames = []
    for item in actors.items():
        if (item[1] == actor1Name):
            fittingActorNames.append(item)

    if(len(fittingActorNames) == 1):
        actor1Id = fittingActorNames[0][0]
        print("{} has been found and his is is: {}".format(actor1Name, actor1Id))
    elif(len(fittingActorNames) == 0):
        sys.exit("Couldn't find the actor")
    else:
        print("More than one actor with the same name")
        actor1Id = fittingActorNames[0]

# finding fits for the second name
    fittingActorNames = []
    for item in actors.items():
        if (item[1] == actor2Name):
            fittingActorNames.append(item)

    if(len(fittingActorNames) == 1):
        actor2Id = fittingActorNames[0][0]
        print("{} has been found and his is is: {}".format(actor2Name, actor2Id))
    elif(len(fittingActorNames) == 0):
        sys.exit("Couldn't find the actor")
    else:
        print("More than one actor with the same name")
        actor2Id = fittingActorNames[0]

    print("Create a graph")
    graphCreationDict = createBaconDependency(rolesInMovies, mooviesForActors)

    print("{} has actor id: {}".format(actor1Name, actor1Id))
    print("{} has actor id: {}".format(actor2Name, actor2Id))

    # print("Node for the actor1: {}".format(graphCreationDict[actor1Id]))

    print("Find the shortest path")
    kavinBaconPath = findKavinBaconPath(graphCreationDict[actor1Id], graphCreationDict[actor2Id])

    print("{} degrees of separation.".format(len(kavinBaconPath)-1))
    for i in range(len(kavinBaconPath)-1):
        name1 = actors[kavinBaconPath[i].node_id]
        name2 = actors[kavinBaconPath[i+1].node_id]
        # checking common movies
        movieSet1 = set(rolesInMovies[kavinBaconPath[i].node_id])
        movieSet2 = set(rolesInMovies[kavinBaconPath[i+1].node_id])
        movieSet = list(movieSet1 & movieSet2)
        movies = list()
        for x in list(movieSet):
            movies.append(moviesList[x])

        movies = " and ".join(movies)
        print("{}: {} and {} starred in {}".format(i+1, name1, name2, movies))