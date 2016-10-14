# Java Multithreading Synchronize

Tags: Java

Base on *Core Java Volume Ⅰ——Fundamentals* and many Posts
> 8.1 - 8.10 为 Java 线程同步的基础——锁和 `synchronized`
8.11 以后为高级并发工具
应用层面优先选择并发工具和并发库

---

<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 flatten:0 bullets:0 updateOnSave:1 -->

[Java Multithreading Synchronize](#java-multithreading-synchronize)  
&emsp;[8.5 线程同步](#85-线程同步)  
&emsp;&emsp;[8.5.0 Intro](#850-intro)  
&emsp;&emsp;[8.5.1 使用 ReentrantLock 实现同步](#851-使用-reentrantlock-实现同步)  
&emsp;&emsp;&emsp;[8.5.1.1 锁的初级使用](#8511-锁的初级使用)  
&emsp;&emsp;&emsp;[8.5.1.2 公平锁](#8512-公平锁)  
&emsp;&emsp;&emsp;[8.5.1.3 条件对象](#8513-条件对象)  
&emsp;&emsp;&emsp;&emsp;[8.5.1.3.1 使用条件对象的原因](#85131-使用条件对象的原因)  
&emsp;&emsp;&emsp;&emsp;[8.5.1.3.2 使用条件对象](#85132-使用条件对象)  
&emsp;&emsp;[8.5.2 `synchronized` 关键字](#852-synchronized-关键字)  
&emsp;&emsp;&emsp;[8.5.2.1 内部锁](#8521-内部锁)  
&emsp;&emsp;&emsp;[8.5.2.2 唯一的条件对象](#8522-唯一的条件对象)  
&emsp;&emsp;&emsp;[8.5.2.3 例子](#8523-例子)  
&emsp;&emsp;&emsp;[8.5.2.4 局限性](#8524-局限性)  
&emsp;&emsp;&emsp;[8.5.2.5 总结](#8525-总结)  
&emsp;&emsp;[8.5.3 同步阻塞](#853-同步阻塞)  
&emsp;&emsp;[8.5.4 监视器](#854-监视器)  
&emsp;&emsp;[8.5.5 Volatile 域](#855-volatile-域)  
&emsp;&emsp;&emsp;[8.5.5.1 正确使用 `volatile` 变量的条件](#8551-正确使用-volatile-变量的条件)  
&emsp;&emsp;&emsp;[8.5.5.2 性能考虑](#8552-性能考虑)  
&emsp;&emsp;&emsp;[8.5.5.3 正确使用的情形](#8553-正确使用的情形)  
&emsp;&emsp;[8.5.6 `final` 变量](#856-final-变量)  
&emsp;&emsp;[8.5.7 死锁](#857-死锁)  
&emsp;&emsp;[8.5.8 线程局部变量](#858-线程局部变量)  
&emsp;&emsp;[8.5.9 锁测试与超时](#859-锁测试与超时)  
&emsp;&emsp;[8.5.10 读/写锁](#8510-读写锁)  
&emsp;&emsp;&emsp;[8.5.10.1 使用步骤](#85101-使用步骤)  
&emsp;&emsp;[8.5.11 并发工具](#8511-并发工具)  
&emsp;&emsp;&emsp;[8.5.11.1 阻塞队列](#85111-阻塞队列)  
&emsp;&emsp;&emsp;&emsp;&emsp;[8.5.11.1.1 API](#851111-api)  
&emsp;&emsp;&emsp;&emsp;[8.5.11.1.2 例子](#851112-例子)  
&emsp;&emsp;&emsp;[8.5.11.2 线程安全的集合](#85112-线程安全的集合)  
&emsp;&emsp;[8.5.12 `Callable` 和  `Future`](#8512-callable-和-future)  
&emsp;&emsp;&emsp;[8.5.12.1 `Callable`](#85121-callable)  
&emsp;&emsp;&emsp;[8.5.12.2 `Future`](#85122-future)  
&emsp;&emsp;&emsp;[8.5.12.3 `FutureTask`](#85123-futuretask)  
&emsp;&emsp;[8.5.13 执行器(Executor)](#8513-执行器executor)  
&emsp;&emsp;&emsp;[8.5.13.1 基本使用](#85131-基本使用)  
&emsp;&emsp;&emsp;[8.5.13.2 `ScheduledExecutorService` 预定执行](#85132-scheduledexecutorservice-预定执行)  
&emsp;&emsp;&emsp;[8.5.13.3 控制任务组](#85133-控制任务组)  
&emsp;&emsp;&emsp;[8.5.13.4 Fork-Join 框架](#85134-fork-join-框架)  
&emsp;&emsp;[8.5.14 同步器（Synchronizer）](#8514-同步器（synchronizer）)  

<!-- /MDTOC -->

---



## 8.5 线程同步

### 8.5.0 Intro

由于每句代码只能在一个线程中执行，当多个线程试图访问同一个对象域时，就会出现**竞争**，导致对象的数据最终出现错误。
特别是当线程中的操作**不是原子操作**的时候，当线程切换的时候。

为了消除竞争的危害，对于多个线程**有可能**同时操作同一个对象的情况，我们就要实现**线程同步**

实现线程同步的方法主要有三种：

1. 使用 `Lock/Condition` 即显式的锁
2. 使用 `synchronized` 关键字
3. 使用并发库和阻塞类来实现线程管理

> **Executor 和 Task 优先于线程**
**并发工具优先于 `wait()` 和 `notify()`**
—— *Effective Java Second Edition*

注意，线程同步不仅要求**互斥性**，也要求**可见性**，即只有一个线程能对同步代码块进行操作，同时，**该代码块对所有线程应是可见的**

### 8.5.1 使用 ReentrantLock 实现同步

#### 8.5.1.1 锁的初级使用

`ReentrantLock` 是一个锁对象，在有可能出现竞争的方法中使用锁，就可以**保护**一段代码块**同一时间只能由一个线程进行读写操作**

例如：

```java
public class Bank {
    private ReentrantLock myLock;
    public void transfer() {
        myLock.lock();
        // ----------- 临界区
        try {
            // some works
        }
        finally {
            myLock.unlock();
        }
        // ---------- 临界区
    }
}
```

在临界区之间的代码是受锁对象保护的，当其他线程试图执行临界区代码（试图获取锁）时，就会导致线程阻塞，直到当前执行的线程解开锁为止。

注意要将解锁代码放置在 `finally` 中，否则可能会由于异常的抛出而无法解锁。
此时，不能使用**带资源的try块**。
因为要在 `finally` 中释放锁，而释放锁的方法不是 `close()`

锁是**可重入**的，锁对象自身维护一个**持有计数**，如果在临界区中调用了另一个被锁保护的方法，那么，计数器增加，解锁后，计数器减少，直到持有计数为 0 时，线程才会释放锁。

当由于**异常而跳出临界区**时，应进行相应的清理操作，保证对象的完整性。
因为在 `finally` 中，锁会被释放。

#### 8.5.1.2 公平锁

使用 `ReentrantLock(boolean fair)` 可以指定构造一个**公平锁**。
它倾向于让阻塞队列中等待时间最长的线程获取到锁，但是额外的检测成本可能会造成性能损失。

#### 8.5.1.3 条件对象

条件对象 `Condition` 用于确保临界区中的代码符合执行条件。

##### 8.5.1.3.1 使用条件对象的原因

1. 不能使用一般的 `if` 语句进行检查

    > 因为 `if` 是非原子性的，线程可能在通过检查之后被剥夺，再次进入时却又不满足执行条件。

    ```java
    // DON'T DO THAT!!
    if (bank.getBalance(form) >= amount) {
        // transfer() was protected by Lock object.
        bank.transfer(from, to, amount)
    }
    ```

2. 不能在临界区内检查条件

    > 有可能在条件不满足的情况下，需要其他线程的协助才能满足条件。
    例如，当前线程操作的账户对象不满足转出余额，那么就需要**等待另一线程向当前账户注资**。
    此时，由于当前线程**占有锁**，其他线程无法操作这一账户。

##### 8.5.1.3.2 使用条件对象

1. 通过锁对象的 `newCondition()` 来获得一个条件对象。
2. 当条件不满足时， 调用**条件对象的** `await()` 方法

    > 该方法会使当前线程阻塞，加入条件对象等待队列，并**放弃锁**

3. 当**条件有可能满足时**，调用**条件对象的** `singalAll()` 方法

    > 这一方法会激活**所有的**等待该条件对象的线程，并尝试重新获取锁，从被阻塞的地方**继续执行**
    此时，线程应**再次测试条件**，因为此时无法确保条件是否被满足。

    > 之所以不能确保，是因为线程在 `await()` 之后，**不具备将自己唤醒的能力**，必须由另一线程执行 `singalAll()` 方法。
    如果没有一个线程能够调用 `singnal`，那么此时系统就**死锁**了。
    所以就应在**对象的状态有利于等待线程的改变时**调用 `singalAll()` 方法。

    > 另外，也有一个 `singal()` 方法，这个方法会随机选择一个等待线程进行唤醒。

综上，以下是使用条件对象的基本框架：

```java
class Bank {
    private Condition sufficientFunds;
    private ReentrantLock bankLock;
    ....
    public Bank() {
        ...
        // Using the Lock object to
        // get the condition object reference
        sufficientFunds = bankLock.newCondition();
    }

    ...

    public void transfer(int from, int to, int amount) {
        // Lock the code
        bankLock.lock();
        try {
            while(accounts[from] < amount) {
                // Don't have sufficient funds, await
                sufficientFunds.await();
            }
            // Have sufficient funds
            // Transfer funds..
            ...
            // Transfer complete, singnal all
            sufficientFund.singnalAll();
        }
        finally {
            // Unlock the code
            bankLock.unlock();
        }
    }
}
```

### 8.5.2 `synchronized` 关键字

#### 8.5.2.1 内部锁

这里比 8.5.1 更 “高级” 和傻瓜性了；
其实从 jdk 1.0 开始，任何 Java 对象都拥有一个**内部锁**；
我们不需要再显式实现一个锁和条件对象的架构了。

如果一个方法用 `synchronized` 声明，那么对象的锁将保护整个方法;

也就是说：

```java
// Both of these method is equivalent

public synchronized void method() {
    // method body
}

public void method() {
    this.intrinsicLock.lock();
    try {
        // method body
    }
    finally {
        this.intrinsicLock.unlock();
    }
}
```

#### 8.5.2.2 唯一的条件对象

对象的内部锁拥有唯一一个条件对象；
通过 `wait()` 方法将线程添加到条件的等待队列；
通过 `notifyAll()` `notify()` 方法解除等待线程的阻塞

也就是说：

```java
wait(); == intrinsicCondition.await();
notify()All == intrinsicCondition.singnalAll();
```

#### 8.5.2.3 例子

使用 `synchronized` 重写的 `Bank` 类

```java
class Bank {
    private double[] accounts;

    public synchronized void transfer(int form, int to, int amount) throws InterruptedException {
        while (accounts[from] < amount) {
            // Do not have suffient funds
            // Using wait() method instead of await()
            wait();
        }
        // Do have suffient funds
        // Transfering..
        accounts[from] -= amount;
        accounts[to] += amount;

        // Transfer done
        // Using notifyAll() method instead of singnalAll()
        notifyAll();
    }

    public synchronized double getTotalBalance() {...}
}
```

#### 8.5.2.4 局限性

可以看到，使用 `synchronized` 关键字大大减少了代码量，使代码更为整洁；
但是对应的，也存在一些缺点：

1. 不能中断一个正在试图获得锁的进程

    > 因为锁在对象内部，开发者无法操作，2 同

2. 试图获得锁时，不能设定超时
3. 每个锁仅有单一的条件，可能是不够的

#### 8.5.2.5 总结

那么，究竟是使用 `synchronized` 关键字还是 `Lock/Condition` 机制呢？

1. **最好两者都不使用**，使用 Java 自带或一些第三方的并发工具来处理同步问题。

    > *Effective Java* 中提到 “并发工具优先” 的概念，即，成套的并发库和并发工具，要优先于使用 `wait()`, `notify()` 方法

2. 如果不想采用并发库，并且 `synchronized` 的缺点并没有对程序造成影响，那么**尽量使用它**

    > 这样可以减少编写的代码，减少出错的几率

3. 如果特别需要 `Lock/Condition` 的独有特性时，那么才使用 `Lock/Condition`

    > 比如说即时中断，特定的等待超时等。

### 8.5.3 同步阻塞

同步阻塞允许客户使用

```java
synchronized(lock) {
    // method body
}
```
获取到内部的锁

这也叫做**客户端锁定**，这个方法是很脆弱的，通常不推荐使用

### 8.5.4 监视器

监视器是 *Per Brinch Hansen* 提出的面向对象的线程安全实现方式。

使用 Java 语言来表述就是：

1. 监视器是只包含**私有域**的类
2. 每个监视器类的对象有一个相关的锁
3. 使用该锁对所有的方法进行加锁
4. 该锁可以有任意多个相关条件

**Java 的 `synchronized` 关键字使用一种不严谨的方法实现了监视器**

> 但是这也导致了 *Per Brinch Hansen* 本人的批评

### 8.5.5 Volatile 域

`volatile` 可以被看做是一种 **程度较轻的 `synchronized`**;
它只具有 `synchronized` 提供的**可见性**，而不具备**原子性**
同时， `volatile` 变量**不会造成阻塞**

这说明了，当我们需要同步的写入操作时，`volatile` 就不适用了；
但是如果该变量仅用于读取，那么 `volatile` 能提供优于 `synchronized` 的性能。


#### 8.5.5.1 正确使用 `volatile` 变量的条件

1. 对该变量的写操作**不依赖于**当前值

    > 比如说，用 `volatile` 变量做计数器是不行的，因为计数器的增加要先读取当前值

2. 该变量没有包含在具有其他变量的不变式中

大多数的编程情形都会和这两个条件的其中之一冲突，使得 `volatile` 不能如 `synchronized` 一样普遍实现线程安全

#### 8.5.5.2 性能考虑

一般情况下， `volatile` 的性能要比使用 `synchronized` 要高；
所以在符合使用 `volatile` 的情形下应该尽量使用。

#### 8.5.5.3 正确使用的情形

1. 状态标志

    > 这是 `volatile` 的最常使用情形，作为一个布尔状态标志，用于指示发生了一个重要的一次性事件，或监视线程状态（是否被终止）

    ```java
    volatile boolean shutdownRequested;

    ...

    public void shutdown() { shutdownRequested = true; }

    public void doWork() {
        while (!shutdownRequested) {
            // do stuff
        }
    }
    ```

    > 此时，很可能需要从外部（另一线程）调用 `shutdown()` 方法，那么就需要保证 `shutdownRequested` 的可见性。
    此时，显然使用 `volatile` 关键字会更好

2. 一次性安全发布

    > 当缺乏同步可见性时，可能会出现一个线程获取到了一个**不完全构建的对象**，从而出现**更新值**和**旧值**同时存在。
    此时，可以将该对象的引用定义为 `volatile` 类型，然后在使用前通过检查该引用就可以知道对象是否安全发布了。

    ```java
    public class BackgroundFloobleLoader {
        public volatile Flooble theFlooble;

        public void initInBackground() {
            // do lots of stuff
            theFlooble = new Flooble();  // this is the only write to theFlooble
        }
    }

    public class SomeOtherClass {
        public void doWork() {
            while (true) {
                // do some stuff...
                // use the Flooble, but only if it is ready
                if (floobleLoader.theFlooble != null)
                    doSomething(floobleLoader.theFlooble);
            }
        }
    }
    ```

    > 注意使用的条件在于，**该对象一经发布就不可修改，或者是线程安全对象**
    如果需要对该对象进行异步更改，那么就需要 `synchronized` 等进行额外的同步操作。

3. 独立观察

    > `volatile` 变量可以定期的发布一些观察结果供程序内部使用，或者收集必要的统计信息

    ```java
    // Record the last login user's account
    public class UserManager {
        public volatile String lastUser;

        public boolean authenticate(String user, String password) {
            boolean valid = passwordIsValid(user, password);
            if (valid) {
                User u = new User();
                activeUsers.add(u);
                lastUser = user;
            }
            return valid;
        }
    }
    ```

    > 这个模式和上述的模式稍有不同，使用该值的代码需要清除该值可能会随时变化。

4. volatile bean 模式

    > 这是 Java Bean 模式的一种。
    它要求，所有的数据成员都是 `volatile` 的，同时， getter & setter 必须非常简单，不包含其他复杂代码
    该模式为一些易变数据提供了容器，但是要求**放入这些容器的对象必须是线程安全的**

    ```java
    @ThreadSafe
    public class Person {
        private volatile String firstName;
        private volatile String lastName;
        private volatile int age;

        public String getFirstName() { return firstName; }
        public String getLastName() { return lastName; }
        public int getAge() { return age; }

        public void setFirstName(String firstName) {
            this.firstName = firstName;
        }

        public void setLastName(String lastName) {
            this.lastName = lastName;
        }

        public void setAge(int age) {
            this.age = age;
       }
}
    ```

5. 高级应用——开销较低的读——写锁策略

    > 当对于一个变量的读操作远远超过写操作时，我们就可以使用 `volatile` 关键字修饰该变量，用于保证可见性，同时对 setter 方法采取 `synchronized` 修饰保证同步性，实现较低开销的读和写锁

    ```java
    @ThreadSafe
    public class CheesyCounter {
        // Employs the cheap read-write lock trick
        // All mutative operations MUST be done with the 'this' lock held
        @GuardedBy("this") private volatile int value;

        public int getValue() { return value; }

        public synchronized int increment() {
            return value++;
        }
    }
    ```

### 8.5.6 `final` 变量

如果一个域被声明为 `final`，那么对于该**变量**将不会出现线程安全问题。
其他线程将在 `final` 变量被赋值成功后才能见到此变量。

注意，只有**变量**是线程安全的，其指向的数组、对象等仍然需要同步操作。

### 8.5.7 死锁

Java 并不能在语言层次上避免或打破死锁的发生，这是程序设计的工作。

### 8.5.8 线程局部变量

如果要避免线程间共享变量，那么可以使用 ThreadLocal 辅助类为各个线程提供各自的实例。

例如，如果要让每个线程都拥有自己的 `SimpleDateFormat` 变量，那么只需要

```java
public static final ThreadLocal<SimpleDateFormat> dateFormat =
    new ThreadLocal<SimpleDateFormat>() {
        protected SimpleDateFormat initalValue() {
            return new SimpleDateFormat("yyyy-MM-dd");
        }
    }
```

如果要访问具体线程的格式化方法，可以调用

```java
String dateStamp = dateFormat.get().format(new Date());
```

在一个**给定线程**中**首次调用** `get()` 方法时，会调用 `initialValue()` 方法。
在此之后， `get()` 会返回属于当前线程的那个实例

$\Delta$ 对于随机数生成器，如果需要线程独享的随机数生成器，那么可以使用

```java
int random = ThreadLocalRandom.current().nextInt(upperBound);
```

`current()` 会返回特定于当前线程的 `Random` 类实例。

另外还有个 `set()` 和 `remove()` 方法，分别用于为当前线程设置新值和删除当前线程的值。

### 8.5.9 锁测试与超时

如果要使用这一特性，就要使用 `Lock/Condition` 架构。

由于尝试获取锁会导致阻塞，使用 `tryLock` 可以试图申请一个锁，成功则返回 `true`, 失败返回 `false`，同时，线程可以**立即离开**做其他事情

```java
if (myLock.tryLock()) {
    // now the thread owns the lock
    try {...}
    finally {
        myLock.unlock();
    }
}
else {
    // Do something else
}
```

同时，还可以设置**超时参数**

```java
if (myLock.tryLock(100, TimeUnit.MILLSECONDS));
```

注意， `tryLock()` 会**忽略**锁的公平性

`lock()` 方法不能被中断，如果一个线程在等待获取锁时被中断，**那么就有可能会造成死锁**

但是，如果采用 `tryLock()`，如果线程在等待期间被中断，将抛出 `InterruptedException` ，此时就可以用这个特性来跳出死锁问题。

同时，`await()` 方法也可以设定超时。

### 8.5.10 读/写锁

如果很多线程从一个数据结构读取数据而很少修改其中数据的话，那么我们使用另一种锁 `ReentrantReadWriteLock` 来提高性能

此时，允许读线程**共享访问**，写线程为**互斥访问**

> 这里有点像 `volatile` 的高级应用；
不同的点在于，`volatile` 用于一个变量，而 `ReentrantReadWriteLock` 用于一个**数据结构**

#### 8.5.10.1 使用步骤

1. 构建 `ReentrantReadWriteLock` 对象

    ```java
    private ReentrantReadWriteLock rwl = new ReentrantReadWriteLock();
    ```

2. 抽取读锁和写锁

    ```java
    private Lock readLock = rwl.readLock();
    private Lock writeLock = rwl.writeLock();1
    ```

3. 对所有的 getter 加读锁

    ```java
    public double getTotalBalance() {
        readLock.lock();
        try {...}
        finally {
            readLock.unlock();
        }
    }
    ```

4. 对所有 setter 加写锁

    ```java
    public void transfer(...) {
        writeLock.lock();
        try {...}
        finally {
            writeLock.unlock();
        }
    }
    ```

### 8.5.11 并发工具

对于很多的多线程问题，我们不需要再去实现一遍底层的锁和同步机制了。
对于一般的应用向问题，应**优先采用并发工具**

> Executor 和 Task 优先于线程(`Runnable`)
并发工具优先于 `wait()` 和 `notify()`
—— *Effective Java Second Edition*

#### 8.5.11.1 阻塞队列

对于许多线程问题，可以通过使用一个或者多个队列来将其形式化。可以通过 `Producesor` 将任务加入队列，然后由 `Comsumor` 来将任务取出然后进行处理的方式来实现。

Java 的阻塞队列自带了阻塞特性，**不再需要显式的同步**

###### 8.5.11.1.1 API

这里只介绍阻塞队列的阻塞方法，实际上阻塞队列也包含一些非阻塞的方法

方法    |   正常动作    |   特殊情况下的动作
:----:  |   :------:    |   :--------:
put     |   添加一个元素    |   如果队列满，则阻塞
take    |   移出并返回头元素|   如果队列空，则阻塞
offer   |   添加一个元素，并返回 true| 如果队列满，则返回 false
poll    |   移出并返回队列的头元素| 如果队列空，则返回 null
peek    |   返回队列的头元素（**不移出**）| 如果队列空，则返回 null

> 注意：

> 1. offer 、peek、poll **在特殊情况下并不阻塞**，但是它们有对应的**超时版本**
2. 由于 peak poll 带有 **返回 `null`** 的属性，所以**不能往这样的队列插入 `null` 值**
3. 这个队列还具有 `add()` 和 `remove` 方法，但是它们在特殊情况下会**抛出异常**，所以在多线程程序中不要使用这样的方法。

Java 准备了多种实现形式的阻塞队列，包括链表、双端链表、数组等实现，甚至包括优先队列。

同时，Java 1.7 还提供了 `TransferQueue` 接口，这个接口允许生产者线程等待，直到消费者线程准备就绪。

##### 8.5.11.1.2 例子

下面是一个使用阻塞队列来管理多线程关系的例子：
即，**生产者线程将元素加入到队列中，消费者线程将元素取出进行处理**

```java
public class BlockingQueueExample {
    public static void main(String[] args) throws Exception {
        BlockingQueue bq = new ArrayBlockingQueue(1000);
        Producer producer = new Producer(bq);
        Consumer consumer = new Consumer(bq);

        new Thread(producer).start();
        new Thread(consumer).start();

        Thread.sleep(4000);
    }
}


/**
* Producer generate the sum.
* And add it into the queue
*/
public class Producer implements Runnable {
    private BlockingQueue bq = null;

    public Producer(BlockingQueue queue) {
        this.setBlockingQueue(queue);
    }

    // The blocking queue has a internal synchronize
    // The delay of each end of the addition will show this
    public void run() {
        Random rand = new Random();
        int res = 0;
        try {
            res = Addition(rand.nextInt(100), rand.nextInt(50));
            System.out.println("Produced: " + res);
            bq.put(res);
            Thread.sleep(1000);

            res = Addition(rand.nextInt(100), rand.nextInt(50));
            System.out.println("Produced: " + res);
            bq.put(res);
            Thread.sleep(1000);

            res = Addition(rand.nextInt(100), rand.nextInt(50));
            System.out.println("Produced: " + res);
            bq.put(res);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    public void setBlockingQueue(BlockingQueue bq) {
        this.bq = bq;
    }

    public int Addition(int x, int y) {
        int result = 0;
        result = x + y;
        return result;
    }
}

/**
* Comsumer take the result from the queue.
* And print it out to the output
*/
public class Consumer implements Runnable {
    protected BlockingQueue queue = null;

    public Consumer(BlockingQueue queue) {
        this.queue = queue;
    }

    public void run() {
        try {
            System.out.println("Consumed: " + queue.take());
            System.out.println("Consumed: " + queue.take());
            System.out.println("Consumed: " + queue.take());
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
```

The output:

```
Produced: 93
Consumed: 93
Produced: 69
Consumed: 69
Produced: 76
Consumed: 76
```

#### 8.5.11.2 线程安全的集合

在 `java.util.concurrent` 包提供了许多线程安全的集合。
主要用于**多线程并发修改一个数据结构**的并发问题。
包括 哈希表、有序集和队列等

一般来说，线程安全的集合要比一般的集合**更高效**

在较早的 Java 版本，曾有“同步包装器”使得一般的集合类型变为同步的，但是现在已经不推荐使用了，**最好使用 `java.util.concurrent` 包中的集合**


### 8.5.12 `Callable` 和  `Future`

#### 8.5.12.1 `Callable`

`Callable` 是一个**带返回值**的 `Runnable`，具有泛型特性。
例如 `Callable<Integer>` 表示一个最终返回 `Interger` 的异步计算

#### 8.5.12.2 `Future`

`Future` 保存异步任务的结果，可以将其启动然后交给一个线程。
所有者在任务执行完毕后，可以通过 `get()` 方法获得结果。

`Future` 具有以下方法

```java
public interface Future<V> {
    V get() throws ...;
    V get(long timeout, TimeUnit unit) throws ...;
    void cancel(boolean mayInterrupt);
    boolean isCancelled();
    boolean isDone();
}
```

第一个 `get()` 调用直到计算完成前会被**阻塞**；
如果任务完成前第二个 `get()` 超时，则抛出 `TimeoutException`
如果线程被中断，则都抛出 `InterruptedException`
如果任务已经完成，那么 `get()` 立即返回

可以使用 `cancel()` 方法来**中断**任务，
如果任务没有开始，则它将被取消而不会再运行，
如果任务已经在运行，那么则由 `mayInterrupt` 参数来决定是否**中断**任务
如果任务**已经被取消**或者**已经完成**，那么返回 `false`，其他情况返回 `true`
> 注意，**此方法一旦返回，则 `isDone()` 永远返回 `true`**

#### 8.5.12.3 `FutureTask`

Java 实现了 `FutureTask` 包装器，它是一个类，同时实现了 `Runnable` 和 `Future` 接口
它接受一个 `Callable` 接口作为构建器参数，主要用于将 `Callable` 转换为 `Runnalbe` 和 `Future`

可以如下使用

```java
Callable<Integer> myComputation = ...;
FutureTask<Integer> task = new FutureTask<Integer>(myComputation);
Thread t = new Thread(task)     // It's a Runnale
t.start();
...
Integer result = task.get();    // It's a Future
```

### 8.5.13 执行器(Executor)

如果你需要做一些重复性较高的异步任务，或者创建大量的生命期很短的线程，那么就应该用线程池来管理。
实际上，为了提高效率，执行任何的并发任务，都应该优先考虑 Execulator 和 Task

> Execulator 和 Task 优先于线程(Thread)
—— *Effective Java Second Edition*

在这里，并发的最小单位升级为 `Executor` 和 `Task`。
所谓的 `Task` 就是用户构建的 `Runnable` 或者 `Callable` 对象；
这也是为什么要优先采用 `Runnable` 的原因

#### 8.5.13.1 基本使用

基本的使用步骤如下：

1. 使用 `Executors` 的静态方法构建线程池，或者叫 `ExecutorService`
2. 调用 `execute()` 或 `submit()` 提交 `Runnable` 或 `Callable` 对象
3. 当不在提交任务时，调用 `shutdown()`

> 注意，还有一个 `execute()` 方法执行 `submit()` 的效果。
它们的主要区别在于，
`execute()` 会触发**未捕获处理器**，从而向 `System.err` 输出错误信息;
`submit()` 会抛出 `ExecutionException`，可以使用 `getCause()` 获取出错信息

> 另外， `submit()` 返回的是 `Future` 对象，可以通过它取消特定任务。
由此，如果使用 `Callable` 那么使用 `submit()`；
如果使用 `Runnable` 那么使用 `execute()`

例子：

```java
ExecutorService executorService = Executors.newFixedThreadPool(10);

executorService.execute(new Runnable() {
    public void run() {
        System.out.println("Asynchronous task");
    }
});

executorService.shutdown();
```

#### 8.5.13.2 `ScheduledExecutorService` 预定执行

该类是 `ExecutorService` 的子类，用于构建**预订性**和**重复性、周期性** 的任务

可以指定任务只运行一次，也可以指定任务的运行周期

#### 8.5.13.3 控制任务组

使用 `ExecutorService` 的另一个重要原因就是可以实现控制一组相关任务。
特别是在采用**分治策略**的算法中常常能用到。

例如，使用对一个大整数进行因式分解，那么我们可以将整个过程分成很多很小的过程，当小任务全部解决完毕时，整数的因式分解也就完毕了。

或者，我们可以用它来提交很多对于同一个问题的不同解决方案，如果有任何一个解决方案得出答案，那整个任务就可以停止了。

对于以上两种情况，使用 `ExecutorService` 分别有两种方法进行对应：

1. `invokeAll()`，这个方法**提交所有的 `Callable` 到一个集合中**，并返回一个 `Future` 对象，代表**所有任务解决结果**
2. `invokeAny()`，这个方法**提交所有的 `Callable` 到一个集合中**，并返回一个 `Future` 对象，代表**某一个任务的解决结果**

例子：

```java
// invokeAll -- Return a List of Future
List<Callable<T>> task = ...;
List<Future<T>> results = executor.invokeAll(task);

// invokeAny -- Return only one Future
Future<T> resultOfInvokeAny = executor.invokeAny(task);
```

可以使用 `ExecutorCompletionService` 来对 `invokeAll()` 得到的结果集进行排列处理

```java
// executor is a ExecutorService
ExecutorCompletionService service = new ExecutroCompletionService(executor);

for (Callable<T> task : tasks) {
    service.submit(task);
}

for (int i = 0; i < tasks.size(); i++) {
    processFurther(service.take().get());
}
```

#### 8.5.13.4 Fork-Join 框架

对于多线程处理的**分治策略**的任务， Java 实现了一种 Fork-Join 框架来更好的实现这种任务流程。

分治的很常见的实现方式是**递归实现**，这个框架也使用了**递归**的思路

使用步骤：

1. 提供一个扩展了 `RecursiveTask<T>` 或者 `RecursiveAction` 的类
2. Override `compute()` 方法，在其中调用子任务并将其合并

例子：

```java
class Counter extends RecursiveTask<Integer> {
    ...
    @Override
    protected Integer computer() {
        if (to - from < THRESHOLD) {
            // solve problem directly
        }
        else {
            int mid = from + (to - from) / 2;
            // Recursive solve left
            Counter first = new Counter(values, form, mid, filter);
            // Recursive solve right
            Counter second = new Counter(values, mid, to, filter);
            invokeAll(first, second);   // Add both to executor
            return first.join() + second.join(); // bind the solution
        }
    }
}
```

### 8.5.14 同步器（Synchronizer）

同步器是并发工具的一种，一些使线程能够等待另一个线程的对象，允许它们协调动作。

<table>
<th colspan="3" style="text-align:center;">同步器</th>

<tr style="text-align:center;">
<td style="text-align:center;">类</td>
<td style="text-align:center;">作用</td>
<td style="text-align:center;">何时使用</td>
</tr>

<tr style="text-align:center;">
<td style="text-align:center;">CyclicBarrier  (不常用)</td>
<td style="text-align:center;">允许线程集等待直到其中预定数目的线程到达一个公共障栅(barrier)，然后可以选择执行一个处理 barrier 的动作</td>
<td style="text-align:center;">当大量的线程需要在它们的结果可用之前完成时</td>
</tr>

<tr style="text-align:center;">
<td style="text-align:center;">CountDownLatch (常用)</td>
<td style="text-align:center;">允许线程集等待直到计数器为 0</td>
<td style="text-align:center;">当线程需要等待事件发生（才允许执行时）</td>
</tr>

<tr style="text-align:center;">
<td style="text-align:center;">Exchanger（不常用）</td>
<td style="text-align:center;">允许两个线程在要交换的对象准备好时交换对象</td>
<td style="text-align:center;">当两个线程工作在同一个数据结构的<b>两个实例</b>上时</td>
</tr>

<tr style="text-align:center;">
<td style="text-align:center;">Semaphore（常用）</td>
<td style="text-align:center;">允许线程集等待知道它被允许继续执行为止</td>
<td style="text-align:center;">限制访问资源的线程总数</td>
</tr>

<tr style="text-align:center;">
<td style="text-align:center;">SynchronousQueue</td>
<td style="text-align:center;">允许一个线程将对象交给另一个线程</td>
<td style="text-align:center;">在没有显式同步的情况下，当两个线程准备好将一个对象传递到另一个时</td>
</tr>
</table>

> 注意 `CountDownLatch`，这个类用于**让某些线程等待其他线程**。
它是唯一一个带有 `int` 构造参数的同步器，用于**指定等待的并发线程的个数**

> 形象来说，就是一个红绿灯，直到倒计时完毕，线程才可以运行
下面是一个简单的多线程计时的例子

```java
/**
* A simple timing concurrent execution.
* The timer will not start until all the worker thread are ready.
* And when the last worker thread done, the timer stop
*/
public static long time(Executor executor, int concurrency, final Runnalbe action) throws InterruptedException {
    final CountDownLatch ready = new CounDownLatch(concurrency);
    final CountDownLatch start = new CounDownLatch(1);
    final CountDownLatch done = new CounDownLatch(concurrency);

    for (int i = 0; i < concurrency; i++) {
        executor.execute(new Runnable() {
            // This is the worker thread
            public void run() {
                ready.countDown(); // Tell the timer worker is ready
                try {
                    start.await(); // Worker stuck at start point

                    // Because of blocking,
                    // this statement will not run
                    // until the start count down reach 0
                    action.run();
                } catch (InterruptedException) {
                    Thread.currentThread().interrupt();
                } finally {
                    done.countDown();   // Tell the timer worker is done
                }
            }
        });
    }

    // This is the timer thread
    ready.await();  // Wait for all the workers are done
    long startNanos = System.nanoTime();
    start.countDown();  // Let worker thread off!!
    done.await();   // Wait for worker done.
    return System.nanoTime() - startNanos;
}
```

> 在**线程**中调用锁存器的 `await()` 方法**可以阻塞当前线程**
当锁存器的计数器为 0 时，**所有的被该锁存器阻塞的线程即刻执行**

> 锁存器是共享的，在任何线程中都可被更改
一旦归 0，障碍即刻被放弃
