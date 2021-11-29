---
layout: default
title: C++ Function Parameters
---

## Pass by value

* In general, don't pass by value.
* But for a always copied parameter, pass by value may be better.
   * When:
      * Both lvalue and rvalue arguments are supported.
      * If it is *always* copied (moved or copied), we can just do the copy at passing the argument.
      * It is should be cheap to move. Because there is an extra move for both lvalue and rvalue cases compared to the pass-by-reference approach.
      * For types that holds values in dynamically allocated memory, in the lvalue case, there may be a big difference. Examples include `std::string` and `std::vector`.
         - pass by reference. Copying a smaller A to a bigger B doesn't need memory reallocation.
         - pass by value. Another smaller A is allocated and B is deallocated.
   * Benefits:
      * Easier to implement.
      * Less object code. Both lvalue and rvalue arguments can be handled.

## Pass by reference

* lvalue reference

* rvalue reference
   * For rvalue arguments, moves almost always suffice.
   * For move-only types.

* overloading
   * Supports both lvalue and rvalue.
   * But more object code.

## Universal reference
   * Uniquely efficient.
   * Bloated header file.
   * Odd failure cases.

