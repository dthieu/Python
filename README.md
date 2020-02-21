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
    
