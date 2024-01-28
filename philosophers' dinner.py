import threading
import time

# Number of philosophers
NUM_PHILOSOPHERS = 5

# Semaphores to represent the forks
forks = [threading.Semaphore(1) for _ in range(NUM_PHILOSOPHERS)]

"""
forks = [threading.Semaphore(1) for _ in range(NUM_PHILOSOPHERS)] means that
forks is a list of NUM_PHILOSOPHERS semaphores, each with an
initial value of 1.

In other words, each philosopher can pick up one fork at a time, and
the value 1 means that the fork is available to be picked up.

When a philosopher picks up a fork, the value of the corresponding semaphore is
decremented to 0, and when the philosopher releases the fork, the semaphore's
value is incremented back to 1.

Threading.Semaphore is a class representing a semaphore,
and it has two methods:
- acquire() and release().

The acquire() method decrements the semaphore's value, and the release() method
increments it. The acquire() method has an optional parameter called blocking,
which is True by default. When blocking is True, the acquire() method blocks
the thread until the semaphore can be decremented.

The release() method has no parameters and always
increments the semaphore's value.

Threading.Semaphore(1) indicates that the semaphore is binary, meaning it can
only take on the values 0 and 1. When the semaphore is binary, it's called a
mutex and is used to control access to shared resources.

When the semaphore is binary, the acquire() method is equivalent to the lock()
method, and the release() method is equivalent to the unlock() method.

forks [ threading.Semaphore(1) for _ in range(NUM_PHILOSOPHERS) ] creates
a list of NUM_PHILOSOPHERS binary semaphores, each with an initial value of 1.

It's a list comprehension, a concise way to create a list.
It creates a list with NUM_PHILOSOPHERS elements,
and each element is a binary semaphore with an initial value of 1.
"""


# Function simulating thinking
def think(philosopher):
    print(f"Philosopher {philosopher} is thinking")
    time.sleep(1)


# Function simulating the action of eating
def eat(philosopher):
    left_fork = philosopher
    right_fork = (philosopher + 1) % NUM_PHILOSOPHERS

    with forks[left_fork]:
        with forks[right_fork]:
            print(f"Philosopher {philosopher} is eating")
            time.sleep(1)
    print(f"Philosopher {philosopher} finished eating and is thinking again")


"""
left_fork = philosopher, philosopher is a parameter of the eat function, and
indicates which philosopher is eating. Each philosopher
has a fork to their left, which is the fork with the same number
as the philosopher. right_fork = (philosopher + 1) % NUM_PHILOSOPHERS,
the fork to the right of the philosopher is the fork with the number
following the philosopher's number. As the
philosopher's number goes from 0 to NUM_PHILOSOPHERS - 1,
the number of the fork to the right is (philosopher + 1) % NUM_PHILOSOPHERS.

The % operator is the modulo operator, and it is used to ensure that
the number of the fork to the right is a number between 0 and
NUM_PHILOSOPHERS - 1.

with forks[left_fork]:, the with statement is used to ensure that the semaphore
corresponding to the fork to the left of the philosopher is released when the
philosopher finishes eating, even if an exception occurs
during the execution of the eat function.

with forks[right_fork]:, the with statement is used to ensure that
the semaphore corresponding to the fork to the right
of the philosopher is released when the philosopher finishes eating,
even if an exception occurs during the execution of the eat function.
"""


# Function representing the life of a philosopher
def philosopher_life(philosopher):
    while True:
        think(philosopher)
        eat(philosopher)


# Creating threads for each philosopher
philosophers = []
for i in range(NUM_PHILOSOPHERS):
    philosopher_thread = threading.Thread(target=philosopher_life, args=(i,))
    philosophers.append(philosopher_thread)

"""
philosopher_thread = threading.Thread(target=philosopher_life, args=(i,))
creates a thread that executes the philosopher
life function and passes the philosopher's number as a parameter.

philosophers.append(philosopher_thread) adds
the created thread to the philosophers list.
"""

# Start the threads
for philosopher_thread in philosophers:
    philosopher_thread.start()

# Wait for all threads to finish
for philosopher_thread in philosophers:
    philosopher_thread.join()
