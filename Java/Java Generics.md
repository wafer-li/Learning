# Java Generics

Tags: Java

Base on *Core Java Volume Ⅰ——Fundamentals**

---

<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 flatten:0 bullets:0 updateOnSave:1 -->

[Java Generics](#java-generics)   
&emsp;[0. 概述](#0-概述)   
&emsp;[1.泛型类](#1泛型类)   
&emsp;[2.泛型方法](#2泛型方法)   
&emsp;[3.类型变量的限定](#3类型变量的限定)   
&emsp;[4.泛型类的实例化](#4泛型类的实例化)   
&emsp;&emsp;[4.1 类型擦除](#41-类型擦除)   
&emsp;&emsp;[4.2 翻译泛型表达式](#42-翻译泛型表达式)   
&emsp;&emsp;[4.3 泛型方法的实例化和桥方法](#43-泛型方法的实例化和桥方法)   
&emsp;&emsp;[4.4 约束和局限性](#44-约束和局限性)   

<!-- /MDTOC -->

---

## 0. 概述

泛型类似于 C++ 中的模板，使得编写的代码可以被多种不同的对象所使用。

在 Java 增加泛型类之前，泛型实际上是以**继承**方式实现的

泛型使用类型参数来指示元素的类型

```java
ArrayList<String> files = new ArrayList<String>();

// Java SE 7 之后可以省略构造函数中的泛型类型
ArrayList<String> files = new ArrayList<>();
```

## 1.泛型类

1. 单个参数

    ```java
    // 其中 T 为类型参数
    public class Pair<T> {
        private T first;
        private T second;

        public Pair() {
            first = null;
            second = null;
        }

        public T getFirst() {
            return this.first;
        }

        public T getSecond() {
            return this.second;
        }
    }
    ```

2. 多个参数

    ```
    // 多个类型参数用逗号隔开
    public class Piar<T, U> {
        ....
    }
    ```

## 2.泛型方法

泛型方法不仅只存在于泛型类中，也可以在非泛型类中定义泛型方法

```java
class ArrarAlg {

    /**
    * 这是一个泛型方法，
    * <T> 表示其为泛型方法
    */
    public static <T> T getMiddle(T... a) {
        return a[a.lenth / 2];
    }
}
```

调用泛型方法时，通过在**方法名前**的尖括号中放入具体的类型来将其实例化

```java
String middle = ArrayAlg.<String>getMiddle("John", "Q.", "Public");
```

其实大多数情况下，编译器都能推断出正确的类型，所以方括号可以省略

## 3.类型变量的限定

有时候我们需要对类型变量进行一定的约束:
比如，当我们需要对变量进行比较操作时，我们需要确保变量都实现了 `Comparable` 接口。

对于类型变量的限定有两种方式

1. 限定上界

    ```java
    public static <T extends Comarable> T min(T[] a) ...
    ```

    > 这里我们限定了 T 必须是实现了 Comarable 接口的变量。
    如果 Comarable 是一个类，那么 T 必须是它，或者它的子类

2. 限定上界

    ```java
    public static <T super Child> T doSomeThings(T[] a) ...
    ```

    > 这里限定了 T 必须是 Child 的超类，或者它本身。

## 4.泛型类的实例化

### 4.1 类型擦除

Java 中的泛型类采用 **类型擦除** 方式来进行实例化。

> 类型擦除即为，擦除类型参数，并将其替换为限定的类型。
如果类型没有被限定，则替换为 `Object`

需要注意的是，虚拟机中没有泛型类型变量，任何的泛型类在需要实例化的时候，都会先进行**类型擦除**，然后替换为实例化的类型。

例如， `Pair<T>` 的原始类型如下

```java
public class Pair {
    private Object first;
    private Object second;

    public Pair() {
        first = null;
        second = null;
    }

    public Object getFirst() {
        return this.first;
    }

    public Object getSecond() {
        return this.second;
    }
}
```

通过类型擦除的方法，Java 使得泛型类就好像一个普通的类，从而避免了 C++ 模板实例化所造成的代码膨胀。

### 4.2 翻译泛型表达式

当程序调用泛型方法时， Java 采用强制类型转换（Cast）来返回或调用正确的类型

例如

```java
Pair<Employee> buddies = ...;
Employee buddy = buddies.getFirst();
```

此时，编译器自动插入强制类型转换使得 `getFirst()` 方法返回 `Employee` 类型

### 4.3 泛型方法的实例化和桥方法

泛型方法在实例化过程中也使用 **类型擦除**
但是这在继承中会导致方法的冲突。

例如：

```java
class DateInterval extends Pair<Date> {
    public void setSecond(Date second) { ... }
}

// 经过类型擦除之后
class DateInterval extends Pair {
    public void setSecond(Date second) { ... }
}
```

当使用基类指针实现多态性的时候

```java
Pair<Date> pair = interval;
pair.setSecond(aDate);
```

此时，存在一个从 `Pair` 继承而来的方法

```java
public void setSecond(Object second)
```

由于**形式参数的改变**，使得这是一个不同的方法；
但是我们对 `pair` 的多态性描述显然是要调用 `setSecond(Date second)` 方法；
此时，编译器就会自动生成一个桥方法，用来保证多态的正确使用。

```java
// 桥方法
public void setSecond(Objedt second) {
    setSecond((Date) second);
}
```

### 4.4 约束和局限性

1. 不能用基本类型实例化类型参数

    由于泛型使用**类型擦除**来实现，所有的未限定类型均会被替换成 `Object`；
    而 `Object` 不能储存基本类型

    > 此时一般使用对象包装器来实现基本类型的实例化

2. 运行时的类型查询只适用于原始类型

    由于使用了类型擦除，所有的类型查询都只对泛型类的**原始类型**适用，而对泛型版本不适用。
    `instanceof` 和 `getClass()` 返回的都是原始类型

3. 不能创建参数化类型的数组

    创建泛型类的**数组**是不合法的。
    由于类型擦除的存在，所有的未限定泛型类都会被替换成 `Object`
    例如

    ```java
    Pair<String>[] table = new Pair<String> [10];   // ERROR
    // After erase
    Pair[] table = new Pair[10];
    ```

    此时，如果有下面的一条语句

    ```java
    Object[] objects = table;   // OK, Pair is a type of Object

    // But, if edit one of the elements
    objects[0] = "Hello";   // ERROR, because the objects[0] is Pair, not String
    ```

    > 当需要收集参数化类型对象时，使用 `ArrayList` 来代替数组实现

4. Varargs 警告

    当使用可变参数的泛型类作为形参时，由于可变类型是一个数组，此时违反了上面一条规则，但是对于这种情况，规则有所放松，使用这个会得到一个**警告**，可以用 `@SafeVarargs` 注解来压制这个警告

5. 不能实例化类型变量

    所谓的类型变量指的是 `T`
    不能使用  `new T(...)` 类似这样的表达式
    而是通过反射调用 `Class.newInstance`

6.
