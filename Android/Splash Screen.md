# Splash Screen

Tags: Android

就是一个一闪而过的画面，展示一个用户友好的界面同时进行一些后台操作

---

<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 flatten:0 bullets:0 updateOnSave:1 -->

[Splash Screen](#splash-screen)  
&emsp;[1. 在 Activity 中实现](#1-在-activity-中实现)  
&emsp;[2. 在 Fragment 中使用](#2-在-fragment-中使用)  

<!-- /MDTOC -->

---

## 1. 在 Activity 中实现

- 将此 `Activity` 设置为 **LANCHER** `Activity`
- 记得加载完之后要跳转到其他 `Activity` 同时 `finish()` 这个 Activity
- 使用 `Handler.postDelayed()` 方法去增强延迟，以免加载过快引起用户体验下降

    > 记得要在**视图被加载之后**使用

``` java
/**
* Use it after
* setContentView() in onCreate() in Activity
*/
new Handler().postDelayed(new Runnable() {
            public void run() {
            goHome();
            }
            }, SPLASH_DELAY_MILLIS);
}
```

## 2. 在 Fragment 中使用

当在 Fragment 中时，与 Activity 并无显著区别，**记住要在视图被加载之后使用**
所以一般在 `onCreateView()` 之后调用 delay。

根据 `Fragment` 生命周期来看，应该在 `onStart()` 方法中使用这个比较合适
