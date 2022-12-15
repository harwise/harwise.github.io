---
layout: default
title: Graph Terminology
---

{% include katex.html %}

# Basic

* Vertices/Nodes
* Edges
* Un/Weighted
* Un/Directed
* In/Out Degree
* Simple Graph
* Multigraph
   * Self-Loop
   * Multiple Edges
* Sparse/Dense
* Path
* Cycle
* Isolated/Reachable Vertices
* Sub-Graph
* Complete Graph: there is an edge for any pair of vertices.
* Tree/Forest
* Spanning Tree
* Euler Path/Cycle
* Hamiltonian Path/Cycle
* Bipartite Graph
   * 2/bi-colorable


* [Directed Graph] DAG: Directed Acyclic Graph
* [DAG] Topological Sort 


* [Directed Graph] SCC: (Strongly) Connected Component
* [Undirected Graph] Connected Component
* [Mostly for Undirected Graph] Cut Vertex/Articulation Points
   * Biconnected Graph: a Graph without any articulation point.
* [Mostly for Undirected Graph] Cut Edges/Bridges

* [Bipartite Graph] MCBM: Max Cardinality Bipartite Matching

* Graph Matching
   * Perfecct Matching: MCM and no vertex is left unmatched.

* MPC: Minimum Path Cover
   * DAG (via converting to a bipartite graph)

* Maximum number of independent paths (from s to t)
   * independent: they don't share any vertex apart from s and t.

* Maximum number of edge-disjoint paths (from s to t)
   * edge-disjoint: they don't share any edge.

* DP on Tree
   * Trees are turned into DAGs if we attach one (or more) parameter(s) to each vertex of the tree. DAGs are naturally solvable with DP.

||Minimm Vertex Cover|Maximum Independent Set|Weighted MIS
|-|-|-|-
||用顶点来覆盖图中的所有边|两两不相连的顶点的集合|
||Complement of IS|Complement of VC|
|Graph|NP-Complete|Complete Search with bitmask (V<=60)|HARD
|Tree|DP on Tree, $O(V)$ ||DP, $O(V)$
|Bipartite|MCBM, $O(VE)$||Max Flow, Dinic $O(VVE)$|

<br>

||Minimum Edge Cover|Maximum Cardinality Matching|Weighted MCM
|-|-|-|-
||用边来覆盖图中所有顶点|不具有公共端点的边的集合|
||对于不存在孤立点的图, 最大匹配+最小边覆盖=顶点数|
||A smallest edge cover can be found in polynomial time by finding a maximum matching and extending it greedily so that all vertices are covered.|可以由最小边覆盖求得，对于最小边覆盖中每对有公共点的边删去其中一条
|Graph||(Edmond's) blossom algorithm, $O(VVE)$|DP with bitmask, $O(VV2^V)$
|Bipartite||MCBM, $O(VE)$|Min Cost (Max) Flow, $O(VVEE)$

<br>

||Minimum Path Cover|
|-|-|
||用path来覆盖图中所有顶点|
|Graph|NP-Complete|
|DAG|MCBM, $O(VE)$|


# Graph Traversal

* DFS
   * DFS_WHITE 未访问
   * DFS_BLACK 已（开始）访问
* BFS

## DAG

* Topological Sort (of a DAG)
   * DFS: 所有子节点都都处理完毕后，再添加当前节点到List中。最后reverse一下List。
   * BFS: 从队列头移除节点的时候，添加到List中。

## Bipartite

* Bipartite Graph Check
   * iff. 2-colorable
   * iff. no odd cycles
   * DFS/BFS：检查每一个edge连接的vertices是不同颜色的。

## Advanced DFS

* Vertex Color
   * DFS_WHITE 未访问
   * DFS_GRAY 已开始访问还未结束
   * DFS_BLACK 已结束访问

* Graph Edge Property
   * Tree Edges: DFS_GRAY to DFS_WHITE
   * Back Edges: DFS_GRAY to DFS_GRAY
      * bi-directional edges should be filered out.
   * Forward/Cross Edges: DFS_GRAY o DFS_BLACK (如果无向图的边不看做双向两条边的话，是不存在这一类型的。)

* Vertex Numbering
   * 比标色更进一步，标记访问序号。
   * dfs_num 在DFS spanning tree中，被访问到的序号。
   * dfs_low 在DFS spanning tree中，能够连到的最小序号（子节点的Back Edges可能会通向更小的序号）。


## Connected Components

* [Undirected Graph] Finding Connected Components
   * Simple DFS
   * Flood Fill - Labeling/Coloring the Connected Components (especially implicit graph)

* [Undirected Graph] Finding Articulation Points and Bridges
   * DFS; O(V+E)
   * Vertex Numbering.
   * Articulation Points：我的子节点最多只能连到我。所以我要是去掉的话，我的子节点们就无法连回去了。
   * Bridges：我的子节点连我都连不到。所以我的这条边去掉的话，我的子节点们就无法连回去了。

* [Directed Graph] SCC
   * There are paths fomr i->j and j->i for every (i,j) node pair.
   * SCC Decomposition - a DAG
   * Warshall's transitive closure.    O(V^3)
   * Tarjan's.
      * DFS; O(V+E)
      * Vertex Numbering.
      * SCC Root在DFS spanning tree的中进行dfs_low标号。我能访问到的最小序号，是我自己。
   * Kosaraju's.
      *  DFS; O(V+E)
      1. DFS，最后标记(post-order标记)的节点一定是包含在DAG中的Source SCC中。（如果在别的SCC中，无论是否是先从它开始，它都不会有最大的post-order)
      2. 反转图(transpose)
      3. 反转后，Source变成了Sink，在Sink中做DFS，得到的就是这个Sink的SCC。
   * Gabow (use stacks)

# MST - Minimum Spanning Tree

* Kruskal's
   * O(E*logV)
* Prim's
   * O(E*logV)
* Minimax/Maximin
   * The minimax path solution is the maximum edge weight along the unique path between i and j in this MST.

# SSSP - Single-Source Shortest Path

* BFS - unweighted graph
   * O(V+E)
* Dijkstra's - weighted graph
   * O(V+E*logV)
* Bellman Ford's - graph with negative weight cycle
   * O(V*E)

# APSP - All-Pairs Shortest Path

* Floyd Warshall's
   * O(V^3) - have to use Adjacent Matrix

# Maximum Flow

* Ford Fulkerson's Method

* Ford Fulkerson's Method with DFS
   * O(f*E) where f is the Max Flow value.

* EK: Edmonds Karp's
   * Ford Fulkerson's Method with BFS
   * O(VEE) (at most O(VE) BFS iterations.)

* Dinic's
   * Ford Fulkerson's Method BFS + DFS
   * O(VVE)

* MCMF - Min Cost (Max) Flow
   * Ford Fulkerson's Method Bellman Ford's
   * 按照cost最小寻找 augmenting path.
   * 由于反向边的cost是负数，所以要求找 augmenting path 的算法能处理weight<0的边。
   * O(VE*VE)









* Circuits
   - Circuit is a closed trail. 
   - These can have repeated vertices only.

* K-vertex-connected

   Properties
   1. The graph has more than k vertices.
   2. The graph remains connected if fewer than k vertices are removed.

* 2-vertex-connected components / bi-connected components / blocks  
   Maximal subset of E s.t. induced subgraph is 2-vertex-connected.  
   Alt Def: all pairs of edges have two vertex-distinct paths. (form cycles)

   Biconnected Vertex Decompositions can be a tree
   * 2VCC -> node
   * CV -> node
   * 2VCC<->CV -> edge

* 2-edge-connected components  
   Maximal subset of V s.t. induced subgraph is 2-edge-connected.
   Alt Def: all pairs of vertices have two edge-distinct paths. (form circuits)

   Biconnected Edge Decompositions is a tree
   * 2ECC -> node
   * bridge -> edge

* Hamiltonian tour
   A cycle in a undirected graph that visits each vertex exactly once.

* TSP - Traveling Salesman Problem
   Find the Hamiltonian tour of the minimum cost.

