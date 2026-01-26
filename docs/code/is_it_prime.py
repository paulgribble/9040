import time
from math import sqrt

n = int(input("enter an integer > 1: "))
start_time = time.perf_counter()
is_prime = True

if (n>2):
    for i in range(3,int(sqrt(n))+1,2):
        if ((n % i) == 0):
            is_prime = False
            break

stop_time = time.perf_counter()
execution_time = stop_time - start_time

if is_prime:
    print(f"the number {n} is prime")
else:
    print(f"the number {n} is not prime")

print(f"execution time was {execution_time*1000:.8f} milliseconds")

