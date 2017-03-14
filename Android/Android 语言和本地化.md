# Android 语言和本地化

<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 flatten:0 bullets:0 updateOnSave:1 -->

[Android 语言和本地化](#android-语言和本地化)   
&emsp;[1. 概述](#1-概述)   
&emsp;[2. 默认 `string.xml` 设置为英语](#2-默认-stringxml-设置为英语)   
&emsp;[3. 地区语言-默认覆盖范围最广的语种](#3-地区语言-默认覆盖范围最广的语种)   
&emsp;[4. Android Studio 设置语言地区](#4-android-studio-设置语言地区)   

<!-- /MDTOC -->

## 1. 概述

虽然 Android 已经内置了 `string.xml` 来进行本地化和国际化的功能；

但是，由于在 7.0 以前，`string.xml` 的 fallback 存在较大问题；

所以，即使拥有了一个 i18n 的机制，也还是需要谨慎规划 Locale 的 fallback 问题。

本文就来提出一些最佳实践。

## 2. 默认 `string.xml` 设置为英语

英语作为世界使用范围最广的语言，是名副其实的通用语。

当应用没有为地区提供本地化内容时，系统就会自动 fallback 到默认的 `string.xml`；

只要有些文化的人就能看懂大部分的英语；

所以，`string.xml` 设置为英语是最为妥当的。

## 3. 地区语言-默认覆盖范围最广的语种

对于地区语言，则应该使用覆盖范围最广的语种作为此 Language 的默认本地化内容。

例如，对于中文地区(zh)，香港、澳门、台湾采用繁体中文，中国和新加坡采用简体中文；

那么，就应该采用覆盖范围最广的 **繁体中文** 作为地区默认语言；

而 **单独** 给 中国和新加坡 设置简体中文内容。

整体设置如下：

```bash
res/value-zh: 繁体中文
res/value-zh-rCN: 简体中文
res/value-zh-rSG: 简体中文
```

原因自然是 Android 的 Buggy 语言 fallback 机制；

在 7.0 以前，如果用户语言区域和内置的本地化内容匹配失败；

那么就会直接 fallback 到 **默认配置**(`/res/value/string.xml`)；

如果我们上面只提供 `zh-rCN` 的话，那么港澳台地区的同胞就只能看英语界面了。

> 7.0 以后，Android 修复了这一问题；
> API 24 之后可以匹配到和语言最为接近的本地化内容；
> 例如上面的例子，在没有繁体的应用，在 7.0 上，港澳台地区就可以看到简体中文。
>
> 但是由于 7.0 目前使用人数过于低下，还是得进行上面所讲的 workaround

## 4. Android Studio 设置语言地区

虽然目前 Android Studio 中内置了 Translation Editor；

但是，目前这个好用的工具还不能实现对语言地区(region) 的设定。

例如，对于中文，有简体中文(zh-CN) 和 繁体中文(zh-{HK, TW})；

但是， Translation Editor 目前并不能指定语言的 Region；

只能选择默认的 `value-zh`。

对于这种情况，我们不得不暂时抛弃这个好用的工具；

自行在 Project Window (就是最左边的窗口):

New -> Value Resource -> Choose Locale -> Select Region；

例如选择 `zh`，然后地区选择 `CN`，创建 `strings.xml`；

此时，Android Studio 就创建了 `value-zh-rCN/strings.xml`；

然后，我们把默认的 `string.xml` 复制到 `string.xml(zh-rCN)`  中；

这样，我们就能够在 Translation Editor 中编辑简体中文了。
