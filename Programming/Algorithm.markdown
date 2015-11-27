# Algorithm

Tags: Programming-Learning Algorithm

<span style="font-size:20px">Base on *Algorithm 4th(Robert Sedgewick)*</span>

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

## 3. Quick-Union Analysis
> Judge if we need a new link or line to make the two point linking

### 1) Concepts
- Link
> Link is an equivalence relationship, means the following
    - Reflexive: $p$ links with $p$
    - Symmetry: If $p$ link with $q$, then $q$ links with $p$
    - Transitive: If $p$ links with $q$, and $q$ links with $r$, then $p$ links with $r$

- Network Concepts
    - Contact
    > The contact we call is the object in the array.

    - Connected Component
    > This word in here means a **Set** which **contain the linked contact**,
    in other way, the contact in the set is all linked with each other
    
### 2) Implementation of Union-Find

```java
public static void main(String[] args) {
    int N = StdIn.readInt();    //read the Number of CONTACTS
    UF UF = new UF(N);          //Initialize the data structure
    
    while(!StdIn.isEmpty()) {
        int p = StdIn.readInt();
        int q = StdIn.readInt();
        
        if(uf.connected(p,q)) {
            //If it is connected, ignore it
            continue;
        }
        
        uf.uinon(p,q);          //Merge the contacts
        StdOut.println(p + " " + q);
    }
}
```

### 3) Implementation of `union()` and `find()`

> All base on the  `id[]` array which its **index** is the **CONTACT**

#### 1. quick-find algorithm
> This version needs $(N + 3)(N - 1) \sim N^2$ times accesses of array

```java
public int find (int p) {
    return id[p];
}

public void union(int p, int q) {
    // Merge p and q into the same component
    int pID = find(p);
    int qID = find(q);
    
    // If the p and q are at the same component,
    // do nothing and return.
    if(pID = qID) {
        retrun;
    }
    
    // Rename the p component to the q component
    for(int i = 0; i< id.lenth; i++) {
        if(id[i] == pID) {
            id[i] = qID;
        }
    }
    count --;   // Decrease the component counter
}
```

#### 2. quick-union alogrithm

##### 1) Basic concepts
- Use **Tree** as the base data structure
- Each contact's `id[]` element is the other contact's name, we call it **linked**
> For instance, $p$ and $q$ two contacts
If $p$ links with $q$, than `id[p] == q`
- When the `id[p]` is `p`, we call $p$ as a ***root*** contact

##### 2) Implementation

```java
private int find(int p) {
    // Find the root of the contact's component
    while (p != id[p]) {
        p = id[p];
    }
    return p;
}

public void union(int p, int q) {
    // Merge the root contact of the p's component and the q's component
    int pRoot = find(p);
    int qRoot = find(q);
    
    // If the two components' root are the same, return.
    if (pRoot == qRoot) {
        return;
    }
    
    // Set the p's tree links with q's tree.
    // Now, the qRoot is the father contact of the qRoot.
    id[pRoot] = qRoot;
    
    count --;
}
```

##### 3) The inprovement 

> The **quick-union** alogrithm use tree as the basic data structure.
Avoid the scanning of **the whole array** in each `union()` operation.

##### 4) The complexity

> Although, usually, the **quick-union** alogrithm is better than the **quick-find**, but in the worst situation, it still need $2(1 + 2 + \dots + N) \sim N^2$ times array accesses

> The `find()` method will recursively scan the tree, until reach the root contact, so what if the depts of the tree keep growing?
The accesses of the array will continue growing.
So we reach the result of the top.

#### 3. Weighted quick-union alogrithm

> Now we are talking about hwo to optimilize the **quick-union** alogrithm.
The basic theory is to reduce the depts of the tree.

- **Weight each tree**
> The reason why the depts of the tree will growing, it's normally as
**The larger tree was linked to the smaller tree**, so the tree's depts keep growing.
> So, why not to count the tree's contacts to avoid the situation happen?

```java
public class WeightedQuickUnionUF {
    
    /**
    * We need a new array to count the tree's size
    * The index is the root contact
    * The value is the corresponding size of the tree
    
    * Baically, we use the root contact to stand for the tree
    */
    private int[] sz;   
    ....
    public WeightedQuickUnionUF (int N) {
        ...
        sz = new int[N];
        for (int i = 0; i < N; i++) {
            // Initialize the sz[] as 1.
            // No one was linked at the first.
            sz[i] = 1;
        }
    }
    ...
    public int find(int p) {
        // Find the root contact
        while (p != id[p]) {
            p = id[p];
        }
        retrun p;
    }
    
    public void union(int p, int q) {
        ...
        if (sz[i] < sz[j]) {    // Link the smaller tree's root contact to the bigger one
            id[i] = j;
            sz[j] += sz[i];     // Adding the weight(or size) of the component
        }
        else {
            id[j] = i;
            sz[i] += sz[j];
        }
    }
}
```

- The improvement
> This algorithm ensures even in the bad situation, which is at **each operation**, the trees' size are all **equal**, the accesses times of the array will limit as $logN$ [^footnote4]

[^footnote4]: The $logN$ in algorithm is equal to $log_2{N}$

#### 4) The weighted quick-union with path compresson
> More adventurous, we can link the contact to the root to more reduce our tree's depts.
It' easy to implement, and do not have any side effect, so why not?

- The Implementation
> The other parts is base on the **weighted quick-union** algorithm
```java
public int find(int p) {
    int pParent = p;
    
    // Find the p's root
    while(pParent != id[pParent]) {
        pParent = id[pParent];
    }
    // Now, the pParent equals to the pRoot
    
    /**
    * Notice:
    * When run the find() method,
    * They will link all the contacts of this component to the root
    */
    while (id[p] != p) {
        p = id[p];  // Move p to its parent
        id[p] = pParent;    // The id[p] is still p's prarent, now link it to the root
    }
    
    return pParent;
}
```

- The improvement

> This alogrithm's complexity is very very close to the constant level

#### 5) The comparation

![The comparation of the Union-Find algorithm](http://algs4.cs.princeton.edu/15uf/images/uf-performance.png)


## 4. Sort Algorithm

> The cost model
Calculate the number of **compare** and the **exchange**
If do **NOT** need to exchange, we calcute the number of array **ACCESS**

### 1) Selection sort

> 1. Find the smallest item
2. Exchange it with the first item
3. Go to step 1 and exchange it with the second, third, fouth... and so on

- Analysis
> With the $N$ lenth array, it needs about $\frac{N^2}{2}$ times comparation and $N$ times exchanges

    - The needed time does **NOT** connect to the input
    - The movement of data is the least

### 2) Insertion sort

> Increasing order for example

> 1. Compare a[i] with each item in range(a[0], a[N - 1])
2. If the item is **smaller** than `a[i]`, exchange it with `a[i]`

- Implementation

```java
public static void sort(Comparable[] a) {
    int N = a.length;
    for (int i = 0; i < N; i++) {
        for (int j = i; j > 0 && less(a[j], a[j-1]); j--) {
            // Compare a[i] with the items which is at its left side.
            exch(a, j, j-1);
        }
        assert isSorted(a, 0, i);
    }
    assert isSorted(a);
}
```

- Analysis
> This algorithm complexity is base on the input.
If the items are partly ordered, then use this algorithm will be more fast
>
> With the double nested for loop, the worst situation still needs $N^2$ times exchanges

- Improvement
> To optimize, we just simply move the bigger item towards right, rather than exchange the two items.
It can reduce **half** of the accesses of array

```java
/**
* Use this method to replace the exac(), 
* the spare space will be left,
* when the movement was completed,
* just insert the specific item into the room.
*/

a[j] = a[j - 1]
```

### 3) Shell Sort

> Shell Sort is base on the insert sort.
The theory is to make the items **ordered** of **each $h$ interval**
If the $h$ is large, we can move the item much further.

> The gold of Hill sort is gradually reduce the $h$ in order to reach $0$
Just use Insert Sort, just largethen the interval of exchange or movement

- Implementation

```java
public class Shell {
    public static void sort(Comparable[] a) {
        // Increasing order of a[]
        
        int N = a.lenth;
        int h = 1;
        
        while (h < N/3) {   // From N/3 to reduce the h
                            // 1, 4, 13, 40, 121, 364, 1093, ...
            h = 3 * h + 1;
        }
        
        while(h >= 1) {
            // Make the array h ordered
            
            for(int i = h; i < N; i++) {
                // Insert the a[i] into the a[i - h], a[i - 2*h] , a[i - 3*h]
                for(int j = i; j >= h && less(a[j], a[j - h]); j -= h) {    
                    // Replace j-- as the j -= h
                    exch(a, j, j-h)
                }
            }
        }
    }
} 
```

- Improvement

> The Shell Sort is faster than the Insert and the Select,
But, when talk about the analysis, we cannot give a mathmatic comlexity expression, we can only say,

> **The comlexity of Shell Sort will never reach the square level.**

### 4) Merge Sort

> Merge Sort base on the recursive function call
In the after will release the loop version

> The main theory is **Divide and Conquer** strategy
> By Divide the big Set into the small Set and use Insert Sort to sort the small one,
and we merge the small sets to generate the ordered set

> Notice:
**You need to do the comparision during the merge**

#### 1) Implementation

```java
public static void merge(Comparable[] a, int lo, int mid, int hi) {
    // Merge the a[lo...mid] and the a[mid... hi]
    
    int i = lo, j = mid + 1;
    
    // Copy the a[lo...hi] to the assistant array
    for (int k = lo; k <= hi; k++) {
        aux[k] = a[k];
    }
    
    // Merge 
    // During the merge, do the comparition
    for (int k = lo; k <= hi; k++) {
        if (i > mid) {                  // When the left side was empty
            a[k] = aux[j++];
        }
        else if (j > hi) {              // When the right side was empty
                                        // Notice that the j is the middle index
                                        // it could also be the lo and gradually reduce
            a[k] = aux[i++];
        }
        else if (less(aux[j], aux[i])) { // Either, compare the left side and the right side
            a[k] = axu[j++];
        }
        else { 
            a[k] = aux[i++];
        }
    }
}
```

#### 2) From Top To Bottom

> This theory is divide the Set and recursive sort and merge.

```java
public static void sort(Comparable[] a) {
    aux = new Comparable[a.lenth];
    sort(a, 0, a.lenth - 1);
}

private static void sort(Comparable[] a, int lo, int hi) {
    if (hi <= lo) return;
    int mid = lo + (hi - lo) / 2;
    
    sort(a, lo, mid);       // Sort the left side
    sort(a, mid + 1, hi);   // Sort the right side
    
    merge(a, lo, mid, hi);  // Merge the result
}
```

- Notice:
> Only the `merge()` method work with the sort, The `sort()` method is to divide and do the recursive `merge()`

- Conclusion
    1. The From Top To Buttom Merge Sort needs ${1 \over 2} NlogN \sim NlogN$
    2. For the $N$ lenth array, from top to buttom merge sort needs $6NlogN$ times array accesses

#### 3) From Buttom To Top

> This theory is to merge the child array pairly, that is, 
first we merge that child array which contains 2 items, and then 4, then 8, $\dots$

- Implementation

```java
public static void sort(Comparable[] a) {
    int N = a.lenth;
    aux = new Comparable[N];
    
    for (int sz = 1; sz < N; sz = sz + sz) {
        for (int lo = 0; lo < N - sz; lo + = sz + sz) {
            merge (a, log, lo + sz - 1, Math.min(lo + sz + sz - 1, N - 1));
        }
    }
}
```

- Notice:
> It use the loop to implemente the algorithm, rather than recursive.

- Conclusion
    1. For the $N$ lenth array, this sort method needs ${1 \over 2} NlogN \sim NlogN$ times comparisions and needs to access the array $6NlogN$ times at **most**.
    2. This method fixs with the **Linked List** organized data, it Only need to reorganize the the linking with sorting it successful. Do NOT need to create the List Node.
        
#### 4) Comparision

> Here are the comparasion of two ways of Merge Sort

1. Two ways have **the same cost**, when the array is $2^N$
> They have the same level of times item comparision, and the same level of times of accessing the arrray.

2. Normally, **the BU way is more efficiently** than the UB way
> Just because the UB way use the implementation of recursive.
It will cost **more memory spece** than the loop version.

3. In some situation, the conclusion might be **opposite**.

#### 5) Outlook

<span style="font-size:20px;">
The Merge sort is the **Progressive optimal** sort algorithm when base on **Comparision**[^footnote5]
</span>

[^footnote5]: That is the Merge Sort Algorithm **Ensure** that even in the worst situation, the least times needed are $NlogN$ level.
And we know that is **NO** algorithm which is base on **Comparision** can ensure the least times comparisions less than $log(N!)$, as we know $\sim NlogN$

### 5) Quick Sort

> Quick Sort is an special Merge Sort algorithm. It bases on the Divided & Conquer theory,
Divide the array into two parts, and individually sort each subarray

> **The partition is extremely important.** 
When the left and right subarray was sorted, the whole array is ordered.

#### 1. Implementation
```java
public class Quick {
    public static void sort (Comparable[] a) {
        // Disable the dependency to the input String
        // It's very important.
        StdRandom.shuffle(a);
        sort(a, 0, a.lenth - 1);
    }
    
    private static void sort (Comparable[] a, int lo, int hi) {
        if (hi <= lo) return;
        int j = partition(a, lo, hi);
        // Sort the left subarray.
        sort(a, lo, j - 1);
        // Sort the right subarray.
        sort(a, j + 1, hi);
    }
}
```

#### 2. The Partition

> The goal of the partition is to find the element,

> - **It's left side is *not large* than it,**
- **It's right side is *not small* than it.**

> Usually, we cannot find such element directly, so we just:

> 1. Choose the element **randomly**
2. Scan the array from left to right and backword at the meanwhile
3. Exchange the element which is at the incorrect position
    >> Exchange the $i$ and $j$ when the a[$i$] is **larger** than $v$ or
    the a[$j$] is **smaller than $v$
> 4. Until the two pointer meet each other, and place the partition element in the position.

![The Partition](http://algs4.cs.princeton.edu/23quicksort/images/partitioning-overview.png)

##### 1) Implementation

```java
private static int partition(Comparable[] a, int lo, int hi) {
    int i = lo, j = hi + 1;     // The scanner
    Comparable v = a[lo];
    while (true) {
        /**
        * Scan the left and ritht, and exchange
        */
        // Check for the a[i] is less than the v
        while (less(a[++i], v)) {
            if (i == hi) {
                break;
            }
        }
        // Check the a[j] is larger than the v
        while (less(v, a[--j])) {
             if (j == lo) {     // Redundant, because the v is the lo
                break;
             } 
        }
        if (i >= j) {
            break;
        }
        
        // if all were checked, then exchange the a[i] and a[j]
        exch(a, i, j);
    }
    
    // Place the v into the a[j] place
    exch(a, lo, j);
    return j;
}
```

##### 2) Notation

1. Partition occurs in the original space.
    > If we use a assistant array to do the partition, it will be more costly

2. Do not cross the boundary.
3. Maintain the Randomness
4. Beware the endless loop.
    > A normal mistake is not considering the element which is the same.
5. Beware of the recursive
    > If you cannot place the partition element into the right place, it might cause the infinity recursive trap.

#### 3. The Performance

> Quick sort needs $\sim 2NlnN$ times comparations, and $1/6$ exchanges.
In the worst situation, Quick Sort needs $N^2 / 2$ times comparations.
**But the *shuffle* can prevent this situation.**

#### 4. Improvement

##### 1) Switch to the Insertion Sort.

> For the small array, the Insertion Sort is a better way compare with the original Quick Sort.
So, we can switch to the Insertion Sort when the subarray is small.

```java
if (hi <= lo) return;
//Just replace the statement as
if (ho <= lo + M) {
    Insertion.sort(a, lo, hi); 
    return;
}
// Usually the M value is system-related, but within 5 to 15 is considerable.
```

##### 2) 3 sampling Partition

> We can randomly pick up some small samples and calculate their **median** to be the partition element.
Usually the number set to 3 will be the best.


##### 3) 3-Way Partition

> When we recieve an array which contains a lot of repeating elements, using the original Quick Sort seems to be slow.
In this situation, we use the 3-Way Partition.

###### 1. Theory

> Using 3 pointer to maintain the 3 parts: less equal larger

> - Point $lt$ make the a[lo...lt - 1] is less than the $v$
> - Pointer $gt$ make the a[gt + 1... hi] is larger than the $v$
> - Pointer $i$ make the a[lt...i - 1] is equal to the $v$

1. When a[$i$] is less than $v$, exchange a[$lt$] and a[$i$], and plus the $lt$ and $i$.
2. When a[$i$] is larger than $v$, exchange a[$gt$] and a[$i$], and minus the $gt$.
3. When a[$i$] is equal  to the $v$, plus the $v$.[^footnote6]

[^footnote6]: **All the operation will ensure the element of the array is static, and shorthen the value of $gt - 1$**, only in this way the loop is finite.

###### 2. Implementation

```java
public class Quick3way {
    private static void sort(Comparable a, int lo, int hi) {
        if (hi <= lo) return;
        int lt = lo, i = lo + 1, gt = hi;
        Comararble v = a[lo];
        while (i <= gt) {
            int cmp = a[i].compareTo(v);l
            if (cmp < 0) {
                exch(a, lt++, i++);
            }
            else if (cmp >0) {
                exch(a, i, gt--);
            }
            else {
                i++;
            }
        }
        sort(a, lo, lt - 1);
        sort(a, gt + 1, hi);
    }
}
```

![3way Quick Sort](http://algs4.cs.princeton.edu/23quicksort/images/partitioning3-overview.png)

###### 3. Performance

> For the array which contains the repeated element, there is a variable to describe it. It calls the **Shannon Information**

$$H = -(p_1lgp_1 + p2lgp_2 + \cdots + p_klgp_k)$$

$H - The \ Shannon\ information$
$p_i - The\ posibillty\ of\ the\ ith\ key\ was\ selected$

> For the array which contains repeated element, there is no algorithm which is base on comparatiion can guarantee it can be within $NH - N$ times comparations complete the sort of the array contains $N$ elements.
In the other way, the up bound of comparation sort for this array is $NH - N$

> For the $N$ array, the 3way Partition needs $\sim 2(ln2)NH$ times comparations.

So it prove that the 3way Partition algorithm is the best of the comparation sort.

## 5. Priority Queue

> Priority Queue is DataStucture which is like a queue,
but support **Delete the Biggest or the Smallest element** and **Insert element**.

> And the most important point is the priority queue can sort the extremely big data, or when your memory was rather small.

### 1) Implementation

#### 1. Primary

1. Array implementation (Without Order)
> When the order is not important, we could reuse the *Stack* DataStructure. 
The `insert()` method is the same as the `push()` method in the *Stack*.
As the `delMax()` method, we could sort the *Stack* and **Exchange the biggest element and the element at boundary**

2. Array implementation (With Order)
> We can use array to implement it with order.
To maintain the order, we could move the larger element to the right, and the array is always ordered.
We could just use `pop()` method to delete the biggest element.

3. Linked List
> As the *Stack* and the *Queue*, we could just use the **linked list** to implement the priority queue.
Rather ordered or not is the same as the *Array implementation*, just override the `push()` and `pop()` method is okay.

#### 2. Binary Heap Implementation

##### 1) The definition of binary heap

> Binary Heap is a group of elements,
which could be sorted as the **heap ordered** **complete binary tree** 
and stored as the **layer level** in the array.

$\Delta$ Heap Ordered:
> When **all** the nodes of a binary tree is **greater or equal** to its **two subnodes**, it's called **Heap Ordered**.

> So that,
The **root node** is the **biggest** node in the heap ordered binary tree.

For the Prerequisite Knowledge, see the [Binary Tree](#BinaryTree).

##### 2) The implementation of binary heap

> Notice that, the binary heap is just the **complete binary tree**, 
so it's easy to use the **array** to implement it.


## Supplement 1: The Binary Tree {#BinaryTree}

### 1. The definition of Binary Tree

> Binary Tree is a tree which only has **two child nodes at most**.
Tree is an connected graph which has **no loop**

> The node which is at the top layer is called the **root node**
The node which contains no child node is called **leaf node**, which contains child node is called **internal node**

### 2. Types of Binary Tree

1. Full Binary Tree
> The full binary is that the node is **either leaf node** or **has two chrildren exactly**.

2. The Complete Binary Tree
> The Complete Binary Tree is 
if all levels except possibly the last are completely full, 
and the last level has all its nodes to the left side.

![Full Binary Tree](http://web.cecs.pdx.edu/~sheard/course/Cs163/Graphics/FullBinary.jpg)       ![Complete Binary Tree](http://web.cecs.pdx.edu/~sheard/course/Cs163/Graphics/CompleteBinary.jpg)

> **A Full Binary Tree is not always a Complete Binary Tree.**
**On the contrary, it' s also true**.

### 3. The implementation

#### 1. Array

> This method is just place the element as the order of the corresponding complete binary tree,
so, if a node is at position $k$, then,
its **parent** is at position $\lfloor k \rfloor$,
its **leftChild** is at position $2k$, the **right** is at $2k + 1$

> As you see, the array implementation is only **suitable** for the **complete binary tree** 
With the incomplete one, it will waste lots of space.

#### 2. Linked List

> The Linked List way is much more space-saving. It has 3 parts of the node.
The `data field`, the `leftChild pointer`, the `rightChild pointer`

Node:
<table style="width:20em;">
<tr>
<td>leftChild</td> <td>data</td> <td>rightChild</td>
</tr>
</table>


### 4. The Traversal Algorithm

> Normally, There are 3 different ways to traversal a binary tree. They are:

> 1. PreOrder Traversal ($DLR$)
2. InOrder Traversal ($LDR$)
3. PostOrder Traversal ($LRD$)

> Actually, there are 3 more ways, but we assume the left child is alway **the elder brother** of the right child. So we reduce to 3 ways.

> The traversal Algorithm all use the **recursive way** to implement.

#### 1) Depth-first

> The first child, then **the grand child** before the second child

##### 1. PreOrder Traversal

1. Display the data part of root element (or current element)
2. Traverse the left subtree by recursively calling the pre-order function.
3. Traverse the right subtree by recursively calling the pre-order function.

##### 2. InOreder Traversal 

1. Traverse the left subtree by recursively calling the in-order function
2. Display the data part of current element.
3. Traverse the right subtree by recursively calling the in-order function

##### 3. PostOrder Traversal

1. Traverse the left subtree by recursively calling the post-order function.
2. Traverse the right subtree by recursively calling the post-order function.
3. Display the data part of root element (or current element).

#### 2) Breadth-first

> The first child, then the second child, and then the first grand child, the second grand child, and so on.
We do not go to the next level until the current level is done.

```java

interface Visitable<Item> {
    void onVisit(Item item);
}

class BreadthFirst {
    Visitable<Node> visiter;
    ....
    void breadFirstTraversal(Node root) {
        Queue q = new Queue();
        q.enQueue(root);
        while (!q.isEmpty()) {
            Node node = q.deQueue();
            visiter.onVisit(node);
            if(node.lChild != null) {
                q.enQueue(node.lChild);
            }
            if(node.rChild != null) {
                q.enQueue(node.rChild);
            }
        }
    }
}
```

### 5. Binary Tree & Forest

#### 1) The definition of Forest

> Forest is consist of a lot of individual trees, when they come together, we call them **Forest**

![Forest](https://helloacm.com/wp-images/acm/2012/data-structure/disjoint1.jpg)

> We could link its root nodes of each tree to bulid a big tree.

#### 1) The Representation of Forest

> Firstly, we tranfer it to the bing tree, just link its root node of each tree together.

##### 1. The Child and Brother Representation

> It's a linked list implementation, The node contains 3 parts, 
the `Data Field`, 
the `leftChild pointer` (or reference), which point to its **left most child**
and the `brother pointer` (or reference), which point to its **right brother**.

Node:
<table style="width:20em;">
<tr>
<td>leftChild</td> <td>Data</td> <td>brother</td>
</tr>
</table>

> Since the Node has **the same number** of parts compare with the **binary tree's node**,
We could transfer **the big tree** to the specific **binary tree**, 
as the big tree is transfered from the **forest**,
so that, we could transfer **the forest** to **the binary tree** easily.
