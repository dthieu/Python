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

```python
# Print date
import datetime 
 
formats=["%d/%m/%Y %H:%M:%S", 
        "%d/%m/%Y %H:%M%f", 
        "%Y-%m-%d %H:%M:%S.%f", 
        "%m/%d/%Y", 
        "%d/%m/%Y", 
        "%m-%d-%Y", 
        "%d-%m-%Y", 
        "%H:%M:%S", 
        "%M:%S" 
        ]  
for ft in formats: 
    time = datetime.datetime.now() 
    time = time.strftime(ft) 
    print("Format",ft,": ", time)
'''
Format %d/%m/%Y %H:%M:%S :  16/05/2023 22:44:51
Format %d/%m/%Y %H:%M%f :  16/05/2023 22:44569000
Format %Y-%m-%d %H:%M:%S.%f :  2023-05-16 22:44:51.574000
Format %m/%d/%Y :  05/16/2023
Format %d/%m/%Y :  16/05/2023
Format %m-%d-%Y :  05-16-2023
Format %d-%m-%Y :  16-05-2023
Format %H:%M:%S :  22:44:51
Format %M:%S :  44:51
'''
```

```python
# List all points in a line which start point (x1, y1) and end point (x2, y2)
import numpy as np

def get_line_coordinates(x1, y1, x2, y2):
    """
    Generates a list of pixel coordinates along the line connecting A(x1, y1) and B(x2, y2).

    Args:
        x1, y1 (int): Coordinates of point A.
        x2, y2 (int): Coordinates of point B.

    Returns:
        list of tuples: List of (x, y) coordinates along the line.
    """
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    # `step_x` is determining the direction in which the x-coordinate should move while iterating over
    # the line between points A and B. It is set to 1 if the x-coordinate of point B is greater than
    # the x-coordinate of point A, indicating that the line is moving to the right. Otherwise, it is
    # set to -1, indicating that the line is moving to the left along the x-axis.
    step_x = 1 if x2 > x1 else -1
    step_y = 1 if y2 > y1 else -1

    line_coordinates = []
    x, y = x1, y1

    if dx >= dy:
        error = dx / 2
        while x != x2:
            line_coordinates.append((x, y))
            error -= dy
            if error < 0:
                y += step_y
                error += dx
            x += step_x
    else:
        error = dy / 2
        while y != y2:
            line_coordinates.append((x, y))
            error -= dx
            if error < 0:
                x += step_x
                error += dy
            y += step_y

    line_coordinates.append((x2, y2))  # Include the endpoint B
    return line_coordinates

# Example usage:
point_A = (25, 25)
point_B = (25, 25)

# Get all pixel coordinates along the line
line_pixels = get_line_coordinates(*point_A, *point_B)

# Now 'line_pixels' contains the list of coordinates along the line
print(line_pixels)
```










