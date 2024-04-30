# Ref: https://leetcode.com/discuss/interview-question/1353434/Doordash-Phone-Screen-or-Senior-Software-Engineer-or-July-2021

import collections, heapq


def find_shortest_paths(g_nodes, sources, destinations, weights):
    graph = collections.defaultdict(list)
    weight_between = {}
    for s, d, w in zip(sources, destinations, weights):
        graph[s].append(d)
        graph[d].append(s)
        weight_between[(s, d)] = w
        weight_between[(d, s)] = w

    parents = collections.defaultdict(set)

    dist = collections.defaultdict(lambda: float('inf'))
    dist[1] = 0

    def relaxation(v, u, w):
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            parents[v] = {u}
        elif dist[v] == dist[u] + w:
            parents[v].add(u)

    q = [(0, 1)]
    relaxed = set()
    while q:
        _, node = heapq.heappop(q)

        for nei in graph[node]:
            if nei not in relaxed:
                relaxation(nei, node, weight_between[(nei, node)])
                heapq.heappush(q, (weight_between[(nei, node)], nei))

        relaxed.add(node)


    shortest_edges = set()
    visited = set()
    dfs(g_nodes, parents, visited, shortest_edges)

    ans = []
    for s, d in zip(sources, destinations):
        if (s, d) in shortest_edges or (d, s) in shortest_edges:
            ans.append('YES')
        else:
            ans.append('NO')
    print(parents)
    print(ans)


def dfs(node, parents, visited, shortest_edges):
    if node in visited:
        return
    visited.add(node)
    while parents[node]:
        p = parents[node].pop()
        shortest_edges.add((node, p))
        dfs(p, parents, visited, shortest_edges)


if __name__ == '__main__':
    find_shortest_paths(
        5,
        [1, 2, 3, 4, 5, 1, 5],
        [2, 3, 4, 5, 1, 3, 3],
        [1, 1, 1, 1, 3, 2, 1]
    )

