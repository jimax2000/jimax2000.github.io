---
layout: post
title: "pyMSNt 和 MSNShell不兼容的问题"
date: 2007-12-25
tags: [技术]
categories: [技术]
---

最早用国外的一些Jabber的MSN Gateway(比如jaim.net 和anywise.com上的)，从MSN发送消息发现消息总会丢失，或者提示"无法将以下消息发送给所有接收者:"但发送消息给MSN客户端却总是能成功。但jabbernet.dk上MSN Gateway的就一直都没问题。后来自己安装了pyMSNt，发现也出现挂不上去的问题，开始总以为是pyMSNt的安装或者配置哪里不对。一个朋友又说总是在家里能挂上，在单位就总是出问题。总结了各种现象，才发现，是MSNShell和pyMSNt不兼容的问题。卸载了MSNShell，不管连哪个都很正常了。而msn.jabbernet.dk不是pyMSNt的，（它有个msnnew.jabbernet.dk好象是pyMSNt的）所以一直没有问题。

问题是这样发生的：在一般情况下协议里都是一个空行来隔开消息头和消息体的。而对于没有消息体的消息来说，消息头结束后要跟两个回车换行，也即下面必须要有个空行的。根据[http://msnpiki.msnfanatic.com/index.php/MSNP8:Payload_Commands](http://msnpiki.msnfanatic.com/index.php/MSNP8:Payload_Commands)：

<blockquote>"It\'s possible for messages to have no body. If you just end a message with the two newlines at the end of the header, it will have an empty body. "</blockquote>

但是如果你安装了MSNShell, 并且开启了\"加密聊天\"模式后，MSNShell会在发送正常的消息前，进行握手(看看对方是不是也支持加密)，发送如下的信息MSG test@msn.com ming 165MIME-Version: 1.0Content-Type: text/x-bobosv: 4.2.28.32mv: 8.1.178.0state: ssShellHandShake1bobo1: 1658134426017880279626016817.6426387281559877623017753问题就在于，MSNShell的这条信息也是没有消息体的，但是在消息头后面只有一个回车换行。虽然前面的MSG后面跟的playload size是正确的。但pyMSNt的做法是在读完一行，发现是消息头之后，并不立刻判断其长度是否已经满足，而总是去读下一行，直到读到一个空行后再判断，如果size还不够再转到读消息体的函数里判断长度。这就造成了pyMSNt把下一条正式消息MSG test@msn.com ming 130MIME-Version: 1.0Content-Type: text/plain; charset=UTF-8X-MMS-IM-Format: FN=%E5%AE%8B%E4%BD%93; EF=; CO=0; CS=86; PF=2的第一行也当成是本消息的内容了，然后丢弃，然后造成把MIME-Version一行当作下一条命令的开始，然后造成Invalid Command 异常。

弄清楚原因，简单改造一下pyMSNt，问题就解决了。圣诞之夜，孩子睡了，独自在屏幕前。不过解决了这个问题，感觉还挺爽....
