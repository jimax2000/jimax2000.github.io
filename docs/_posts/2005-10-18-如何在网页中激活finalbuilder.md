---
layout: post
title: "如何在网页中激活FinalBuilder?"
date: 2005-10-18
tags: [技术]
---

现在在我们公司rdserver的“每日构建”页面下增加了一个“立即构建”的按钮，按此按钮可以直接激活在rdserver上的FinalBuilder，自动对工程项目进行构建，而不需要等到半夜的重编，适应一些需要立即出结果的情况。由于重编需要比较长时间，因此在激活后就可以不管它，过一阵子（现在大概10分钟左右）再重新刷新。部分人员也可以通过Email得到构建完成的通知。

这里解释后台的一些情况。关于在ASP中如何在后台调用一个应用程序，高占勇提供了一个方法 `WScript.Shell`对象， 以及相应的 `Run(strCommand, [intWindowStyle], [bWaitOnReturn])` 方法：

```vbscript
Dim oShell
Set oShell = WScript.CreateObject("WSCript.shell")
oShell.run "cmd /K CD C:\ & Dir"
Set oShell = Nothing
```

我现在用的是ASP .NET with C#, 因此直接使用了Process组件：

```csharp
private void Button1_Click(object sender, System.EventArgs e)
{
    string exe = @"""C:\Program Files\FinalBuilder2\finalbuilder2.exe""";
    string param= @"/n /r /e /f ""D:\jtts-builder\jtts.fbz2""";
    Process.Start(exe, param);

    Label2.Text = "每日构建已激活！请等待邮件通知或10分钟后重新刷新此页面！";
}
```

exe为执行程序名，param为参数。Start是一个静态方法，因此不需要实例化一个Process组件。

FinalBuilder2的命令行参数： /n 不显示初始窗口， /r 自动执行后面所跟脚本， /e 执行完毕自动退出， /f 忽略错误。

到这一步都很简单，但是实际在运行时FinalBuilder并不能运行下去。主要原因在于jTTS4 Daily Builder的FinalBuilder脚本中使用了SourceSafe来访问我们的代码库，而VSS Server(`\\myserver`)上的vss共享目录是有用户访问权限限制的。而在Windows Server 2003, IIS6中，缺省时FinalBuilder是用NETWORK_SERVICE用户执行的，因而造成错误。

解决方法是让FinalBuilder以其它具有vss目录访问权限的用户执行，具体是通过修改IIS中DailyBuilder虚拟目录的"应用程序池"(Application Pool)来实现的。

下面的内容摘自：http://doc.4kiki.net/content/1/23/200505/01/d271a7fc84170273.html

**Enabling ASP.NET to run as another user on Windows XP Professional**

As an Administrator, edit the attributes of the file `"%INSTALLROOT%\Config\machine.config"` on the processModel tag, as shown:

```xml
<processModel
  enable="true"
  userName="DOMAIN\username"
  password="MyPswd2"
  ... />
```

**Note**: %INSTALLROOT% is of the form `D:\WINDOWS\Microsoft.NET\Framework\v1.0.3705`

---

**Enabling ASP.NET to run as another user on Windows Server 2003**

With Windows Server 2003 and IIS 6, there is a new feature named application pools. Each pool can be configured to run as a different user, provided that user has membership in the IIS_WPG group. Virtual roots can be added to an application pool, and the debugger will then be able to attach to it if the pool is running as the same user that launched the debugger. This mechanism provides an easy way to set up an alternate execution environment, safely protect user credentials, and set up additional virtual roots.

### Adding and Configuring an Application Pool

1. Run the Management Console `compmgmt.msc` as an administrative user
2. Expand the Services and Applications node to display the Internet Information Services, and Application Pools nodes
3. Right-click the Application Pools node, choose New, and then choose Application Pool
4. Type the name for the Application Pool and click OK
5. Right-click on the new Application Pool and choose Properties
6. Under the Identity tab, choose the Configurable option
7. In the corresponding boxes, enter the User name and Password that you will be running the debugger with and click OK

**Note**: This account must be a member of the IIS_WPG group and have the access permissions listed above in order to run ASP.NET applications.

### Setting a Virtual Root to run in an Application Pool

1. Run the Management Console `compmgmt.msc` as an administrative user
2. Expand the Services and Applications node to display the Internet Information Services, Web Sites, and Default Web Site nodes
3. Expand the Default Web Sites node to display all of the virtual roots available
4. Right-click on the virtual root to configure and choose Properties
5. On the Virtual Directory tab, change the Application Pool drop-down to select the application pool running with the appropriate user identity and click OK
