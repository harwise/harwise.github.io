---
layout: default
title: C++ emplace
---

*Effective Modern C++ Chapter 8*

## emplace methods

* push_back -> emplace_back
* push_front -> emplace_front
* insert -> emplace
   * All containers supports insert except *std::forward_list* and *std::array*.
* insert with hint -> emplace_hint
* insert_after -> emplace_after
   * *std::forward_list*

## pros and cons

* perfect forwarding - doesn't require creation and destruction of a temporary object.
* In principle, emplacement should never be less efficient. But in practice, benchmarking will tell.

### If all the following are true, emplacement will almost certainly outperform insertion:

* The value being added is constructed into the container, not assigned.
   - Node-based containers virtually always use construction to add new values. vector, deque, and string are not noed-based.
* The argument types being passed differ from the type held by the container.
* The container is unlikely to reject the new value as a duplicate.
   - A temporary node has to be created to compare against the existing nodes.

### Don't

* resource management.
   ```
   std::list<std::shared_ptr<Widget>> ptrs;
   ptrs.emplace_back(new Widget, Kill Widget);  // An exception in emplace_back leads to the new Widget object leak.
   ```
* unintentional explicit constructor.  
   ```
   std::vector<std::regex> regexes;
   regexes.emplace_back(nullptr);   // an explicit ctor is called.
   ```


