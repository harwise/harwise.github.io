---
layout: default
title: C++ Type Deduction
---

*Effective Modern C++ Chapter 1*
# Template Type Deduction

## Mainstream

```
template<typename T>
void f(ParamType param);
```
```
f(expr)
```

During complication, compilers use *expr* to deduce two types: one for *T* and ont for *ParamType*.

The type deduced for T is dependent not just on the type of *expr*, but also on the form of *ParamType*.

* *ParamType* is a pointer or reference type, but not a universal reference.
  1. If *expr*'s type is a reference, ignore the reference part.
  2. Then pattern-match *expr*'s type against *ParamType* to determine *T*. (pattern-match: 看`void f(T& param)`中的T应该是什么，才能让`f(expr)`编译通过)

* *ParamType* is a universal reference. （Universal reference is like `template<typename T> void f(T&& param)`)
  1. If *expr* is an lvalue, both *T* and *ParamType* are deduced to be lvalue references.
    * This is the only situation in template type deduction where *T* is deduced to be a reference.
    * Although *ParamType* is declared using the syntax for an rvalue reference, its deduced type is an lvalue reference.
  2. If *expr* is an rvlaue, the "normal" rules (i.e., Case 1) apply.

* *ParamType* is neither a pointer nor a reference.
  1. As before, if *expr*'s type is a reference (**reference, not include pointer**), ignore the reference part.
  2. If, after ignoring *expr*'s reference-ness, *expr* is const/volatile, ignore that, too.

Reference-ness：
* 写模板的时候通过`ParamType`的写法来决定，需要的参数是不是引用。
* Universal reference情况下，调用者`expr`是lvalue还是rvalue会被捕获在`T`中。
* 非universal reference情况下，调用者`expr`中的引用会被完全忽略掉。

CV：
* 写模板的时候通过`ParamType`的写法来决定，需要的CV形式。
* `ParamType`是引用或指针的时候，`expr`中的CV需要保留。因为要保持原来变量的const-ness。
* `ParamType`不是引用或指针的时候，`expr`中的CV会被完全忽略掉。因为值传递不关心原来变量的CV。

T的推导：
* 实际上我们很少关心T具体是什么，我们更多关注的是`ParamType`是什么。（使用`auto`时，这一点体现得更加明显。）
* `T`应该是什么，是由`ParamType`和`expr`做match来决定的。
* 除了universal reference的情况，`T`不可能是reference。
* CV如果没match到`ParamType`上，就会被捕捉到`T`中。

## Array Arguments

*Array decays to pointer*
```
template<typename T>
void f(T param)
```
```
const char name[] = "J. P. Briggs";
f(name)
```
`T` is deduced to be `const char*`.

*Although functions can't declare parameters that a truly arrays, they can declare parameters that are **references** to arrays.*
```
template <typename T>
void f(T& param)
```
```
const char name[] = "J. P. Briggs";
f(name)
```
`T` is deduced `const char [13]`, and `param`'s type is `const char (&)[13]` (a reference to the array).

So, we can:
```
template<typename T, std::size_t N>
constexpr std::size_t arraySize(T (&)[N]) noexcept
{
   return N;
}
```
> Of course, prefer a `std::array` to a built-in array.

## Function Arguments

*Like arrays decay into pointers, function types can decay into function pointers.*

```
void someFunc(int, double);

template<typename T>
void f1(T param);

template<typename T>
void f2(T& param);

f1(someFunc);  // param's type is void (*)(int, double)
f2(someFunc);  // param's type is void (&)(int, double)
```

## `auto` Type Deduction

```
template<typename T>
void f(ParamType param);
f(arguments)
```

* T -> auto
* ParamType -> type specifier
* argument -> rhs expression

```
auto x = 27;
const auto cx = x;
const auto& rx = x;

template <typename T>
void func_for_x(T param);
func_for_x(27);

template <typename T>
void func_for_cx(const T param);
func_for_cx(x);

template <typename T>
void func_for_rx(const T& param);
func_for_rx(x);
```

But only with one **exception**:

```
auto x3 = { 27 };
auto x4{ 27 };
```

The deduced type (i.e. `T` or `auto`) is `std::initializer_list<int>`.

`auto` assumes that a braced initializer represents a `std::initializer_list`, but template type deduction doesn't.

```
template <typename T>
void f(T param);
f({ 11, 23, 9})      // compiling error! can't deduce type for T
```
```
template <typename T>
void f(std::initializer_list<T> initList);
f({ 11, 23, 9})      // T deduced as in
```

But, `auto` return and `auto` parameter type employ *template type deduction*.

```
auto createInitList()
{
   return {1, 2, 3};    // error: can't deduce type for {1, 2, 3}
}

std::vector<int> ;
auto resetV = [&v](const auto& newValue) {v = newValue};
resetV({1, 2, 3});      // error: can't deduce type for {1, 2, 3}
```
