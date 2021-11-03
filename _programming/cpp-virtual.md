---
layout: default
title: C++ virtual
---

*Effective Modern C++ Chapter 3*

For overriding to occur, several acquirements must be met:

* The base class function must be virtual.
* Functions names must be identical. (except in the case of destructors.)
* The parameter types must be identical.
* The constness must be identical.
* The *reference qualifiers* must be identical.
* The return type and exception specifications must be **compatible**.


