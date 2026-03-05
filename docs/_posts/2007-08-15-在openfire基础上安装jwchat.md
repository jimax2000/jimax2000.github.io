---
layout: post
title: "在openfire基础上安装jwchat"
date: 2007-08-15
tags: [技术]
categories: [技术]
---

Openfire 已经直接支持HTTP Binding, 因此jwchat不用再依赖于JHB(JabberHTTPBinding)，但Openfire的Http binding 是以8080端口提供的，因此需要做如下步骤：

1. 在apache的httpd.conf中添加：

```apache
AddDefaultCharset UTF-8
ProxyPass /http-bind/ http://127.0.0.1:8080/http-bind/
```

另外要注意的是，需要把以下两句都打开：

```apache
LoadModule proxy_module modules/mod_proxy.so
LoadModule proxy_http_module modules/mod_proxy_http.so
```

2 更改jwchat/config.js里面的 SITENAME 为你所提供的jabber server的域名。

注释掉其它的，增加一个新的Backend：

```javascript
httpbase: "http-bind/"
type: "binding"
servers_allowed: [SITENAME]
```

3. 在openserver的管理端增加两个服务器属性：

```
xmpp.httpbind.client.requests.polling = 0
xmpp.httpbind.client.requests.wait = 10
```

这就OK了。

参考了[http://chromus.kajigger.com/blog/index.php?p=100](http://chromus.kajigger.com/blog/index.php?p=100)，但实际上没有必要和 `<virtualhost>` 较劲, 开始的失败就是配置 `<virtualhost>` 总不对。

还有一个问题是只打开了proxy_module，没有打开 proxy_http_module，这时候的现象就是总说server disconnected。
