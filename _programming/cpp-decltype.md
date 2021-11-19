---
layout: default
title: C++ decltype
---

*Effective Modern C++ Chapter 1*

*In C++11, perhaps the primary use for `decltype` is declaring function templates where the function's return type depends on its parameter types.*

## decltype

* Applying `decltype` to a name yields the declared type for that name. (Notice that names themselves are lvalue expressions.)
* For lvalue expressions other than names, `decltype` ensures that the type reported is always an lvalue **reference**.

```
int x = 0;
decltype(x);   // int
decltype((x)); // int&
```

## decltype(auto)

```
Widget w;
const Widget& cw = w;
auto myWidget1 = cw;             // Widget
decltype(auto) myWidget2 = cw;   // const Widget&
```

```
template <typename Container, typename Index>
decltype(auto)
authAndAccess(Container&& c, Index i)
{
   authenticateUser();
   return std::forward<Container>(c)[i];
}
```
* The return type is `decltype(auto)`, but not `auto`. The latter `auto` is problematic because the reference part of the type is lost.
* `Container&&` is used because that supports both lvalue reference and rvalue reference. (i.e. universal reference)
