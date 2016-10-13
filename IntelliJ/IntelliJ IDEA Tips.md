# IntelliJ IDEA Tips

Tags: IntelliJ

[TOC]

---

## 0. Introduction

This is the tips of using the **IntelliJ IDEA**

Although IntelliJ is the best and the most intelligent Java IDE ever.
But it still exsit quite a few bugs and problems.

This article is to tell you some tips how to fix it.

## 1. Project Template

The project template is really convient, you can use this to establish your own project template which will appeear in the wizard.

But there is a bug that: **If you create a project template, it's hard to remove it from the original manager dialog inside the IntelliJ**. It make the dialog useless.

So, how to delete it? By now, you **could remove it from you **IntelliJ config folder**, it will start at a **point**(`.`), and it usually locate at the **user's home dir**, which Windows is the `C:\\Users\\username`, and the Linux is `/usr/home`

This config folder's dir can be change at the `idea.properties` file

Once got into the folder, you could search the floder named **projectTemplate**, and you will find all of the project templates you created. Just remove it. 

It's done.



