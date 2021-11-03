---
layout: default
title: C++ deleted functions
---

*Effective Modern C++ Chapter 3*

* Deleted methods should be `public` for better compiling messages.
* Deleted functions don't have to be member functions.

```
// C++'s C heritage means that pretty much any type that can be viewed as vaguely numerical will implicitly convert to int.
bool isLucky(int number);
bool isLucky(char) = delete;
```

* Prevents use of template instantiations that should be disabled.

```
template <typename T>
void processPointer(T* ptr);

template <>
void processPointer<void>(T* ptr) = delete;
```

* To disable some instantiations of a function template inside a class, declaring them `private` is not going to work. The problem is that template specializations must be written at namespace scope, not class scope. (So, how to make them private outside the class scope?) But `delete` can work.

```
template<>
void Widget::processPointer<void>(void*) = delete;
```
