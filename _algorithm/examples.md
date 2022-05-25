---
layout: default
title: TODO
---

### Counting inversions problem

Question: 给定 [1, n] 数字的一个permutation，求inversion pair的个数。
Attack:
* 把元素本身作为数组下标使用；数组的值为0或1；
* 按照先后出现的顺序处理数字，对每一个查询在它之前的比它大的数字有多少个；
* 使用Fenwick Tree，可以快速区域求和。

### Kth largest element problem

Question: 给定值小于10^6的一些整数，求第K大的数。
Attack:
* 把元素本身作为数组下标使用；数组的值为大小等于此数的元素个数；
* 使用Binary Search的思想进行查找；通过区域求和查询当前排序的序号；
* Fenwick Tree本身就是按照Binary Tree的思想来组织的；Fenwick Tree可以快速区域求和。

### Range updates and point queries

Question：区域内元素都同时加一个delta；查询某一个元素。
Attack：
* 和Fenwick Tree有类同的地方。Fenwick可以快速更新一个元素，查询区域。
* 利用求和和差分（积分和求导）的对应关系。每个slot保存的是和差分值（导数）：
    * 给一个区域的整体加一个delta，对应到差分（导数）只是边缘两个元素的改变。
    * 查询一个元素，需要做求和（积分），也就是Fenwick的区域查询。


