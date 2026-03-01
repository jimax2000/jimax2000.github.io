---
layout: post
title: "恢复IIS的ASP.NET支持"
date: 2005-11-29
tags: [技术]
---

本地的IIS不知道怎么不能支持ASP.NET了，用VS.NET 2003创建一个新的Web Application 就说IIS不支持ASP.NET。使用aspnet_regiis -i -enable恢复了。

下面摘自http://www.163er.com/zz/Server/Windows/6159.shtml：

使用 Aspnet_regiis.exe 修复 ASP.NET 的 IIS 映射

从“开始”菜单，单击“运行”。在“运行”对话框中的“打开”框中，键入 cmd，然后单击“确定”。在新窗口中的命令提示符下，键入以下行：\"%systemroot%\\Microsoft.NET\\Framework\\version\\aspnet_regiis.exe\" –i。

在该路径中，version 表示安装在服务器上的 .NET Framework 的版本号。在键入命令时，必须用实际的版本号去代替这个占位符。

注意 在该命令中必须包含引号。

有关 Aspnet_regiis.exe 的详细信息，请以 -? 作为参数重复步骤 3 或参阅 ASP.NET IIS 注册工具 (Aspnet_regiis.exe)。

另外，在 Windows Server 2003 上，如果从 Web 下载或通过 Visual Studio .NET 安装了 .NET Framework 和 ASP.NET，则必须从 IIS 管理器中手动启用 ASP.NET。详细信息，请参阅安装 ASP.NET。

注意 如果要在域控制器上安装 ASP.NET，您必须采取特殊的步骤来使安装正常进行。详细信息，请参阅位于 http://support.microsoft.com 的 Microsoft 知识库中的文章 CHS315158：“ASP.NET 在域控制器上不能使用默认 ASPNET 帐户”。

ASP.NET IIS 注册工具 (Aspnet_regiis.exe)当您在单个计算机上并行执行多个版本的 .NET Framework 时，脚本映射到 ASP.NET 应用程序的 ASP.NET ISAPI 版本将确定该应用程序使用的公共语言运行库版本。ASP.NET IIS 注册工具 (Aspnet_regiis.exe) 允许管理员或安装程序很容易地更新 ASP.NET 应用程序的脚本映射，以便指向与工具相关的 ASP.NET ISAPI 版本。此工具还可以用于显示所有已安装的 ASP 版本的状态。NET 注册与工具配对的 ASP.NET 版本，创建客户端脚本目录，并执行其他配置操作。

Aspnet_regiis [options]您可以指定下列一个或多个选项。

选项 描述-c 将 ASP.NET 的客户端脚本（如客户端的验证脚本）安装到每个 IIS 站点目录的 aspnet_client 子目录中。注意 仅安装与 Aspnet_regiis.exe 相关的 ASP.NET 版本的客户端脚本。

-e 从每个 IIS 站点目录中的 aspnet_client 子目录中删除 ASP.NET 的客户端脚本。注意 仅删除与 Aspnet_regiis.exe 相关的 ASP.NET 版本的客户端脚本。

-ea 从每个 IIS 站点目录的 Aspnet_client 子目录中删除所有 ASP.NET 版本的客户端脚本。-i 安装与 Aspnet_regiis.exe 相关的 ASP.NET 版本，并更新 IIS 配置数据库根及其下的脚本映射。注意 仅更新使用早期 ASP.NET 版本的应用程序的脚本映射。使用后续版本的应用程序不受影响。

-ir 安装与 Aspnet_regiis.exe 相关的 ASP.NET 版本并仅在 IIS 中注册 ASP.NET。注意 此选项不会更新脚本映射。要安装 ASP.NET 并更新脚本映射，请使用 -i 选项。

-k path 从所有 ASP.NET 应用程序中将脚本映射删除到所有 ASP.NET 版本中，这些 ASP.NET 应用程序位于所指定的应用程序的根路径及其子目录中。-kn path  仅从所指定的应用程序根路径中的 ASP.NET 应用程序中将脚本映射删除到 ASP.NET 版本中。注意 该选项不影响 path 子目录中的应用程序。

-lk 列出 ASP.NET 脚本映射的路径和所有 IIS 配置数据库项的版本。注意 从父项继承 ASP.NET 脚本映射的项不会显示。

-lv 列出在计算机上安装的所有 ASP.NET 版本的状态和安装路径。-r 更新 IIS 配置数据库中及其下的所有脚本映射，以便将其指向与 Aspnet_regiis.exe 相关的 ASP.NET ISAPI 版本。注意 除当前版本外，所有现有脚本都将更新到指向与 Aspnet_regiis.exe 相关的 ASP.NET ISAPI 版本。

-s path 将指向与 Aspnet_regiis.exe 关联的 ASP.NET ISAPI 版本的脚本映射安装到所指定的应用程序的根路径及其子目录处的所有 ASP.NET 应用程序中。所有在指定路径和其下面使用 ASP.NET ISAPI 版本的现有脚本映射都会更新。-sn path 将指向与 Aspnet_regiis.exe 关联的 ASP.NET ISAPI 版本的脚本映射安装到所指定的应用程序根路径处的 ASP.NET 应用程序中。所有在指定路径中使用 ASP.NET ISAPI 早期版本的现存脚本映射都会更新。注意 该选项不影响 path 子目录中的应用程序。

-u 从计算机中卸载与 Aspnet_regiis.exe 相关联的 ASP.NET 版本。此 ASP.NET ISAPI 版本的现有脚本映射会自动重新映射到所安装的最高的剩余 ASP.NET ISAPI 版本中。-ua 从计算机中卸载全部 ASP.NET 版本。-? 显示工具的选项和命令语法。

注释当计算机中安装了多个版本的 ASP.NET 时，ASP.NET 会并行地运行。在此安装过程中，Internet 信息服务 (IIS) 需要知道应在 ASP.NET 中处理页的 ASP.NET ISAPI (aspnet_isapi.dll) 版本。与 ASP.NET 应用程序相关联的 ASP.NET ISAPI 版本将确定用于该应用程序的公共语言运行库。ASP.NET 应用程序通过 IIS 中的脚本映射与 ASP.NET ISAPI 版本相关联。要简化 ASP.NET 应用程序的配置过程，每个 ASP.NET 版本应该包括链接的 Aspnet_regiis.exe 版本。

注意 每个版本的 .NET Framework 都包含唯一的 Aspnet_regiis.exe 版本。因为工具的每个版本仅能应用于与其相关联的 .NET Framework 版本，所以请使用该版本的适当工具来配置 ASP.NET 应用程序。

Aspnet_regiis.exe 通常与 -s 或 -sn 选项一起使用，以将 ASP.NET 应用程序重新映射到与工具相关联的 .NET Framework 版本中。请使用 -s 选项更新在指定路径和它们所有子目录中的应用程序。如果不想更新子目录中的应用程序，请使用 -sn 选项。要立即更新计算机中所有现有 ASP.NET 应用程序的脚本映射，请使用 -r 选项。

注意 path 参数引用的是应用程序的根路径，而不是物理路径。例如，W3SVC/1/ROOT/SampleApp1。

相反，您可以使用此工具从使用 -k 或 -kn 选项的任何 ASP.NET 版本中删除脚本映射，并指定应用程序的根路径。

注意 如果指定的根路径从父根路径中继承了其脚本映射，则 -k 和 -kn 选项不起作用。

该工具也可用来安装或卸载链接的 ASP.NET 版本。请使用 -i 选项安装 ASP.NET 并更新所有现有 ASP.NET 应用程序的脚本映射。使用 -ir 选项安装 ASP.NET，无需更新脚本映射。要卸载与该工具相关的 ASP.NET 版本，请使用 -u 选项。如果想从计算机中卸载所有版本的 ASP.NET，请使用 -ua 选项。

您可以使用 Aspnet_regiis.exe 查看关于 ASP.NET 的信息。要列出所有已安装的 ASP.NET 版本的状态和安装路径，请使用 -lv 选项。如果您要查看由 ASP.NET 脚本映射的所有 IIS 配置数据库项的路径，请使用 -lk 选项。

客户端脚本（如客户端验证）可以使用 Aspnet_regiis.exe 来进行安装和删除。将与工具相关联的 ASP.NET 版本的客户端脚本安装到每个 IIS 站点目录的 aspnet_client 子目录中，请使用 -c 选项。要删除与工具相关的 ASP.NET 版本的客户端脚本，请使用 -e 选项。要删除所有已安装的 ASP.NET 版本，请使用 -ea 选项。

有关在 ASP.NET 中并行执行的详细信息，请参阅 ASP.NET 中的并行支持。有关脚本映射和应用程序根路径的详细信息，请参阅设置应用程序映射。

示例下列命令将指向与 Aspnet_regiis.exe 相关的 ASP.NET 版本的脚本映射安装到 SampleApp1 应用程序及其所有子应用程序中。

Aspnet_regiis -s W3SVC/1/ROOT/SampleApp1下列命令仅会更新 SampleApp1 应用程序的脚本映射，而不会影响子目录中的应用程序。

Aspnet_regiis -sn W3SVC/1/ROOT/SampleApp1下列命令将安装与工具相关的 ASP.NET 版本，并更新所有现有 ASP.NET 应用程序的脚本映射。请注意仅有在当前脚本映射到早期 ASP.NET 版本的应用程序才会受到影响。

Aspnet_regiis -i下列命令将安装与工具相关的 ASP.NET 版本，但不会更新现有 ASP.NET 应用程序的脚本映射。

Aspnet_regiis -ir下列命令显示在计算机上安装的所有 ASP.NET 版本的状态和安装路径。

Aspnet_regiis -lv
