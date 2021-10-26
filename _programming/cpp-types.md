---
layout: default
title: C++ types
---

*Effective Modern C++ Chapter 3*

# nullptr

* `nullptr`'s actual type is `std::nullptr_t`, which implicitly converts to all raw pointer types, and that's what makes `nullptr` act as if it were a pointer of all types.
* 0 or NULL is treated as integers in template type deduction.

