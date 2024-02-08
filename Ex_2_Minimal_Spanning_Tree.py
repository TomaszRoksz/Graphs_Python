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

def graph_connected(matrix):
    visited=[False]*len(matrix)
    visited[0]=True
    stack=[0]
    current=0

    while stack:
        for i in range(len(matrix)):
            
            if matrix[current][i]!="0" and not visited[i]:
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

def create_edges(matrix):
        edges=[]
        vi=[]
        vj=[]
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                if matrix[i][j]!="0": 
                    vi.append(i)
                    vj.append(j)
                    edges.append(int(matrix[i][j]))

        return vi, vj, edges

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank= [0 for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False
        
        if self.rank[root_x]<self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x]>self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
            self.rank[root_x]+=1
            return True
        
        
def heapify(vi, vj, edges, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and edges[i] < edges[l]:
        largest = l
 
    if r < n and edges[largest] < edges[r]:
        largest = r
  
    if largest != i:
        (edges[i], edges[largest]) = (edges[largest], edges[i])# swap
        (vi[i], vi[largest]) = (vi[largest], vi[i])
        (vj[i], vj[largest]) = (vj[largest], vj[i])
        
        heapify(vi, vj, edges, n, largest)
        
def heapSort(vi, vj, edges):
    n = len(edges)
    
 # Build a maxheap.
 # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(vi, vj, edges, n, i)
        
 # One by one extract elements
    for i in range(n - 1, 0, -1):
        (edges[i], edges[0]) = (edges[0], edges[i])  # swap
        (vi[i], vi[0]) = (vi[0], vi[i])
        (vj[i], vj[0]) = (vj[0], vj[i])
        heapify(vi,vj, edges, i, 0)
    return vi, vj, edges 

def cost_calculate(vi, vj, edges):
    n=len(edges)
    uf=UnionFind(n)
    cost=0
    
    for i in range(len(edges)):
        if uf.union(vi[i], vj[i]):
            cost+=edges[i]
    return cost



matrix=matrix_input()

if graph_connected(matrix):
        
    vi, vj, edges=create_edges(matrix)

    vi, vj, edges=(heapSort(vi, vj, edges))
    
    cost=cost_calculate(vi, vj, edges)

    print(cost)
else: print("Graf nie jest spójny")
