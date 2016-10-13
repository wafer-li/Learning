# Kotlin Basic

Tags: Kotlin

---

[TOC]

---

## 1. 基本语法

### 1.1 变量定义

1. 使用 `val` 定义**常量**（只读）

    ```
    val a: Int = 1
    val b = 1   // 类型可以被自动推断
    val c: Int  // 如果没有进行变量初始化，则需要指定变量类型
    c = 1
    ```
    
    > 注意，kotlin 取消了分号
    
2. 使用 `var` 定义变量

    ```
    var x = 5
    x += 1
    ```

### 1.2 注释

与 Java 相同，单行注释使用 `//` ，多行注释使用 `/* */`

不同的是，kotlin 中允许注释块嵌套。

## 2. 编码规范

### 2.1 命名风格

命名风格和 Java 相同。

- 类名采用大驼峰
- 函数、方法、变量采用小驼峰
- 使用 4 空格缩进
- 公有方法和函数必须加上 KDoc

### 2.2 关于冒号

冒号在分隔两个类型的时候，**前后都要有空格**

其余情况，只需后有空格即可。

```
interface Foo<out T : Any> : Bar {
    fun foo(a: Int): T
}
```

### 2.3 Lambda 表达式

在使用 lambda 表达式时，lambda 表达式应与花括号有空格分隔。

lambda 表达式应尽量的短。

```
list.filter { it > 10 }.map { element -> element * 2 }
```

### 2.4 关于 Unit

当一个函数返回 `Unit` 类型时，应将其省略。

类似于 Java 中的返回值为 `void`

## 3. 基本类型

Kotlin 中，任何事物都是对象。

### 3.1 数字类型

Kotlin 中的数字类型有 `Double`、`Float`、`Long`、`Int`、`Short`、`Byte`

#### 3.1.1 位宽

Type| BitWidth
:---:|:---:
Double| 64
Float| 32
Long| 64
Int | 32
Short| 16
Byte| 8

> 注意，在 Kotlin 中，**字符不是一种数字类型**

#### 3.1.2 字面常量

数字类型可以有多种字面表示形式。

1. 整数
- 十进制数字 `123`
    - `Long` 类型通过加 `L` 后缀实现: `123L`
- 十六进制 `0x0F`
- 二进制 `0b00001011`

2. 浮点数
    - 默认为 `Double` 类型: `123.5`, `123.5e10`
    - 使用 `f` 或者 `F` 后缀来表示 `Float`: `123.5f`

#### 3.1.3 表示法

Kotlin 中，任何数字都会被**自动装箱**

```
val a: Int = 10000
print(a === a) // true
val boxedA: Int? = a // 在类型后加 ? 表示一个 Nullable 对象
val anotherBoxedA: Int? = a
print(boxedA === anotherBoxedA) // false
print(boxedA == anotherBoxedA) // true
```

> 上面是一个很好的例子，由于所有的数字都会被自动装箱，所以 **`boxedA` 与 `anotherBoxedA` 不一致**。
但是由于两者均指向 `a`，所以保持了相等性。

> 这里的 `Int` 与 Java 的 `Integer` 相同

#### 3.1.4 转换

Kotlin 的原则之一就是尽量让事务明显化。
所以，Kotlin **禁止隐式转换**，就算是隐式向上转换也是不允许的。

```
val a: Int? = 1
val b: Long? = a
print(a == b) // false
```

> 由于 `Int` 不是 `Long` 的子类，而且禁止隐式转换，所以即使 `b` 指向了 `a`，它们也不相等。

```
val b: Byte = 1 // OK
val i: Int = b // ERROR
```

> 字面值会经编译器静态检查赋值给整数形式的变量，但是由于禁止隐式转换，第二个语句会产生 ERROR。

需要转换时，应采用内置的转换方法

- `toByte()`
- `toShort()`
- `toInt()`
- `toLong()`
- `toFloat()`
- `toDouble()`
- `toChar()`

#### 3.1.5 位运算符

Kotlin 支持全套 Java 的普通数字运算符。
但关于位运算符则稍有不同，Kotlin 采用**单词型**而非 Java 的**符号型**位运算符。

下面是 Kotlin 的位运算符列表

- `shl(bits)` => 位左移，相当于 Java 的 `<<`
- `shr(bits)` => 位右移，相当于 Java 的 `>>`
- `ushr(bits)` => 无符号数右移，相当于 Java 的 `>>>`
- `and(bits)` => 按位取与操作，相当于 Java 的 `&`
- `or(bits)` => 按位取或操作，相当于 Java 的 `|`
- `xor(bits)` => 按位取异或操作，相当于 Java 的 `^`
- `inv()` => 按位取反操作，相当于 Java 的 `~`


### 3.2 字符类型

字符类型使用 `Char` 来表示，**字符不是数字**。

```
fun check(c: Char) {
    if (c == 1) // ERROR
}
```

字符使用单引号括起来`'1'`，反斜杠 `\` 表示转义，转义字符和 Java 相同。

和数字类型一样，字符类型也被自动装箱，保持相等性，而不保持一致性。

### 3.3 布尔类型

使用 `Boolean` 来表示布尔类型，布尔类型有两个值，`true` 和 `false`。

内置的逻辑布尔操作与 Java 相同。

### 3.4 数组

使用 `Array` 表示数组，这是一个泛型类，类似于 Java 中的 `ArrayList<T>`，但并不完全相同。

数组是 **invariant** 的，也就是说不能把 `Array<String>` 的数组赋予 `Array<Any>` 的实例，这会产生一个**runtime failure**

> Kotlin 同样拥有 `List` 和 `ArrayList` 类型，在 JVM 上，`Array` 会被替换成 Java array。

> 所以，事实上 `Array` 只是 


#### 3.4.1 创建数组

使用 `arrayOf()` 创建数组。

```
val array = arrayOf(1, 2, 3)
val nullArray = arrayOfNulls(5) // Array with 5 null elements
```

> 注意变量具有自动推断功能，类似 C++ 中的 `auto`

也可以使用 `Array()` 创建数组。

```
// Crates an Array<String> with values
// ["0", "1", "4", "9", "16"]
val asc = Array(5, {i -> (i * i).toString()})
```

Kotlin 内置了一些特定的数组类型，如 `IntArray`, `ByteArray` 等。

```
val x: IntArray = intArrayOf(1, 2, 3)
```

#### 3.4.2 访问数组

`Array` 内置了 `get()` 和 `set()` 方法和 `size` 属性。
但是也支持使用方括号进行访问的操作 `[]`

#### 3.4.3 多维数组

```
val int2d: Array<IntArray>
int2d = arrayOf(intArrayOf(1, 2, 3), intArrayOf(4, 5, 6), intArrayOf(7, 8, 9))
```


### 3.5 字符串

使用 `String` 来表示字符串。与 Java 一样，字符串是一个不可变对象。

#### 3.5.1 相对 Java 增加的新特性

与 Java 不同的是，Kotlin 支持使用方括号 `[]` 来获取字符串中的字符，同时也支持对字符串字符进行遍历。

```
for (c in str) {
    println(c)
}
```

#### 3.5.2 raw string

此外，Kotlin 还吸收了 Python 的多行字符串特性，使用三个双引号来表示一个 **raw string**，raw string 不接受转义，其中任何的字符都是字面字符。

```
val rawString = """
    This is a raw string.
    \n and \t will be displayed as
    its literal stirng.
"""
```

#### 3.5.3 字符串模板

Kotlin 字符串具有模板功能，使用 `$` 来指定参数
例如：

```
val i = 10
val s = "i = $i" // evaluates to "i = 10"
```

也可以使用花括号 `{}` 来获取**对象的属性**填充到字符串中。
例如：

```
val s = "abc"
val str = "$s.lenth is ${s.lenth}" //  evaluates to "abc.length is 3"
```

需要注意的是，字符串的模板功能不仅可以在普通字符串中使用，同时**也可以在 raw string 中使用。**

此时，如果需要表示 `$` 美元符号，必须使用以下表达式：

```
var price = """
${'$'}9.99
"""
```

> 这里使用双引号`${"$"}`也是可以的，模板引用一个字面量时，结果就是它本身。

## 4. 包和导入

Kotlin 中的包和导入与 Java 区别不大。

另外增加了 `as` 关键字用于赋予别名给类和函数，以防出现名称冲突。
同时，Kotlin 中没有 Java 中的 `import static` 语句，所有的导入均使用 `import` 进行。

## 5. 控制流程

### 5.1 If

Kotlin 中 `if` 语句是一个表达式，**有返回值**，功能和 C++ 和 Java 中的**条件表达式**相同。

所以，Kotlin 中不支持条件表达式，因为 `if` 语句已经具备了这个功能。

```
// Traditional usage
var max = a if (a < b)
max = b
// With else
var max: Int if (a > b)
max = a
else
max = b
// As expression
val max = if (a > b) a else b
```

同时，`if` 表达式也支持**语句块**，语句块中的**最后一个**变量或常量的值就是语句块的返回值。

```
val max = if (a > b) { print("Choose a") a
}
else {
    print("Choose b")
b }
```

需要注意的是，**如果 `if` 作为一个表达式（需要其返回值），那么 `else` 语句就必须存在**。

### 5.2 When

Kotlin 用 `when` 表达式替代了 Java 和 C++ 中的 `switch` 语句的功能。

一个简单的 `when` 语句如下：

```
when (x) {
1 -> print("x == 1")
2 -> print("x == 2")
else -> { // Note the block
    print("x is neither 1 nor 2")
  }
}
```

与 `if` 语句一样，`when` 语句也可以作为表达式；当 `when` 作为表达式时，它的返回值是与其 case 相符的值。

同样，`when` 作为表达式时，也可以使用**块语句。**

与 Java 不同的是，`when` 语句可以对于一些不同的 case 进行一些相同的相应，而使用较少的代码量。

```
when (x) {
    0, 1 -> print("x == 0 or x == 1") 
    else -> print("otherwise")
}
```

同时， `when` 语句的 case 可以使用**随意的表达式**，而不是 Java 中的仅能使用常量。

```
when (x) {
    parseInt(s) -> print("s encodes x") 
    else -> print("s does not encode x")
}
```

此外，也可以使用 `in`、`!in`、`is`、`!is` 进行**范围**和**类型**检测。

```
when (x) {
    in 1..10 -> print("x is in the range")
    in validNumbers -> print("x is valid")
    !in 10..20 -> print("x is outside the range") 
    else ->     print("none of the above")
}
```

```
val hasPrefix = when(x) {
    is String -> x.startsWith("prefix") 
    else -> false
}
```

Kotlin 在这里拥有一个非常好的特性叫 **smart casts**，
当一个 `is` 表达式满足时，变量 `x` 将被**自动 cast 到相应的类型，**调用相应类型的方法。

最后，`when` 也可以不接受参数使用，此时，`when` 的各个分支条件就变成了简单的**布尔表达式**，可以用于替代 `if-else-if` 结构。

```
when {
    x.isOdd() -> print("x is odd") 
    x.isEven() -> print("x is even") 
    else -> print("x is funny")
}
```

### 5.3 For 

Kotlin 中的 `for` 类似 Python 和 Java 中的 `for-each` 结构，使用 `in` 标识符来分隔 `item` 和 `collection`。

```
for (item in collection) [}
    print(item)
}
```

如果需要使用一个索引值，则可以使用 `indices`，它内置在 Kotlin 中的所有 `collection` 中。

```
for (i in array.indices)
    print(array[i]);
```

同时也可以使用 `withIndex()` 方法。

```
for ((index, value) in array.withIndex())
    print("$index, $value")
```

### 5.4 While 和 do-while

这两者和 Java 没有区别。

### 5.5 跳转

Kotlin 支持三种形式的跳转：

- `return`：在最近的函数（包括匿名函数）返回
- `break`：跳出当前最近的循环
- `continue`：结束当前最近循环内工作，并从下一次最近循环开始

与 Java 一样，Kotlin 也支持**带标签的跳转**，标签使用 `@` 符号来指定。

```
loop@ for (i in 1..100) { 
    for (j in 1..100) {
        if (...) break@loop
    } 
}
```

带标签的 `break` 用于跳出指定的循环结构，而带标签的 `continue` 则用于开始下一次指定的循环。

#### 5.5.1 带标签的 return

不仅如此，Kotlin 还支持带标签的 `return`，这主要是因为 Kotlin 允许**函数的嵌套。**

一个比较普遍的使用场景是在 Lamda 表达式上。

```
fun foo() { 
    ints.forEach { 
        if (it == 0) return
        print(it) 
    }
}
```

类似如上的语句，`return` 的作用对象是其最近的**函数**，在这里是 `foo()`。

但是如果我们要只从 Lambda 函数中返回(`forEach`)，则需要指定一个标签。

```
fun foo() { 
    ints.forEach lit@ {
        if (it == 0) re turn@lit
        print(it) 
    }
}
```

一个更为常用的形式是**直接使用 Lambda 表达式的名字**。

```
fun foo() { 
    ints.forEach {
        if (it == 0) return@forEach
        print(it) 
    }
}
```

另外的，我们也可以使用传统的匿名函数，来实现这个功能。

```
fun foo() { 
    ints.forEach(fun(value: Int) {
        if (value == 0) return
        print(value)
    })
}
```

当需要返回某个值时，标签的解析具有更高优先权。

例如：

```
return@a 1
```

表示在 `a` 标签中返回 `1`，而不是返回 `@a 1`
