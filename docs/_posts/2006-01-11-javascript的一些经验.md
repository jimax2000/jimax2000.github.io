---
layout: post
title: "JavaScript的一些经验"
date: 2006-01-11
tags: [技术]
categories: [技术]
---

firefox下 没有obj.innerText，只能用innerHTML

firefox下 没有currentStyle, 可以用document.defaultView.getComputedStyle(aaa,null) 得到类似的

currentStyleprototype.js 中提供的class挺好的，能把代码组织得比较清晰，但什么原理还没搞得太清楚
