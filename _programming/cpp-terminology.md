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

* Overload
* Override

* Reference Qualifiers
   ```
   class Widget {
      public:
         using DataType = std::vector<double>;
         DataType& data() &
         { return values; }
         DataType data() &&
         { return std::move(values); }
      private:
         DataType values;
   }
   ```

* Contextual Keywords
   * They are reversed only in certain contexts.
   * `override`
   * `final`

* Call Stack Unwinding

* Functions with Wide Contracts
   * Has no preconditions.
   * Can be called regardless of the state of the program.
   * Imposes no constrains on the arguments the callers pass it.
* Functions Narrow Contracts
   * If a precondition is violated, results are undefined.


