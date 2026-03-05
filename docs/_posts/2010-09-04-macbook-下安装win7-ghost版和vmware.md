---
layout: post
title: "MacBook  下安装Win7 ghost版和VMware"
date: 2010-09-04
tags: [技术]
categories: [技术]
---


买了一台MacBook Pro 372，作为给自己的生日礼物吧。

买的时候让店里的人给装了个BootCamp的XP，回来还是想试试装Win7，但我的Win7是个ghost版的，于是试啊试的，终于被安装上了。

1. 在Mac里面启动BootCamp助理，开始安装。
2. 用光盘启动后，执行里面的ghost，复制分区到Windows分区。
3. 复制完成后，直接想启动Windows分区，是无法启动的。原因应该是启动缺省用的是分区1，但在BootCamp里面，Windows分区是分区3。
4. 仍然用光盘启动，进入WinPE，进行分区表修复
5. 这时候再启动Windows分区就能启动了
6. 插入MacOS的光盘，安装驱动程序。

这时候，盗版Win7里面自带的一个激活工具也无法使用了，它好象也是要修改grldr, 又会把分区改掉。找了半天，找到一个OEM激活的，发现能用。

然后回到MacOS里面，安装VMware Fusion, 选择建立BootCamp的虚拟机。再用Spaces把启动的Windows虚拟机搞到新的桌面上，很爽～～
