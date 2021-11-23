---
layout: default
title: C++ lambda
---

*Effective Modern C++ Chapter 6*

* Objects with static storage duration. Such objects are defined at global or namespace scope or are declared static inside classes, functions, or files. These Objects can be used inside lambdas, but they can't be captured.

* By default, the operator() member function inside the closure class generated from a lambda is const. (That means, the captured variables cannot be modified.) But a lambda can be declared `mutable`.

## *Init Capture* (*Generalized lambda capture*)

* Moving objects into closures.  
   ```
   auto func = [pw = std::move(pw)] {
      return pw->isValidated() && pw->isArchived();
   }
   ```
   The scope on the left of the '=' is that of the closure class. (closure class data member.)  
   The scope on the right is the same as where the lambda is being defined.

* *init capture* can be emulated via std::bind.
   * The arguments to bind are copied or moved, and are never passed by reference unless wrapped in std::ref or std::cref.
   * All arguments passed to bind objects are passed by reference, because the function call operator for such objects uses perfect forwarding.
   * A bind object contains copies of all the arguments passed to std::bind. We can make it move-constructed.

* Use `decltype` on auto&& parameters to std::forward them.  
   Instantiating std::forward with an rvalue reference type yields the same result as instantiating it with a non-reference type.
   ```
   auto f = 
      [](auto&&...params)
      {
         return func(normalize(std::forward<decltype(params)>(params)...));
      }
   ```

* Lambdas are more readable, more expressive, and may be more efficient than using std::bind.

* Lambdas with an auto parameter.
   ```
   auto boundPW = [pw](const auto& param) {
      pw(param);
   };

   // operator() is templatized.
   boundPW(1930);
   boundPW(nullptr);
   boundPW("Rosebud");
   ```

