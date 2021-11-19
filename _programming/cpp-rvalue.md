---
layout: default
title: C++ rvalue
---

*Effective Modern C++ Chapter 5*

* Move-only types.
   * `std::unique_ptr`
   * `std::promise`
   * `std::future`
   * `std::thread`

* A parameter is always an lvalue, even if its type is an rvalue reference.
   ```
   void f(Widget&& w);
   ```

* `std::move` performs an unconditional cast to an rvalue. In and of itself, it doesn't mov anything.
* `std::forward` casts its argument to an rvalue only if that argument is bound to an rvalue.
   * When the parameter is a universal reference, and
   * When an argument is passed to a template function, the type deduced for the template parameter encodes whether the argument is an lvalue or an rvalue.
   * i.e.
      ```
      template<typename T> void f(T&& param);
      f(expr);
      ```
      If *expr* is an lvalue, both *T* and *ParamType* are deduced to be lvalue references. This is the only situation in template type deduction where *T* is deduced to be a reference.

* reference collapsing
   * template instantiation
   * auto type generation
      ```
      auto&& w1 = w;
      ```
   * typedefs and alias declarations
      ```
      typedef T&& universalReftoT;
      ```
   * decltype

* universal reference
   * must have the correct form (T&&)
   * type deduction must take place

* Universal reference is better than overloads of different parameters.
   * better scalability.
   * more efficient. e.g. we can pass a sting literal (i.e. const char*) and forward it to the last stage, instead of constructing a temporary std::string.

* Apply std::move to rvalue reference the last time it is used.
* Apply std::forward to universal reference the last time it is used.
* Do the same thing for rvalue references and universal references being returned from functions that **return by value**.
* Never apply std::move or std::forward to local objects if they would otherwise be eligible for the return value optimization (RVO).
   1. return by value.
   2. the type of the local object is **exactly** the same as that returned by the function.
   3. the local object is what's being returned.
   * copy elision:
      * most local variables.
      * temporary objects created as part of a return statement.
      * Function parameters don't qualify.
   * If the conditions for the RVO are met, but compilers choose not to perform copy elision, the object being returned *must be treated as an rvalue*.
      * 对于function parameter作为返回值的情况，考虑到在call stack上的位置，无法做到copy elision，所以只能走后面这条优化的路了。

* Universal Reference
   * Functions taking universal references are the greediest functions in C++. They instantiate to create exact matches for almost any type of argument. This is why combining overloading and universal references is almost always a bad idea.
   * An easy way to topple into this pit is to write a perfect forwarding ctor.

* If we have to combine Universal Reference and overloading, consider:
   * *tag dispatch*
   * *std::enable_if*
      * *tag dispatch* can't work for perfect-forwarding ctors. Compilers may generate copy and move ctors.
      * It can force compilers to behave as if a particular template didn't exist.
      * SFINAE
      * std::is_same
      * std::is_base_of
      * std::decay: strip any references and cv-qualifiers. (And turns arrays and functions into pointers.)
      ```
      class Person {
      public:
         template<
            typename T,
            typename = typename std::enable_if_t<
                           !std::is_base_of_v<Person,
                                              typename std::decay_t<T>>
                       >
         >
      }
      ```

* Move is not necessary better than Copy.
   * No move operations.
   * Move not faster.
      * std::array. Because there is no pointer to move.
      * std::string for SSO reason (small string optimization).
   * Move not useable.
      * The context requires a move operation that emits no exceptions.

* Perfect Forwarding Failures
   * Perfect Forwarding fails when template type deduction fails or when it deduces the wrong type.
   1. Braced initializers.
      - `f({1, 2, 3})` vs. `fwd({1, 2, 3})`
      - Compilers compare the arguments at the call site to the parameters declared by f. `{1, 2, 3} `can be implicitly converted to a `std::vector<int>` object.
      - A *braced initializer* must not be deduced as a `std::initializer_list` unless the function template parameter is declared to be `std::initializer_list`.
      - Make it explicitly a `std::initializer_list`: `auto il = {1, 2, 3}`.
   2. 0 or NULL as nullptr.
   3. Declaration-only integral static const data members.
      - `static const int MinVals = 28;`
      - A declaration is not required because of *const propagation* on such members' values. The value 28 is plopped into all places where the variable is mentioned.
      - It is not there in the memory and we cannot get a pointer/reference, so perfect forwarding will fail at linking time.
      - Declare it. `const std::size_t Widget::MinVals;`
   4. Overloaded function names and template names.
      - Type deduction fails for not knowing which one to use.
      - `fwd(static_cast<ProcessFuncType>(workOnVal));`. It can also work for template functions.
   5. Bitfields.
      - We cannot get the address of a bitfield.
         ```
         struct IPv4Header {
            std::uint32_t  version:4,
                           IHL:4,
                           DSCP:6,
                           ECN:2,
                           totalLengtH:16;
         };
         ```
