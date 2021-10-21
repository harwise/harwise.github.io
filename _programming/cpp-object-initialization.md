---
layout: default
title: C++ object initialization
---

*Effective Modern C++ Chapter 3*

## Uniform initialization / braced initialization 

* Parentheses initialization cannot be used to specify *default initialization values*.
   * `class Widget { private: int z(0); };   // error!`
* Uncopyable objects (e.g. std::atomics) cannot be initialized using "=".
   * `std::atomic<int> ai3 = 0;  // error!`
* Braced initialization prohibits implicit *narrowing conversions*.
* Immunity to *most vexing parse*.
* Only if there's no way to convert the types of the arguments in a braced initializer to the type in a std::initializer_list do compilers fall back on normal overload resolution. Compilers' determination is so strong, it prevails even if the best-match std::initializer_list constructor can't be called.

```
class Widget {
public:
   Widget(int i ,bool b);
   Widget(int i ,double d);
   Widget(std::initializer_list<bool> il);
};
Widget w{10, 5.0};   // error! requires narrowing conversions
```

* But empty braces mean no arguments, not an empty std::initializer_list.
   * Use `Widget {{}}` to make it an empty std::initializer_list.

* If you're a template author, the tension between parentheses and braces for object creation can be especially frustrating, because, in general, it's not possible to know which should be used.
   * `std::make_unique` and `std::make_shared` resolve the problem by internally using parentheses and by documenting this decision as part of their interfaces.

```
template <typename T, typename... Ts>
void doSomeWork(Ts&&... params)
{
   // create local T object from params
   // option 1. 
   T localObject(std::forward<Ts>(params)...);
   // option 2.
   T localObject{std::forward<Ts>(params)...};
}

doSomeWork<std::vector<int>>(10, 20);
```
