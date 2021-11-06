---
layout: default
title: C++ special member functions
---

*Effective Modern C++ Chapter 3*

* These functions are generated only if they're needed.
* They are public and inline.

## Rule of Three

* If you declare any of a copy ctor, copy assignment operator, or dtor, you should declare all three.
* The need to take over the meaning of a copy operation almost always stems from the class performing some kind of resource management, and that almost always implies that all the three would be participating in management of the resource.
* The presence of a user-declared dtor should have prevented compilers from generating copy operations, but this rule was not fully appreciated in C++98.

## C++11 Rules

default ctor
* A default ctor is generated only if the class declares no ctors at all.

dtor
* The dtor is nonvirtual unless its base class has a virtual dtor.

move
* The heart of each memberwise 'move' is application of `std::move`, so a move or a copy may be performed during function overload resolution.
* If you declare one of the two move operations, the other is prevented from generating by compilers.
* If a copy operation is explicitly declared, move operations won't be generated.
* If the ctor is declared, move operations won't be generated.

copy
* Copy ctor and copy assignment is independently treated.
* Declaring a move operation disables compilers to generate copy operations.
* If the ctor is declared, copy operations should not be generated. But in practice, may or may not.

Member function templates never suppress generation of special member functions.

```
class Widget {
   // Compilers will still generate copy and move operations for Widget.
   template<typename T>
   Widget(const T& rhs);
   template<typename T>
   Widget& operator = (const T& rhs);
}
```

## Best Practice

`=default` is often useful in polymorphic base classes.

```
class Base {
public:
   virtual ~Base() = default;    // make dtor virtual

   Base(Base&&) = default;       // support moving
   Base& operator = (Base&&) = default;

   Base(const Base&) = default;  // support copying
   Base& operator = (const Base&) = default;
}
```

Even if you have a class where compilers are willing to generate the copy and move operations and where the generated functions would behave as you want, you may choose to adopt a policy of declaring them yourself and using `=default` for their definitions.

