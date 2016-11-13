# C# Basic

[TOC]

## 1. Hello, World!

```c#
namespace SimpleCSharpApp 
{
  class Program 
  {
    static void Main(string[] app) 
    {
      Console.WriteLine("Hello, World!");
      
      Console.ReadLine();
    }
  }
}
```

​	基本的编码规范：

- 区分大小写
- 命名空间、类、成员（包括方法）采用**大驼峰**
- 大括号另起一行

## 2. 基本类型

C# 中的基本类型都是**对象**，事实上，基本类型的关键字都对应一个 `System` 命名空间中的一个**类**

> 显然是相对于 Java 的重大进步

下表给出了 C# 基本类型和 CLS，系统类型的对应关系。

| 基本类型    | 符合 CLS？ | 系统类型           | 范围                                       | 作用                  |
| ------- | ------- | -------------- | ---------------------------------------- | ------------------- |
| bool    | T       | System.Boolean | true or false                            | 布尔值                 |
| sbyte   | F       | System.SByte   | -128 ~ 127                               | 有符号的 8 bit 整数       |
| byte    | T       | System.Bute    | 0 ~255                                   | 无符号的 8 bit 整数       |
| short   | T       | System.Int16   | -32768 ~32767                            | 有符号的 16 bit 整数      |
| ushort  | F       | System.UInt16  | 0 ~ 65535                                | 无符号的 16 bit 整数      |
| int     | T       | System.Int32   | -$2^{31}$ ~ $2^{31} -1$                  | 带符号的 32 bit 整数      |
| uint    | F       | System.UInt32  | 0 ~ $2^{32}$                             | 无符号的 32 bit 整数      |
| long    | T       | System.Int64   | -$2^{63}$ ~ $2^{63} -1$                  | 有符号的 64 bit 整数      |
| ulong   | F       | Sytem.UInt64   | 0 ~ $2^{64}$                             | 无符号的 64 bit 整数      |
| char    | T       | System.Char    | U+0000 ~U+ffff                           | 16 bit 的 Unicode 字符 |
| float   | T       | System.Single  | $-3.4 \times 10^{38} \sim +3.4 \times 10^{38}$ | 32 bit 浮点数          |
| double  | T       | System.Double  | $\pm 5.0 \times 10^{-324} \sim \ \pm 1.7 \times 10 ^{308}$ | 64 bit 浮点数          |
| decimal | T       | System.Decimal | $(-7.9 \times 10^{28} \sim 7.9 \times 10^{28})/(10^{0 \sim 28})$ | 128 bit 带符号数        |
| string  | T       | System.String  | 受系统内存限制                                  | 字符串                 |
| object  | T       | System.Object  | 任何类型都能保存在一个 object 变量中                   | 所有类的基类              |