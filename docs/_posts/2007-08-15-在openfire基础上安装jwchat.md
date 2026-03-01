---
layout: post
title: "在openfire基础上安装jwchat"
date: 2007-08-15
tags: [技术]
---

Openfire 已经直接支持HTTP Binding, 因此jwchat不用再依赖于JHB(JabberHTTPBinding)，但Openfire的Http binding 是以8080端口提供的，因此需要做如下步骤：

1. 在apache的httpd.conf<coolcode linenum=\"off\">AddDefaultCharset UTF-8ProxyPass /http-bind/ http://127.0.0.1:8080/http-bind/</coolcode>

另外要注意的是，需要把<coolcode linenum=\"off\">LoadModule proxy_module modules/mod_proxy.soLoadModule proxy_http_module modules/mod_proxy_http.so</coolcode>这两句都打开。

2 更改jwchat/config.js里面的 SITENAME 为你所提供的jabber server的域名。

注释掉其它的增加一个新的Backend<coolcode linenum=\"off\">httpbase:\"http-bind/\"type:\"binding\"servers_allowed:[SITENAME]</coolcode>

3. 在openserver的管理端增加两个服务器属性：<coolcode linenum=\"off\">xmpp.httpbind.client.requests.polling = 0xmpp.httpbind.client.requests.wait = 10</coolcode>

这就OK了。

参考了[http://chromus.kajigger.com/blog/index.php?p=100](http://chromus.kajigger.com/blog/index.php?p=100)，但实际上没有必要和&lt;virtualhost&gt;较劲, 开始的失败就是配置&lt;virtualhost&gt;总不对。

还有一个问题是只打开了proxy_module，没有打开 proxy_http_module，这时候的现象就是总说server disconnected。
