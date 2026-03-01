---
layout: post
title: "Powershell创建目录+更改文件名"
date: 2010-10-13
tags: [青春涂鸦]
---

<p>要将一堆1001.png, 1002.png变成1001目录下的icon.png, 1002目录下的icon.png，写了个Powershell脚本，先创建子目录，再将文件移动过去</p><coolcode>ls *.png |% {if($_.fullname -match \"([\\d]+)\\.png\") {  echo $($($matches[1]))  New-Item -Path $($($matches[1])) -ItemType Directory -Force  Move-Item -Path $_.fullname -Destination \"$($($matches[1]))\\icon.png\" -PassThru -Force}  }</coolcode>
