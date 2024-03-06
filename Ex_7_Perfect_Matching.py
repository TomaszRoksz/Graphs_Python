def listInput():
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        lines.append(line)
    return lines

def createList():
    matrixLines=listInput()
    matrix=matrixLines
      
    for i in range(len(matrixLines)):
        matrix[i]=list(map(int, matrixLines[i].split()))
        matrix[i].pop(0)
                          
    return matrix

def DFS(graph):

    vertexes=len(graph)
    colors=[""]*vertexes
    stack=[1]
    visited=[1]
    colors[0]="red"
   
    while stack:
        condition=True
        
        for el in graph[stack[-1]-1]:
            if el not in visited:
                visited.append(el)
                
                if colors[stack[-1]-1]=="red":
                    colors[el-1]="blue"
                elif colors[stack[-1]-1]=="blue":
                    colors[el-1]="red"
                    
                stack.append(el)
                
                if len(visited)==vertexes:
                    return colors
                condition=False
                break
                
        if condition:
            stack.pop(-1)
    return False

def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if not seq:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item

def graphPerfectMatching(graph, colors):
    
    acceptedHusbands=[]
    nWifes=0
    wifes=[]
    husbands=[]
    
    for i in range(len(colors)):
        if colors[i]=="red":
            wifes.append(i+1)
        elif colors[i]=="blue":
            husbands.append(i+1)
    
    if husbands<wifes:
        wifes, husbands = husbands, wifes
        
    subsets = [x for x in powerset(wifes)]

    
    for subset in subsets:
        for wife in subset:
            for man in graph[wife-1]:
                if man not in acceptedHusbands:
                    acceptedHusbands.append(man)
        if len(acceptedHusbands)<len(subset):
            return False
        else: acceptedHusbands=[]
            
    return True

            
    

graph = createList()
colors=DFS(graph)

if graphPerfectMatching(graph, colors):
    print("Istnieje skojarzenie doskonałe")
else: print("Nie istnieje skojarzenie doskonałe")
