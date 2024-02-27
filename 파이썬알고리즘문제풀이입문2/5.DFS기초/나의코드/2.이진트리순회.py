def DFS(x):
    if x>7:
        return
    else:
        print(x)
        DFS(2*x)
        DFS(2*x+1)

DFS(1)

print()

def DFS(x):
    if x>7:
        return
    else:
        
        DFS(2*x)
        print(x)
        DFS(2*x+1)

DFS(1)


print()



def DFS(x):
    if x>7:
        return
    else:
        
        DFS(2*x)
        DFS(2*x+1)
        print(x)

DFS(1)














