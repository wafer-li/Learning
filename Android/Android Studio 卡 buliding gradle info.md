# Android Studio 卡 buliding gradle info

Tags: Android

---
<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 flatten:0 bullets:0 updateOnSave:1 -->

[Android Studio 卡 buliding gradle info](#android-studio-卡-buliding-gradle-info)  
&emsp;[1. 问题](#1-问题)  
&emsp;[2. 解决办法](#2-解决办法)  

<!-- /MDTOC -->
---

## 1. 问题

有时候第一次使用 Android Studio 打开某个项目时，会出现项目一直卡在 `buliding gradle info` 的问题，如图所示：

<center>![Building project  info](http://i4.buimg.com/563021/c4ee7577d3d0bcde.jpg)</center>

此问题的原因在于：**用于下载 gradle 本体的网站被墙了，导致下载速度缓慢。**

## 2. 解决办法

打开 gradle 的 `gradle.properties`，然后直接从里面的链接下载 gradle，放入 gradle 的文件夹中即可。

当然，最靠谱的方法还是去翻墙啦。
