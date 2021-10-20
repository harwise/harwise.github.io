---
layout: default
title: C++ auto
---

*Effective Modern C++ Chapter 2*

* Avoid uninitialized variables.
   * `auto x; // error! initializer required`
* How to declare a local variable whose type is that of a closure?
   * It is different from `std::function` which is generally bigger and slower.
* Use explicitly typed initializer idiom to force `auto` to deduce the type you want it to have.
   * `int index = static_cast<int>(d * c.size());`
   * "Invisible" proxy types.

## "Invisible" proxy types
```
std::vector<bool> features(const Widget& w);
// bool highPriority = feature(w)[5];
auto highPriority = static_cast<bool>(feature(w)[5]); // explicitly cast std::vector<bool>::reference to bool
```
```
auto sum = static_cast<Matrix>(m1 + m2 + m3 + m4);    // explicitly cast Sum<Matrix, Matrix> to Matrix
```
