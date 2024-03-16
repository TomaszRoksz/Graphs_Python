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

def is_graph_connected(matrix):
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

def is_euler_graph(matrix):
    
    for el in matrix:
        if sum(el)%2!=0:
            return False
    return True

def is_half_euler_graph(matrix):
    odd=0
    
    for el in matrix:
        if sum(el)%2!=0:
            odd+=1
            if odd>2:
                return False
    return True



matrix=matrix_input()

if is_graph_connected(matrix):
    if is_euler_graph(matrix):
        print("Graf jest eulerowski")
    elif is_half_euler_graph(matrix):
        print("Graf jest półeulerowski")
    else: print("Graf nie jest eulerowski")
else: print("Graf jest niespójny")





