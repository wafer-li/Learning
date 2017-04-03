# Scala Hello World

<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 flatten:0 bullets:0 updateOnSave:1 -->

[Scala Hello World](#scala-hello-world)   
&emsp;[1. 简介](#1-简介)   
&emsp;[2. `main()` 方法](#2-main-方法)   
&emsp;[3. 使用 `Application` 特质](#3-使用-application-特质)   

<!-- /MDTOC -->

## 1. 简介

Scala 既可以使用交互式命令行来编程，也可以将其写成一个独立的程序；

其中，关于构建独立程序的写法一共有两种。

## 2. `main()` 方法

使用 `main()` 方法是通常各种语言的程序入口，Scala 也不例外：

```scala
def main(args: Array[String]) {
    println("Hello, World!")
}
```

## 3. 使用 `Application` 特质

```scala
object Hello extends Application {
    println("Hello, World!")
}
```
