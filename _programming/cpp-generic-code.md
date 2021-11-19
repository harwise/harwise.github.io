---
layout: default
title: C++ generic code
---

*Effective Modern C++ Chapter 3*

* In maximally generic code, prefer non-member versions of `begin`, `end`, `cbegin`, etc., over their member function counterparts.
   * 所有就能理解为什么会有那么多non-member functions了。
   * std::to_string
   * std::swap, std::sort
   * std::lower_bound, std::upper_bound, std::binary_search

* Tag Dispatch
   * It's a standard building block of template metaprogramming, and the more you look at code inside contemporary C++ libraries, the more often you'll encounter it.
   


