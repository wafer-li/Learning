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

##### 5) The classification of the growing level

![Classification](http://algs4.cs.princeton.edu/14analysis/images/classifications.png)

###### 1. Constant

> Most of the Java operation

###### 2. Logarithmic

> A little slow than the constant, such as **BinarySearch**

###### 3. Liner

> The single `for` loop

###### 4. Linerithmic

> Such as the `Merge.sort()` and the `Quick.sort()`

###### 5. Quadratic

> Two `for` loop, such as `Selection.sort()`, the `Insertion.sort()` and the `Bubble.sort()`

###### 6. Cubic

> Three `for` loop, such as the **3-sum**

###### 7. Exponential

> Very slow, try to avoid to use it.

##### 6) Build the faster algorithm

> The ***Divide and Conquer Algorithm*** to solve 3-sum problem
    
- 2-sum problem

> if the result of 2-sum is zero, there must be $ A + B = 0 $
or $A = -B$
So, we can use **BinarySearch** to find the opposite number of the specific number.

Notes:

> if the return value of **BinarySearch** is in the range $ 0< return < spec$ it means we **refind** the previous number, the number is **redundancy** , we should **abort** it

> So, we reduce the running time from the $N^2$ level to the $logN$ level

- 3-sum problem 

> As the 2-sum, when the $-(a[i] + a[j])$ is the part of the array, nor the $a[i]$ or $a[j]$, and the pair $(a[i], a[j])$ is the part of the 3-sum.

> By using the BinarySearch, we reduce the running time from the  $N^3$ level to the $N^2logN$ level

##### 7) The prediction of running time in growing levels

| Describe   | Function | Modulus is 2  | Modulus is 10 | Handle the 10N | Handle 10N in 10 times faster|
|--------|------|------|-------|-----|-----|
| Linear| $N$|2|10| a day| couples of hours|
| Linearrithmic|$NlogN$|2|10|a day | couples of hours|
| Quadratic| $N^2$| 4| 100| a few weeks| a day|
| Cubic| $N^3$ | 8 | 1000 | a few months | couples of weeks|
| Exponential| $2^N$ | $2^N$ | $2^{10N}$ | forever | forever

##### 8) The notice of algorithm analysis

###### 1. Big constant number

> Normally, we suppose that $2N^2 + cN$ is $\sim 2N^2$, but when c is equal to $10^3$ or $10^6$, that is incorrect.

###### 2. No decisive inner cycle

> The wrong cost model cannot get the correct analysis result.

###### 3. Time of instructions

> If you are using the ARRAY to access some number which doesn't nearby, it might cost a lot of time

###### 4. The system cause

> When you are running your program to analysis the algorithm, perhaps your computer is not only running your program, but **OTHER** program, basically, it cannot be reproduce

###### 5. This part might be good, but other doesn't

> The choice of algorithm often depend on the situation, in some situation, the algorithm $A$ might be the best, but other situation doesn't.

###### 6. Dependencies of input

> In 3-sum problem, when we ask "is there exsist the number which match the 3-sum?", if **YES**, the growing level is **constant**, but if **NOT**, the growing level is $N^3$.

> In this case, we often decribe the growing level as  $T_w$ which means **Time of WORST** situation, and the $T_{av}$ which means **Time of AVERAGE**

###### 7. Multiable paramater

> When using the BinarySearch to figure out the *White Name List* problem, the List cotains $N$ numbers, which the Input contains $M$ numbers, the growing level is usually $MlogN$

#### 2. Memory

> When in java, the usage of the memory is filled as **the multiple of 8**

##### 1) Object
- Integer
    - Totally 24 bytes
    - 16 bytes of the Object itself (stable)
    - 4 bytes of the int value 
    - reference, which the address of memory, cost 8 bytes (stable)

##### 2) Linked List
- Node(inner class)
    - Totally 40 bytes
    - 16 bytes Object itslef
    - 2 * 8 bytes reference (2 reference)
    - when inner class, need another reference point to the owener, 8 bytes
    - The cost of the data

##### 3) Array

- The Object array
    - 24 bytes header message
        -  16 bytes object cost
        -  4 bytes fill cost

##### 4) String

- 40 bytes
- Object cost, 16 bytes
- reference, 8 bytes
- 3 int, 12 bytes
    - offset 
    - counter 
    - hash 

> The subString
when you involved the `substring()` method, it does create a new String object, but it doesn't create the `value[]` array, it was contained in the **constant area**

> So, the subString extra memory need is a **constant**

### 3) Outlook

- Premature optimization is the root of all evil
    - if the running time is peticularly fast, it is worthless to make the speed ten times faster
- But we **DO NEED** the great algorithm, when we handle the **large-scale** problem, the faster algorithm make more profits.