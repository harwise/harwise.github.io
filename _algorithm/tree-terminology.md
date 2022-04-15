---
layout: default
title: Tree Terminology
---

{% include katex.html %}

* Centroid
  - node whose removal guarantees the largest remaining subtree is as small as possible.
  - a tree can have one centroid or two. For the latter, the two are next to each other.

* LCA
   - Lowest Common Ancestor.

* Dominator Trees
   - Given a graph + some node $S$
   - $V_i$ dominates $V_j$ if any path $S$-->$V_j$ has to go through $V_i$
      - When $V_i \ne V_j$, $V_i$ is called *strict dominator*.
   - *Immediate dominator*: $V_i$ is a *strict dominator* of $V_j$, and there is nothing in the middle also dominates $V_j$.
      - *Immediate dominators* are unique. (Tha is, for $V_j$, its parent is unique.)
   - All *Immediate dominators* constructs a **rooted($S$)** tree structure.

* Dominator Trees for DAGs
   - Implemented by looking for nodes' LCA
      - LCAs can be easily found by first finding the topological order.

* Binary Lifting Table
   - Binary jumping on tree

* Traversal
   - pre-order
   - post-order
   - Tree Linearization

* Euler Tour of a Tree
   - A circuit
   - DFS the tree

