# Kotlin 枚举类

Tags: Kotlin

---

<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 flatten:0 bullets:0 updateOnSave:1 -->

[Kotlin 枚举类](#kotlin-枚举类)  
&emsp;[1. 概述](#1-概述)  
&emsp;[2. 声明](#2-声明)  
&emsp;[3. 初始化](#3-初始化)  
&emsp;[4. 匿名类](#4-匿名类)  
&emsp;[5. 创建枚举](#5-创建枚举)  

<!-- /MDTOC -->

---

## 1. 概述

事实上，Kotlin 的枚举和 Java 一样，只是提供了一个类型限定范围。

而如果要使用在 `switch`，都必须使用 `valueOf()` 方法，同时使用 try-catch。

> 当然，在 Kotlin 中，可以使用 sealed clasdd 来方便的实现需要 switch 的情景。


## 2. 声明

```
enum class Direction {
  NORTH, SOUTH, WEST, EAST
}
```

## 3. 初始化

与 Java 一样，枚举类也可以被初始化

```
enum class Color(val rgb: Int) {
    RED(0xFF0000),
    GREEN(0x00FF00),
    BLUE(0x0000FF)
}
```

## 4. 匿名类

每一个枚举项都能拥有它自己的匿名类和重载方法。

```
enum class ProtocolState {
  WAITING {
    override fun signal() = TALKING
  },

  TALKING {
    override fun signal() = WAITING
  };

  abstract fun signal(): ProtocolState
}
```

## 5. 创建枚举

创建枚举和 Java 相同，只能使用 `valueOf()` 方法。
而且，此方法在参数不符合枚举值时，会抛出异常。

同时 Kotlin 也提供了 `values()` 方法来遍历所有的枚举值。
