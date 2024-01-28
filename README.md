# Threading Library in Python

### The goal is to complement Chapter 13 of the Clean Code book, which addresses the topic of concurrency.

## Basic Concepts

### What is concurrency?

Concurrency is the ability of a program to be executed by more than one process or thread simultaneously.

### What is a process?

A process is a running program. A process is composed of one or more threads.

### What is a thread?

A thread is a sequence of instructions that can be executed simultaneously with other sequences of instructions. A thread is composed of one or more processes.

### What is a concurrent program?

A concurrent program is a program that has more than one thread.

### What is a parallel program?

A parallel program is a program that has more than one process.

### Semaphore

A semaphore is an object that controls access to a resource shared by multiple processes. A semaphore consists of a counter and a list of processes waiting to access the resource.

## Threading Library

```python
threading.active_count()
```

Returns the number of threads currently running.

```python
threading.current_thread()
```

Returns the thread object currently being executed.

```python
threading.get_ident()
```

Returns the identifier of the currently executing thread.

```python
threading.enumerate()
```

Returns a list of all currently running thread objects.

```python
threading.main_thread()
```

Returns the main thread object.

```python
threading.settrace(func)
```

Sets a trace function for all threads. The parameter to be passed is a function that takes four arguments: frame, event, arg, and thread.

```python
threading.setprofile(func)
```

Sets a profile function for all threads. The parameter to be passed is a function that takes three arguments: frame, event, and arg.

```python
threading.stack_size([size])
```

Sets the stack size for new threads. The default size is 0 (no limit).

```python
threading.TIMEOUT_MAX
```

The maximum timeout value that can be used with blocking methods.

```python
threading.active_count()
```

Returns the number of threads currently running.

```python
threading.excepthook(args)
```

Default function called when an unhandled exception occurs in a thread.

### Thread Class

```python
threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
```

Creates a new thread object. The parameters are:

- group: should be None, reserved for future use.
- target: function to be called when the thread starts.
- name: thread name.
- args: tuple of positional arguments for the target function.
- kwargs: dictionary of named arguments for the target function.
- daemon: indicates whether the thread is a daemon.

```python
threading.Thread.getName()
```

Returns the name of the thread.

```python
threading.Thread.setName(name)
```

Sets the name of the thread.

```python
threading.Thread.ident
```

Returns the identifier of the thread.

### How to use the Thread class

```python
import threading

def worker():
    print('Worker')

threads = []

for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
```
Explanation:
- The `worker()` function is the function to be executed by the thread.
- The `threads` variable is a list that will store the thread objects.
- The `for` loop will create 5 threads and store them in the `threads` list.
- The `start()` method will start the thread.
- `target=worker` indicates that the `worker()` function will be executed by the thread.

### Lock Class

```python
threading.Lock()
```

Creates a lock object. A lock is an object that has two states: locked and unlocked. A lock is created in the unlocked state. A lock has two methods: acquire() and release(). The acquire() method puts the lock in the locked state, and the release() method puts the lock in the unlocked state.

```python
threading.Lock.acquire(blocking=True, timeout=-1)
```

Puts the lock in the locked state. The parameters are:

- blocking: indicates whether the thread will be blocked until the lock is in the unlocked state.
- timeout: indicates the maximum time the thread will be blocked.

```python
threading.Lock.release()
```

Puts the lock in the unlocked state.

### How to use the Lock class

```python
import threading

lock = threading.Lock()

def worker():
    lock.acquire()
    print('Worker')
    lock.release()

threads = []

for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
```

Explanation:
- The `lock` variable is a lock object.
- The `acquire()` method puts the lock in the locked state.
- The `release()` method puts the lock in the unlocked state.

### Timer Object

```python
threading.Timer(interval, function, args=None, kwargs=None)
```

Creates a timer object. The parameters are:

- interval: time interval in seconds.
- function: function to be called when the timer expires.
- args: tuple of positional arguments for the function.
- kwargs: dictionary of named arguments for the function.

Example:

```python
import threading

def worker():
    print('Worker')

t = threading.Timer(5.0, worker)
t.start()
```

Explanation:
- The object `t` is a timer that will execute the `worker()` function after 5 seconds.

```python
threading.Timer.cancel()
```

Cancels the timer.

```python
threading.Timer.finished
```

Returns True if the timer has already expired.

```python
threading.Timer.is_alive()
```

Returns True if the timer is running.

### Barrier Object

```python
threading.Barrier(parties, action=None, timeout=None)
```

Creates a barrier object. The parameters are:

- parties: number of threads that must call the wait() method to release the barrier.
- action: function to be called when the barrier is released.
- timeout: maximum time a thread should wait to release the barrier.

```python
threading.Barrier.broken
```

Returns True if the barrier is broken.

```python
threading.Barrier.n_waiting
```

Returns the number of threads waiting to release the barrier.

```python
threading.Barrier.parties
```

Returns the number of threads that must call the wait() method to release the barrier.

```python
threading.Barrier.wait(timeout=None)
```

Puts the thread in the waiting state until the specified number of threads, given by the parties parameter, call the wait() method.

```python
threading.Barrier.reset()
```

Resets the barrier.

### With Statement

```python
with threading.Lock():
    # code to be executed with the lock
```

The `with` statement is used to ensure that the lock is released after the code execution.

### Code Example

```python
import threading

lock = threading.Lock()

def worker():
    with lock:
        print('Worker')

threads = []

for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
```

Explanation:

- The `with` statement ensures that the lock is released after the code execution.
- It is a context manager for

 the lock.
- The `with` statement is equivalent to:

```python
lock.acquire()
try:
    # code to be executed with the lock
finally:
    lock.release()
```

### Semaphore

```python
threading.Semaphore(value=1)
```

Creates a semaphore object. The parameters are:

- value: initial value of the semaphore counter.

```python
threading.Semaphore.acquire(blocking=True, timeout=None)
```

Decrements the semaphore counter. The parameters are:

- blocking: indicates whether the thread will be blocked until the semaphore is in the unlocked state.
- timeout: indicates the maximum time the thread will be blocked.

```python
threading.Semaphore.release()
```

Increments the semaphore counter.

```python
threading.Semaphore._value
```

Returns the value of the semaphore counter.

### Code Example

```python
import threading

semaphore = threading.Semaphore(2)

def worker():
    semaphore.acquire()
    print('Worker')
    semaphore.release()

threads = []

for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
```

Explanation:

- The semaphore is created with a value of 2.
- The `acquire()` method decrements the semaphore counter.
- The `release()` method increments the semaphore counter.

The semaphore being created with a value of 2 indicates that only 2 threads can execute the code simultaneously.