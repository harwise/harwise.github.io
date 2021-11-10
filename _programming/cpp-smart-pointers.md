---
layout: default
title: C++ smart pointers
---

*Effective Modern C++ Chapter 4*

## unique_ptr

* It's reasonable to assume that, by default, `std::unique_ptr`s are the same size as raw pointers, and for most operations (including dereferencing), they execute exactly the same instructions.
   * Custom deleters may cause the size to grow from one to two. Or more if there is much state is stored in the function object.
   * Stateless function object (e.g. from lambda expressions with no captures) incur no size penalty.
* 'Exclusive ownership' semantics, and copying isn't allowed ('move-only type').
* Be default, resource destruction is accomplished by applying `delete` to the raw pointer. But during construction, `std::unique_ptr` objects can be configured to use 'Custom deleters'.
* Two forms: `std::unique_ptr<T>` and `std::unique_ptr<T[]>`
   * But prefer `std::array, std::vector and std::string` for the latter.
* It is easily and efficiently converts to a `std::shared_ptr`.
* It is so well suited as a factory function return type.
   ```
   auto delInvmt1 = [](Investment* p)
                     {
                        ...
                        delete p;
                     };

   template<typename... Ts>
   std::unique_ptr<Investment, decltype(delInvmt1)>
   makeInvestment(Ts&&... args);

   std::shared_ptr<Investment> sp = makeInvestment(arguments);
   ```

# shared_ptr

* 'Shared ownership' semantics.
* `std::shared_ptr`s are twice the size of a raw pointer.
   * Ptr to T
   * Prt to Control Block
* To store the reference count, the memory must be dynamically allocated.
* Increments and decrements of the reference count must be atomic.
* Specifying a custom deleter doesn't change the size of a `std::shared_ptr` object.
   * Because it is stored in the 'control block', the same to the reference count.
* A 'control block' is created when:
   * `std::make_shared` always creates a control block.
   * a `std::shared_ptr` is constructed from a unique-ownership pointer.
   * a `std::shared_ptr` is called with a raw pointer.
* Avoid creating `std::shared_ptr`s from variables of raw pinter type.
   * Especially pay more attention to the `this` raw pointer.
   * For the `this` case, the `std::enable_shared_from_this` base class and the `enable_shared_from_this::shared_from_this` method may help.
* `enable_shared_from_this`
   * Need the control block to implement `shared_from_this`.
   * The ctors should be private. And the factory method should return a `std::shared_ptr`.
* Control Block
   * Reference count
   * Weak count
   * Custom allocator
   * Custom deleter
   * A virtual function used to ensure that the pointed-object is properly destroyed.
* There's **no** `std::shared_ptr<T[]>`.
   * Derived-to-base pointer conversions may not make sense for arrays.

# weak_ptr

* An augmentation of `std::shared_ptr`.
* Can't be dereferenced.
* `std::weak_ptr`s that dangle are said to have *expired*.
* Need an atomic operation that checks to see if the `std::weak_ptr` has expired and, if not, gives you access to the object it point to. This is done by creating a `std::shared_ptr` from the `std::weak_ptr`.
   * `auto spw = wpw.lock()`. The return value is null if the `std::weak_ptr` has expired.
   * `std::shared_ptr<Widget> spw2(wpw)`. An exception is thrown if wpw is expired.
* Use cases.
   * Caching.
   * Observer design pattern. A reasonable design is for each subject to hold a container of `std::weak_ptr`s to its observers, thus making it possible for the subject to determine whether a pointer dangles before using it.
   * A->B, B->A problem. Break the cycle.
* `std::weak_ptr` objects are the same size as `std::shared_ptr` objects, and they make use of the same control blocks.

# std::make_unique, std::make_shared, std::allocate_shared

`std::allocate_shared` acts just like `std::make_shared`, except its first argument is an allocator object to be used for the dynamic memory allocation.

`auto spw1(std::make_shared<Widget>())`

* Explicitly call `new` may cause memory leak.
   ```
   processWidget(std::shared_ptr<Widget>(new Widget),
                  computePriority());
   ```
   1. Perform `new Widget`.
   2. Execute `computePriority`.    // The widget object will leak if an exception is thrown here.
   3. Run `std::shared_ptr` ctor.
* When you use `new` directly, you should immediately pass the result to a smart pointer ctor in *a statement that does nothing else*.
   ```
   std::shared_ptr<Widget> spw(new Widget, cusDel);
   processWidget(std::move(spw), computePriority());
   ```
* Improved Efficiency. `std::make_shared` allocates a single chunk of memory to hold both the Widget object and the control block.
   * However, a single chunk means the lifecycle of the object and the lifecycle of the control block are bound together. The object cannot be deallocated until all its weak references are gone.
* Custom deleters are not supported.
* Braced initializers can't be perfect-forwarded. Workaround:
   ```
   auto initlist = {10 ,20};
   auto spv = std::make_shared<std::vector<int>>(initList);
   ```

* The Pimpl Idiom

```
// .h file
class Widget {
public:
   Widget();
   ~Widget();

   // 2. We must declare them because we have declared the custom dtor.
   Widget(Widget&& rhs);
   Widget& operator = (Widget&& rhs);

   // 3. We must implement them ourselves because std::unique_ptr is a move-only type.
   Widget(const Widget& rhs);
   Widget& operator = (const Widget& rhs);

private:
   struct Impl;
   std::unique_ptr<Impl> pImpl;
}

// .cpp file
struct Widget::Impl {...};
Widget::Widget()
   : pImpl(std::make_unique<Impl>())
{}

/*
 * 1. We have to put it in cpp because if it is in h file,
 *    compilers don't know how to delete a incomplete type.
 *    But if the smart ptr is std::shared_ptr, we don't need
 *    to do so. In that case, the type of the deleter is
 *    not a part of the type of the smart pointer. (The deleter
 *    can just be a pointer.)
 */
Widget::~Widget() = default;

Widget::Widget(Widget&& rhs) = default;
Widget::Widget& operator = (Widget&& rhs) = default;

Widget::Widget(const Widget& rhs)
   : pImple(std::make_unique<Impl>(*rhs.pImpl))
{}

Widget& Widget::operator = (const Widget& rhs)
{
   *pImple = *rhs.pImpl;
   return *this;
}
```