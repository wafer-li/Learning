# Material Design 实体属性

Tags: MaterialDesign

---

<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 flatten:0 bullets:0 updateOnSave:1 -->

[Material Design 实体属性](#material-design-实体属性)  
&emsp;[1. 概述](#1-概述)  
&emsp;[2. Material 的特点](#2-material-的特点)  
&emsp;[3. 物理特性](#3-物理特性)  
&emsp;&emsp;[3.1 厚度](#31-厚度)  
&emsp;&emsp;[3.2 投射阴影](#32-投射阴影)  
&emsp;&emsp;[3.3 内容](#33-内容)  

<!-- /MDTOC -->

---

## 1. 概述

**Material 具有某些不可变的特点和固有的行为模式**

<center><img src="https://material-design.storage.googleapis.com/publish/material_v_9/0B7WCemMG6e0VU1RSV0tORnl5a2M/what_is_material_material_properties.png" width="300"></center>

了解关于 Material 的特点能有助于你更好的利用 Material，以期与 Material Design 具有一致性。

## 2. Material 的特点

1. 固体
2. 占用空间中唯一的位置
3. 不可穿透的
4. 形状可改变
5. 只在平面方向上改变大小
6. 不可弯折
7. 可以融入其他 Material
8. 可以分割，分裂，和恢复
9. 可以被创建和摧毁
10. 可以在任何轴进行移动

## 3. 物理特性

### 3.1 厚度

实体具有可变化的长宽尺寸，和 1 dp 的厚度。

<center><img src="https://material-design.storage.googleapis.com/publish/material_v_9/0B8v7jImPsDi-aTBFT1FDVEstenM/whatismaterial_materialproperties_physicalproperties_thickness_01_yes.png" width="300"/></center>
<center><div style="color:#4CAF50;">Do，材料的长和宽可以变化</div></center>

<center><img src="https://material-design.storage.googleapis.com/publish/material_v_9/0B8v7jImPsDi-Sno0Qy1FY3UtaFk/whatismaterial_materialproperties_physicalproperties_thickness_02_no.png" width="300"/></center>
<center><div style="color:#D32F2F;">Don't，材料的厚度为 1 dp</div></center>

### 3.2 投射阴影

投射阴影是用来表示两个实体之间的相对距离。

<center><img src="http://im2.ezgif.com/tmp/ezgif-1731017759.gif" width="500" /></center>
<center><div style="color:#4CAF50;">Do，材料的阴影是实体间距离的体现</div></center>

<center><img src="http://im2.ezgif.com/tmp/ezgif-1896488788.gif" width="500"/></center>
<center><div style="color:#D32F2F;">Don't，阴影不能用来描边</div></center>

### 3.3 内容

内容能以任意的形状和颜色在实体上显示，内容不给实体增加厚度。

<center><img src="http://im2.ezgif.com/tmp/ezgif-1807962366.gif" width="500"/></center>
<center><div style="color:#4CAF50;"> Do，内容能以任意的形状和颜色来展示</div></center>

内容的行为可以独立于实体，但是被实体的大小所限制。

<center><img src="http://im2.ezgif.com/tmp/ezgif-3203165216.gif" width="500"/></center>
<center><div style="color:#4CAF50;"> Do，内容被实体大小所限制</div></center>
