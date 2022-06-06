import networkx as nx

def AllConnectedSubGraph(n):
    count = 0
    for i in range(1,n+1): #1->n
        for j in range(1,n+1):
            if i != j :
                DG.add_edge(i,j)
    print(DG)
    return 

if __name__ == "__main__":    
    DG = nx.DiGraph()
    size = 3
    AllConnectedSubGraph(size)
    print("n = " + str(size))
    #print("count = "+ str(count))
    