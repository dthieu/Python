# Section 1: Introduction
# Section 2: Python introduction
# Section 3: Python basic
# Section 4: Python basic II
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
# Section 5: Development environment
Virtual environment:
```bash
$ cd <your_prj_folder>
$ python3 -m venv ./
$ source <your_prj_folder>/bin/activate # Linux
$ .\<your_prj_folder>\Scripts\Activate.ps1 # Windows powershell 
$ <your_prj_folder>\Scripts\activate.bat # or Windows batch script
```
## I. PEP 8 – Style Guide for Python Code
<u>Link</u>: [PEP 8 Python](https://peps.python.org/pep-0008/)

# Section 6: Advanced Python: Object Oriented Programming
## 1 .Encapsulation
## 2. Abstraction
Don't care about how method is implemented. ex: arr.append(1)
## 3. Inheritance
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
## 4. Polymorphism

## 5. <code>@classmethod</code> and <code>@staticmethod</code>
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
# Section 7: Advanced Python: Functional Programming
## map()
## filter()
## zip()
## reduce()
## Lambda Expression
## List comprehensions
## Set and Dictionary comprehension

# Section 8: Advanced Python: Decorators
## 1. Decorator
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

# Section 9: Advanced Python: Error handling
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

# Section 10: Advanced Python: Generators
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


# Section 11: Modules
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
# Section 12: Debugging in Python
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


# Section 13: File I/O
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

# Section 14: Regular Expressions
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

# Section 15: Testing in Python
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
# Section 16: Carrer Of A Python Developer
Some common carrer paths + needed knowledge can be found at: \
https://zerotomastery.io/career-paths/

# Section 17: Scripting with Python
## 1. Common libraries and tools
* Library:
  | Name   | Function |
  |--------|---------------------|
  | pyPDF2 | pdf file processing |
  | Pillow | Image processing |
  | OpenCV | Image processing |
  | smtplib | Send email message |
  | hashlib | Hashing (encode) |
* Tools:
  * http://mailchimp.com : send mail
  *   
## 2. Send mail
Quick Note: Google Security Updates

Heads up! If you are following along (and using google Gmail account), a recent Google update to their terms and features means you have to do an extra step to be able to send emails. Otherwise, you will see this error:
```error
raise SMTPAuthenticationError(code, resp) smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5 .7.8 https://support.google.com/mail/?p=BadCredentials n24sm10301669pjq.51 - gsmtp') 
```
In the case that you are sending emails through GMAIL,  just go to your account(gmail) -> Account setting -> Scroll to the bottom of the page and you see Less Secured Apps tab ,now you just have to turn that feature ON. for more info visit this:

Links Less Secured Apps : https://support.google.com/accounts/answer/6010255 \
Third party sites & apps: https://support.google.com/accounts/answer/3466521

The reason that Google blocks this is because they do not trust your "app". Google states:
Less secure apps & your Google Account: If an app or site doesn’t meet our security standards, Google might block anyone who’s trying to sign in to your account from it. Less secure apps can make it easier for hackers to get in to your account, so blocking sign-ins from these apps helps keep your account safe.

I recommend turning that feature back OFF once done experimenting with email in the next video since it is an extra security feature for your gmail account. 

## 3. Hashing
Encode a string for protecting data, we can use md5, sha1, sha256,...
```python
import hashlib

my_psw = "Chayngaydi123"

print(hashlib.sha1(my_psw.encode('utf-8')).hexdigest())
# Output: 66b6c14a2fae0cdf691f7ead06543a7094d911e6
```

Sample project
```python
# PASSWORD CHECKER
#You will not be able to run this file here and will need to copy it onto your computer and run it on your machine. 
#You will also need to make sure you have installed the requests module from PyPi (pip install)
import requests
import hashlib
import sys

def request_api_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)
  if res.status_code != 200:
    raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
  return res

def get_password_leaks_count(hashes, hash_to_check):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hash_to_check:
      return count
  return 0

def pwned_api_check(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1password[:5], sha1password[5:]
  response = request_api_data(first5_char)
  return get_password_leaks_count(response, tail)

def main(args):
  for password in args:
    count = pwned_api_check(password)
    if count:
      print(f'{password} was found {count} times... you should probably change your password!')
    else:
      print(f'{password} was NOT found. Carry on!')
  return 'done!'

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
```


### 3. Tweeter API
https://www.twilio.com/docs

IN CASE YOU WANT TO USE TWITTER API v2, just using below code:
```python
    # pip install tweepy
    import tweepy
     
    # config.py : where I keep my keys as constants
    import config
     
     
    def about_me(client: tweepy.Client) -> None:
        """Print information about the client's user."""
        # The `public_metrics` addition will give me my followers count, among other things
        me = client.get_me(user_fields=["public_metrics"])
        print(f"My name: {me.data.name}")
        print(f"My handle: @{me.data.username}")
        print(f"My followers count: {me.data.public_metrics['followers_count']}")
     
     
    def get_ztm_tweets(client: tweepy.Client) -> list[tweepy.Tweet]:
        """Return a list of latest ZTM tweets"""
        ztm = client.get_user(username="zerotomasteryio")
        response = client.get_users_tweets(ztm.data.id)
        return response.data
     
     
    if __name__ == "__main__":
        client = tweepy.Client(
            bearer_token=config.BEARER_TOKEN,
            consumer_key=config.API_KEY,
            consumer_secret=config.API_SECRET,
            access_token=config.ACCESS_TOKEN,
            access_token_secret=config.ACCESS_SECRET,
        )
        print("=== About Me ===")
        about_me(client)
        print()
        print("=== ZTM Tweets ===")
        for tweet in get_ztm_tweets(client):
            print(tweet, end="\n\n")
```
In order to get all the keys, you need to sign up at https://developer.twitter.com/ and create an app. Go to your newly created app, and in the center screen you'll see two tabs: "Settings" and "Keys and tokens". Under "Settings", click "Edit" in the "User authentication settings" box, choose OAuth 1.0a and give https://example.com as a redirect and personal website. In the "Keys and tokens" tab, generate all keys. You need 5 in total: bearer token, API key, API key secret, access token, access token secret. After that you should be good to go.

To interact with API, we need tweepy:
```python
pip3 install tweepy==3.8
```

Example:
```python
#You will need to PIP INSTALL tweepy for this to work and also create a twitter API. Run this on your own machine, not in this Repl. 
import tweepy
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name) #prints your name.
print (user.screen_name)
print (user.followers_count)

search = "zerotomastery"
numberOfTweets = 2

def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(1000)

#Be nice to your followers. Follow everyone!
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
  if follower.name == 'Usernamehere':
    print(follower.name)
    follower.follow()


# Be a narcisist and love your own tweets. or retweet anything with a keyword!
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
```

# Section 18: Scrapping Data
Check "allow" and "disallow" by checking robots.txt of website. \
Example: https://sharewareonsale.com/robots.txt
```
User-agent: *
Allow: /wp-admin/admin-ajax.php
Disallow: /wp-admin/

Sitemap: https://sharewareonsale.com/sitemap.xml
Sitemap: https://sharewareonsale.com/sitemap.rss
```
Common library for scrapping:
* Beautiful Soup
  * Document: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
* Scrapy
  * Document: https://docs.scrapy.org/en/latest/intro/tutorial.html

# Section 19: Web development
Flask 
```python
from flask import Flask, render_template
app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    # return 'Hello World'
    return render_template('index.html') # Using html file in templates/ folder. 
                                         # If you don't create templates folder, 
                                         # the server cannot find this index.html file and an error will be raised "inja2.exceptions.TemplateNotFound: index.html"

@app.route('/page1')
def doHello():
    return 'Wellcome to new world'

@app.route('/about.html')
def about():
    return render_template("about.html")
```
Powershell script for run this file:
```powershell
Write-Host "Server is running..."
$env:FLASK_APP="server.py"
# Linux command: export FLASK_APP=server.py

# Set debug mode
$env:FLASK_ENV="development"
# Linux command: export FLASK_ENV=development

python -m flask run
# or just type: $ flask run
```
Save this script as <code>run.ps1</code> and execute by <code>. run.ps1</code>

## Insert icon for web page
Refs: https://flask.palletsprojects.com/en/1.1.x/patterns/favicon/ 
```html
<!-- Icon for web page, url_for is a flask python function, static is folder contains *.ico file-->
<!-- from flask import url_for: using it in python code -->
<!-- {{ }} the code in this pair will be executed -->
<link rel="shortcut icon" href="{{ url_for('static', filename='my_ico.ico') }}"> 
```
## URL parameter
Refs: https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules \
With this function of Flask lib, we can customize the url link
```python
from markupsafe import escape

@app.route('/user/<username>') # Pass username into function
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
```
Converter types:
| Type   | Function |
|--------|---------------------|
| string|(default) accepts any text without a slash|
| int|accepts positive integers |
| float|accepts positive floating point values|
| path |like string but also accepts slashes|
| uuid | accepts UUID strings|

### MIME types (IANA media types)
A media type (also known as a <b>Multipurpose Internet Mail Extensions</b> or MIME type) indicates the nature and format of a document, file, or assortment of bytes. MIME types are defined and standardized in IETF's RFC 6838.

The Internet Assigned Numbers Authority (IANA) is responsible for all official MIME types, and you can find the most up-to-date and complete list at their Media Types page.

Refs:
* https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types
* Fun website: https://robohash.org/
#### 1. Structure of a MIME type
```
type/subtype
```
#### 2. Important MIME types for Web developers:
* text/plain
* text/css
* text/html
* text/javascript
* application/octet-stream: unknown binary file

### Website template
<u>LINKs:</u>
* http://www.mashup-template.com/templates.html
* https://www.creative-tim.com/bootstrap-themes/ui-kit?direction=asc&sort=price
* https://html5up.net/

Sample project:
```python
from dataclasses import dataclass
from http import server
from flask import Flask, render_template, url_for, request, redirect
# render_template: render a web page from html file
# request: for check post or get method (request.method == "GET | POST")
# redirect: navigation destination webpage ex: redirect("Goodbye.html")
import csv

DATABASE_FILE_PATH = "database.csv"
FIELD_NAME = ['email', 'subject', 'message']

app = Flask(__name__)
print(__name__)

@app.route('/')
def my_root():
    return render_template('index.html')

# @app.route('/index.html')
# def other():
#     return render_template('index.html')

# @app.route('/home.html')
# def my_home():
#     return render_template('index.html')

# ...

# Instead write a lot of function as above, just using string:page_name
# It will call corressponding web page html
@app.route('/<string:page_name>')
def my_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open(DATABASE_FILE_PATH, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAME)
        writer.writerow(data)
        
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict() # get input from browser (email, subject, message)
            print("Data: ", data)
            write_to_csv(data)
            return redirect("/submitted.html")
        except:
            return "Did not save to database!"
    else:
        return "Something went wrong. Please try again!"
```
```html
<div class="row">
  <div class="col-md-10 col-md-offset-1">
      <form action="submit_form" method="post" class="reveal-content"> <!-- Here we can choose action post or get, coressponding submit form sever function -->
        <div class="row">
          <div class="col-md-7">
            <div class="form-group">
              <input name="email" type="email" class="form-control" id="email" placeholder="Email"> <!--Here: name="email" will be passed into submit_form function -->
            </div>
            <div class="form-group">
              <input name="subject" type="text" class="form-control" id="subject" placeholder="Subject"> <!--Here: name="subject" will be passed into submit_form function -->
            </div>
            <div class="form-group">
              <textarea name="message" class="form-control" rows="5" placeholder="Enter your message"></textarea> <!--Here: name="message" will be passed into submit_form function -->
            </div>
            <button type="submit" class="btn btn-default btn-lg">Send</button>
          </div>
```
### Host website at https://www.pythonanywhere.com
1. Upload source code to Github
2. Access https://www.pythonanywhere.com -> Choose free account
   1. Dashboard -> Bash -> Clone flask source code
   2. Create virtual environment (Using Bash console) 
      1. Create virtual environment:
      ```bash
      cd <to flask project>
      mkvirtualenv myvirtualenv --python=/usr/bin/python3.9 # optional
      # Install python package for virtual environment ex flask
      pip install flask
      workon myvirtualenv # active virtual env
      ```
   3. Update source code path at https://www.pythonanywhere.com/user/<user_acc>/webapps/#tab_id_<user_acc>_pythonanywhere_com
   4. Go to https://www.pythonanywhere.com/user/<user_acc>/files/var/www/<user_acc>_pythonanywhere_com_wsgi.py?edit
   5. Only keep FLASK part and edit code as below:
   ```python
    import sys

    path = '/home/<user_acc>/<website>/'
    if path not in sys.path:
        sys.path.append(path)

    from <name_py_file_server> import app as application  # noqa
   ```
   6. Open Web tab -> Press Reload <user_acc>.pythonanywhere.com
   7. Done! You can check <user_acc>.pythonanywhere.com on your browser ^_^ 

# Section 20: Automation / Testing
## Selenium
* https://demo.seleniumeasy.com/
* https://demo.seleniumeasy.com/basic-first-form-demo.html
* https://www.seleniumeasy.com/
* http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/ <-- good example for beginner / reference
* https://selenium-python.readthedocs.io/

```python
from selenium import webdriver

# Load auto tool
chrome_driver = webdriver.Chrome(r"D:/HIEU/PYTHON_WORLD/automation testing/chromedriver.exe")

# Open website
chrome_driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")

# 1. Find user message
user_mess = chrome_driver.find_element_by_id("user-message")
# 2. Clear all input if any
user_mess.clear()
# 3. Send input "Hello World!"
MESS = "Hello World!"
user_mess.send_keys(MESS)
# 4. Find and Click Show Message button
show_mess = chrome_driver.find_element_by_css_selector("#get-input > .btn")
# show_mess = chrome_driver.find_element_by_class_name("btn-default") # or using this
show_mess.click()
# 5. Get output message
out_mess = chrome_driver.find_element_by_id("display")
print(out_mess.text)
# Output: Hello World!
assert MESS in out_mess.text
chrome_driver.close()
# chrome_driver.quit() # Or
```

# Section 21: Machine Learning + Data Science
## Common steps
1. Import data
2. Clean data
3. Split data: Training set/Test set
4. Create a Model
5. Check the output
6. Improve

## Library for data processing
* Numpy : array / matrix... handling
* Pandas : handle data
* Scikit-learn : built-model https://scikit-learn.org/stable/
* visualyze data (VERY GOOD AT VISUALYZE DATA)
  * Matplotlib
  * bokeh: https://docs.bokeh.org/en/latest/index.html
  * seaborn: https://seaborn.pydata.org

## Tools
* Kaggle: big website for improve / check model and more
* Jupyter notebook: IDE for executing python script 

* Save and load trained model by using Joblib module
```
Quick Note: Joblib Update

Heads up! In the next video you are going to see me import something called joblib like this:

from sklearn.externals import joblib

in the latest version of sklearn, you no longer need to do it like the above and can instead do this:

from joblib import dump, load

You will see in the next video where we do this, but I have also attached the documentation reference to the next video so you can read about it yourself. Let's get to it!
```
```python
>>> from joblib import dump, load
>>> dump(<model: ex knn_model>, '<model>.joblib')
>>> clf = load('<model>.joblib') 
```

Tensorflow
The below script is what I will show you in the next video (but the code below has a few modifications in case you have the latest version of TensorFlow and not the version I show you in the coming video). You can always copy and paste this as a reference while you code along in the next video. (Thanks to Ben our Star Mentor for the code!)
```python
import numpy as np
import tensorflow as tf
  
# from tensorflow.keras.applications.resnet50 import (
#     ResNet50,
#     decode_predictions,
#     preprocess_input,
# )
  
from tensorflow.keras.applications.efficientnet_v2 import (
    EfficientNetV2L,
    decode_predictions,
)
  
image = tf.keras.preprocessing.image.load_img("./giraffe.jpg")
input_arr = tf.keras.preprocessing.image.img_to_array(image)
  
# If using ResNet50, use this line:
# input_arr = tf.image.resize(input_arr, (224, 224))
  
# If using EfficientNetV2L, use this line:
input_arr = tf.image.resize(input_arr, (480, 480))
  
input_arr = np.array([input_arr])
  
# model = ResNet50()
model = EfficientNetV2L()
  
predictions = decode_predictions(model.predict(input_arr))
  
for _, label, prob in predictions[0]:
    print(f"{label}: {prob}")
```
Image recognize AI \
Supper tool for image detection 
https://github.com/OlafenwaMoses/ImageAI

# Section 22: Where to go from here?
* Cheat Sheet:
https://zerotomastery.io/cheatsheets/python-cheat-sheet/?utm_source=udemy&utm_medium=coursecontent

# Section 23: Extra Bits
## CWD: Git + Github
Github Update: Master --> Main \
Heads up! In the next video we are going to be speaking about Github and branching. Recently Github has decided to rename the original branch from master to main . If you want to find out the reason why they did this, you can read about it here (main is less offensive than master).

For this reason, for any new Github repositories created from now on (old ones will stay the same with master as the main branch), you will have to use main instead of master. So anytime you see me use master, simply replace it with main in the next video!

For example if you see a command like: \
<code>$ git push origin master</code> \
it should now be: \
<code>$ git push origin main</code>

* Github guideline: https://github.com/zero-to-mastery/start-here-guidelines
* Contribute: https://github.com/zero-to-mastery
