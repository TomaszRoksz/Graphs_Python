def matrix_input():
    y=input()
    y = list(map(int, y.split()))
    matrix=[]

    matrix.append(y)

    for i in range(len(y)-1):
        a=input()
        a=list(map(int, a.split()))
        matrix.append(a)
    return matrix

def min_distance(distances, visited):
    min_value = float("inf")
    min_index=-1
    
    for i in range(len(distances)):
        if distances[i]<min_value and i not in visited:
            min_value=distances[i]
            min_index=i
            
    return min_index

def dijkstra(matrix, s):
    vertices=len(matrix)
        
    distances=[float('inf')]*vertices
    distances[s]=0
    
    visited=[]
    
    for i in range(vertices):
        current_vertice=min_distance(distances, visited)
        visited.append(current_vertice)

                
        for j in range(vertices):
            if matrix[current_vertice][j]!=0:
                
                new_distance=distances[current_vertice]+matrix[current_vertice][j]
                if new_distance<distances[j]:
                    distances[j]=new_distance
                    
    return distances         
        
def longest_diameter(matrix):
    longest_dia=0
    distances=0
    diameters=[]
    startIndexes=[]
    
    for i in range(len(matrix)):
        distances=dijkstra(matrix, i)
        
        longest_dia=max(distances)
                
        diameters.append(longest_dia)
        
    return diameters

def graph_connected(matrix):
    visited=[False]*len(matrix)
    visited[0]=True
    stack=[0]
    current=0

    while stack:
        for i in range(len(matrix)):
            
            if matrix[current][i]!=0 and not visited[i]:
                current=i
                stack.append(i)
                visited[i]=True
                if all(visited): return True
                break
                
            elif i==len(matrix)-1:
                stack.pop()
                if not stack: return False
                current=stack[-1]
    return False

def print_vertices(diameters):
    longest=0
    
    longest=max(diameters)

    string=""
    
    for i in range(len(diameters)):
        if diameters[i]==longest:
            string+=str(i+1)+" "
            
    print(string[:-1])
    
    

    
matrix=matrix_input()

if graph_connected(matrix):
    diameters=longest_diameter(matrix)

    print_vertices(diameters)   
        
else: print("Graf jest niespójny")