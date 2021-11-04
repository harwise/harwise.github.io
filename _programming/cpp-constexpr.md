---
layout: default
title: C++ constexpr
---

*Effective Modern C++ Chapter 3*

* Values known during compilation are privileged.
   * They may be placed in read-only memory, which may be a feature of considerable importance.
   * Integral values can be used in contexts where C++ requires an *integral constant expression*. 
      * array sizes.
      * integral template arguments.
      * enumerator values.
      * alignment specifiers.

* `constexpr` functions produce compile-time constants *when they are called with compile-time constants*.
* `constexpr` functions are limited to taking and returning *literal types*.

* By using `constexpr` whenever possible, you maximize the range of situations in which your objects and functions may be used.

