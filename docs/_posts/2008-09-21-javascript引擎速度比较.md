---
layout: post
title: "JavaScript引擎速度比较"
date: 2008-09-21
tags: [技术]
---

自从Google的Chrom浏览器推出以来，Javascript的速度就成为大家追的焦点。一个比一个宣称快。

- Mozilla的TraceMonkey: (现在Firefox3.0里面的还是SpiderMonkey)
  - [Mozilla：下一版Firefox速度会赢过Chrome](http://news.csdn.net/n/20080909/118849.html)

- Webkit的SquirrelFish & SquirrelFish  Extreme：
  - [Webkit 最新 Javascript 引擎领先 Chrome](http://www.cnbeta.com/articles/65143.htm)
  - [金鳞鱼越游越快，极限版横空出世](http://www.yeeyan.com/articles/view/july/14400)

于是测试了玩玩。SquirrelFish Extreme用的是Webkit r36712 [nightly build版本](http://nightly.webkit.org/)。有空再补TraceMonkey的。

<table>
  <tr><td width=\"150\">测试集</td><td width=\"150\">V8</td><td width=\"150\">IE8</td><td width=\"200\">SpiderMonkey</td><td width=\"200\">SquaireFish Extreme</td></tr>
  <tr><td>[SunSpider](http://www2.webkit.org/perf/sunspider-0.9/sunspider.html)</td><td>3080.8ms</td><td>12977.8ms</td><td>5744.0ms</td><td>2704.2ms</td></tr><td>[jsTimeTest](http://wd-testnet.world-direct.at/mozilla/dhtml/funo/jsTimeTest.htm)</td><td>74ms</td><td>785ms(*)</td><td>329ms</td><td>107ms</td></table>

(*): 这个数据可能偏大，因为中间弹出了对话框：”脚本执行时间太长，是否继续”之类的，但不比不知道，IE8还是慢得太多了。
