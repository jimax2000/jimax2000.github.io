---
layout: post
title: "R6025 - pure virtual function call"
date: 2007-06-04
tags: [技术]
---

今天的一个程序出了 R6025 - pure virtual function call 错误，主要原因是在基类的构造函数中调用了纯虚函数。1. 如果不是纯虚函数，没问题。2. 如果构造函数直接调用纯虚函数，链接时会出错。只有通过一个其它成员函数转调一下。

下面是一个简化的例子：<coolcode  lang=\"cpp\" linenum=\"off\"> class CBase{public:CBase() { func2(); }virtual void func() = 0;void func2(){    func();}};

class CDrived : public CBase{public:CDrived() { }virtual void func() { printf(\"hello\"); }};

int _tmain(int argc, _TCHAR* argv[]){CDrived * d = new CDrived();

return 0;}</coolcode>
