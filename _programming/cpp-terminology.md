---
layout: default
title: C++ Terminology
---

* Statement
   * Declaration
   * Definition
* Expression

* Function Signature

* Argument
* Parameter

* Exception safe
   * basic guarantee
   * strong guarantee

* Function Object
* Callable Object
* Closure

* Template Function
* Function Template

* Default initialization
* Default constructors

* Uniform initialization (Braced initialization)

* Most vexing parse
   * `Widget w2();    // declares a function?`

* Alias Declarations
   * `using`
* Alias Templates
   * When alias declarations are templated

* Dependent Type
   * `typename MyAllocList<T>::type list; // The keyword **typename** is required`
   * With alias templates, `typename std::remove_const<T>::type` is simplified as `std::remove_const_t<T>`.

* Underlying Type

