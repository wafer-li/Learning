# Java Class

Tags: Java

Base on *Core Java Volume Ⅰ——Fundamentals**

[TOC]

---


## 1. 类

△Java语言就是基于类的语言，许多术语与C++稍有区别
C++      |       Java
---|---
函数          |      方法
构造函数       |     构造器
析构函数        |    析构器 
类中的数据   |     实例域
静态数据     |  静态域

> 例如 `String a;`
C++ 称 `String` 为类，而 `a` 为对象，C++ 在此时就分配了内存，构建了对象
Java 称 `String` 为类，`a` 为引用，而当使用 `new` 请求，分配了空间，构建出的数据块称为对象

### 1.0 注意

类对象必须使用new来构建，单纯的声明类仅仅只是声明了类的引用，并没有分配空间

### 1.1 自定义类

1. 一个源文件只能拥有一个 `public` 类，且必须与文件名一致

    > 通过在类的class前缀上public获得这一特性

    >※包含main方法的类才能成为启动类，每个类都可以拥有main方法

2. Java不支持析构函数，反之，会自动进行垃圾回收


3. 所有的方法都要在类的内部进行定义【实际上，任何一个Java程序都是从类开始的】


4. 如果需要返回一个可变对象的引用，应该对其进行克隆（clone）

    >※这是由于变量都是一个指向对象的“类似指针的”引用，有可能会使得数据封装性遭到破坏

5. `final` 修饰符在使用时大多应用于不可修改的类，当应用在可变的类的时候，并不意味着类的内容不可修改
 
    ```
    class Employee
    {
	    private final String name;
    	private final Date hiredate;
    }

    /**
    * 此时，name引用和对象都不能被修改【String类是不可变的类】
    * hiredate所“指向的”对象不能改变，但是，仍然可以通过hiredate来调用对象方法改变对象的实例域
    * 这里的hiredate类似于一个“指针常量”，即“指针所指向的位置不可改变，但是该内存块上所储存的数据却是可以改变的”
    */
    ```
    
6. 通过static声明静态域和静态方法

- 静态域和C++类中的静态变量没有什么区别
- 静态公有常量可以通过类名来直接调用，由于有final限制，所以不会造成封装性破坏

    > ※如Math.PI就是一个静态公有变量
    ※其实也可以通过对象引用来调用，不过一般通过类名调用使得易读性更强
    静态方法可以通过类名和对象引用直接调用，但一般使用类名调用增强易读性

    > ※如 Math.pow(x,y)

- 静态方法只能对对象静态域实施操作，而不能对实例域实施操作
- 通常只有在接受外来参数和调用静态域的时候才使用静态方法

7. 对象的构造

    1. 可以直接在构造器内初始化实例域，即使是包含关系
    2. 通过使用this来实现传参和实例域同名，甚至调用另一个构造器
        ```
        public Class(String name, double salary)
        {
	        this.name = name;
        	this.salary = salary;
        }

        public Class(double s)
        {
	        this("Class * " + nextId, s);
	        nextId++;
        }
        ```

    3. 默认将所有数值初始化为0，布尔值初始化为false，引用初始化为null
    
        > 如果没有提供显式构造器，则系统自动生成隐式（无参）构造器完成上述工作
        如果提供了显式构造器，则系统将不再自动生成无参构造器，上述操作将被视为非法

    4. 初始化块
    
        ※这个不常用，通常使用构造器完成工作
        可以使用一个代码块对实例域进行初始化操作
        ```
        class Class
        {
	        private int id;
	        ....
	
	        {
		        id  = 1;
	        }

        }
        ```
    
        初始化块在所有构造器执行之前执行。
        通过标记关键字static可以对静态域进行初始化块操作
        ```
        static
        {
	        id = 1;
        }
        ```
    
8. 类的基本结构
- 数据域
 - 构造器（constructor）
    - 访问器（getter）
    - 更改器（setter）
    

### 1.2 方法参数

1. Java总是按值传参，对象引用也是一个值
2. 方法不能修改传递给它的实参
3. 方法可以通过调用传入对象引用的对象的方法，实现对对象的修改
4. 方法不能让对象参数引用一个新的对象
5. 方法能够**直接访问和修改**相同类作为参数的对象实例的**私有域**

    ```java
    class Foo {
        private String text;

        public void doStuff(Foo f) {
            System.out.println(f.text);
        }
    }
    ```

### 1.3 包（`package`）

※类似于C++的名称空间

- 通过import语句来导入Java包
- 添加static指令可以直接导入静态方法和静态域，使用的时候就无需使用类名来调用【UnRecommended】
- 通过使用包名来具体访问一个类
- 通过package语句来将类放入包中，通常在开头加入

    ```
    package com.myApp.corejava
    ```

    > 注意包名的命名要与目录树相匹配，即上述类文件必须位于com/myApp/corejava中，否则，最终的程序将无法运行

- 包作用域
    
    - 如果实例域没有指定访问控制符，则这一个部分可以被同一个包的所有方法访问

        > ※在编写类的时候，必须为实例域添加上访问控制符

- 类路径（※好像只有使用Shell编译才会遇到这个问题？）
- javadoc文档注释
    - 以 `/**` 开头，以 `*/` 结尾
    - 可以使用 `HTML` 修饰符
    - 还有各种注释，这里不一一说明

### 1.4 类设计技巧

1. 保证数据私有

2. 一定要对数据初始化，可以直接提供默认值，也可以在构造器中提供

3. 不要在类中使用过多的基本类型，可以通过一个封装类来减少使用
    
    ```
    private String street;
    private String city;
    private String state;
    ```

    > 这个可以通过一个Address类来解决
    
4. 并不是所有的数据都需要访问器和更改器

5. 将职责过多的类进行分解

    > 如果一个类能被拆分成两个或者多个独立的概念，那就进行拆分
    注意这里是概念的拆分，而不是单纯将方法拆分

6. 类名和方法名要能够体现它们的职责

    > 类名常用一个名词或者有定语修饰的名词
    访问器使用小写的get开头
    更改器使用小写的set开头

## 2. 继承

C++ | Java
---|---
基类|父类、超类
派生类|子类

### 2.1 Java 只允许一重继承

 ※可以有多个继承链，但是不能有多个基类

### 2.2 使用 `extends` 来表明继承关系

```
class Derived extends Base
{
	....
};
```

### 2.3 使用 `super` 来调用超类方法

### 2.4 构造器

可以使用 `super` 实现对超类构造器的调用
如果没有显式调用超类构造器，将自动调用超类构造器的隐式版本;
如果没有隐式版本（即超类构造器只定义了显示版本）则报错

### 2.5 多态

1. 可以将超类引用指向子类对象，但不能反过来

    > 基类指针可以指向派生类对象

2. 数组可以进行相反的赋值，所以必须注意元素类型的监督


3. `public` 方法默认为动态绑定，无需添加 `vitual` 或者类似的关键字

    > private、static、final方法为静态绑定

4. 子类方法覆盖超类方法时，其访问权限不能严格于超类方法

    > ※注意不要遗漏public关键字，否则将会被解释成为更严格的访问权限
    
5. 覆盖允许返回类型协变（超类可以协变为子类）

### 2.6 `final` 阻止继承

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
 
### 2.7 强制类型转换

在继承链上不允许进行由上到下的转换（超类不能转换成子类）
使用 `instanceof` 进行转换检查，返回布尔值，表示是否能够成功转换
语法：(要转换的对象) `instanceof` (转换目标)
强制转换语法类似 C 语言，执行过程类似 `dynamic_cast` 操作，不成功则抛出一个异常，而不是生成 `null` 对象

### 2.8 抽象类

```
    abstract class Person {...}   // 抽象类
    public abstract String getDescription();   // 抽象方法
```

> 抽象类不一定要有抽象方法，但是包含抽象方法的类必须声明为抽象类
抽象类可以包含具体数据和具体方法
抽象类不能被实例化（即不能创建对象）

### 2.9 谨慎的使用protected

### 2.10 Object类

#### 2.10.1 `equals()`方法

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

##### 2.10.2 `hashCode()` 方法

如果重新定义了 `equals()` 方法，则必须重新定义 `hashCode()` 方法
`equals()` 与 `hashCode()` 的定义必须一致，如果 `x.equals(y) return true`, 则，`x.hashCode()` 就必须与 `y.hashCode()` 返回一样的值

#### 2.10.3 `toString()` 方法

一般形式：类名 + 方括号括起来的阈值
调用 `x.toString()` 可以用 `""+x` 代替
应该为每一个自定义类提供 `toString()` 方法。

### 2.11 泛型数组列表（`ArrayList<>`）

1. 构造

    ```
    ArrayList<ClassName> staff = new ArrayList<>();
    ```
    
2. 优点：可以实现动态更改数组大小

3. 使用 `add()` 方法添加元素，`remove()` 方法删除元素
4. 使用 `get()` 方法访问元素，`set()` 方法设置元素【而不是使用[]语法】

### 2.12 对象包装器和自动装箱

一般用于将基本类型转换成类对象

首字母大写即为相应的包装器

包装器的比较应使用 `equals()`方法，而不是 `==`
包装器为 `final` 类，不可以用来修改基本数据类型的数值
应使用 `holder` 类型来修改基本数据类型的值

### 2.13 不定参数

```
public static double max(double... values)
```

其中的 `double...` 相同于`double[]`，其实就是接受了一个 `double` 数组
可以将数组传递给可变参数方法的最后一个参数。

### 2.14 枚举类
这里的枚举类是一个类对象，而不是一种类型


### 2.15 继承设计的技巧

1. 将公共操作和域放在超类
2. 不要使用受保护的域
3. 使用继承实现 **“is-a”** 关系
4. 覆盖方法时，不要改变预期的行为

    > 这里说的是不要偏离设计，并不是不能改变基类方法的操作
    
5. 能使用多态就使用多态
6. 不要过多的使用反射

## 3. 接口

这是 Java 中的专有名词，指代的是 **interface** 关键字

### 3.1 接口

```
public interface Comparable {...}
```
    
- 接口不是类，而是对类的一组需求描述
- 接口中的所有方法自动为public
- 实现接口
    - 将类声明为实现给定的接口
    
        ```    
        class Employee implements Comparable {....}
        ```
    
    - 对接口中的所有方法进行定义
    
        > **接口实现必须声明为public**
        
- 特性
    - 不是类，不能使用new来实例化
    - 不能包含实例域和静态方法
    - 可以包含常量，接口中的域被自动设为public static final
    - 可以声明接口的变量
        
        ```
        Comparable x;
        ```
    - 必须引用实现了接口的类对象
    
        ```
        x = new Employee();
        ```

- 可以使用instanceof来检查一个对象是否实现了某个特定接口
    
    ```
    if(anObject instanceof Comparable)
    ```
    
- 可以扩展（**继承**）
    
    ```
    public interface Powered extends Moveable
    ```

- 每个类只能拥有一个超类，但是可以实现多个接口

    ```
    class Employee extends Persons implements Comparable
    ```
    
### 3.2 对象克隆

- 默认克隆（`Object.clone()`）
- 浅拷贝
- protected方法
- 实现克隆
    - 必须实现 `Cloneable` 接口
    - 使用 `public` 重新定义 `clone()` 方法
    - 即使浅拷贝能满足要求，也要进行上述两条操作
    - 需要声明 `CloneNotSupportedException` 异常

## 4. 内部类

```java
class TalkingClock
{
	public class TimePrinter implements ActionListenner
	{
		...
	}
}
```

### 4.1 概述

- 在类的内部直接定义，类似于C++的嵌套类
- 可以访问作用域内的数据，包括私有的
- 可以隐藏内部类
- 可以便捷实现回调

### 4.2 普通内部类

- 可以访问外围类对象数据（包括私有的）
- 通过OuterClass.this访问外围类
- 在外围类的作用域之外，使用OuterClass.InnerClass引用内部类

### 4.3 局部内部类

- 简称局部类，在一个方法内进行定义

    ```java
    public void start()
    {
	    class TinmePrinter implements ActionListenner
	    {
		    ...
	    }
    }
    ```
- 局部类可以访问局部变量（必须声明为 `final`）
- 更新封闭作用域内的计数器时，使用 `final` 的长度为 $1$ 的数组

### 4.4 匿名内部类

```java
new SuperType(cosntruction parameters)
	{
		...	
	}
如果只创建局部类的一个对象的时候才使用
```

- SuperType可以是类或者接口
- 如果用于实现接口时，不能有任何构造参数
 
```java
new InterfaceType()
	{
		...
	}
```

### 4.5 静态内部类

- 用于将一个类隐藏在另一个类之中，通常用于防止名称的冲突
- 只有内部类可以声明为static
- 特别的，通过静态方法构造的内部类必须声明为static


