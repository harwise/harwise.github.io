---
layout: default
title: Graph Terminology
---

{% include katex.html %}

* MST
   - minimum spanning tree

* Circuits
   - Circuit is a closed trail. 
   - These can have repeated vertices only.

* Cut Vertex / Articulation Points
   - make the graph disconnected
   - O(V+E). DFS + store the lowlink value at each node/subtree; and a special case for the root node.
      - lowlink: how far up the tree can I get using back edges from the subtree.

* Cut Edge / Bridges
   - make the graph disconnected.
   - every edge in a tree is a bridge.
   - O(V+E). DFS + store the lowlink value at each node/subtree.
      - lowlink: how far up the tree can I get using back edges from the subtree.

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

* Bipartite
   * iff. 2-colorable
   * iff. no odd cycles

* Strongly Connected components (on directed graphs)
   * There are paths fomr i->j and j->i for every (i,j) node pair.
   * Warshall's transitive closure.    O(V^3)
   * |V| DFS's.                        O(V(V+E))
   * Kosaraju (2 DFS)                  O(V+E)
   * Tarjan (use stacks)(lowlink DFS)
   * Gabow (use stacks)

   SCC Decomposition
   * a DAG
   * With Tarjan algorithm, the DAG is topology sorted.

   