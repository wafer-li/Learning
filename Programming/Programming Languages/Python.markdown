# Python 

Tags: Programming-Learning Python

[TOC]

---

## 1. Comment
> -  Start with `#`, not the `//`
- `#!` use to specfy the interpreter

## 2. Type
> Everything is object

### 1) Number
> - int
- long
- float
- complex number (use `j` stand for the $i$ in math) 

### 2) String

#### 1.quote singnal

- Singgle & double quote are **the same**
- Triple can contains the multiple lines string, can use single and double quote inside
- Scape `\`
    - Use id to escape the single quote to the **RAW** eidition
    - Use it at the end of line, escape the breakikng to the space, to link multiple lines
- **For C/C++ programmer, Python does not have char**

### 3) Variable
> For C/C++, doesn't need to announce and define the Variable

## 3.Logic line and physis line
> Python treat an physis line as an logic line.
So, please follow this instruction, usually, python does not use semicolon.

## 4. Intent
> The same statement block has the same intent
Do **NOT** mix up the `Tab` and the `Space` for intent

## 5. Operator
- `*` if the value is string, it repeat itself and become larger.
> 'la' * 3 $\to$ 'lalala'

- `**` the same as `pow()`
> 3**4 equals to $3^4$

- `//` return the integer of the quotient.

- the bool operator is quite diffirent with C/C++ and Java
> `and` equals to `&&`
`or` equals to `||`
`not` equals to `!`

## 6. Control Statement
> The control statement end the line with an `:`
Means there will be the statement **block**
Also, you need to obey the right intent rules

### 1) if
```python
if condition:
    # do somthing
elif another-condition:
    # do other things
else:
    # do the default thing
```
Notice:

- **The `if` statement end with a `:`**, it tells there will be a statement **block**
    - The same as `else` and `elif`
- `elif` is the same as the `eles if` in C/C++ and Java
- **There is no `switch` statement, use the `if..elif..else` statement to do the same function**

### 2) while
```python
while condition:
    # do things
    
else:
    # do other things
```

Notice:

- Remember the `:`
- You can use the `else` statement, but it's **OPTIONAL**

### 3) for 
```python
# The same as the for statement in C/C++ and Java
for i in range(1,5):
    # do something

```

```java
//The same as Java
for(i = 1;i<5;i++) {
    //do something
}
```

```python
# The same as the foreach statement in Java
for word in wordlist:
    # do things
    
```

```java
// The same as in Java 
for (Word word : wordlist) {
    //do somthing
}
```

### 4) break & continue
> `break` and `continue` is the same as in C/C++
There is no `break label` in Python, use the function return instead of the multiple loop

## 7. Function

### 1) Define the function
```python
# There show you how to define an function in Python
def function():
    print(`Hello!`)
    # do the function should do
    # The block belongs to the function itself

function()  # call the function
```

### 2) Formal paramater
```python
def printMax(a, b):
    # do the thing y
```

### 3) Local variables
> Use `global` key word to use the global variables

### 4) Default paramater
```python
def say(message, times = 1):
    print(message * times)

say('Hello')    # if the default paramater is **NOT** specfy, then it will use the default value
```

### 5) Specfy the paramater
```python
def func(a, b=5, c=10)
    # do things

func(c=50, a = 100) # Use the formal paramater NAME to specfy the paramater name
```

### 6) DocStrings
> The same function as `javadoc`

```python
def printMax(x, y):
    ```Prints the maximun of two numbers.
    
    The tow values must be integers.```
    
```

- Use the multiple string to present the doc
- Begins with an **UPPER** letter and ends with the dot
- The second line is empty, the details start at the thrid line
- Use the `__doc__` property to gain the DocStrings
- The help function use the DocStrings to display the help message

##8. Module
> The same as `package` in Java

### 1) Import module

- Use `import` statement to import module
```python
import sys

print sys.path
```

- Use `from...import` statement to import the specfic function name
```python
from collection import OrderedDict

d = OrderedDict(...) # The dict you want to ordered.
```

- Use the `as` statement to rename the module name to you want
```python
import simplejson as json

json.load()
```

### 2) The `__name__` property of module
> You can use this property to avoid the other script to run this module

```python
if __name__ == `__main__`:
    # do the right thing
else:
    # permission deny
```

### 3) Define your own module
> Just write the `.py` file and import it (using its name) at the other file

```python
# Filename: mymodule.py

def func():
    # do something

version = '0.1'

# End of this file
```

```python
# Filename mymodule_demo.py

import mymodule

func()

# End of mymodule_demo.py
```

- You can use `dir()` function to display the identifier of the module
    - The **identifier** include the **fucntion**, **class**, and **variable**
    

## 9.Data Structure

### 1) List
> **The list is mutable, the list method will change the origin data of the list** 

- Use the `[]` to wrap an list
    
    ```python
    shoplist = ['apple', 'mango', 'carrot', 'banana']
    ```

- Use the `list[index]` to access the item
    ```python
    shoplist[0] # Start with 0
    ```

- Use the class method to do more things
    ```python
    shoplist.append() # Append at the end of the list
    shoplist.sort() # Sort the list
    ```

- Use the `del` statement to remove the item in the list
    ```python
    del shoplist[0]
    # The whole instance of the item was deleted
    # The list will automatically fill the space
    ```


### 2) Tuple
> **The Tuple is immutable object, just as String as Java**

- Use `()` to wrap the tuple

    ```python
    zoo = ('wolf', 'elephant', 'penguin')
    ```
- The tuple can be nested
    - Also the list and the dict
    
    ```python
    new_zoo = ('lion', 'tigger', zoo)
    ```

- Use the `tuple[index]` to access the item

- Tuple is empty or only 1 item
    - Use the empty `()` to build an empty tuple
    - Use the comma at the end of the  only one item
    
    ```python
    # The empty tuple
    empty_tuple =  ()
    
    # The only one item tuple
    one_item_tuple = (1, )
    ```

- Tuple with the `print` statament
> the `print` statement can use the `%` to specfy the paramater as C `printf()` 

```python
age = 22
name = 'Swaroop'

print '%s is %d years old' % (name, age)
```

### 3) Dictionary
> The dictionary is **UNORDERED**

- Use the `{}` to wrap dict

    ```python
    d = {'a' : 'a'}
    ```

- Use the 










