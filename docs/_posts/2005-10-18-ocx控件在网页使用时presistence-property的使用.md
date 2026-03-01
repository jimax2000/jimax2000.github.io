---
layout: post
title: "OCX控件在网页使用时Presistence Property的使用"
date: 2005-10-18
tags: [技术]
---

在网页中使用OCX时，可以使用PARAM，这时候在初始化时这些OCX的属性就会被设置, 如

&lt;OBJECT ID=\"abcd\" WIDTH=500 HEIGHT=500CLASSID=\"CLSID:7B222D80-14C1-44CD-ABBB-45CDEE0E5E8E\"CODEBASE=\"http://chenming/jkaraok.cab#Version=1,0,0,001\"&gt;&lt;PARAM NAME=\"LyricFontName\" VALUE=\"隶书\"&gt;&lt;PARAM NAME=\"LyricFontSize\" VALUE=\"18\"&gt;&lt;PARAM NAME=\"LyricTextColor\" VALUE=\"255\"&gt;&lt;PARAM NAME=\"LyricCurTextColor\" VALUE=\"16776960\"&gt;&lt;PARAM NAME=\"WavForeColor\" VALUE=\"65280\"&gt;&lt;/OBJECT&gt;

如果这些属性的使用还要通过别的一些处理才能起到作用，那么就需要在PX_* 函数交换过数据后进行实际的一些处理工作：

void CJKaraOKCtrl::DoPropExchange(CPropExchange* pPX){ExchangeVersion(pPX, MAKELONG(_wVerMinor, _wVerMajor));COleControl::DoPropExchange(pPX);

// TODO: Call PX_ functions for each persistent custom property.PX_Color(pPX, \"LyricBackColor\", m_lyricBackColor, (DWORD)RGB(178, 198, 218));PX_Short(pPX, \"LyricLineHeight\", m_lyricLineHeight, 20);PX_String(pPX, \"LyricFontName\", m_lyricFontName, \"宋体\");......

if (pPX-&gt;IsLoading()){// 具体的一些处理工作......}

}
