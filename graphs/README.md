### **Shortest Path Algorithms**
 - **Create a Grpah**: First you have to create a graph before applying algorithms on it


Certainly! Graph algorithms are a broad field with numerous techniques for solving various types of problems. Below is a comprehensive list of graph algorithms, categorized by their primary use cases:

### **Shortest Path Algorithms**

1. **Dijkstra’s Algorithm**
   - **Purpose**: Find the shortest path from a single source to all other nodes.
   - **Complexity**: \(O((V + E) \log V)\) with a priority queue.

2. **Bellman-Ford Algorithm**
   - **Purpose**: Find the shortest path from a single source to all other nodes, handles negative weights.
   - **Complexity**: \(O(VE)\).

3. **Floyd-Warshall Algorithm**
   - **Purpose**: Find the shortest paths between all pairs of nodes.
   - **Complexity**: \(O(V^3)\).

4. **A* Search Algorithm**
   - **Purpose**: Find the shortest path from a source to a target node using heuristics.
   - **Complexity**: \(O(E)\) with a good heuristic.

5. **Johnson’s Algorithm**
   - **Purpose**: Find the shortest paths between all pairs of nodes, handles negative weights.
   - **Complexity**: \(O(V^2 \log V + VE)\).

### **Minimum Spanning Tree (MST) Algorithms**

1. **Kruskal’s Algorithm**
   - **Purpose**: Find the minimum spanning tree of a graph.
   - **Complexity**: \(O(E \log V)\) with sorting and union-find.

2. **Prim’s Algorithm**
   - **Purpose**: Find the minimum spanning tree of a graph.
   - **Complexity**: \(O(E + V \log V)\) with priority queues.

### **Network Flow Algorithms**

1. **Ford-Fulkerson Algorithm**
   - **Purpose**: Compute the maximum flow in a flow network.
   - **Complexity**: Depends on the implementation; typically \(O(E \cdot f)\) where \(f\) is the maximum flow.

2. **Edmonds-Karp Algorithm**
   - **Purpose**: An implementation of Ford-Fulkerson using BFS.
   - **Complexity**: \(O(VE^2)\).

3. **Dinic’s Algorithm**
   - **Purpose**: Compute the maximum flow in a flow network with better complexity for certain cases.
   - **Complexity**: \(O(V^2 E)\) in general, but \(O(\sqrt{V} E)\) in some cases.

4. **Push-Relabel Algorithm**
   - **Purpose**: Compute the maximum flow using a different approach than Ford-Fulkerson.
   - **Complexity**: \(O(V^3)\).

### **Graph Traversal Algorithms**

1. **Breadth-First Search (BFS)**
   - **Purpose**: Traverse or search through a graph level by level.
   - **Complexity**: \(O(V + E)\).

2. **Depth-First Search (DFS)**
   - **Purpose**: Traverse or search through a graph by going as deep as possible.
   - **Complexity**: \(O(V + E)\).

3. **Topological Sort**
   - **Purpose**: Order nodes in a Directed Acyclic Graph (DAG) such that for every directed edge \(u \to v\), node \(u\) comes before \(v\).
   - **Complexity**: \(O(V + E)\).

### **Strongly Connected Components (SCC) Algorithms**

1. **Kosaraju’s Algorithm**
   - **Purpose**: Find all strongly connected components in a directed graph.
   - **Complexity**: \(O(V + E)\).

2. **Tarjan’s Algorithm**
   - **Purpose**: Find all strongly connected components in a directed graph.
   - **Complexity**: \(O(V + E)\).

### **Graph Coloring Algorithms**

1. **Greedy Coloring**
   - **Purpose**: Assign colors to nodes such that no two adjacent nodes share the same color, using a greedy approach.
   - **Complexity**: Depends on the implementation.

2. **Backtracking Algorithm**
   - **Purpose**: Assign colors to nodes with backtracking to ensure a valid coloring.
   - **Complexity**: Typically exponential in the worst case.

### **Cycle Detection Algorithms**

1. **Floyd-Warshall Cycle Detection**
   - **Purpose**: Detect negative weight cycles in a graph.
   - **Complexity**: \(O(V^3)\).

2. **DFS-Based Cycle Detection**
   - **Purpose**: Detect cycles in a directed or undirected graph using DFS.
   - **Complexity**: \(O(V + E)\).

### **Miscellaneous Algorithms**

1. **Eulerian Path and Circuit Algorithms**
   - **Purpose**: Find an Eulerian path or circuit (a path that visits every edge exactly once).
   - **Complexity**: Depends on the implementation.

2. **Hamiltonian Path and Circuit Algorithms**
   - **Purpose**: Find a Hamiltonian path or circuit (a path that visits every vertex exactly once).
   - **Complexity**: Typically exponential due to the problem's complexity.

3. **Articulation Points and Bridges**
   - **Purpose**: Find articulation points (nodes that, if removed, increase the number of connected components) and bridges (edges that, if removed, increase the number of connected components).
   - **Complexity**: \(O(V + E)\).

4. **Chinese Postman Problem**
   - **Purpose**: Find the shortest path that visits every edge of a graph at least once.
   - **Complexity**: Depends on the implementation.

5. **Traveling Salesman Problem (TSP)**
   - **Purpose**: Find the shortest possible route that visits each city once and returns to the origin city.
   - **Complexity**: NP-hard; exact algorithms are exponential in time complexity.

### **Summary**

- **Shortest Path**: Dijkstra’s, Bellman-Ford, Floyd-Warshall, A*, Johnson’s.
- **MST**: Kruskal’s, Prim’s.
- **Network Flow**: Ford-Fulkerson, Edmonds-Karp, Dinic’s, Push-Relabel.
- **Traversal**: BFS, DFS, Topological Sort.
- **SCC**: Kosaraju’s, Tarjan’s.
- **Coloring**: Greedy, Backtracking.
- **Cycle Detection**: Floyd-Warshall, DFS-based.
- **Miscellaneous**: Eulerian Path/Circuit, Hamiltonian Path/Circuit, Articulation Points/Bridges, Chinese Postman Problem, TSP.
