G ={
    '8':['3','10'], #this establishing the graph structure to be further 
    #organized in the class below
    '3':['1','6'],
    '10':['14'],
    '6':['4','7'],
    '14':['13'],
    '13':[],
    '4':[],
    '7':[]
}
from collections import deque
def bfs(G, S): #Establishes the class, the graph and the start node
    visited = set() #creates a list where all visited vertexes are stored
    queue=deque([S]) #Takes each node from the list for evaluation

    while queue:#code that runs as you pick the first node from the list
        N = queue.popleft()#takes the vertex furthest left on the list which would be the first vertex
        if N not in visited:#If the vertex is not in the visited list already this if statement will then add that vertex.
            #the reason for this is to keep track of all the vertexes that have been evaluated to avoid a cycle.
            queue.add(N)
            print(N)
    for neighbor in G[N]:#this checks for all the variables attached to each initial vertex, so for 8 the neighbor would be (3,10)
        if neighbor in G[N]:#no code follows this because if its in the G(N) list nothing further should be done.
            if neighbor not in visited: #if its not in that list then the queue.append function places it in the back of the queue to be evaluated after any nodes currently present in the queue.
                queue.append(neighbor)
print("Breadth-First Search: ")#Title of the function
print(G, "A")#this just prints out the G after everything has been sorted.
