# Java Learning 

>※Base on 《Core Java Volume Ⅰ——Fundamentals》
※The Simple Contents Only Compare To C++

Tags: Programming-Learning Java

[TOC]

---

##变量和数据类型
1、boolean【Java】 = bool【C ++】

2、所有的变量都要被初始化，最好在声明的时候就对其赋值
```java
double n = 0.0;		//Recommended
```
3、使用final关键字指定常量

4、注意所有的变量都是对于真正的数据类型的引用，这个对于大型数据类型来说更为明显

    - 数组和对象名都是对于真正的数组或者对象的引用，而不是其自身
    - 【这里的“引用”类似于指针，而不是对象的别名】
 
**5、数组和对象都要使用new来声明构建，Java会自动进行垃圾处理，因而不需要显式delete**

>※数组的声明：int[] a = new int[100];
※类的构建：Class a = new Class(...);
    
>※注意只有使用了new才会分配空间和构建对象，单纯的声明int[] a 类似于声明一个指向数组的指针
※Java对于大型数据类型只有通过new来构建，int a [100] 这种语法将不被接受，对于数组还可以使用列表初始化的语法int[] a = {1,2,3,4,6};
    
6、Java允许数组长度为0 **（注意这里和null并不同）**

##作用域

1、Java不允许在嵌套的代码块内声明同名变量

> ※所以尽量保证变量的名称不重复【在同一个包(package)内】

##控制流程

1、for循环中，Java要求在三个部分对同一计数器变量进行初始化，检测和更新

2、可以使用break label的形式来跳出多重嵌套循环
```java
//例如
label:
for()
{
	for()
	{
		for()
		{
			if()
			{
				break label;
			}
		}
	}
}

//break语句使得程序跳转到带标签的语句块末尾
//即最外层的for循环的末尾
```

**3、for each循环，可以依此处理数组（或其他形式的集合）的每个元素，而不需要在意下标值**
```
//语法
for(variable : colletion)
{
	//statement
}

//依次打印数组内字符
a[]  = new int [100];
....
for(int element : a)
{
	System.out.println(element);
}
```

##类

>△Java语言就是基于类的语言，许多术语与C++稍有区别
C++      =>       Java
函数                方法
构造函数            构造器
析构函数            析构器 
类中的数据        实例域
静态数据       静态域

>例如 String a;

>C++ 称String 为类，而a为对象，C++在此时就分配了内存，构建了对象
Java称String为类，a为引用，而当使用new请求，分配了空间，构建出的数据块称为对象

###1、类对象必须使用new来构建，单纯的声明类仅仅只是声明了类的引用，并没有分配空间

###2、自定义类
####1)一个源文件只能拥有一个public类，且必须与文件名一致（通过在类的class前缀上public获得这一特性）

>※包含main方法的类才能成为启动类，每个类都可以拥有main方法

####2)Java不支持析构函数，反之，会自动进行垃圾回收
<br/>
####3)所有的方法都要在类的内部进行定义【实际上，任何一个Java程序都是从类开始的】
<br/>
####4)如果需要返回一个可变对象的引用，应该对其进行克隆（clone）

>※这是由于变量都是一个指向对象的“类似指针的”引用，有可能会使得数据封装性遭到破坏

####5)final修饰符在使用时大多应用于不可修改的类，当应用在可变的类的时候，并不意味着类的内容不可修改
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
####6)通过static声明静态域和静态方法

- 静态域和C++类中的静态变量没有什么区别
- 静态公有常量可以通过类名来直接调用，由于有final限制，所以不会造成封装性破坏

>※如Math.PI就是一个静态公有变量
※其实也可以通过对象引用来调用，不过一般通过类名调用使得易读性更强
静态方法可以通过类名和对象引用直接调用，但一般使用类名调用增强易读性

>※如 Math.pow(x,y)

- 静态方法只能对对象静态域实施操作，而不能对实例域实施操作
- 通常只有在接受外来参数和调用静态域的时候才使用静态方法

####7)对象的构造
#####①可以直接在构造器内初始化实例域，即使是包含关系
#####②通过使用this来实现传参和实例域同名，甚至调用另一个构造器
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

#####③默认将所有数值初始化为0，布尔值初始化为false，引用初始化为null
>如果没有提供显式构造器，则系统自动生成隐式（无参）构造器完成上述工作
如果提供了显式构造器，则系统将不再自动生成无参构造器，上述操作将被视为非法

#####④初始化块
    ※这个不常用，通常使用构造器完成工作
    可以使用一个代码块对实例域进行初始化操作
    class Class
    {
	    private int id;
	    ....
	
	    {
		    id  = 1;
	    }

    }
    
    初始化块在所有构造器执行之前执行。
    通过标记关键字static可以对静态域进行初始化块操作
    static
    {
	    id = 1;
    }
    
#####8)类的基本结构
- 数据域
 - 构造器（constructor）
    - 访问器（getter）
    - 更改器（setter）
###3、方法参数
>Java总是按值传参，对象引用也是一个值
方法不能修改传递给它的实参
方法可以通过调用传入对象引用的对象的方法，实现对对象的修改
方法不能让对象参数引用一个新的对象

###4、包（package）
>※类似于C++的名称空间

- 通过import语句来导入Java包
- 添加static指令可以直接导入静态方法和静态域，使用的时候就无需使用类名来调用【UnRecommended】
- 通过使用包名来具体访问一个类
- 通过package语句来将类放入包中，通常在开头加入
```
package com.myApp.corejava
```
>注意包名的命名要与目录树相匹配，即上述类文件必须位于com/myApp/corejava中，否则，最终的程序将无法运行

- 包作用域
    - 如果实例域没有指定访问控制符，则这一个部分可以被同一个包的所有方法访问
>※在编写类的时候，必须为实例域添加上访问控制符

- 类路径（※好像只有使用Shell编译才会遇到这个问题？）
- javadoc文档注释
    - 以/**开头，以*/结尾
    - 可以使用HTML修饰符
    - 还有各种注释，这里不一一说明
     
###5、类设计技巧
####1)保证数据私有

####2)一定要对数据初始化，可以直接提供默认值，也可以在构造器中提供

####3)不要在类中使用过多的基本类型，可以通过一个封装类来减少使用
    private String street;
    private String city;
    private String state;

    ※这个可以通过一个Address类来解决
####4)并不是所有的数据都需要访问器和更改器

####5)将职责过多的类进行分解
>如果一个类能被拆分成两个或者多个独立的概念，那就进行拆分
※注意这里是概念的拆分，而不是单纯将方法拆分

####6)类名和方法名要能够体现它们的职责
>类名常用一个名词或者有定语修饰的名词
访问器使用小写的get开头
更改器使用小写的set开头

###6、继承
>△术语
基类：父类、超类
派生类：子类

####1)Java只允许一重继承
> ※可以有多个继承链，但是不能有多个基类

####2)使用extends来表明继承关系
```
class Derived extends Base
{
	....
};
```
####3)使用super来调用超类方法

####4)构造器
>可以使用super实现对超类构造器的调用
如果没有显式调用超类构造器，将自动调用超类构造器的隐式版本，如果没有隐式版本（即超类构造器只定义了显示版本）则报错

####5)多态
- 可以将超类引用指向子类对象，但不能反过来
>※基类指针可以指向派生类对象
- △数组可以进行相反的赋值，所以必须注意元素类型的监督
- public方法默认为动态绑定，无需添加vitual或者类似的关键字
>private、static、final方法为静态绑定

- 子类方法覆盖超类方法时，其访问权限不能严格于超类方法
> ※注意不要遗漏public关键字，否则将会被解释成为更严格的访问权限
- 覆盖允许返回类型协变（超类可以协变为子类）
 
####6)final阻止继承
- final类
>final class Excutive extends Manager
这种类型被称为final类，不允许定义子类，即无法继承
- final方法
>public final String getName() {...}
这种方法称为final方法，这种方法不允许子类覆盖它，确保其不会在子类中改变语义

- △注意final的位置不同
 
####7)强制类型转换
>在继承链上不允许进行由上到下的转换（超类不能转换成子类）
使用instanceof进行转换检查，返回布尔值，表示是否能够成功转换
语法：(要转换的对象) instanceof (转换目标)
强制转换语法类似C语言，执行过程类似dynamic_cast操作，不成功则抛出一个异常，而不是生成null对象

####8)抽象类
    abstract class Person {...}   【抽象类】
    public abstract String getDescription();   【抽象方法】
> 抽象类不一定要有抽象方法，但是包含抽象方法的类必须声明为抽象类
抽象类可以包含具体数据和具体方法
抽象类不能被实例化（即不能创建对象）

####9)谨慎的使用protected
####10)Object类
#####①equals方法
- 特性
    - 自反：x.equals(x) return true
    - 对称：y.equals(x) = x.equals(y)
    - 传递：if (x.equals(y) && y.equals(z)) then x.equals(z);
    - 一致：The return value of x.equals(y) should be stable;
对于非空引用x, x.equals(null) return false;
Object类equals：判断两个对象是否具有相同的引用
- equals方法的设计理念
1. 接受一个Object类参数（为了覆盖Object类的equals方法）
2. 检测是否为自身
    this == otherObject
3. 检测传参是否为null
4. 比较是否为同一个类
> 如果子类有特有的equals概念，则使用getClass方法
if(getClass() != otherObject.getClass()) return false;
如果子类没有特有的equals概念，则使用instanceof方法
if(!(otherObject instanceof ClassName)) return false;

5. 转换为相应的类变量
> 由于接受的是一个Object变量，所以必须进行强制类型转换才能进行具体实例域的相等判定
此时已经判别类型相同了，可以进行转换

6. 判别实例域
> △如果在子类中重新定义equals，则先调用超类的equals

######②hashCode方法
如果重新定义了equals方法，则必须重新定义hashCode方法
equals与hashCode的定义必须一致，如果x.equals(y) return true, 则，x.hashCode()就必须与y.hashCode()返回一样的值

#####③toString方法
一般形式：类名 + 方括号括起来的阈值
调用x.toString()可以用""+x代替
应该为每一个自定义类提供toString方法。

####11)泛型数组列表（ArrayList<>）
- 构造：ArrayList<ClassName> staff = new ArrayList<>();
- 优点：可以实现动态更改数组大小
使用add方法添加元素，remove方法删除元素
使用get方法访问元素，set方法设置元素【而不是使用[]语法】

####12)对象包装器和自动装箱
一般用于将基本类型转换成类对象
首字母大写即为相应的包装器
包装器的比较应使用equals方法，而不是==
包装器为final类，不可以用来修改基本数据类型的数值
应使用holder类型来修改基本数据类型的值

####13)不定参数
public static double max(double... values)
其中的double...相同于double[]，其实就是接受了一个double数组
可以将数组传递给可变参数方法的最后一个参数。
####14)枚举类
这里的枚举类是一个类对象，而不是一种类型

####15)反射 TODO

####16)继承设计的技巧
①将公共操作和域放在超类
②不要使用受保护的域
③使用继承实现“is-a”关系
④覆盖方法时，不要改变预期的行为
※这里说的是不要偏离设计，并不是不能改变基类方法的操作
⑤能使用多态就使用多态
⑥不要过多的使用反射

###7、接口
> 这是 Java 中的专有名词，指代的是 **interface** 关键字

####1)接口
    public interface Comparable {...}
    
- 接口不是类，而是对类的一组需求描述
- 接口中的所有方法自动为public
- 实现接口
    - 将类声明为实现给定的接口
    > class Employee implements Comparable {....}
    - 对接口中的所有方法进行定义
    **接口实现必须声明为public**
- 特性
    - 不是类，不能使用new来实例化
    - 不能包含实例域和静态方法
    - 可以包含常量，接口中的域被自动设为public static final
    - 可以声明接口的变量
    > Comparable x;

    - 必须引用实现了接口的类对象
> x = new Employee();

- 可以使用instanceof来检查一个对象是否实现了某个特定接口
> if(anObject instanceof Comparable)
- 可以扩展（**继承**）
> public interface Powered extends Moveable

- 每个类只能拥有一个超类，但是可以实现多个接口
> class Employee extends Persons implements Comparable

####2)对象克隆
- 默认克隆（Object.clone()）
- 浅拷贝
- protected方法
- 实现克隆
    - 必须实现Cloneable接口
    - 使用public重新定义clone方法
    - 即使浅拷贝能满足要求，也要进行上述两条操作
    - 需要声明CloneNotSupportedException异常
###8、内部类
```java
class TalkingClock
{
	public class TimePrinter implements ActionListenner
	{
		...
	}
}
```

####1)概述
- 在类的内部直接定义，类似于C++的嵌套类
- 可以访问作用域内的数据，包括私有的
- 可以隐藏内部类
- 可以便捷实现回调

####2)普通内部类
- 可以访问外围类对象数据（包括私有的）
- 通过OuterClass.this访问外围类
- 在外围类的作用域之外，使用OuterClass.InnerClass引用内部类

####3)局部内部类
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
- 局部类可以访问局部变量（必须声明为final）
- 更新封闭作用域内的计数器时，使用final的长度为1的数组
 
####4)匿名内部类
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

####5)静态内部类
- 用于将一个类隐藏在另一个类之中，通常用于防止名称的冲突
- 只有内部类可以声明为static
- 特别的，通过静态方法构造的内部类必须声明为static

##异常处理
###1. 异常分类
> ※具体的结构层次如图http://img.my.csdn.net/uploads/201310/29/1383051170_4167.jpeg

- Throwable
    - Error
> ※Java运行时系统的内部错误和资源耗尽错误，应用程序不该抛出这类异常，该异常出现时，只能终止程序

    - Exception
        - IOException及其他
> ※包含
	试图在文件尾部后面读取数据（IO）
	试图打开一个不存在的文件（IO）
	试图根据给定的字符串查找Class，而这个类并不存在

        - Runtime Exception
> ※包含
	错误的类型转换
	数组访问越界
	访问空指针
	
- 注意要点
    - 如果出现RuntimeException，那么就一定是你的问题，需要从程序设计方面进行改进
    - 所有派生于Error和RuntimeException的异常称为未检查异常
    - 注意IOException并不包含用户输入的部分，此类通过一般检查可以避免的异常不应作为异常抛出并处理，应该由流程控制语句（if else while continue）处理

###2. 声明异常
> ※类似于C++98的异常规范

- 在方法的首部声明
    public FileInputStream(String name) throws FileNotFoundException

- **声明多个时 ，使用逗号隔开**
- 必须声明所有可能抛出的已检查异常
> ※如果未声明，则表明方法不会抛出（已检查）异常

- 不必声明未检查异常
- 子类方法的声明异常不能比超类方法更为通用
>※即子类声明的异常层次不能高于超类方法
※超类没有声明异常时，子类也不能声明异常

###3. 抛出异常
- 使用throw关键字表明抛出异常
> ※注意与声明异常的关键字（throws）区分开
只能抛出Throwable子类的对象
※而C++能抛出任何类型的值
- 抛出异常与捕获异常不同，如果没有异常处理器（try catch）捕获异常，则程序将会终止
- 自定义异常
    - 通常包含一个默认构造器和一个带有详细描述信息的构造器
    - 必须派生于Exception及其子类

###4. 捕获异常

####使用try/catch语句块来捕获异常
> 如果调用一个抛出已检查异常的方法，则必须对其处理（try/catch），或继续将其传递（throws）
一个catch语句里面可以捕获多个异常类型，使用|间隔开
※此时，异常变量为final
可以在catch语句中再次抛出异常
※与C++不同的是，不能只写throw关键字，而需要将整个抛出异常都写上

####finally子句
```java
try
{
	...
}
catch(...)
{
	...
}
finally
{
	...
}
```
#####1.概述
- 不管是否有异常被捕获，finally子句都将被执行
- 抛出异常并被捕获时，先执行catch语句，后执行finally语句
- 抛出异常未被捕获时，先执行finally语句，后将异常返回给调用者
> try可以只有finally，而没有catch

- **当finally语句抛出异常时，会覆盖掉原有异常（此时建议使用带资源的try语句）**
    - ※如果此异常必须返回给调用者的话，则需要进行一些处理才能返回给调用者
    - ※如果原异常具有异常处理器（被捕获）则不需要这种解决办法
 
        - 常规解决办法
```java
InputStream in = ....;
Excepiton ex = null;
try
{
	try
	{
		...
	}
	catch(Exception e)
	{
		ex = e;
		throw e;					//这里重新抛出了e，为的就是将这个异常返回给调用者
	}
}
finally
{
	try
	{
		in.close();
	}
	catch(Exception e)			//在这里捕获（抑制）了close方法的异常，
	{
		if(ex == null)	throw e;
	}
}
```
#####2.带资源的try语句
- **只要需要关闭资源，就要尽可能使用带资源的try语句**
- **资源必须属于一个实现了AutoCloseable的类，否则应使用常规方法**
```
try(Resource res = ...)
{
	....
}
```
- 资源：特指文件和输入输出流等，和**申请的内存无关**
> 当try块退出时，将会自动调用res.close()
- 可以指定多个资源
当出现异常时，close异常会被自动捕获（抑制），原有异常将会重新抛出
※close的异常将会被增加到原有异常中，可以使用getSuppressed方法获取到被抑制的异常列表
此try块也可以有catch和finally子句，会在关闭资源之后执行

###5. 使用异常的技巧
####1.异常处理不能代替简单的测试
- 异常处理会比简单的测试花费更多的时间
- 应该仅在异常状况下使用异常机制
- **资源的IO错误，设备错误，物理限制等等**
- **而对于用户的输入错误，应该使用流程控制来进行处理**
 
####2.不要过分细化异常
**应该将整个任务包装在一个try语句内**
####3.利用异常层次结构
>※应该尽量的抛出更为恰当的子类，而不是仅仅抛出较为高层次的异常类对象
※捕获时同理

####4.应该关闭不重要的异常
> ※在方法多重调用时使用

####5.早抛出，晚捕获

###6. 断言 TODO

##多线程

###1. 创建线程

####1) 实现 Runnable 接口
```java
class Myrunnable implement Runnable {
	run();
}
```
####2) 创建 Runnable 对象
    Runnable r = new Myrunnable();
####3) 由 Runnable 对象创建 Thread 对象
    Thread t = new Thread(r);
####4) 启动线程
    t.start();
    △不能直接调用 run 方法，应调用 Thread.start 方法来间接调用 run 方法
###2. 中断线程TODO


