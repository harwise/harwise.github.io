---
layout: default
title: C++ Terminology
---

Initialization & Constructor
---

* Default initialization
   * T object;
   * new T;
   * A base class or a non-static data member is not mentioned in a constructor initializer list.

   This is the initialization performed when an object is constructed with no initializer.

   * static and thread-local objects get zero initialized.
   * if T is an array type: every element of the array is default-initialized.
   * non-POD: one of the default constructors is called.
   * otherwise, no initialization is performed.

* Default constructors\
   A constructor that can be called without having to provide any arguments, irrespective of whether the constructor is auto-generated or user-defined. Note that a constructor with formal parameters can still be called without arguments if default arguments were provided in the constructor's definition.
   
   * A trivial default constructor is a constructor that performs no action. All data types compatible with the C language (POD types) are trivially default-constructible.

* Zero-initialization\
   * Variables with static or thread-local (since C++11) storage duration.
   * **value-initialization** of types that have no constructors (e.g. POD).
   * When an array of any character type is initialized with a string literal that is too short, the remainder of the array is zero-initialized.

* Uniform initialization: Braced initialization.

---

* direct initialization  
   * std::regex r2(nullptr);
   * explicit constructors can be used.

* copy initialization: Initializes an object from another object.
   * std::regex r1 = nullptr;
   * explicit constructors are not permitted to use.

Copy-initialization is less permissive than direct-initialization: explicit constructors are not converting constructors and are not considered for copy-initialization.

---

Thread
------

* Thread-based programming
* Task-based programming

* Hardware Threads  
   Contemporary machine architectures offer one or more hardware threads per CPU core.
* Software Threads  
   OS threads or system threads.
* std::threads  
   Handles to underlying software threads. Some std::thread objects represent "null" handles.
* Oversubscription  
   There are more ready-to-run software threads than hardware threads.  
   Context Switch can be costly. (CPU caches.)

---

Meta Programming
----------------
* Template Function
* Function Template

* Tag Dispatch
   * C++17 `if constexpr` supersedes tag dispatch in almost every situation and we're using it in new C++17-and-later code.\
      Note: Tag dispatch works with delegating constructors, whereas if constexpr works only in function bodies.

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
```
class MyTest
{
public:

   template<class T>
   static constexpr bool something_possible(T&&)
   {
      return std::is_same<std::decay_t<T>, std::uint64_t>();
   }

   template<typename T>
   void do_something(T value)
   {
      // switch behaviour on result of constexpr predicate    
      if constexpr (something_possible(value))
      {
            std::cout << "supported\n";
      }
      else 
      {
            std::cout << "not supported\n";
      }
   }
};   
```
* SFINAE: Substitution Failure Is Not An Error.
   * 而使用enable_if<>就是实现SFINAE最直接的方式。

   ```
   template<typename T>
   typename std::enable_if<(sizeof(T) > 4)>::type
   foo() {
   }

   template<typename T,
   typename = std::enable_if_t<(sizeof(T) > 4)>>
   void foo() {
   }   
   ```
   在C++中针对不同参数类型做函数重载时很常见的。编译器需要为一个调用选择一个最适合的函数。

   当这些重载函数包含模板函数时，编译器一般会执行如下步骤：

   确定模板参数类型。
   将函数参数列表和返回值的模板参数替换掉（substitute）
   根据规则决定哪一个函数最匹配。
   但是替换的结果可能是毫无意义的。这时，编译器不会报错，反而会忽略这个函数模板。

   我们将这个原则叫做：SFINAE（“substitution failure is not an error）

   但是替换(substitute)和实例化(instantiation)不一样：即使最终不需要被实例化的模板也要进行替换（不然就无法执行上面的第3步）。不过它只会替换直接出现在函数声明中的相关内容（不包含函数体）。   
   
---

Statement & Expression
----------------------

* Statement
   * Declaration
   * Definition
* Expression

   Expression: Something which evaluates to a value. Example: `1+2/x`\
   Statement: A line of code which does something. Example: `GOTO 100`\
   In C, every syntactic expression can be made into a statement just by tacking a semicolon along the end:

   ```
   1 + 2 / x;
   ```
   Similarly, in C, an expression can have side-effects—it can change something.

   ```
   1 + 2 / callfunc(12);
   ```
   
Designers of other languages didn't like this kind of duplication, and they saw early on that if expressions can have side effects as well as values, then the syntactic distinction between statements and expressions is not all that useful—so they got rid of it. Haskell, Icon, Lisp, and ML are all languages that don't have syntactic statements—they only have expressions. Even the class structured looping and conditional forms are considered expressions, and they have values—but not very interesting ones.

---

Function
--------

* Function Signature

* Call Stack Unwinding

* Argument
* Parameter

* Overload
* Override

* Exception Safe
   * basic guarantee  
      If an exception occurs, no memory is leaked and the object is still in a usable state even though the data might have been modified. (Rely on that destructors are no-fail.)
   * strong guarantee  
      If a function goes out of scope because of an exception, it will not leak memory and program state will not be modified. Either it completely succeeds or it has no effect. (Rely on that destructors are no-fail.)
   * no-fail (or no-throw) guarantee  
      The strongest guarantee that a function can provide. It states that the function will not throw an exception or allow one to propagate. 

---

* Functions with Wide Contracts
   * Has no preconditions.
   * Can be called regardless of the state of the program.
   * Imposes no constraints on the arguments the callers pass it.
* Functions with Narrow Contracts
   * If a precondition is violated, results are undefined.

Wide contract functions have well-defined behavior for all possible inputs, while narrow contracts mean that the functions can only be called when certain preconditions are met.   

For example, `std::vector<int>.size()` member function has a wide contract because it can be called on any instance of a vector (as in std::vector<int> v; /* anything can happen with v here... */; auto s = v.size(); is always valid). The `operator[](size_t index)` (as in int x = v[10]) has a narrow contract, because it can only be called with a parameter that is less than .size(), **otherwise it is undefined**. The `.at(size_t i)` member function (as in int y = v.at(10)) however has a wide contract, because **it is specified to throw an exception** when the index is out of range.

---

* Callable Objects
   * Function Objects
      * Bind Objects (function objects returned from std::bind)

A FunctionObject type is the type of an object that can be used on the left of the function call operator.

A Callable type is a type for which the INVOKE operation (used by, e.g., std::function, std::bind, and std::thread::thread) is applicable.

INVOKE(f, t1, t2, ..., tN) is defined as follows:\
if f is a pointer to member function of class T.\
otherwise, if N == 1 and f is a pointer to data member of class T.\
otherwise, f is a FunctionObject.

* Lambda Expression  
   the expression.
* Closure  
   the runtime object created by a lambda.
* Closure Class  
   the class from which a closure is instantiated. Each lambda causes compilers to generate a unique closure class.
* Init Capture = Generalized Lambda Capture

---

Member Function
---------------

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
   * They are reserved only in certain contexts.
   * `override`
   * `final`

* Special Member Functions
   * The ones that C++ is willing to generate on its own.
      * The default ctor.
      * The dtor.
      * The copy ctor.
      * The copy assignment operator.
      * The move ctor.
      * The move assignment operator.

* The Rule of Three/Five/Zero
   * If you define or =delete any default operation, define or =delete them all.

* Slicing
   * A polymorphic class should suppress public copy/move.
   * A polymorphic class is a class that defines or inherits at least one virtual function. It is likely that it will be used as a base class for other derived classes with polymorphic behavior. If it is accidentally passed by value, with the implicitly generated copy constructor and assignment, we risk slicing: only the base portion of a derived object will be copied, and the polymorphic behavior will be corrupted.
   * For making deep copies of polymorphic classes prefer a virtual clone function instead of public copy construction/assignment.

---

Structure & Layout
------------------

* POD
   * Trivial types
      * No virtual.
      * When a class or struct in C++ has compiler-provided or explicitly defaulted special member functions, then it is a trivial type. It occupies a contiguous memory area.
      * In C++, the compiler is free to choose how to order members in this situation.
      * You **can memcopy** such objects but you cannot reliably consume them from a C program.
   * Standard layout types
      * When a class or struct does not contain certain C++ language features such as virtual functions which are not found in the C language, and all members have the same access control, it is a standard-layout type.
      * It is memcopy-able and the layout is sufficiently defined that it can be **consumed by C programs**. 

```
// Trivial but not standard-layout
struct C
{
   int a;
private:
   int b;   // Different access control
};

// Standard-layout but not trivial
struct D
{
   int a;
   int b;
   D() {} //User-defined constructor
};

struct POD
{
   int a;
   int b;
};

```

Type
----
* Incomplete Type
   * A type that has been declared, but not defined.

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
   * Each enumeration type has an underlying type
   * Can be Specified explicitly (both scoped and unscoped enumerations)
   * Or Omitted, in which case it is int for scoped enumerations or an implementation-defined integral type capable of representing all values of the enum (for unscoped enumerations)

* Decay
   * C-style arrays are very basic constructs which are **not assignable, copyable or referenceable** in the way built-ins or user defined types are. 
      * In many context, an array decays into a pointer to its first element.
      * e.g. An array is passed to a template taking a by-value parameter.
      * But NOT when the parameters are references to arrays.
      
      ```
      template<typename T, std::size_t N>
      constexpr std::size_t arraySize(T (&)[N]) noexpect
      {
         return N;
      }
      ```
   * Function types can decay into function pointers.

* Literal Types
   * Types that can have values determined during compilation.
      * All built-in types except `void` qualify.
      * User-defined types may be literal, too, because ctors and other member functions may be `constexpr`.

---

Misc
----

* Dangling Pointers
* Raw Pointers
* Smart Pointers

* CRTP: the Curiously Recurring Template Pattern
   * A derived class inherits from a base class templatized on the derived class.
   * CRTP是C++模板编程时的一种惯用法（idiom）：把派生类作为基类的模板参数。更一般地被称作F-bound polymorphism。

* Pimpl: pointer to implementation

* RVO: Return Value Optimization

* SSO: small string optimization

* RMW: read-modify-write
