# 观察者模式(Observer Pattern)

[TOC]

## 1. 概述

观察者模式，是在对象间定义一个**一对多**的关系。

当“一个” 对象的改变状态，依赖它的对象都会**收到通知**，并自动更新。

其中，“一个” 对象称作**主题、可观察者、被观察者**；

“多个” 对象被称作**观察者、倾听者、订阅者**。

> 这有点类似报社和读者的关系：发生新闻后，报社通过报纸来通知读者。
>
> 实际上就是一个典型的观察者模式。

## 2. 实现方式

### 2.1 实现思路

1. 封装变化

   > 观察者模式中，主题的状态和观察者的种类和数量都会变化。
   >
   > 所以，需要对观察者进行封装。
   >
   > 同理，观察者也可能订阅多个主题，所以主题也需要进行封装。

2. 针对接口编程，不针对实现编程

   > 所以，我们使用接口，分别将主题和观察者进行封装。
   >
   > 实际上就是让各个主题实现统一的 `Subject` 接口；观察者实现统一的 `Observer` 接口。

3. 多用组合，少用继承

   > 观察者模式是一个一对多的**依赖关系**，这意味着，主题必须维护一个**观察者列表**。
   >
   > 状态改变后，通过调用通知方法来**逐个**通知观察者。
   >
   > 实际上，这意味着将观察者**组合**进了主题中。

### 2.2 图解

![](http://www.plantuml.com/plantuml/png/oymhIIrAIqnELGWkJSfAJIvHgEPIK2XAJSyi1ahu9nMd5fMb5cbeWWLpyyjIKOJoyaioqofXGiL0iLgkJBY9C76maQK5AOabgM0LoJc9nSKAplbvoKMf9Qd8zYh4nsErNQ5QJq-l5eiRu18OBe7BwEa1YVJKak0IYFqA2iK83hfZi3ePrIXzVOMdhTkUx9xsRDhEPvkd0es0-S165-vbBdJV0UNGxK3egz7JGmyEBhXBK6HXeW00)

## 3. 新设计原则——松耦合

**为了交互对象之间的松耦合设计而努力！**

> 所谓的**松耦合**，指的就是两个类、函数、模块之间相关度不高，改变其中的一个类不会造成另一个类的大幅变化。

观察者模式通过**接口**的形式来进行交互，主题可以随时增加和删除观察者列表中的观察者；

观察者也不需要关心主题的内容，它只需要接受主题的通知就可以了。

## 4. 气象站例子的 UML 图解

![](http://www.plantuml.com/plantuml/png/bLD1JiCm4Bpx5Jw2LD8FS44jY4j5fLRYM6sJRJ5gd6YzgOX2_ewRO9FOAL8lbkoPdPtPR9Hcf0EaA3VL_XDJbesG3UmD4wJSIiAZCfRojZT8PwIx-m3EYpDU0NN1wb0xq5Yq5KBvXWu8EbPb1emXUQbCUOBw-OGvwj1areDzJNe2O-Gx0dyWBO7XGfPojxDdd4OsIPAq7JHEue4eXKUIn1v7v2tc9H9mHHVRtTDhbQjCSUtkQq9ZUjnRN5H4DikYq9Qf2cr-CtP-tHJ6pNnGsSpdJg2rahtYXe5jFfNUBBM2hvbSAJsJe3FvP8F24Ti_hoy5OGg6RzLrTGEfxOUYR0t4zQrYNQKiBwMTdjlOnmU_IsButUtxjHc7l6Xo8I4OG0X7eGRklfDak8v2-CNleAiMnxJOuHWF3OxH2NyY-AN-DpD5ZYrDiK9ZKvp8tWy0)

## 5. 推和拉

