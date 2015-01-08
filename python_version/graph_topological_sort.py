class Graph:
    def __init__(self, vertices = [], Adj = {}):
        self.vertices = vertices
        self.Adj = Adj

    def itervertices(self):
        return self.vertices

    def neighbors(self, v):
        return self.Adj[v]


class DFSResult:     # More practice
    def __init__(self):
        self.parent = {}
        self.start_time = {}
        self.finish_time = {}
        self.order = []
        self.edges = {}
        self.t = 0


def dfs(g):
    results = DFSResult()
    for v in g.itervertices():
        if v not in results.parent:
            dfs_visit(g, v, results)

    return results

def dfs_visit(g, v, results, parent = None):
    results.parent[v] = parent
    results.t += 1
    results.start_time[v] = results.t

    if parent is not None:
        results.edge[(parent, v)] = 'tree edge'

    for n in g.neighbors(v):
        if n not in results.parent:
            dfs_visit(g, n, results, v)
        elif n not in results.finish_time:
            results.edges[(v, n)] = 'back edge'
        elif results.start_time[n] < results.start_time[v]:
            results.edges[(v, n)] = 'forward edge'
        else:
            results.edges[(v, n)] = 'cross edge'

    results.t += 1
    results.finish_time[v] = results.t
    results.order.append(v)

def topological_sort(g):
    results = dfs(g)
    results.order.reverse()
    return results.order







