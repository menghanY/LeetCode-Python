def grayCodeDFS(n):
    '''
    depth-first search solution
    '''
    visited = {0}
    seq = [0]
    for _ in range(1, 1 << n):
        val = seq[-1]
        for i in range(n):
            neighbor = val ^ (1 << i)
            if neighbor not in visited:
                seq.append(neighbor)
                visited.add(neighbor)
                break
    return seq

