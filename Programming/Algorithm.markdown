# Algorithm

Tags: Programming-Learning Algorithm

[TOC]

---

## 1. Bag Queue and Stack

> They are all the **Set** of Data Objects

### Feature

#### 1) Bag
> - Do **not** support delete the element
- Use to collect data element, **iterate** and **traversal** it.
- The **order** is not so important and not necessary.

#### 2) Queue(FIFO)
> The Queue there refer to the **First In First Out** Queue

> - The data element **First In First Out**.
- This Set collect the data element and **remain their order** meanwhile

#### 3) Stack
> - Right opposite with the **FIFO Queue**, the date element **Last In First Out**
- Also, remain the **relative order** of the data element.

##### The Arithmetic expression evaluate
> Using double Stacks
When receive the arithmetic expression

> - Push the **value** into the ***value stack***
- Push the **operator** into the ***operator stack***
- Ignore the **left bracket**
- When reaching the **right bracket**, pop **ONE operator** and **the necessary value** and push the **calculated result** into the value stack

### Implementation 

#### 0. Using Array to implement the Stack

> - push() needs to check if the stack is full, if true, resize it.
- resize() aims to double the array's room.
- pop() needs to check if the stack's room if less than **the 1/4 of the array**[^footnote], resize the array to the 1/2 lenth.
- Avoid the **Object Free**. When the data object was poped, assign it **as null**[^footnote2]
- The disavantages
    - The time using of each operation is **connect to the size** of the data set
    - The room needs is **unpredicte**

[^footnote]: If the stack is less than the 1/4 of the array, even though the pop() shorten it, it still larger than **the double of the stack**, so it still have room to store the data.

[^footnote2]: At this point, the data object will **NEVER** be access, but the reference is still there. In java, if the reference is sitll **EXIST**, the garbage collector will **NOT** collect it. This phenomenon is called **Object Free**


#### 1. Linked List
> List is an **recursive** data structure, it is null, or an reference which point to a node.
The node contains one **generics** data element and the reference which point to **another List**
Node is often used as an inner class.

##### 1) Construct
```java
private class Node
{
    Item item;
    Node next;
}
```

> - Only need to assign an Node value, we can present a List.
- Because of the inner class ability, we can assign the node's menber directly.

```java
Node first = new Node();
Node second = new Node();
Node thrid = new Node();

//Items
first.item = "to";
second.item = "be";
thrid.item = "or";

//Nexts
first.next = second;
second.next = thrid;
```
![Build linked List](http://algs4.cs.princeton.edu/13stacks/images/linked-list.png)

##### 2) Insert at the beginning

> Use another reference(such as `oldfirst`) to store the first Node, and build another Node to store the data and set the next field as `first`

![Insert at beginning](http://algs4.cs.princeton.edu/13stacks/images/linked-list-insert-front.png)

##### 3) Remove from the beginning

> Make the `first` directly point to `first.next`
The garbage collector will collect the memory the oldfirst used.

![Remove from the beginning](http://algs4.cs.princeton.edu/13stacks/images/linked-list-remove-first.png)

##### 4) Insert at the end

> Just as the Insert at the beginning.
Use another reference(such as `oldlast`) to store the last Node, and build a new Node named `last` to store the data and set the `olderlast.next`as `last`

![Insert at the end](http://algs4.cs.princeton.edu/13stacks/images/linked-list-insert-end.png)

##### 5) Other place Insert and Remove

> Such as the **Remove from the end**
The `last` reference cannot help us, because we need to set the previous's `next` field as null.
In this situation, we can only **traversal** to the previous Node and set the `next` field

##### 6) Traversal
- Normally, we use `foreach` statement to traversal and iterate.
With this way, the class must implement the `Iterable` and the `Iterator` interface to return a Iterator and define how to iterate.

- But with linked List, we only need to use normal `for` statement
```java
for(Node x = first; x != null; x = x.next) {
    //handle x.item
}
```

#### 3. Using Linked List

> The Use of linked list achieve this:

> - It can handle the data with any type
- Its room needs is always proportional with the Set's size
- Its time using of operations does **NOT** connect to the size of Set.[^footnote3]

[^footnote3]: The insert and the remove operation with linked List only need to **assign** and **construct Objects**. The time of operations is all **constant number level**.

##### 1) The implementation of Stack

> - Set the beginning as the top of the stack
- When push(), we insert the data element at the beginning
- When pop(), we remove the data element from the beginning

##### 2) The implementation of Queue

> - Set the beginning as the beginning of the Queue, so the end is the end of the Queue
- When push(), insert the data element at the end
- When pop(), remove the data element from the beginning

##### 3) The implementation of Bag

> - Remove the pop() method is Ok

## 2. Algorithm Analysis

### 1) Observe

> - Run the program and use the time counter to measure the time usage
- Use the large data to guess and verify the mathematical model

### 2) Mathematical Model

#### 1. Time

> The time usage is connected to 

> - The time usage of the operation of each statement.
- The frequency of each statement being operate.

##### 1) Approximation

> We use $\sim f(N)$ refer to when N grows, the result of divided by $f(N)$ equals to $1$,
use $g(N) \sim f(N)$ refer to when N grows, the result of $g(N)/f(N)$ equals to $1$

##### 2) Inner Loop

> - The inner loop refers to the operation which the program execute the **MOST** frequently
- The program's time usage depens on the inner loop.

##### 3) Cost Model

> - The cost model refers to the basic operation of the algorithm
- Such as 3-sum, the cost model of 3-sum is the frequency of access the array element

##### 4) The step of gain the mathematical model

1. Verify the **input model**, and the size of the problem
2. Identify the **inner loop**
3. According to the inner loop, to verify the **cost model**
4. Accroding to the input model, verify the frequency of each operation

#### 3) The classification of the growing level

![Classification](http://algs4.cs.princeton.edu/14analysis/images/classifications.png)

#### 1. Constant

> Most of the Java operation

#### 2. Logarithmic

> A little slow than the constant, such as **BinarySearch**

#### 3. Liner

> The single `for` loop

#### 4. Linerithmic

> Such as the `Merge.sort()` and the `Quick.sort()`

#### 5. Quadratic

> Two `for` loop, such as `Selection.sort()`, the `Insertion.sort()` and the `Bubble.sort()`

#### 6. Cubic

> Three `for` loop, such as the **3-sum**

#### 7. Exponential

> Very slow, try to avoid to use it.

