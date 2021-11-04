---
layout: default
title: C++ noexcept
---

*Effective Modern C++ Chapter 3*

* C++98-style exception specifications remain valid, but they're deprecated.
   * Most programmers ultimately decided that C++98 exception specifications weren't worth the trouble.
* C++98 style `throw()` is less optimizable because of call stack unwinding.

1. `move` operations.
   * std::vector::push_back's strong exception safety guarantee: if an exception was thrown during the copying of the elements, the state of the std::vector remained unchanged.
   * To optimize by replacing the copying of elements with moves, elements' move operations must be `noexcept`.

2. `swap`.
   * Is a key component of many STL algorithm implementations.
   * Is commonly employed in copy assignment operators.
   * *conditionally noexcept*.
      ```
      template <class T1, class T2>
      struct pair {
         void swap(pair& p) noexcept(noexcept(swap(first, p.first)) &&
                                    noexcept(swap(second, p.second)));
      };
      ```
3. memory de-allocation functions.
   * `operator delete, operator delete[]`
   * They are noexcept by default.

4. destructors.
   * They are noexcept by default.
   * `noexcept(false)` destructors are **uncommon**, and there are **none** in the Standard Library. If the destructor for an object being used by the Standard Library emits an exception, the behavior of the program is undefined.

* Most functions are exception-neutral. Such functions throw no exceptions themselves, but functions they call might emit one. They are never `noexcept`.
* Library designers who distinguish wide from narrow contracts generally reserve noexcept for functions with wide contracts.
   * These functions may check for precondition violations and throw exceptions.