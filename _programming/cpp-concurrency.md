---
layout: default
title: C++ concurrency
---

*Effective Modern C++ Chapter 7*

## `auto fut = std::async(doAsyncWork);`

* The return value is a `future`.
* If `doAsyncWork` emits an exception, the exception will be caught in the future object.
   ```
   try {
      int n = fut.get();
   } catch(const std::exception& e) {
      std::cout << time() << " caught exception " << e.what()
                  << ", fut.valid() == " << fut.valid() << "\n";
   }
   ```
* Software threads are a limited resource. a std::system_error exception may be thrown.
   ```
   std::thread t(doAsyncWork);
   ```
   And avoiding oversubscription is difficult.  

* Task-based programming shifts the thread management responsibility to the implementer of the C++ Standard Library.
   * System-wide thread pool is employed to avoid oversubscription.
   * Load balancing is improved across hardware cores through work-stealing algorithms.

* Launch Policy
   * `std::launch::async`: asynchronously; on a different thread.
   * `std::launch::deferred`: synchronously; when get/wait is called on the future.
      - Calling wait_for or wait_until yields the value `std::launch::deferred`
   * The default value is `async|deferred`

## std::thread

* joinable
   - Destruction of a joinable thread causes program termination. Make std::threads unjoinable on all paths.
   - Invoking join or detach on an unjoinable thread yields undefined behavior.
* unjoinable
   - Default constructed std::threads.
   - std::thread objects that have been moved from.
   - std::threads that have been joined.
   - std::threads that have been detached.
* Declare std::thread objects last in lists of data members.

## Futures As Thread Handles

* A future for a non-deferred task can be thought of as a handle to a system thread.
* But different from std::threads, its destruction never causes program termination.
* The *shared state* is shared among:
   - std::promise
   - std::future
   - std::shared_future
* A future does an implicit join only when:
   - It refers to a shared state that was created due to a call to *std::async*.
   - The task's launch policy is std::launch::async.
   - The future is the last future referring to the shared state.
* The API for futures offers no way to determine whether a future refers to a shared state arising from a call to std::async.
* Only shared states arising from calls to *std::async* qualify for the special behavior ,but there are other ways that shared states get created.
   - A `std::packaged_task` object prepares a function for asynchronous execution by wrapping it such that its result is put into a shared state.
      ```
      int calcValue();
      std::packaged_task<int()> pt(calcValue);
      auto fut = pt.get_future();
      std::thread t(std::move(pt));
      // Please note that t will take care of the join/attach problem.
      ```

## condition_variable

* Require a superfluous mutex.
* If the detecting task notifies the condvar before the reacting task waits, the reacting task will hang.
* The wait statement fails to account for *spurious wakeups*.
   - A fact of life in threading APIs is that code waiting on a condition variable may be awakened even if the condvar wasn't notified.

## One-shot event

* Option1. A flag + polling. Cons: it is based on polling, not blocking. (It should be blocking.)
* Option2. A condvar + a flag. Cons: still, a mutex is required. stilted.
* Option3. std::promises + futures (std::future or std::shared_future). Cons: heap memory for shared states; limited to one-shot communication.
   ```
   std::promise<void> p;
   void detect()
   {
      auto sf = p.get_future().share();
      std::vector<std::thread> vt;
      for (int i = 0; i < threadsToRun; ++i) {
         vt.emplace_back([sf]{
            sf.wait();  // wait on local copy of sf.
            react();
         });
      }
      ...               // detect hangs if this "..." code throws!
      p.set_value();    // unsuspend all threads.
      ...
      for (auto& t: vt) {
         t.join();
      }
   }
   ```

## Use std::atomic for concurrency

* RMW
* Restrictions on code reordering
   - Compilers
   - Hardwares
* Use `load` and `store` member functions to make it explicit that the variables involved aren't normal. slower and may communicate information to other threads.)

## Use volatile for special memory

* memory-mapping I/O.
   - Locations in such memory actually communicates with peripherals, e.g. external sensors or displays, printers, network ports, etc.
   - (seemingly redundant) Reads and writes should not be optimized away.

## `volatile std::atomic<int> vai`
   - operations on vai are atomic and can't be optimized away.
