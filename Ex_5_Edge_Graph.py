def graphInput():
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        lines.append(line)
    return lines

def graphList():
    graphLines=graphInput()
    graph=graphLines
    
    for i in range(len(graphLines)):
            graph[i]=list(map(int, graphLines[i].split()))
            graph[i].pop(0)
    return graph

def directedEdges(graph):
    edges={}
    vertices=len(graph)
    
    for i in range(vertices):
        for j in graph[i]:
            if i+1<j:
                edges[(i+1,j)]=set()
                
    for (x, y) in edges:
        x_neighbors=set(graph[x-1]) - {y}
        y_neighbors=set(graph[y-1]) - {x}  
        
        for z in x_neighbors:
            if z<x:
                edges[(x, y)].add((z, x))
            else:
                edges[(x, y)].add((x, z))
                
        for z in y_neighbors:
            if z<y:
                edges[(x, y)].add((z, y))
            else:
                edges[(x, y)].add((y, z))
                
    return edges

def unDirectedEdges(graph):
    edges={}
    vertices=len(graph)
    
    for i in range(vertices):
        for j in graph[i]:
            edges[(i+1,j)]=set()
                
        
    for (x, y) in edges:
        y_neighbors=set(graph[y-1])
        
        for z in y_neighbors:
            edges[(x, y)].add((y, z))
                
    return edges


def directedGraph(graph):
    for i in range(len(graph)):
        for vertice in graph[i]:
            if i+1 not in graph[vertice-1]:
                return False
    return True

def printEdges(edges):
    for key, values in edges.items():
        string=""
        string=str(key)
        for value in sorted(values):
            string+=" "+str(value)
        print(string)

graph=graphList()

if directedGraph(graph):
    edges=directedEdges(graph)
else:
    edges=unDirectedEdges(graph)

printEdges(edges)