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

以上是先从`ParamType`的角度看，分为了三类；如果先从`expr`的角度看，规则看起来更清楚：
* `expr`'s reference-ness is ignored.
* `expr`'s cv is ignored if ParamType is not a pointer/reference.
* When deducing types for universal reference parameters, lvalue arguments get special treatment.

背后的原因：
* T 应该是什么，是由ParamType期望的效果来决定的。

* ParamType的reference-ness 主要由函数模板的写法（即ParamType）决定；其次在universal reference情况下看调用者（即expr）是lvalue还是rvalue。
  * 如果paramType不是引用，那么它期望的是值传递。
  * 如果paramType是普通引用，那么它期望的是普通引用传递。
  * 如果paramType是universal reference，那么它期望的是也是引用传递。但引用类型（lvalue or rvalue）由expr决定。

* ParamType的cv 主要由函数模板的写法（即ParamType）决定；其次在调用者（即expr）是引用和指针的情况下，expr的cv不能忽略。
  * 如果paramType不是引用或指针，那么expr的cv对于函数模板来说没有意义，所以cv被忽略。
  * 如果paramType是引用或指针，那么expr的cv不能忽略。


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
