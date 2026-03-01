---
layout: post
title: "在人员离职时如何检查SourceSafe中是否还有CheckOut的项目"
date: 2005-10-18
tags: [技术]
---

虽然平时一直要求在工作时不要把文件都CheckOut出来，而是只CheckOut所需要修改的文件，并且要在修改后及时CheckIn。但有些开发人员仍不能很好执行。因此在人员离职时常常在SourceSafe下留下很多仍然CheckOut的文件，同时也不知道本地是否有已经修改的新版本。

因此，在离职时需要检查一下是否有其仍然CHECKOUT的内容。先使用SOURCESAFE Administrator来检查一下此用户在SourceSafe 中有CheckOut权限的目录,然后对每个目录分别使用：

```
<server>\vss\win32\ss status $/proj -R -U -yuser,password
```

此命令会记录所有被CheckOut的文件，`$/proj`表示从具体的某个proj目录开始， `-R` 表示递归检查子目录。`-U` 表示只显示指定用户CheckOut的文件，user和password需要替换成离职人员的信息。当然你也可以从`$/`开始检查所有的目录，但对于没有权限的目录会提示"You do not have access rights to $/xxxx".

如果有显示信息，则必须要求其将所有文件都CheckIn或者Undo CheckOut，最好先比较所有文件的差异，确认后再操作。
