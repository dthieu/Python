## I. Arguments  *args , **kwargs, sys.argv
### 1. args: any input parameters
```python
def super_fun(*args):
  print(args)
  print(*args)

super_fun(1,2,3,4)
```
<code><u>Output:</u>\
$ (1,2,3,4) \
$ 1,2,3,4 </code>

### 2. kwargs : key word arguments
```python
def super_fun(*args, **kwargs):
  total = 0
  for items in kwargs.values():
    total += items
  print(total)
  print(kwargs)

super_fun(1,2,3,4, num1=5, num2=10)
```
<code><u>Output:</u> \
$ 15 # it will get values of kwargs and sum of them \
$ {'num1':5, 'num2':10} # kwargs is as a dictionary with key & value</code>

<u>Rule:</u> params -> *args -> default parameters -> **kwargs

### 3. sys.argv
This is command line input parameters\
```python
hello.py
import sys
print(f"Hello {sys.argv[1]}")

# How to run hello.py
python  hello.py  Ueih
            |       |
            v       v
          argv[0]  argv[1]
# Output: Hello Ueih
```

## II. Walrus Operator :=
Using for asigning values to variables as part of a larger expression. 
Minimize doing calcuation that are similar
ex:
```python
a = "Hieu"
if ((n := len(a)) < 10): # using n = len(a) will raise error
  print(n)
```
<code><u>Output:</u> $ Hieu </code>

## III. Scope

### 1. Global, nonlocal variable
To change value of global variable => need declare "global <global_variable>" and then use it in a function 
ex:
```python
num_color = 10
def change_global_var():
  global num_color
  num_color = 5
  b = 10
  def inner():
    # nonlocal b # value of b will no change after call inner fun
    b = 5
  inner() # value of b will change to 5
  
```
## IV. PEP 8 – Style Guide for Python Code
<u>Link</u>: [PEP 8 Python](https://peps.python.org/pep-0008/)
## V. OOP
### 1 .Encapsulation
### 2. Abstraction
Don't care about how method is implemented. ex: arr.append(1)
### 3. Inheritance
Check instance, we can use builtin funtion <code>isinstance</code> \
ex: <code>print(isinstance(newIns, Animal)) # check newIns whether is Animal instance or not, return value is bool value</code> \
All objects is inheritanced from <code>object</code>, that is also a base class
<u>Multi-inheritance:</u>
```
    A     <---- Base class
  /   \
 B     C  <---- Both B and C are inherited from A
  \   /
    D     <---- D is inherited from B and C
```
We have an terminology "__MRO - Method Resolution Order__" for this case.

We can check the flow by using method <code>mro()</code> \

The order of above flow is: D -> B -> C -> A -> object
Ex: 
```python
print(D.mro())
# Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```
### 4. Polymorphism

### 5. <code>@classmethod</code> and <code>@staticmethod</code>
So we would use something like <b>static method</b> where we don't care \
anything about the class state, a class state is something like these.\
We don't care about the attributes, really.

We use something like <b>a class method</b> when we do care about these \
attributes and maybe we want to modify them or change them.
```python
class Animal:
  def __init__(self, name):
    self.name = name
  
  def shout(self):
    printf(f"I'm {self.name}")

  @classmethod
  def show_default_name(cls): # cls = class, it means class's method same [].append and its name similar with "self"
    print("Anonymous!")
  
  @staticmethod
  def sum_two(a, b): # no need self or cls, we don't care about class's atributes
    return a + b

# Calling
Animal.show_default_name() # same [].append
# Output: Anonymous! 
```
Sample code:
```python
class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1 Add nother Cat
class Suzy(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Simon('Simon', 4), Sally('Sally', 21), Suzy('Suzy', 1)]

#3 Instantiate the Pet class with all your cats
my_pets = Pets(my_cats)

#4 Output all of the cats singing using the my_pets instance
my_pets.walk()
```

<u>Note:</u>

* __ method __ : methods cannot be overrided, ex __ init __
  * And when we dir(object) -> some listed methods like __ str __, __ eq __,.. are called __Dunder Methods__
  * We can override these methods. 
    * <u>ex:</u> <code>__ len __(self)</code> -> get len of obj
    * <code> __ str __(self)</code> -> Convert obj to string
* _ atribute: private variable
* <code>super().__ init __(args...)</code>: Call init of supper class (base class)
* <code>__ call __(self)</code> this method is used for calling similar as <code>obj()</code>
  * Ex:
```python
  class Toy():
    def __init__(self, color="Red"):
      self.color = color
      print("Init toy!")
    def __call__(self):
      print("Calling!")

  my_toy = Toy("Blue")
  my_toy() # Output: Calling!
```
### 6. Decorator
Using for decorating one function. \
<u>Example 1:</u>
```python
def my_decorator(fn):
  def wrap_func(*args, **kwargs):
    print("*******************")
    fn(*args, **kwargs)
    print("*******************")
  return wrap_func

@my_decorator
def hello(name, emoji=":)"):
  print(f"Hello {name} {emoji}")

hello("Ueih")
# Output: Hello Ueih :)

# We can call this function in another way without @my_decorator above function name
# my_decorator(hello)("Ueih", ":(")
```
<u>Example 2:</u>
```python
from time import time

def performance_measure(fn):
  def wrap_fn(*args, **kwargs):
    start = time()
    result = fn(*args, **kwargs)
    end = time()
    print(f"It takes {end - start} ms")
  return wrap_fn

@performance_measure
def check_loop(n):
  sum = 0
  for i in range(n):
    sum += i*i
  return sum

result = check_loop(10000)
print(result)
```




