# Scala 简介

<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 flatten:0 bullets:0 updateOnSave:1 -->

[Scala 简介](#scala-简介)   
&emsp;[1. 概述](#1-概述)   
&emsp;[2. 什么是函数式语言](#2-什么是函数式语言)   
&emsp;[3. 没有分号](#3-没有分号)   
&emsp;[4. 面向对象](#4-面向对象)   
&emsp;[4. 变量定义](#4-变量定义)   
&emsp;[5. 函数定义](#5-函数定义)   
&emsp;[6. 使用函数式风格](#6-使用函数式风格)   

<!-- /MDTOC -->

## 1. 概述

Scala 是高层级的，函数式，基于 JVM，完美调用 Java 的编程语言。
其主要特点就是它是一门函数式语言。

语法上，Kotlin 借鉴了其大部分的语法，所以体现出和 Kotlin 非常相似的特征。

同时，由于基于 JVM，所以类型系统和 Java 没有多大区别。

## 2. 什么是函数式语言

函数式语言的两大理念：

1. 函数也是值，可以作为参数，也可以保存在变量中，与其他类型同级
2. 函数只应该接受参数输入，并输出返回值，不应该具有其他副作用

## 3. 没有分号

这里需要说的一个问题是，虽然 Scala 没有分号；

但是当你写长表达式的时候可能会有问题：

```scala
someLongExpression
+ someOtherExpression
```

上面的语句会被隐式加上分号：

```scala
someLongExpression;
+ someOtherExpression
```

这样显然是不符合我们的实际意图的，解决办法有两个：

1. 使用括号

    ```scala
    (someLongExpression
        + someOtherLongExpression)
    ```

2. 将操作符放在行尾

    ```scala
    someLongExpression +
    someOtherExpression
    ```

## 4. 面向对象

Scala 中所有东西都是 **对象**；

操作符实际上是对象的 **方法**

## 4. 变量定义

语法上和 Kotlin 无多大差别

```scala
var x: Int = 0
```

## 5. 函数定义

```scala
def max(x: Int, y: Int): Int = {
    if (x > y) x
    else y
}
```

有趣的是，Scala 中，函数定义需要一个**等号**；

这意味着，函数实际上是一个 **变量**，而函数体实际上是一个 **返回值的表达式**。

同时，函数体 **没有 `return`**，这主要是因为函数体是一个 **表达式**，而一个表达式理应返回其计算得到的值。

这正好体现了函数式编程的思想，函数是一个值，函数体是一个表达式。

## 6. 使用函数式风格

Scala 程序员在解决问题时，应该优先考虑函数式风格而非指令式风格。

简单的判断标准有：

1. 尽量使用 `val` 解决问题

    > 使用 `var` 会让你的 编码层级变低，而函数式编程的一个重要作用就是使你的视野聚焦在高层级中。
2. 尽量避免定义返回 `Unit` 的函数

    > 函数式编程一个理念就是函数体是表达式，而返回 `Unit` (Java 中的 `void`) 的函数一般来说都具有 **副作用** (即函数做了不是生成返回值的工作)
