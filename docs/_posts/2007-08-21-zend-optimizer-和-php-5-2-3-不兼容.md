---
layout: post
title: "Zend Optimizer 和 PHP 5.2.3 不兼容？"
date: 2007-08-21
tags: [技术]
categories: [技术]
---

客户的机器是台FreeBSD，装了PHP 5.2.3 和 Zend Optimizer 3.2.8。想给用户先是加密的代码，等客户付钱后再改成不加密的，但是Zend Guard 4 加密过的代码执行起来IE说找不到网页，Firefox提示下载这个网页。于是换了Zend Guard 5, 因为Guard 5需要Zend Optimizer 3.3.0以上，于是升级了Zend Optimizer，但是仍然不行，加密过的代码显示一片空白。试了几个简单的加密倒是没问题，但一到比较复杂的程序就不行了。在网上也查不到相关的问题和说明。

最后实在没辙了，把PHP5.2.3换成5.2.1，问题解决了。看样子是5.2.3和Optimizer的兼容性问题，感觉这是个挺大的 BUG，PHP的这次升级太不负责任了，折腾了起码三四天 :(
