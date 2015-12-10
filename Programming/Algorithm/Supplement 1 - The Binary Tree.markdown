# Supplement 1: The Binary Tree

Tags: Algorithm

---



## 1. The definition of Binary Tree

> Binary Tree is a tree which only has **two child nodes at most**.
Tree is an connected graph which has **no loop**

> The node which is at the top layer is called the **root node**
The node which contains no child node is called **leaf node**, which contains child node is called **internal node**

## 2. Types of Binary Tree

1. Full Binary Tree
> The full binary is that the node is **either leaf node** or **has two chrildren exactly**.

2. The Complete Binary Tree
> The Complete Binary Tree is 
if all levels except possibly the last are completely full, 
and the last level has all its nodes to the left side.

![Full Binary Tree](http://web.cecs.pdx.edu/~sheard/course/Cs163/Graphics/FullBinary.jpg)       ![Complete Binary Tree](http://web.cecs.pdx.edu/~sheard/course/Cs163/Graphics/CompleteBinary.jpg)

> **A Full Binary Tree is not always a Complete Binary Tree.**
**On the contrary, it' s also true**.

## 3. The implementation {#CompleteBinaryTree}

### 1. Array

> This method is just place the element as the order of the corresponding complete binary tree,
so, if a node is at position $k$, then,
its **parent** is at position $\lfloor k \rfloor$,
its **leftChild** is at position $2k$, the **right** is at $2k + 1$

> As you see, the array implementation is only **suitable** for the **complete binary tree** 
With the incomplete one, it will waste lots of space.

### 2. Linked List

> The Linked List way is much more space-saving. It has 3 parts of the node.
The `data field`, the `leftChild pointer`, the `rightChild pointer`

Node:
<table style="width:20em;">
<tr>
<td style="text-align:center;vertical-align:middle;">leftChild</td> <td style="text-align:center;vertical-align:middle;">data</td> <td style="text-align:center;vertical-align:middle;">rightChild</td>
</tr>
</table>


## 4. The Traversal Algorithm

> Normally, There are 3 different ways to traversal a binary tree. They are:

> 1. PreOrder Traversal ($DLR$)
2. InOrder Traversal ($LDR$)
3. PostOrder Traversal ($LRD$)

> Actually, there are 3 more ways, but we assume the left child is alway **the elder brother** of the right child. So we reduce to 3 ways.

> The traversal Algorithm all use the **recursive way** to implement.

### 1) Depth-first

> The first child, then **the grand child** before the second child

#### 1. PreOrder Traversal

1. Display the data part of root element (or current element)
2. Traverse the left subtree by recursively calling the pre-order function.
3. Traverse the right subtree by recursively calling the pre-order function.

#### 2. InOreder Traversal 

1. Traverse the left subtree by recursively calling the in-order function
2. Display the data part of current element.
3. Traverse the right subtree by recursively calling the in-order function

#### 3. PostOrder Traversal

1. Traverse the left subtree by recursively calling the post-order function.
2. Traverse the right subtree by recursively calling the post-order function.
3. Display the data part of root element (or current element).

### 2) Breadth-first

> The first child, then the second child, and then the first grand child, the second grand child, and so on.
We do not go to the next level until the current level is done.

```java

interface Visitable<Item> {
    void onVisit(Item item);
}

class BreadthFirst {
    Visitable<Node> visiter;
    ....
    void breadFirstTraversal(Node root) {
        Queue q = new Queue();
        q.enQueue(root);
        while (!q.isEmpty()) {
            Node node = q.deQueue();
            visiter.onVisit(node);
            if(node.lChild != null) {
                q.enQueue(node.lChild);
            }
            if(node.rChild != null) {
                q.enQueue(node.rChild);
            }
        }
    }
}
```
## 5. Threaded Binary Tree

> A Threaded Binary Tree is that, when using the linked list to implemente the Binary Tree, using the empty node field to store the **traversal thread** to increase the traversal efficiency.
The thread depens on the traversal method you selected.

> Addition: Only according to the **depth-first** traversal.

### 0) Adjust the data struct

> To bulid an thread binary tree, we need to adjust the node's data structure.

The Threaded Binary Tree Node:
<table style="width:20em;">
<tr>
<td style="text-align:center;">leftFlag</td>
<td style="text-align:center;">leftChild</td>
<td style="text-align:center;">data</td>
<td style="text-align:center;">rightChild</td>
<td style="text-align:center;">rightFlag</td>
</tr>
</table>

## 6. Binary Tree & Forest

### 1) The definition of Forest

> Forest is consist of a lot of individual trees, when they come together, we call them **Forest**

![Forest](https://helloacm.com/wp-images/acm/2012/data-structure/disjoint1.jpg)

> We could link its root nodes of each tree to bulid a big tree.

### 1) The Representation of Forest

> Firstly, we tranfer it to the bing tree, just link its root node of each tree together.

#### 1. The Child and Brother Representation

> It's a linked list implementation, The node contains 3 parts, 
the `Data Field`, 
the `leftChild pointer` (or reference), which point to its **left most child**
and the `brother pointer` (or reference), which point to its **right brother**.

Node:
<table style="width:20em;">
<tr>
<td style="text-align:center;vertical-align:middle;">leftChild</td> <td style="text-align:center;vertical-align:middle;">Data</td> <td style="text-align:center;vertical-align:middle;">brother</td>
</tr>
</table>

> Since the Node has **the same number** of parts compare with the **binary tree's node**,
We could transfer **the big tree** to the specific **binary tree**, 
as the big tree is transfered from the **forest**,
so that, we could transfer **the forest** to **the binary tree** easily.

## 7. Huffman Tree

> Huffman Tree, is also called **the most Optimal Binary Tree**, is an weighted binary tree which has the minmum weighted an the shortest tree.

## 1) Feature

1. As the same weight, the Huffman Tree is not unique
2. Children of the Huffman Tree can be reversed, because it doesn't affect the lenth.
3. The weighted node is all the leaf node, the nodes not weighted is the root of the tree of subtree.
4. The bigger weight, the closer to the root node.
5. Huffman Tree do not have the 1-degree node.
6. A Huffman Tree which has $N$ leaf nodes, has $2N - 1$ nodes.

## 2) Create Steps

1. Unify the given weighted node into a Set
2. Pick up the 2 least weighed node, unify them and **remove them from the Set**, and **generate a node as they parent**, and **add the parent into the Set**
    > The 2 node was unified, and the parent's weight is the **sum** of the two nodes.

3. Repeat the step 2, until the Set is empty.

Example: Suppose we have the 5 nodes
![Huffman Nodes](http://img.blog.csdn.net/20140213234608531)
and then, follow the steps above, we can create an Huffman Tree such as below:
![Huffman Tree](http://img.blog.csdn.net/20140213234743687) ![Huffman Tree](http://img.blog.csdn.net/20140213234754390)

$\Delta$  Notice that: the Huffman Tree is **NOT unique**

## 3) Application: Huffman Code

> The Huffman Code is that, accoring to the frequncy of the words, which is needs be encrypted, to generate the Huffman Tree to decrease the size of the code.

> Because the Huffman Tree has its **most weighted node closest to its root**, using the Huffman Code, it will much more narrow down the size of code.

As above(left side), if we define the left edge is $0$, the right edge is $1$, and then, the code is:

- 5 = '11'
- 4 = '10'
- 3 = '00'
- 2 = '011'
- 1 = '010'
