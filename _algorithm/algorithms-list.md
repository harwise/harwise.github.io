---
layout: default
title: Problem Solving Strategies
---

{% include katex.html %}

* Kruskal's             - MST                                                   [ Greedy ]
* Prim's                - MST                                                   [ Greedy ]

* Dijkstra's            - SSSP
* Bellman-Ford's        - SSSP                                                  [DP + 全局扩散]

* Floyd-Warshall's      - APSP


* Ford-Fulkerson's method   - MaxFlow
* EK: Edmonds-karp's        - MaxFlow
* Dinic's                   - MaxFlow

* EK + Bellman-Ford         - MCMF



* Kahn's                - Topological Sort; DAG Cycle Detection                 [Greedy, pick any one of indegree=0]
* DFS Topological sort  - Topological Sort; DAG Cycle Detection                 [DFS + stack]
* Kosaraju's            - SCC Meta Graph; Its Topological Sort                  [DFS + stack -> Reverse Edge -> DFS/BFS]



* Needleman-Wunsch's    - String (Global) Alignment; Longest Common Subsequence  [ DP ]
* Smith-Waterman's      - String (Local) Alignment                              