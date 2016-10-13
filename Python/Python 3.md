# Python 3

Tags: Python

Basic on *A byte of Python 3rd edition*

[TOC]

---

## 1. 基本概念

### 1.1 注释

1. 注释以 `#` 开头
2. 以 `#!` 开头的称为**组织行**，表明了执行脚本的**解释器**

> Linux/Unix 中，如果不清楚 Python 的位置，可以使用 `#!/usr/bin/env python`，`env` 会自动寻找 Python 的解释器路径进行执行。

### 1.2 字面意义的常量

如同 5, 1.23, 9.25e-3 这样的**数**，以及 "This is a string" 等**字符串**被称作字面意义上的**常量**

#### 1.2.1 数

数的类型有三种——整数、浮点数和复数

1. `2` 是整数
2. `3.23` 和 `52.3E-4` 是浮点数
3. `(-5+4j)` 和 `(2.3-4.6j)` 是复数

> Python 3 只有一种整数类型，不区分 `long` 和 `int`
Python 2 中区分 `long` 类型
布尔型(`bool`) 属于整型(`integer`)的一种

#### 1.2.2 字符串

1. 字符串是字符的**序列**，其编码默认为 **Unicode**。

    > 可以使用 `str.encode("ascii")` 将字符串编码转换为 ASCII

2. 可以用**单引号**和**双引号**来指定字符串，**单引号和双引号的意义完全相同**

3. 利用**三引号** `"""` 或者 `'''` 可以指定一个**多行字符串**

    ```python
'''This is a multi-line-string. This is the first line.
And this is the second line.
"What's your name?" I asked.
He said "Bond, James Bond."
'''
    ```
    
    > 在三引号中，可以自由使用单引号和双引号

4. 使用**转义**来表示原有字符

    > 例如 `'What's your name?'` 中，由于（**使用单引号界定的**）字符串中有单引号，会使 Python 解释出现错误，此时需要用转义来表示原有的单引号。
    正确的应该是 `'What\'s your name?'`。
    但是，**可以在用双引号界定的字符串中使用单引号。**
    这个也是正确的 `"What's your name?"`
    
    > 另外，在一行的末尾的反斜杠 `\` 仅仅表示下一行的字符串是上一行的**继续**，**并不增加新的行**
    
    ```python
    # 以下字符串是等价的
    "This is the first line.\
    This is also the first line."
    
    "This is the firstline. This is also the first line."
    ```
    
5. 原始字符串

    > 当需要指定一些字符不被特殊处理时，可以使用 `r` 或者 `R` 附加在字符串前面指定**原始字符串**。
    例如： `r"Newlines are indicated by \n"` 
    此时，**字符串中的所有字符都不会被转义**
    
    > **在正则表达式使用的时候，请尽量使用原始字符串**
    
6. 字符串是**不可变**的
7. 字符串按字面意义连接

    > 如果将两个字符串按字面意义相邻放着，会被自动转为一个字符串

8. `format()` 方法

    > 可以使用 `format()` 方法来通过使用其他信息构建字符串
    
    
    ```
    #!/usr/bin/python
    age = 25
    name = 'Swaroop'
    print('{0} is {1} years old'.format(name, age))

    # 输出为
    # Swaroop is 25 years old.
    ```
    
    > 也可以使用 `format()` 进行格式化输出
    
    ```python
    >>> '{0:.3}'.format(1/3)
    '0.333'
    ```
    
### 1.3 变量

#### 1.3.1 命名

同其他语言的变量命名无多大差别。

1. 不允许数字开头
2. 大小写敏感

#### 1.3.2 类型

Python 变量**不需要声明类型**，但仍然是**强类型**
实际上，Python 的任何一切都称为**对象**

### 1.4 逻辑行和物理行

Python 中**一个逻辑行对应一个物理行**，虽然 Python 也可以使用分号，但是**一般不使用分号**

> 其他语言一般强制要求行尾分号，Python 不推荐分号的使用。

### 1.5 缩进

Python 有着严格的缩进区分，不能随意缩进，**缩进用来标明语句块**
**同一个语句块具有相同的缩进层次**

> Python 使用缩进来表示代码块，**不再使用花括号**

### 1.6 操作符

1. Python 中的 `//` 符号表示**向下取整相除**，而不是单行注释。注释使用 `#` 来开头。
    
    > 注意这里是**向下取整**，而不是**趋零取整**

2. 布尔操作
    - `not` 表示布尔非（相当于 `!`）
    - `and` 表示布尔与（相当于 `&&`）
    - `or` 表示布尔或（相当于 `||`）

    > 有趣的是，不等于仍然使用 `!=` 来表示

3. 优先级

    > 在 Python 中，`lambda` 表达式处在最高优先级，而并非布尔运算
    
## 2. 控制流程

控制流程包括 `if` `for` 和 `while`

Python 的流程控制语句有些特殊

1. 首先，关于流程控制**不使用括号**，只有函数和表达式才使用小括号
2. 使用冒号指示语句块的开头

### 2.1 if 语句

下面是一个 `if` 语句的例子

```python
#!/usr/bin/python
# Filename: if.py

number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    print('Congratualtions, you guessed it!')
    print('But you do not win any prizes!')
elif guess < number:
    print('No, it is a little higher than that')
else:
    print('No, it is a little lower than that')
print('Done')
```

> 几个注意要点：
1. Python 中为了减少缩进，使用 `elif` 来代替 `if...else if...else` 
2. 注意缩进，同样的缩进等级表示了同一个代码块
3. **Python 中没有 `switch` 语句，使用相应的 `if..eles` 结构来替代**
4. **注意不要漏掉冒号**

### 2.2 while 语句

while 语句与其他语言无太大差别，讲几个注意事项
1. **注意不要漏掉 `while` 语句末尾的冒号**
2. `Ture` 和 `False` 代表布尔类型
3. `while` 可以有 `else` 语句，但一般不使用

### 2.3 for 语句

`for` 语句和其他语言有较大区别，以下是 Python 和 Java 语言的对比

```python
# Python
for i in range(0, 4):
    print(i)
```

下面是等价的 Java

```java
// Java
for(int i = 0; i < 4; i++) {
    System.out.println(i);
}
```

实际上 Python 的 `for` 语句更像 Java 中的 `foreach` 语句，下面是两种等价的语法形式

```python
# Python
for word in wordList:
    print(word)
```

下面是 Java 语法表述

```java
// Java
for(word : wordList) {
    System.out.println(word);
}
```

需要注意的几个要点：

1. `range()` 函数的指示区间为**左闭右开**

2. `print()` 函数会**默认打印换行符**
    
    > 通过指示 `end` 来进行单行打印
    `print(word, end='')`
    如果缓冲区中有字符，那么指定 `flush` 为 `True` 来清除缓冲区
    `print(word, end='', flush=True)`

### 2.4 其他流程控制

`break` 和 `continue` 都和其他语言无异


## 3. 函数

### 3.1 函数的定义

函数通过 `def` 关键字来定义。
`def` 后跟一个函数名称，**然后跟一对圆括号**，表示函数。
**注意不要漏掉括号**

```python
#!/usr/bin/python
# Filename: function1.py

def sayHello():
    print('Hello, World!')

sayHello() # 调用函数
```

### 3.2 函数参数

在函数定义的圆括号中可以指定形参。
**注意，不需要声明形参类型**

```python
def printMax(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')
```

> 注意，Python 的方法是 **Pass by reference**

其中 a, b 是形参

> 这里由于形参类型不确定，一般的 IDE 无法进行提示。所以可以使用冒号指明其类型

```python3
def printMax(a:int, b:int):
```

### 3.3 变量作用域

1. 函数内声明的变量称作**局部变量**
2. 可以使用 `global` 语句来调用和**修改函数外部声明的变量**

    > 但是，**不建议使用** `global` 语句。
    应通过其他方式实现。
    
3. 非局部变量

    > 在嵌套定义函数的情况下会遇到。
    通过 `nonlocal` 来调用外部函数定义的变量
    
    ```python
    def funcOuter():
        x = 2
        print('x is ', x)
        
        def funcInner():
            nonlocal x
            x = 5
    ```
    
    > 有毒性，最好不要这么搞
    
### 3.4 默认参数

通过在**函数定义**的时候对**形参进行指定**，可以指定默认参数

```python
def say(message, times = 1):
    print(message * times)
```

**只有形参表末尾的形参才能有默认参数**

```python
def func(a, b = 5) # Correct
def func(a = 5, b) # Wrong
```

### 3.5 关键参数

在**函数调用**的时候对**形参进行指定**，可以**忽略形参顺序**指定实参

```python
def func(a, b = 5, c = 10):
    print('a is ', a, 'and b is ', b, 'and c is ', c)
    
func(3, 7)
func(25, c = 24)
func(c = 50, a = 100)
```

### 3.6 不定参数

通过在**函数定义**的时候使用**星号**标识形参

```python
#!/usr/bin/python
# Filename: total.py

def total(initial = 5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count

print(total(10, 1, 2, 3, vegetables = 50, fruits = 100))
```

> 带一个星号的参数范围内的参数会被收集为一个**列表**
如上面的函数会将 `1, 2, 3` 收集为一个叫做 `numbers` 的列表。

> 带两个星号的参数范围内的参数会被收集为一个**字典**
如上面的函数会将 `vegetables = 50, fruits = 100` 收集为一个叫做 `keywords` 的字典。

### 3.7 Keyword-only 参数

在**带星参数**之后的**普通参数**会成为 Keyword-only 参数，即**只能通过关键参数形式来传递实参**

假如不需要不定参数而又想使用 Keyword-only 参数，那么可以使用**没有名字的空星**，如下所示

```python
>>> def foo(a,b,*,c,d):
...     print(a,b,c,d)
...
>>> foo(1,2,3,4)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: foo() takes exactly 2 positional arguments (4 given)
```

### 3.8 return 语句

Python 的函数**默认为没有返回值**
一个没有返回值的函数的 `return` 语句等价于 `return None`

### 3.9 DocStrings

这一特性很类似 Java 的 javadoc。与 Java 不同的是，Python 的 DocStrings 在**函数的第一个逻辑行处定义**

特点如下：

1. 一个**多行字符串**
2. 以大写字母开头，句号结尾
3. **第二行是空行**

> Python 的每个函数都拥有 `__doc__` 属性，可以通过调用这个属性来显示 DocStrings
在 DocStrings 中可以使用 reStructureText 的格式来实现 Javadoc 中的 `@parma` `@retrun` 功能

```python
def foo(a, b):
    '''This is the foo function
    
    It is just a foo function
    :parma a: This is the parma a
    :type a: int
    :parma b: This is the parma b
    :type b: int
    '''
```

也可以使用 Google 的规范

```pyothon
def module_level_function(param1, param2=None, *args, **kwargs):
    """This is an example of a module level function.

    Function parameters should be documented in the ``Args`` section. The name
    of each parameter is required. The type and description of each parameter
    is optional, but should be included if not obvious.

    Parameter types -- if given -- should be specified according to
    `PEP 484`_, though `PEP 484`_ conformance isn't required or enforced.

    If \*args or \*\*kwargs are accepted,
    they should be listed as ``*args`` and ``**kwargs``.

    The format for a parameter is::

        name (type): description
            The description may span multiple lines. Following
            lines should be indented. The "(type)" is optional.

            Multiple paragraphs are supported in parameter
            descriptions.

    Args:
        param1 (int): The first parameter.
        param2 (Optional[str]): The second parameter. Defaults to None.
            Second line of description should be indented.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        bool: True if successful, False otherwise.

        The return type is optional and may be specified at the beginning of
        the ``Returns`` section followed by a colon.

        The ``Returns`` section may span multiple lines and paragraphs.
        Following lines should be indented to match the first line.

        The ``Returns`` section supports any reStructuredText formatting,
        including literal blocks::

            {
                'param1': param1,
                'param2': param2
            }

    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.


    .. _PEP 484:
       https://www.python.org/dev/peps/pep-0484/

    """
    if param1 == param2:
        raise ValueError('param1 may not be equal to param2')
    return True
```

### 3.10 注解(Annotations)

#### 3.10.1 参数注解

Python 的参数注解定义在**形参声明的位置，与形参以括号间隔，置于参数默认值之前**

```python
def foo(a: "This is param a", b: "This is param b" = 5):
```

#### 3.10.2 返回值注解

Python 的返回值注解定义在**函数头末尾的冒号之前，使用 `->` 和函数头分隔**

```python
def haul(item: Haulable, *vargs: PackAnimal) -> Distance:
```

> 注意，注解可以是字符串，也可以是类型。
可以通过注解实现类型检查

#### 3.10.3 Lambda 表达式

Lambda 表达式不支持注解

## 4. 模块(Module)

模块有点类似 C++ 中的 Namespace，但并不完全相同

### 4.1 导入模块

通过使用 `import` 语句来导入一个模块进行使用

```python
#!/usr/bin/python
# Filename: using_sys.py

import sys

print ('The conmmand line arguments are:')
for i in sys.argv:
    print(i)
    
print('\n\nThe PYTHONPATH is', sys.path, '\n')
```
    
> 在上面的例子中，通过使用 `import sys` 就可以通过 `sys.function` 的形式来调用 sys 模块中的函数和变量。
    
> 用户自定义模块在第一次导入时，会编译成**字节码**文件，这是 Python 处理的，可以提高模块导入的效率。
这些文件以 `.pyc` 为扩展名，如果 Python 没有当前目录的访问权限，那么就不会创建 `.pyc` 文件

> 第三方模块可以通过 Python 自带的 `pip` 进行安装

另外，还可以通过使用 `from...import...` 语句来导入语句；
它和 `import` 语句的唯一区别就是在模块导入之后，不用再在调用的时候填写模块名称。

```python
# Import statement
import sys
print(sys.path)

# From...import... statement
from sys import argv
print(argv)

# If you want to import all the identifiers,
# use this statement.
form sys import *
```

> 注意，`from...import *` 语句**不会导入以双下划线开头的标识符**，如 `__version__`

> 一般来说，**不建议使用 `from...import...` 语句**

### 4.2 创建模块

创建模块最简单的方法就是**编写 .py 文件**；
一个 `.py` 文件就是一个 Python 模块。
例如：

```python
#!/usr/bin/python
# Filename: mymodule.py

__version__ = '0.1'

def sayHi():
    print('Hi')
```

Module Demo:

```python
#!/usr/bin/python
# Filename: mymodule_demo.py

import mymodule

mymodule.sayHi()
print('Version', mymodule.__version__)
```

### 4.3 模块的默认变量

每个模块都有几个默认变量，它们是由 Python 自动构建的；
如 `__name__` 变量，这是**模块的名字**（即 `.py` 文件的名字）

可以使用 `__name__` 变量来检测其自身是否是作为主程序运行

```python
#!/usr/bin/python
# Filename: using_name.py

if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')
```

> `'__main__'` 是主模块的名字，也就是**主程序的文件名**

### 4.4 `dir()` 函数

`dir()` 函数是内建函数，可以通过它来列出模块定义的标识符，包括**函数、类和变量**
如果不提供参数，则返回**当前模块**中定义的名称列表

```python
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
```

> 由此可以看出，主模块具有 `__buitins__` 对象，实际上这就是 Python 的内建函数和类
`dir()` 函数一般不会将内建函数列出，如果需要查看，可以通过 `dir(builtins)` 查看

### 4.5 包(Package)

包是模块的文件夹，其中包含了很多模块；
同时一个包也可以包含**另一个包**。

**一个包必须包含 `__init__.py` 文件，以免 Python 将包识别为普通目录**

可以使用点号来访问到包中的模块

例如：

```
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

> 关于 `__init__.py`:

> 1. 一个包必须包含这个文件
> 2. 这个文件可以是空的，也可以做一些包的初始化工作，比如定义 `__all__` 变量

#### 4.5.1 导入包

包的导入有如下几种形式：

1. 使用 `import` 语句

    > 例如 `import sound.effects.echo`, 将 `sound/effects/echo` 模块导入；
    使用方法为 `sound.effects.echo.echofilter(input, output, delay = 0.7, atten = 4`
    
2. 使用 `from package import item`

    > 在包(Package)层面，**Python 推荐这么导入**，主要的优点在于能够减少没有必要的前缀修饰。
    例如： `from sound.effects import echo` 将 `echo` 模块导入
    使用方法为：`echo.echofilter(input, output, delay = 0.7, atten = 4)`
    
3. 补充：关于 `from package import *` 和 `__all__` 变量

    > `__all__` 变量通常在 `__init__.py` 文件中定义，用于指定**允许 `import *` 识别的标识符**，即允许导出的标识符；
    如果没有指定这个变量，那么在使用 `import *` 时便会自动**忽略以下划线开头的标识符**
    
4. 内包导入

    > 对于**包中的模块**，在可能需要到另一个兄弟包模块的时候，由于它们处在同一个目录结构中，所以可以简单地省略一些前缀。
    Python 在导入包时，首先会搜寻**当前目录**，如果搜索不到，则再到系统 PATH 中进行搜索
    例如 `srround` 想要利用 `echo` 模块，则直接简单地 `import echo` 即可。
    
    > 在 Python 2.5 之后，可以使用**相对路径**进行包导入，例如：
    
    ```python
    # 一个点代表当前目录
    # 两个点代表父目录
    from . import echo
    from .. import formats
    from ..filters import equalizer
    ```

> 目前，Python 推荐使用 `from package import item` 的包层面导入，和 `import module` 的模块层面导入方法，能更好地避免冗余和变量名称冲突。

## 5. 数据结构

### 5.1 列表(list)

列表是用于处理**有序项目**的数据结构，与 Java 的**数组**类似，自带排序方法，可以使用 `[]` 进行**随机访问**

列表使用方括号定义，使用 `len()` 函数来获取列表长度

```python
#!/usr/bin/python

# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print(len(shoplist))

olditem = shoplist[0]
del shoplist[0]
```

> `del` 类似 C++ 中的 `delete`，用于释放一个对象。
这里使用 `del` 来将列表元素移除

### 5.2 元组(tupple)

元组和列表相似，唯一的区别是**元组不可改变**

元组使用**圆括号来定义**

```python
#!/usr/bin/python

# 圆括号是可选的，但是还是加上圆括号为好
zoo = ('python', 'elephant', 'penguin')
print('Number of annimal in the zoo is', len(zoo))

new_zoo = ('monkey', 'camel', zoo)
print('Last annimal in the zoo is', new_zoo[2][2])
```

> 注意到，元组是**可以嵌套的**，有点类似于 Java 中的**二维数组**，但**并不完全相同**。

> `new_zoo[0]` ==> `'monkey'`
`new_zoo[2]` ==> `zoo` ==> `('python', 'elephant', 'penguin')`
`new_zoo[2][2]` ==> `zoo[2]` ==> `'penguin'`

> 含有 0 个或者 1 个元素的元组
含有 0 个元素的元组用**空圆括号**表示，`empty = ()`
含有 1 个元素的元组**要在元素后面接一个逗号** `singleton = (2, )`

### 5.3 字典(dict)

字典是一个**键值对**的表，类似于 Java 中的哈希表，一个项目具有 `Key` 和 `Value`

只能用**不可变**对象作为项目的**键**，值则可以是可变的也可以是不可变的。

字典使用**花括号**定义，用**冒号**分隔键和值，用**逗号**分隔项目，使用 `[]` 来取值。

```python
ab = {
        'Swaroop'   :   'swaroop@swaroopch.com'
        'Larry'     :   'larry@wall.org'
     }
     
     
print("Swaroop's address is", ab['Swaroop'])

for name, adderss in ab:
    # iterate the dict
```

> 在字典中，使用**键**来充当索引成分。
字典可以通过 `items()` 方法来返回键值对的列表，但是是无序的。
注意字典是没有顺序的（不能维持插入时的顺序），要使用时最好先排序。

### 5.4 序列

列表，元组和字符串都是序列，序列具有以下特点：

1. 支持索引操作符 `[]` 随机访问

    > 索引从 0 开始，可以**支持负数**
    当索引是负数时，它会抓取倒数的项目

2. 可以采取**切片操作**

    > 即返回一个序列的子集，例如子数组等
    切片操作通过冒号完成，例如下面的 `shoplist[1:3]`。
    切片操作的区间是**左闭右开**，上面返回的是 `shoplist[1]` 和 `shoplist[2]` 组成的子列表
    假如前一个为空，切片从**序列头**开始，后一个为空，切片在**序列尾**停止。（后一个为空，最后结果**包括最后一个元素**，`shoplist[:]` 返回整个列表）
    
    > 也可以使用**负数**作切片，此时的负数只作为一个定位元素的**索引**，例如 `shoplist[:-1]` 会在**倒数第一个停止**，也就是**不包括最后一个元素的子列表**
    
    > 也可以给切片定义第三个参数——切片的**步长**。其实就是切片操作在遍历数组时的步长。
    步长通过两个冒号的最后一个参数定义
    `shoplist[::3]` ==> `shoplist[0], shoplist[3], shoplist[6]...`

```python
# Indexing or 'Subscription' operation
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# Slicing on a list
print('Item 1 to 3 is', shoplist[1:3]) 
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# Slicing on a string
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])
```

### 5.5 集合

集合是无顺序的简单对象的聚集。

使用集合，可以**检查是否是成员**，**是否是另一个集合的子集**，**得到两个集合的交集**

```python
>>> bri = set(['brazil', 'russia', 'india'])
>>> 'india' in bri 
True
>>> 'usa' in bri 
False
>>> bric = bri.copy() >>> bric.add('china')
>>> bric.issuperset(bri)
True
>>> bri.remove('russia')
>>> bri & bric # OR bri.intersection(bric)
{'brazil', 'india'}
```

### 5.6 引用

这个概念和 Java 中的引用相同。

注意切片操作可以对一个序列进行**深拷贝(deep copy)**

## 6. 类

Python 是高度面向对象的语言，事实上，任何的变量类型都是**类**

### 6.1 创建类

类由 `class` 关键词定义，后面加冒号表示类的作用域

```python
class Person:
    pass
```

### 6.2 self 参数

Python 的 `self` 参数类似于 Java 的 `this`，但是这个参数在 Python 中的作用则更为重要，具体可以看下面的内容

### 6.3 类域

Python 类的域与 Java 不同

1. 不带 `self` 参数修饰的普通变量为**静态变量**
2. 只有带 `self` 修饰的才是对象变量

    > 例如 `self.name` 是对象变量，`name` 是静态变量
    
3. **成员都是公有的，包括数据成员**

    > 但是以双下划线 `__` 开头的成员会被 Python 的名称管理体系作为**私有变量**，这是 Python 的名称管理体系做出的，而不是类的特性

### 6.4 类方法

Python 的类方法和 Java 稍有不同

1. 类的普通方法必须定义 `self` 参数
2. 类块中不带 `self` 参数的方法一般为**静态方法**，需要用 `staticmethod()` 修饰

    ```python
    class Robot:
        '''Represent a robot, with a name'''
    
        def sayHi(self):
            print("hehe")
        
        def howMany():
            print('We have {0:d} robot'.format(Robot.population) )
        howMany = staticmethod(howMany)
    ```
    
    > 静态方法也可以用以下语句修饰
    
    ```python
    @staticmethod
    def howMany():
        print('We have {0:d} robot'.format(Robot.population))
    ```

### 6.5 构造函数和析构函数

Python 拥有构造函数和析构函数。工作原理和 C++ 的构造函数和析构函数相同。

```python
class Person:
    def __init__(self, name):
        self.name = name 
        
    def sayHi(self):
        print('Hello, my name is', self.name)
    
    def __del__(self):
        print("I am dying.")
```

### 6.6 继承

Python 的继承通过在类名称后面添加括号实现。
括号中为父类的名字

```python
class SchoolMember:
    def __init__(self,name,age): 
        self.name = name
        self.age = age
        print('(Initialize SchoolMember:{0})'.format(self.name))
    def tell(self):
        '''Tell my details.'''
        print('Name:"{0}" Age:"{1}"'.format(self.name,self.age),end ='')
        
class Teacher(SchoolMember):
    '''Repressent a teacher.'''
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print('(Initialized Teacher:{0})'.format(self.name))
    
    def tell(self):
        SchoolMember.tell(self)
        print('Salary:"{0:d}"'.format(self.salary))

class Student(SchoolMember):
    '''Represents a student'''
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print('(Initialized Student:{0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks:"{0:d}"'.format(self.marks))

t = Teacher('Mrs.Shrividya',30,30000)
s = Student('Swaroop',25,75)
print() # print a blank line

members = [t,s]
for member in members:
    member.tell() # work for both Teacher and Students
```

> 上面的例子中，`Student` 和 `Teacher` 都继承自 `SchoolMenber`
通过 `SchoolMenber` 调用父类方法

## 7. 输入输出与文件

### 7.1 使用 `input()` 进行输入

Python3 使用 `input()` 函数获取用户输入。

`input()` 函数会返回一个字符串，随后可以使用 `int()` `float()` 等方法将字符串转为对应的类型或者格式

> 在 Python 3 中，`raw_input()` 被整合到 `input()` 函数中，Python 2 的 `input()` 函数的功能被抛弃了。

### 7.2 文件输入输出

与 C++ 和 Java 读取文件流的形式一样，Python 通过使用 `file` 类的函数来对文件进行读取写入

```python
poem = '''\ Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

f = open('poem.txt', 'w') # open for 'w'riting 
f.write(poem) # write text to file
f.close() # close the file
f = open('poem.txt') # if no mode is specified, 'r'ead mode is assumed by default

while True:
    line = f.readline()
    if len(line) == 0: # Zero length indicates EOF
        break
    print(line, end='')

f.close() # close the file
```

> 使用 `open()` 打开文件，模式规则和 C++ 的相同
文件交互完毕后，使用 `close()` 来关闭文件流

### 7.3 pickle 模块

Python 提供了一个 `pickle` 的标准模块，用于将对象储存在文件中，称为对象的持久化保存

```python
#!/usr/bin/python
# Filename: pickling.py

import pickle

# the name of the file where we will store the object
shoplistfile = 'shoplist.data'
# the list of things to buy
shoplist = ['apple','mango','carrot']

# Write to the file
f = open(shoplistfile,'wb')
pickle.dump(shoplist, f) #dump the object to a file f.close()

del shoplist # detroy the shoplist variable

# Read back from the storage
f = open(shoplistfile,'rb')
storedlist = pickle.load(f) # load the object from the file 
print(storedlist)
```

> 注意，持久化保存要求使用**二进制模式**
通过 `dump()` 和 `load()` 就可以对对象进行导入和导出

## 8. 异常

Python 的异常处理和 Java 相似，函数拼写错误等也会触发异常。

### 8.1 处理异常

通过 `try...except` 语句来处理异常

```python
try:
    text = input('Enter something --> ')

except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You entered {0}'.format(text))
```

> `try` 还可以带一个 `else` 语句，作用与 `while` 的语句类似

### 8.2 引发异常

通过 `raise` 语句来引发异常

```python
class ShortInputException(Exception):
'''A user-defined exception class'''
    def __init__(self, length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
try:
    text = input('Enter something-->')
    if len(text) < 3:
        raise ShortInputException(len(text),3)
    #other work can continue as usual here

except EOFError:
    print('Why did you do an EOF on me')

except ShortInputException as ex:
    print('ShortInputException The input was {0} long, excepted \
atleast {1}'.format(ex.length, ex.atleast))

else:
    print('No exception was raised.')
```

### 8.3 Try...Finally 语句

这点与 Java 相似，Python 使用 `finally` 语句来对流进行一些收尾操作

```python
#!/usr/bin/python
# Filename: finally.py

import time 

try:
    f = open('poem.txt')
    while True: # our usual file-reading idiom
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end = '')
        time.sleep(2) # To make sure it runs for a while

except KeyboardInterrupt:
    print('!! You cancelled the reading from the file.')

finally:
    f.close()
    print('(Cleanig up: closed the file)')
```

### 8.4 with 语句

这个语句类似 Java 中的**带资源的 `try` 块**
通过使用 `with` 来打开一个带资源的操作，则其会自动在最后将资源关闭

```python
#!/usr/bin/python
# Filename: using_with.py
with open("poem.txt") as f:
    for line in f:
        print(line,end='')
```

## 9. 高级技巧

### 9.1 函数返回多个值

函数可以通过返回一个**元组**来达到返回多个值的目的。

```python
def get_error_details():
    return (2, 'second error details')

errnum, errstr = get_error_details()
```

> 上面运用到了**元组解包**技术，通过使用逗号分隔变量，就可以分别取出对应位置的元组元素。

### 9.2 特殊方法

Python 的类中有许多内置的特殊方法，例如 `__init__()` 和 `__del__()`

可以在 Python 的参考手册中找到它们以及对应的作用。

### 9.3 单行语句块

如果一个语句块只有一个逻辑行，则可以把它置于条件语句或者循环语句的同一行

```python
if flag: print 'Yes'
```

### 9.4 Lambda 表达式

`lambda` 语句用来创建新的**函数对象**，并且在运行时返回它们。

```python
def make_repeater(n):
    return lambda s: s*n
```

> 本质上, `lambda` 需要一个参数,后面仅跟单个表达 式作为函数体,而表达式的值被这个新建的函数返回。注意,即便是 `print` 语句也不 能用在 `lambda` 形式中,只能使用表达式。

### 9.5 列表综合

通过列表综合，可以从一个已有的列表导出一个新的列表。

```python
#!/usr/bin/python
# Filename: list_comprehension.py

listone = [2,3,4]
listtwo = [2*i for i in listone if i > 2]
```

> 通过在列表中使用这样的语句就可以对符合条件的每个列表元素进行处理
注意原有的列表并没有改变，这个操作实际上是**生成了一个新列表**

### 9.6 `exec` 和 `eval`

`exec` 语句用来执行**字符串形式**的 Python 语句

```
>>> exec('print("Hello, World")')
Hello, World
```

`eval` 语句用来执行**字符串形式**的 Python 表达式

```python
>>> eval('2*3')
6
```

> 两者看似相同，但是也有细微区别：

> 1. `eval` 只接受**单行字符串表达式**，`exec` 可以接受一个语句和语句块
    >> “表达式”所指的就是**可以放在等号右边的东西**，`break` `if` `pass` 等不是表达式

> 2. `eval` 会**返回表达式的结果**，`exec` 则会忽略该结果

### 9.7 `assert` 语句

同 Java 中的 `assert` 语句一样，以调试为目的。
但是 Python 的 `assert` 语句功能是默认启动的
当 `assert` 失败时，会引发一个 `AssertionError`

### 9.8 repr 函数

该函数用来取得对象的规范字符串表示，实际上它的作用就是**为对象包了一层`""`**

```python
>>> i = []
>>> i.append('item')
>>> i
['item']
>>> repr(i)
"['item']"
>>> eval(repr(i))
['item']
>>> eval(repr(i)) == i
True
```