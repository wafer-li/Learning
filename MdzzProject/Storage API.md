# Storage API

Tags： MdzzProject

Database part is base on **Sugar ORM**

----

<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 flatten:0 bullets:0 updateOnSave:1 -->

[Storage API](#storage-api)  
&emsp;[1. 概述](#1-概述)  
&emsp;[2. SharedPreferences 部分](#2-sharedpreferences-部分)  
&emsp;&emsp;[2.1 储存的数据](#21-储存的数据)  
&emsp;[3. 数据库部分](#3-数据库部分)  

<!-- /MDTOC -->

---

## 1. 概述

1. 所有的储存信息和操作均通过**实体**实现。
2. 所有实体均存放在 `models` 包中。
3. SharedPreferences 存放在 `models/shared_preferences` 包中
4. 数据库相关的实体存放在 `models/db` 包中。
5. **取消 Intant Run 再运行，否则程序将会报错！！！**

## 2. SharedPreferences 部分

此部分的数据需要先获取实体 instance 之后再进行操作。

通过实体的 getter 和 setter 对数据进行获取和更改，更改后数据会自动进行持久化保存。

### 2.1 储存的数据

1. 用户的个人信息，包括注册信息和是否单身，**是否第一次登陆**等，实体为 `UserInfo`
2. 系统的信息，目前只包括**是否第一次启动**，实体为 `AppInfo`

## 3. 数据库部分

数据库使用 Sugar ORM，需要注意的是，此库需要取消 Instant Run 才能正常使用。

通过相应的 find 方法来获取相应的实体，对实体进行数据操作之后，使用 save() 方法对其进行更新。

此库已经极其简单，具体的使用说明请参照

https://github.com/satyan/sugar#examples
http://satyan.github.io/sugar/
