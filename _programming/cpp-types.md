---
layout: default
title: C++ types
---

*Effective Modern C++ Chapter 3*

## nullptr

* `nullptr`'s actual type is `std::nullptr_t`, which implicitly converts to all raw pointer types, and that's what makes `nullptr` act as if it were a pointer of all types.
* 0 or NULL is treated as integers in template type deduction.

## scoped enum & unscoped enum

* Unscoped enums implicitly convert to integral types. Scoped enums are strongly typed.
* The *underlying type* of unscoped enum is determined by compilers, based on its range of values. That leads to that *forward declaration* is forbidden. The *underlying type* of a scoped enum is always known (*the default is int*).
* *Underlying type specifications* can be used for both scoped and unscoped enums.
   * `enum Color: std::uint8_t`. So it can be forward-declared.
   * `enum class Color: std::uint32_t`

## std::literals

* Don't forget `using namespace std::literals`.
* s:second, ms:millisecond, us:microsecond, h:hour.

## Move-only types.

* `std::unique_ptr`
* `std::promise`
* `std::future`
* `std::thread`

## Non-Move & Non-Copy types.

* `std::atomic`
