# Java Class Inheritance

<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 flatten:0 bullets:0 updateOnSave:1 -->

[Java Class Inheritance](#java-class-inheritance)   
&emsp;[0. 概述](#0-概述)   
&emsp;[1. Java 只允许一重继承](#1-java-只允许一重继承)   
&emsp;[2. 使用 `extends` 来表明继承关系](#2-使用-extends-来表明继承关系)   
&emsp;[3. 使用 `super` 来调用超类方法](#3-使用-super-来调用超类方法)   
&emsp;[4. 构造器](#4-构造器)   
&emsp;[5. 多态](#5-多态)   
&emsp;[6. `final` 阻止继承](#6-final-阻止继承)   
&emsp;[7. 强制类型转换](#7-强制类型转换)   
&emsp;[8. 抽象类](#8-抽象类)   
&emsp;[9. 谨慎的使用protected](#9-谨慎的使用protected)   
&emsp;[10. Object类](#10-object类)   
&emsp;&emsp;[10.1 `equals()`方法](#101-equals方法)   
&emsp;&emsp;[10.2 `hashCode()` 方法](#102-hashcode-方法)   
&emsp;&emsp;[10.3 `toString()` 方法](#103-tostring-方法)   
&emsp;[11. 泛型数组列表（`ArrayList<>`）](#11-泛型数组列表（arraylist）)   
&emsp;[12. 对象包装器和自动装箱](#12-对象包装器和自动装箱)   
&emsp;[13. 不定参数](#13-不定参数)   
&emsp;[14. 枚举类](#14-枚举类)   
&emsp;[15. 继承设计的技巧](#15-继承设计的技巧)   

<!-- /MDTOC -->

## 0. 概述

C++ | Java
---|---
基类|父类、超类
派生类|子类

## 1. Java 只允许一重继承

 ※可以有多个继承链，但是不能有多个基类

## 2. 使用 `extends` 来表明继承关系

```
class Derived extends Base
{
	....
};
```

## 3. 使用 `super` 来调用超类方法

## 4. 构造器

可以使用 `super` 实现对超类构造器的调用
如果没有显式调用超类构造器，将自动调用超类构造器的隐式版本;
如果没有隐式版本（即超类构造器只定义了显示版本）则报错

## 5. 多态

1. 可以将超类引用指向子类对象，但不能反过来

    > 基类指针可以指向派生类对象

2. 数组可以进行相反的赋值，所以必须注意元素类型的监督


3. `public` 方法默认为动态绑定，无需添加 `vitual` 或者类似的关键字

    > private、static、final方法为静态绑定

4. 子类方法覆盖超类方法时，其访问权限不能严格于超类方法

    > ※注意不要遗漏public关键字，否则将会被解释成为更严格的访问权限

5. 覆盖允许返回类型协变（超类可以协变为子类）

## 6. `final` 阻止继承

1. `final` 类

    ```
    final class Excutive extends Manager
    ```

    > 这种类型被称为final类，不允许定义子类，即无法继承

2. `final` 方法

    ```
    public final String getName() {...}
    ```
    > 这种方法称为final方法，这种方法不允许子类覆盖它，确保其不会在子类中改变语义

**注意 `final` 的位置不同**

## 7. 强制类型转换

在继承链上不允许进行由上到下的转换（超类不能转换成子类）
使用 `instanceof` 进行转换检查，返回布尔值，表示是否能够成功转换
语法：(要转换的对象) `instanceof` (转换目标)
强制转换语法类似 C 语言，执行过程类似 `dynamic_cast` 操作，不成功则抛出一个异常，而不是生成 `null` 对象

## 8. 抽象类

```
    abstract class Person {...}   // 抽象类
    public abstract String getDescription();   // 抽象方法
```

> 抽象类不一定要有抽象方法，但是包含抽象方法的类必须声明为抽象类
抽象类可以包含具体数据和具体方法
抽象类不能被实例化（即不能创建对象）

## 9. 谨慎的使用protected

## 10. Object类

### 10.1 `equals()`方法

- 特性
    - 自反：`x.equals(x) return true`
    - 对称：`y.equals(x) = x.equals(y)`
    - 传递：`if (x.equals(y) && y.equals(z)) then x.equals(z);`
    - 一致：`The return value of x.equals(y) should be stable;`

对于非空引用 `x`, `x.equals(null) return false;`

`Object` 类 `equals`：**判断两个对象是否具有相同的引用**

- equals方法的设计理念

    1. 接受一个Object类参数（为了覆盖Object类的equals方法）
    2. 检测是否为自身
        `this == otherObject`
    3. 检测传参是否为null
    4. 比较是否为同一个类

        > 如果子类有特有的equals概念，则使用getClass方法
        `if(getClass() != otherObject.getClass()) return false;`
        如果子类没有特有的equals概念，则使用instanceof方法
        `if(!(otherObject instanceof ClassName)) return false;`

    5. 转换为相应的类变量

    > 由于接受的是一个Object变量，所以必须进行强制类型转换才能进行具体实例域的相等判定
    此时已经判别类型相同了，可以进行转换

6. 判别实例域

    > △如果在子类中重新定义equals，则先调用超类的equals

### 10.2 `hashCode()` 方法

如果重新定义了 `equals()` 方法，则必须重新定义 `hashCode()` 方法
`equals()` 与 `hashCode()` 的定义必须一致，如果 `x.equals(y) return true`, 则，`x.hashCode()` 就必须与 `y.hashCode()` 返回一样的值

### 10.3 `toString()` 方法

一般形式：类名 + 方括号括起来的阈值
调用 `x.toString()` 可以用 `""+x` 代替
应该为每一个自定义类提供 `toString()` 方法。

## 11. 泛型数组列表（`ArrayList<>`）

1. 构造

    ```
    ArrayList<ClassName> staff = new ArrayList<>();
    ```

2. 优点：可以实现动态更改数组大小

3. 使用 `add()` 方法添加元素，`remove()` 方法删除元素
4. 使用 `get()` 方法访问元素，`set()` 方法设置元素【而不是使用[]语法】

## 12. 对象包装器和自动装箱

一般用于将基本类型转换成类对象

首字母大写即为相应的包装器

包装器的比较应使用 `equals()`方法，而不是 `==`
包装器为 `final` 类，不可以用来修改基本数据类型的数值
应使用 `holder` 类型来修改基本数据类型的值

## 13. 不定参数

```
public static double max(double... values)
```

其中的 `double...` 相同于`double[]`，其实就是接受了一个 `double` 数组
可以将数组传递给可变参数方法的最后一个参数。

## 14. 枚举类
这里的枚举类是一个类对象，而不是一种类型


## 15. 继承设计的技巧

1. 将公共操作和域放在超类
2. 不要使用受保护的域
3. 使用继承实现 **“is-a”** 关系
4. 覆盖方法时，不要改变预期的行为

    > 这里说的是不要偏离设计，并不是不能改变基类方法的操作

5. 能使用多态就使用多态
6. 不要过多的使用反射