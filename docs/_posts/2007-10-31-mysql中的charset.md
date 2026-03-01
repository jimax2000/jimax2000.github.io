---
layout: post
title: "mysql中的charset"
date: 2007-10-31
tags: [技术]
---

今天碰到一个问题，用C++写了一个访问mysql的程序，在我自己机器上好好的，到别人的机器上就不对了，汉字都显示成？？。底层使用了mysql++，它再用了mysql的C API接口。

开始查询资料：

1. 首先是mysql++里面关于字符集的说明，里面提到了关于Unicode不直接支持，是通过UTF8来支持的。但我的程序是MBCS的，没有用Unicode。没啥关系。

2. 网上查询mysql的字符集的资料，提到了一些关于SET NAMES的描述. 按照里面的说法，进mysql命令行的客户端，show variables like \'character_set_%\', 两台机器上都是 character_set_client, character_set_connection,character_set_results几项都是UTF8. 但这就不对了，我程序用的是MBCS(GBK), 并不是UTF8，为啥在我的机器上还能显示对呢？另外，即便是UTF8，显示的也不应该是'？'啊。

3. 比了比两台机器MySQL Server目录下的my.ini文件, [mysql]下写的都是default-character-set=utf8, 这倒是和mysql命令行客户端的表现是一致的。

4. 我试着在我的程序里加上了SET NAMES \'gbk\'的调用，居然两台机器上都对了。

5. 可是还是不清楚为什么会两台机器不一样。于是在我的程序里SET NAMES \'gbk\'的前后都加上show variables show variables like \'character_set_%\', 发现不一样的地方了。在我的机器上，一开始character_set_client, character_set_connection,character_set_results就都是GBK，所以SET NAMES \'gbk\'实际上也不起作用。而别的机器上，一开始这几项都是\'utf8\'，设完后变成了\'gbk\'，这下说得过去了。如果这几项是gbk的话，我读出来的直接都是gbk字符，显示也正确了。而如果没有SET NAMES,别的机器上开始是\'utf8\'，这下汉字都转成\'?\'，这是有道理的。

6. 虽然现在问题解决了，但还需要追下去。现在的问题就变成了为啥我的机器开始的时候是GBK，而别人的机器开始是utf8? 而mysql客户端进去可能是因为读了my.ini后主动设置成utf8的，这是正常的。

7. 没辙，跟踪进mysql++，发现在调用mysqlpp::Connection::connect() 里面，调用C API的mysql_real_connect之后，mysql句柄的codeset项就被改变了。

8. 还是没辙，试试在connect之前用mysqlpp::Connection::set_option() 把opt_set_charset_name 设成latin2，发现别人的机器设完那几个\'character_set-%\'变成latin2了，但我的机器上仍然始终是gbk.

9. 以前下载过mysql的源代码，找到mysql_real_connect, 发现一开始就用到了mysql->options.my_cnf_file，如果设置了，会用它重新读取options，觉得看到解决的曙光了。试试在connect之前用mysqlpp::Connection::set_option() 把opt_read_default_file设成一个不存在的\"haha\"，这下我的机器也是utf8了。

10. 再看mysqlpp::Connection里面，有一句set_option_default(opt_read_default_file, \"my\"); 因此，缺省情况下（不设置opt_read_default_file的时候）两台机器上实际上都会去用my.ini初始化。可是我比较的my.ini一样啊。

11. 简单浏览mysql源代码，找到init_default_directories，前面的注释说On Microsoft Windows, this is:1. C:/2. GetWindowsDirectory()3. GetSystemWindowsDirectory()4. getenv(DEFAULT_HOME_ENV)5. Directory above where the executable is located6. \"\"7. --sysconfdir=<path>

于是查找这些目录下，有没有my.ini，发现我的windows目录下有一个my.ini, 打开一看，哈哈，[client]里面有 default_character_set = gbk. 把这个文件删掉，ok了，我的机器上也是utf8了。

12. 进一步试验，发现MySQL Server目录下的my.ini对于mysql++或mysql C API没有任何用处，也是，这个目录不在上面列出来的7项之内。

13. 这下明白了，实际上在我的机器上，这里找到的是windows目录下的my.ini，因此设置了client_character_%为gbk,误打误撞我的机器上显示就对了。而对于别人的机器，没有合适的my.ini, 因此缺省为utf8. 而mysql总是找MySQL Server目录下面的my.ini里面的[mysql]下面的。

14. windows目录下的my.ini可能是原来装过4.x版本的mysql留下来的。
