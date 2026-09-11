# 安装方式：version.dll、ASI 或 dxgi.dll

这些说明介绍为下一版本准备的加载模式。
提供下载的 -7 二进制文件不支持这些模式。

同一个二进制文件包含 DX12/Vulkan 桥接、运行库、内核和 INI 配置功能。
请在游戏实际可执行文件所在目录中选择**一种**安装方式，
不要同时安装多个本项目桥接文件。

## 使用 Ultimate ASI Loader

1. 安装 [Ultimate ASI Loader x64](https://github.com/ThirteenAG/Ultimate-ASI-Loader)，
   文件名为 `version.dll`。
2. 将**本项目的** `version.dll` 重命名为 `dxgi.asi`，放在加载器旁边。
3. 将 `dlssg_sm86.ini` 放在同一目录，保持文件名不变。
4. 重启游戏，在游戏设置中启用 DLSS 帧生成。

```text
Game.exe
version.dll       <- Ultimate ASI Loader x64
dxgi.asi          <- 本项目桥接文件
dlssg_sm86.ini     <- 桥接配置
```

REFramework 可以继续使用自己的 `dinput8.dll`。这里的加载器和桥接文件
是两个不同的程序。UAL 会调用插件的 `InitializeASI`，因此也可以使用其他
`.asi` 文件名；我们已在独立加载测试中验证 `dlssg_sm86.asi`。
对于不调用该导出函数的加载器，请使用能够自动启动的 `dxgi.asi`。
如果插件放在 ASI 子目录中，INI 文件也应放在插件旁边。

## 直接使用 dxgi.dll

将本项目的 `version.dll` 重命名为 `dxgi.dll`，与 `dlssg_sm86.ini`
一起放在游戏可执行文件旁边。此方式不需要 ASI 加载器。

```text
Game.exe
dxgi.dll          <- 本项目桥接文件，同时将 DXGI 调用转发给 Windows
dlssg_sm86.ini
```

如果 ReShade 等其他模组已经使用 `dxgi.dll`，请保留原模组并选择 ASI 方式。
本项目的 DXGI 代理转发给 Windows，不会自动串联另一个 DXGI 代理。

## 直接使用 version.dll

将本项目的 `version.dll` 和 `dlssg_sm86.ini` 放在游戏可执行文件旁边，
无需额外安装 ASI 加载器。如果该文件名已被占用，请选择其他方式。
游戏必须实际加载所选文件名，桥接功能才会启动。

## 配置与检查

无论桥接文件使用什么名称，配置文件都必须保持 **`dlssg_sm86.ini`**。
`[Optimizations]` 下的四个选项使用 `1` 或 `0`；文件或选项缺失时默认为 `1`。
修改配置后需要重启游戏。X3/X4 时间插值修正始终启用。

在 `dlssg3109.log` 中检查 `asi_attached`、`dxgi_attached` 或 `proxy_attached`；
运行库接入成功后会出现 `installed_310_9_1`。ASI 加载器不需要显示界面。
插件被加载，并不等于帧生成已经运行。

整合版本已通过自动加载测试和 DX12/Vulkan 图像测试。
直接使用 dxgi.dll 的游戏内效果仍需验证。文件名不会为未集成帧生成的
游戏添加该功能，也不会增加 DX11 DLSSG 支持。
