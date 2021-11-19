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

* Literal Types
   * Types that can have values determined during compilation.
      * All built-in types except `void` qualify.
      * User-defined types may be literal, too, because ctors and other member functions may be `constexpr`.

* Special Member Functions
   * The ones that C++ is willing to generate on its own.
      * The default ctor.
      * The dtor.
      * The copy ctor.
      * The copy assignment operator.
      * The move ctor.
      * The move assignment operator.

* Dangling Pointers
* Raw Pointers
* Smart Pointers

* CRTP
   * The Curiously Recurring Template Pattern
   * A derived class inherits from a base class templatized on the derived class.

* Pimpl
   * pointer to implementation

* Incomplete Type
   * A type that has been declared, but not defined.

* RVO
   * Return Value Optimization

* Tag Dispatch
   ```
   template<typename T>
   void logAndAdd(T&& name)
   {
      /*
       * std::is_integral inherits from std::true_type or std::false_type
       * depending on the template argument.
       */
      logAndAddImpl(
         std::forward<T>(name),
         std::is_integral<typename std::remove_reference_t<T>>());
   }

   template<typename T>
   void logAndAddImpl(T&& name, std::false_type)
   {
      auto now = std::chrono::system_clock::now();
      log(now, "logAndAdd");
      names.emplace(std::forward<T>(name));
   }

   void logAndAddImpl(int idx, std::true_type)
   {
      logAndAdd(nameFromIdx(idx));
   }
   ```

* SFINAE
   * Substitution Failure Is Not A Error.

* SSO
   * small string optimization

* Braced Initializer
