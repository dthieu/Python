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
## VI. Error handling
Built-in Error Exceptions:\
Refs: https://docs.python.org/3/library/exceptions.html \
Some common exceptions:
* ZerorDivisionError: Division by zero
* KeyError
* IndexError
* NameError
* ValueError

```python
# Error Handling Syntax
try:
  # TODO: Function / peace of code may get error
  # We can choose raise an error here!
  raise ValueError('Hey you got an error!') # print our message in Value Error exception
  # raise Exception('Hey you got an error!')
except ValueError: # Can use some common error at here
  # TODO: What need to handling if error is raised 
except KeyError as err:
  # TODO: another exception
  # use continue to jump out to finally
except (KeyError, ValueError) as err: # Combine exceptions, only exception will be choosen
  # TODO: another exception
else:
  # TODO: Maybe invokes break in case while loop or print somthing in case no error
finally:
  # TODO: After all exceptions, else... are executed, 'finally' will be done!
  # This is like an information to inform that exception is executed 
  # This useful in case we want to log / record errors example login error 
```
Note that we only have 1 exception will be executed!

## VII. Generators
```python
class MyGen():
  curr = 0
  def __init__(self, first, last):
    self.first = first
    self.last = last
  
  def __iter__(self):
    return self
  
  def __next__(self):
    if self.curr < self.last:
      num = MyGen.curr
      MyGen.curr += 1
      return num
    raise StopIteration # there is no element

my_it = MyGen(0, 100)
for i in my_it:
  print(f"i = {i}")
```

## VIII. Module
* Refs: https://softwaremaniacs.org/blog/2020/02/05/dicts-ordered/en/ \
* Built-in module: https://docs.python.org/3/py-modindex.html \
* This link contains all modules which are available when we install Python3 such as random, calendar, gzip,...

### Useful module
```python
from collections import Counter, defaultdict, OrderedDict

arr = [1, 2, 7, 4, 3, 5, 8, 9, 0, 1, 3, 2]
print(Counter(arr))
# Output: Counter({1: 2, 2: 2, 3: 2, 7: 1, 4: 1, 5: 1, 8: 1, 9: 1, 0: 1})

mydic = defaultdict(int, {'a': 1, 'b': 2})
print(mydic['c']) 
# Output: 0 # there is no 'c'

mydic1 = defaultdict(lambda: 'does not exist!', {'a': 1, 'b': 2})
print(mydic1['c']) 
# Output: does not exist! # default for non-existent elements

mydic2 = OrderedDict()
mydic2['a'] = 1
mydic2['b'] = 2

mydic3 = OrderedDict()
mydic3['b'] = 2
mydic3['a'] = 1

print(mydic2 == mydic2)
# Output: False # because this is Ordered dictionary
# True when they are common dictionary { ... }

from array import array

myarr = array('i', [1, 2, 3])
print(myarr)
# Output: array('i', [1, 2, 3]) # i = int
# We can search it in built-in modules part
print(myarr[0])
# Output: 1
```
## IX. Debug code
pdb (Python Debugger):
* is a built-in module,
* Interact with the code
* Using:
```python
import pdb
pdb.set_trace() # call this at wherever you want to tracing
```
* pdb help
```
(Pdb) help

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt
alias  clear      disable  ignore    longlist  r        source   until
args   commands   display  interact  n         restart  step     up
b      condition  down     j         next      return   tbreak   w
break  cont       enable   jump      p         retval   u        whatis
bt     continue   exit     l         pp        run      unalias  where

Miscellaneous help topics:
==========================
exec  pdb
(Pdb) list
(Pdb) help list
...
```
Common pdb commands:
* (Pdb) step : jump into line which is set trace function
* (Pdb) next : next line of code
* (Pdb) continue : continue debug
* (Pdb) break : break current loop
* (Pdb) w : show the context of current line of code
* (Pdb) a : show all variables


## X. FILE
* Mode:
  * a : append
  * w : write
  * r : read 
### 1. Read/write file
#### 1.1 Read
* Method:
  * <code>my_file.read()</code>
  * <code>my_file.readlines()</code>
* 1st method
```python
f = open("test.txt", 'a')
f.readlines()
f.read()
f.close()
```
* 2nd method: using <code>with</code> keyword. <b>We don't need to invoke close file method.</b>
```python
try:
  with open("test.txt", mode='a') as f:
    print(f.readlines())
except FileNotFoundError as err:
  print("File does not exist!")
  raise err
except IOError as err: # read/write/open/IO error
  print("IO error!")
  raise err
```
#### 1.2 Write
* Method:
  * <code>my_file.read()</code>

## XI. Regular Expressions
<u>Refs:</u>: 
* Learn more detail about regex: https://www.w3schools.com/python/python_regex.asp 
* Analysis, Create and Debug regex syntax: https://regex101.com/
* Practice regex: https://regexone.com/
### <u>Example 1:</u> Email validation
```python
import re 
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$)")
email1 = "hieudang95@gmail.com"
email2 = "Hieudang95"

result1 = pattern.search(email1)
print(result1)
# <re.Match object; span=(0, 20), match='hieudang95@gmail.com'>
# 'span' is matching position.

result2 = pattern.search(email2)
print(result2)
# None
```
### <u>Example 2:</u> Password validation
* At least 8 char long
* Contain any sort letters, number, special char $#%@
* Has to end with a number
```python
import re
pattern2 = re.compile(r"[a-zA-Z0-9$#%@]{8,}\d")

passwd1 = "LKasjdlka@#asd1"
print(pattern2.fullmatch(passwd1))
# <re.Match object; span=(0, 15), match='LKasjdlka@#asd1'>

passwd2 = "LKasjd"
print(pattern2.fullmatch(passwd2))
# None
```

## XII. Testing in Python
<u>Example:</u>
```python
import unittest

def add(num1, num2):
    return num1 - num2

class TestMain(unittest.TestCase):
    def test_add_1(self):
        test_param = [10, 10]
        result = add(test_param[0], test_param[1])
        self.assertEqual(result, 20)
    
    def test_add_2(self):
        test_param = [6, 10]
        result = add(test_param[0], test_param[1])
        self.assertEqual(result, 16)

unittest.main()
# Setting up for each test case!
# Cleaning up each test case!
# FSetting up for each test case!
# Cleaning up each test case!
# F
# ======================================================================
# FAIL: test_add_1 (__main__.TestMain)
# You can comment here! Ex: testing with input: 10 and 10
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "c:\Users\dthie\OneDrive\Documents\ex.py", line 15, in test_add_1
#     self.assertEqual(result, 20)
# AssertionError: 0 != 20
# 
# ======================================================================
# FAIL: test_add_2 (__main__.TestMain)
# testing with input: 6 and 10
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "c:\Users\dthie\OneDrive\Documents\ex.py", line 21, in test_add_2
#     self.assertEqual(result, 16)
# AssertionError: -4 != 16
# 
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
# 
# FAILED (failures=2)
```

