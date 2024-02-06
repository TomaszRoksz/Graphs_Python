def matrix_input():
    y=input()
    y=y.split()
    matrix=[]

    matrix.append(y)

    for i in range(len(y)-1):
        a=input()
        a=a.split()
        matrix.append(a)
    return matrix
        
def edges_count(matrix):
    edges=0
    for el in matrix:
        for value in el:
            if value=="1":
                edges+=1
    return int(edges/2)

def vertex_degree(matrix):
    vertexes=[0]*len(matrix)
    for i in range(len(matrix)):
        for x in range(len(matrix[i])):
            if matrix[i][x]=="1":
                vertexes[i]+=1
    vertexes_str=""
    for i in range(len(vertexes)):
        vertexes_str+=" "+str(vertexes[i])
    return vertexes_str

def average_degree(matrix):
    edges=edges_count(matrix)
    vertexes=len(matrix)
    average=str(edges/vertexes*2)
    if average[-2:]==".0": average=average[:-2]
    return average

def complete_graph(matrix):
    edges=edges_count(matrix)
    
    if edges==len(matrix)*(len(matrix)-1)/2:
        return True

def isCyclicUtil(matrix, v, visited, parent):
        visited[v] = True
 
        for i in range(len(matrix)): 
            if matrix[v][i]=="1" and visited[i] == False:
                if(isCyclicUtil(matrix, i, visited, v)):
                    return True

            elif matrix[v][i]=="1" and parent != i:
                return True
        return False

def isCyclic(matrix):
    visited=[False]*len(matrix)
    for i in range(len(matrix)): 
        if visited[i]==False:
            if(isCyclicUtil(matrix, i, visited, -1)) == True:
                return True
    return False

def isCycleUtil(matrix, v, visited, parent):
        visited[v] = True
 
        for i in range(len(matrix)): 
            if matrix[v][i]=="1" and visited[i] == False:
                if(isCycleUtil(matrix, i, visited, v)):
                    return True

            elif matrix[v][i]=="1" and parent != i:
                if False not in visited:
                    return True
        return False

def isCycle(matrix):
    vertexes=[0]*len(matrix)
    for i in range(len(matrix)):
        for x in range(len(matrix[i])):
            if matrix[i][x]=="1":
                vertexes[i]+=1
                
    for el in vertexes:
        if el != 2:
            return False
            
    visited=[False]*len(matrix)
    if(isCycleUtil(matrix, 0, visited, -1)):
        return True
    return False
    
def ispath(matrix):
    vertexes=[0]*len(matrix)
    for i in range(len(matrix)):
        for x in range(len(matrix[i])):
            if matrix[i][x]=="1":
                vertexes[i]+=1
    
    starters=0
    middles=0
    for el in vertexes:
        if el==1: starters+=1
        elif el==2: middles+=1
    if starters!=2 and middles!=len(vertexes)-2:
        return False
                 
    if isCyclic(matrix):
        return False
    
    return True

def istree(matrix):
    if isCyclic(matrix):
        return False
    
    stack=[0]
    visited=[False]*len(matrix)
    visited[0]=True
    current=0
    
    while stack:
        arg=False
        
        for i in range(len(matrix)): 
            if matrix[current][i]=="1" and visited[i] == False:
                stack.append(i)
                current=i
                visited[i]=True
                arg=True
                
        if arg==False:
            stack.pop(-1)
            if stack:
                current=stack[-1]
    
    if all(visited): return True
    else: return False
    
def have_common_neighbors(matrix, vertex1, vertex2):
    neighbors_vertex1 = set(i for i, value in enumerate(matrix[vertex1]) if value == "1")
    neighbors_vertex2 = set(i for i, value in enumerate(matrix[vertex2]) if value == "1")

    common_neighbors = neighbors_vertex1.intersection(neighbors_vertex2)

    return len(common_neighbors) > 2
    
def ishypercube(matrix):
    v=2
    n=1
    while v<len(matrix):
        v*=2
        n+=1
    
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if x!=y and have_common_neighbors(matrix, x, y):
                return False
        
    edges=edges_count(matrix)    
    if len(matrix)!=v or edges!=v*n/2:
        return False
    return True
                
    
matrix=matrix_input()
print("Ilość wierzchołków:",len(matrix))
print("Ilość krawędzi:",edges_count(matrix))
print("Stopnie wierzchołków:"+vertex_degree(matrix))
print("Średni stopień:", average_degree(matrix))

graph=True
if complete_graph(matrix):
    graph=False
    print("Jest to graf pełny")
if isCycle(matrix):
    graph=False
    print("Jest to cykl")
if ispath(matrix):
    graph=False
    print("Jest to ścieżka")
if istree(matrix):
    graph=False
    print("Jest to drzewo")
if ishypercube(matrix):
    graph=False
    print("Jest to hiperkostka")
if graph:
    print("Graf nie należy do żadnej z podstawowych klas")
