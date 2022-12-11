# Python
Some useful code

```python
# shiff character: "crazy" => "dsbaz" (c->d, r->s, a->b, z->a, y->z)
def alphabeticShift(inputString):

    chars = list(inputString)
    print(chars)
    for i in range(len(chars)):
        number = ord(chars[i]) - ord('a')
        number = (number + 1) % 26
        chars[i] = chr(number + ord('a'))
    return ''.join(chars)
```
    
```python
# Print all primes number less than n using Eratosthenes
def sieveOfEratosthenes(n):
    # All number is prime
    primes = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        # If primes[p] does not change => p is a prime number 
        if primes[p]:
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    
    for i in range(2, n + 1):
        if primes[i]:
            print(f"{i} ", end=" ")
            
sieveOfEratosthenes(10000000)
```
