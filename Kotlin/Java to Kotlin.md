# Java to Kotlin

Tags: Kotlin

---

<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 flatten:0 bullets:0 updateOnSave:1 -->

[Java to Kotlin](#java-to-kotlin)  
&emsp;[0. 概述](#0-概述)  
&emsp;[1. if null then initialize else return](#1-if-null-then-initialize-else-return)  
&emsp;[2. App.getContext()](#2-appgetcontext)  
&emsp;[3. `it` in lambda](#3-it-in-lambda)  

<!-- /MDTOC -->

---

## 0. 概述

下面总结一些代码段，用于帮助从 Java 迁移到 Kotlin

## 1. if null then initialize else return

```
// Java

private A a = null;

public A getA() {
    if (a == null) {
        a = initA();
    }

    return a;
}

private A initA() {
    // ...
}
```

```
// Kotlin

val a: A by lazy { initA() }

private fun initA(): A {
    // ...
}
```

## 2. App.getContext()

```
// Java

class App extends Application {
    private Context context = null;

    @Override
    public void onCreate() {
        super.onCreate();

        context = getAppContext();
    }

    public Context getContext() {
        retrun context;
    }
}
```

```
// Kotlin

class App : Application() {
    conpanion object {
        lateinit var context: Context
        private set
    }

    override fun onCreate() {
        context = applicationContext
    }
}
```

或者也可以直接扩展 `Context` 类

```
val Context.myApp: MyApp
        get() = applicationContext as MyApp
```

## 3. `it` in lambda

当实现的接口是单方法接口时，Kotlin 会自动使用 lambda 来代替；
这时候很容易出现不知道怎么写的问题。

此时，放心大胆的用 `it` 这个内置的 lambda 表达式参数。

```
// Java

button.setOnClickListener(new OnClickListener() {
    @Override
    public void onClick(View view) {
        // Perform action on click
    }
});
```

```
// Kotlin

button.setOnClickListener { it -> // it is a view
    // Perform action on click
}
```

> 需要注意的是 lambda 是表达式，默认返回值为最后执行函数的返回值或者字面量；
不需要 `return` 关键字。
