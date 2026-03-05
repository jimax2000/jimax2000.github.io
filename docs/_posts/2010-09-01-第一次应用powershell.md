---
layout: post
title: "第一次应用Powershell"
date: 2010-09-01
tags: [技术]
categories: [技术]
---


在日志中要统计一下收到多少次短信，试了试PowshellShell, 确实比较方便
 ```
Select-String e:\\temp\\logger\\*.log -pattern \"收到的短信\" -Encoding \"Default\" | Measure-Object
```
日志是用GB码的，所以要带上 -Encoding \"Default\"

结果是：

```
Count    : 2947
Average  :
Sum      :
Maximum  :
Minimum  :
Property :
```
