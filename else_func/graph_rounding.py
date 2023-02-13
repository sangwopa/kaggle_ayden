#재귀
def recursive_dfs(v, discovered=[]):
    graph = {
        1: [5, 6], #1에는 5와 6이 연결되어 있다.
        2: [3, 4, 6], #2에는 3과 4와 6이 연결되어 있다.
        3: [2, 4, 5], #3에는 2와 4와 5가 연결되어 있다.
        4: [2, 3], #4에는 2와 3이 연결되어 있다.
        5: [1, 3, 6], #5에는 1과 3과 6이 연결되어 있다.
        6: [1, 2, 5] #6에는 1과 2와 5가 연결되어 있다.
    }
    discovered.append(v) # discovered는 탐색한 노드들을 저장한다.
    for w in graph[v]:
        if not w in discovered: # w가 탐색한 노드가 아니라면 탐색한다.
            discovered=recursive_dfs(w,discovered) 
    return discovered

print(recursive_dfs(1))

#스택
def iterative_dfs(start_v):
    graph = {
        1: [5, 6], #1에는 5와 6이 연결되어 있다.
        2: [3, 4, 6], #2에는 3과 4와 6이 연결되어 있다.
        3: [2, 4, 5], #3에는 2와 4와 5가 연결되어 있다.
        4: [2, 3], #4에는 2와 3이 연결되어 있다.
        5: [1, 3, 6], #5에는 1과 3과 6이 연결되어 있다.
        6: [1, 2, 5] #6에는 1과 2와 5가 연결되어 있다.
    }
    discovered = []
    stack = [start_v]
    while stack :
        v = stack.pop()
        if v not in discovered : # 노드를 탐색하지 않았다면 discovered에 추가하고 탐색한다.
            discovered.append(v) 
            for w in graph[v] :
                stack.append(w) # stack에는 탐색해야할 노드들을 추가한다.
    return discovered