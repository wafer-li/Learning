# 8 Puzzle

Tags: Algorithm

---

<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 flatten:0 bullets:0 updateOnSave:1 -->

[8 Puzzle](#8-puzzle)  
&emsp;[1. Intro](#1-intro)  
&emsp;[2. Best-first search](#2-best-first-search)  
&emsp;&emsp;[2.1 Search node](#21-search-node)  

<!-- /MDTOC -->

---

## 1. Intro

Give a 3-by-3 grid with 8 square blocks and 1 blank.
Rearrange the block to make it in order, using as **few moves** as possible.

Return the result of sequence. Like this below:

```
    1  3        1     3        1  2  3        1  2  3        1  2  3
 4  2  5   =>   4  2  5   =>   4     5   =>   4  5      =>   4  5  6
 7  8  6        7  8  6        7  8  6        7  8  6        7  8

 initial        1 left          2 up          5 left          goal
```

## 2. Best-first search

The best-first search is that from initial broad to the goal, we do our each step at the best, or small cost move.

### 2.1 Search node

First, we need to define our start and goal. We use a terminology called
