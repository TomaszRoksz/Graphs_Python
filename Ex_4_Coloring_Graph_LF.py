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
        
def stackVertices(matrix):
    vertices=len(matrix)
    stack=[-1]*vertices
    
    for i in range(vertices):
        for j in range(vertices):
            if j not in stack:
                if len(matrix[j])>=len(matrix[stack[i]]) or stack[i]==-1:
                    stack[i]=j
   
    return stack

def addColorsToVertices(matrix, stack):
    colors=[0]*len(stack)
    
    for vertice in stack:
        legalColor=False

        while legalColor==False:
            legalColor=True
            colors[vertice]+=1
            
            for el in matrix[vertice]:
                if colors[vertice] == colors[el-1]:
                
                    legalColor=False
    
    return colors

                           
def createString(colors):
    string=""
    
    for el in colors:
        string+=str(el)+" "
    string=string[:-1]
    return string

    
graph=graphList()
stack=stackVertices(graph)
colors=addColorsToVertices(graph, stack)
colors=createString(colors)

print("Pokolorowanie wierzchołków:", colors)
print("Liczba chromatyczna ==", max(colors))
