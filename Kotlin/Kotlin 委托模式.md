# Kotlin 委托模式

Tags: Kotlin

---

<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 flatten:0 bullets:0 updateOnSave:1 -->

[Kotlin 委托模式](#kotlin-委托模式)  
&emsp;[1. 委托模式](#1-委托模式)  
&emsp;[2. Java 例子](#2-java-例子)  
&emsp;[3. Kotlin 的委托模式](#3-kotlin-的委托模式)  

<!-- /MDTOC -->

---

## 1. 委托模式

> 委托模式是软件设计模式中的一项基本技巧。
在委托模式中，有两个对象参与处理同一个请求，接受请求的对象将请求委托给另一个对象来处理。
委托模式是一项基本技巧，许多其他的模式，如状态模式、策略模式、访问者模式本质上是在更特殊的场合采用了委托模式。
委托模式使得我们可以用聚合来替代继承。

## 2. Java 例子

```
interface I {
     void f();
     void g();
 }

 class A implements I {
     public void f() { System.out.println("A: doing f()"); }
     public void g() { System.out.println("A: doing g()"); }
 }

 class B implements I {
     public void f() { System.out.println("B: doing f()"); }
     public void g() { System.out.println("B: doing g()"); }
 }

 class C implements I {
     // delegation
     I i = new A();

     public void f() { i.f(); }
     public void g() { i.g(); }

     // normal attributes
     public void toA() { i = new A(); }
     public void toB() { i = new B(); }
 }


 public class Main {
     public static void main(String[] args) {
         C c = new C();
         c.f();     // output: A: doing f()
         c.g();     // output: A: doing g()
         c.toB();
         c.f();     // output: B: doing f()
         c.g();     // output: B: doing g()
     }
 }
```

`C` 将 `I` 接口的工作委托给 `A` 或者 `B` 来做。

可以看出，Java 中的委托模式的缺点在于要求比较多的代码。

## 3. Kotlin 的委托模式

而在 Kotlin 中，委托模式要求的代码量非常低。

只需要一个 `by` 表达式就能实现委托模式

```
interface Base {
  fun print()
}

class BaseImpl(val x: Int) : Base {
  override fun print() { print(x) }
}

class Derived(b: Base) : Base by b

fun main(args: Array<String>) {
  val b = BaseImpl(10)
  Derived(b).print() // prints 10
}
```

在这里 `by` 表达式表示，变量 `b` 会储存在类 `Derived` 中，
编译器会在 `Derived` 生成所有的 `Base` 的方法，并将它们都用 `b` 来执行。
