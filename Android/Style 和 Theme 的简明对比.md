# Style 和 Theme 的简明对比

Tags: Android

---

<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 flatten:0 bullets:0 updateOnSave:1 -->

[Style 和 Theme 的简明对比](#style-和-theme-的简明对比)  
&emsp;[1. Style 应用于局部，而 Theme 应用于整体](#1-style-应用于局部，而-theme-应用于整体)  
&emsp;[2. Style 是组件多种属性的集合](#2-style-是组件多种属性的集合)  

<!-- /MDTOC -->

---

## 1. Style 应用于局部，而 Theme 应用于整体

一个 `Style` 只对一个 `View` 组件有效；

而一个 `Theme` 对整个 `application` 或 `activity` 或者一个 `ViewGroup`(`View` 组件和它的子项) 有效。

## 2. Style 是组件多种属性的集合

实际上，一个组件的 style 就是其多种属性的集合。

也就是说，可以直接在 style 中设置 theme。
