import heapq
import sys
    

def read_input():
    n, m, b, s = map(int, input().split())
    
    if n <= 0 or m <= 0 or b < 0 or s < 0:
        raise ValueError("invalid input (n, m, b, s)")
    
    boss_towns = list(map(int, input().split()))
    if (len(boss_towns)) != b:
        raise ValueError("invalid input, number of boss town does not match B")
    for town in boss_towns:
        if not (1 <= town <= n):
            raise ValueError("invalid town number in boss town")
    
    save_points = list(map(int, input().split()))
    if len(save_points) != s:
        raise ValueError("number of save points doesn't match with S")
    for town in save_points:
        if not (1 <= town <= n):
            raise ValueError("invalid number of twons in save points")
    
    roads = []
    for _ in range(m):
        u, v, t = map(int, input().split())
        if not (1 <= u <= n and 1 <= v <= n):
            raise ValueError("invalid town numbers in road")
        if t < 0:
            raise ValueError("Invalid trave time")
        roads.append((u, v, t))
    return n, m, b, s, boss_towns, save_points, roads


def dijkstra(graph, start, n):
    try:
        dist = [sys.maxsize] * (n + 1)
        dist[start] = 0
        pq = [(0, start)]  # (distance, node)
    
        while pq:
            curr_dist, u = heapq.heappop(pq)
            if curr_dist > dist[u]:
                continue
            for time, v in graph[u]:
                if dist[u] + time < dist[v]:
                    dist[v] = dist[u] + time
                    heapq.heappush(pq, (dist[v], v))
        return dist
    except Exception as e:
        # print(f"Error in Dijkstra's function : {e}")
        sys.exit(1)


def shortest_time_to_clear(n, roads, save_points, boss_towns):
    try:
        # create graph
        graph = [[] for _ in range(n + 1)]
        for u, v, t in roads:
            graph[u].append((t, v))
            graph[v].append((t, u))
            
        # shortest path from town 1 to all towns
        dfstart = dijkstra(graph, 1, n)
        
        if all(dfstart[boss] == sys.maxsize for boss in boss_towns):
            # print("no possible patho to reach all boss towns")
            return sys.maxsize
        
        # shortest path from save points to all towns
        dfsaves = []
        for save_point in save_points:
            dfsaves.append(dijkstra(graph, save_point, n))
            
        # shortest path to defeat bosses
        mt = 0
        for b in boss_towns:
            mtb = sys.maxsize
            for i, save_point in enumerate(save_points):
                if dfstart[save_point] == sys.maxsize or dfsaves[i][b] == sys.maxsize:
                    # no valid path found to boss town via save point
                    continue
                
                t = dfstart[save_point] + dfsaves[i][b]
                mtb = min(mtb, t)
                
            if mtb == sys.maxsize:
                return sys.maxsize

            mt += mtb
    
        return mt
    except Exception as e:
        # print(f"Error in calculating shortest time: {e}")
        pass
    

### main function

n, m, b, s, boss_towns, save_points, roads = read_input()

result = shortest_time_to_clear(n, roads, save_points, boss_towns)
print(result)
