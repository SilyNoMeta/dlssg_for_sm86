# 安装方式：version.dll、ASI 或 dxgi.dll

**310.9.1-9** — [下载通用压缩包](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-9)。
其中仅含一个 `version.dll`，也可改名为 `dxgi.dll` 或 `dxgi.asi`。
这些方式从 -8 起提供；原始 -7 二进制文件必须保留 `version.dll` 名称。

所有文件名均使用相同的 DX12/Vulkan 运行库、内核、时间修正和 INI 选项。
请先关闭游戏并备份现有文件，在实际可执行文件所在目录选择**一种**安装方式。
只安装一份本项目桥接文件，切换加载方式时保留自己的 INI 配置。

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
不可将桥接文件改名为 `nvngx_dlssg.dll`。

## 在 INI 中配置帧生成

根目录 INI 通过 `MaxMultiplier=6`、`ForceMultiplier=0`、`DynamicMFG=0`
保留游戏选择。编辑本项目 DLL 旁的 `dlssg_sm86.ini`，填写自己希望的固定倍率
或动态设置。重启后启用游戏 FG；若集成需要重新提交选项，可关闭再开启一次 FG。
所有设置只需一个 DLL 和一个 INI。

设 `DynamicMFG=1` 请求动态，并自行选择 `DynamicTargetFPS`：0 为显示器刷新率，
1–1000 为目标 FPS。`ForceMultiplier=0` 回退至游戏选择，也可用其他受支持的值
指定固定回退。固定倍率请设 `DynamicMFG=0`，并将 `ForceMultiplier` 设为 2 至
`MaxMultiplier`。原生动态需要兼容的 DX12 Streamline 与驱动。固定覆盖也需要已识别的
Streamline 路径；直接调用 NGX 的集成仍由游戏控制。游戏自身选择的原生动态
模式会被保留。详见[设置说明](../README.zh-CN.md)。

缺少 `[FrameGeneration]` 时仍使用 X4 上限，不强制固定或动态模式。省略的
优化键仍默认开启。这两个配置节均不能关闭时间修正。

## 配置与检查

原生动态模式中，`sl_native_dynamic_supported=1` 后出现
`sl_native_dynamic_accepted=<目标>` 表示能力和请求已被接受。
`sl_state_viewport`、`sl_options_viewport` 可诊断跨视图集成。也要检查实际行为：
可用的 NVIDIA 水印会显示 `Dyn DRV` 和 `4x/6x`（当前倍率 / 上限）。仅接受请求
不等于完成呈现基准测试。本包不会自动启用水印。日志 `dlssg3109.log` 位于本项目
DLL 旁；查询间帧计数不能当作倍率。


无论桥接文件使用什么名称，配置文件都必须保持 **`dlssg_sm86.ini`**。
`[Optimizations]` 下的四个选项使用 `1` 或 `0`；文件或选项缺失时默认为 `1`。
修改配置后需要重启游戏。X3/X4 时间插值修正始终启用。

在 `dlssg3109.log` 中检查 `asi_attached`、`dxgi_attached` 或 `proxy_attached`；
运行库接入成功后会出现 `installed_310_9_1`。ASI 加载器不需要显示界面。
插件被加载，并不等于帧生成已经运行。

通用加载已在 -8 中验证；-9 保留其导出与启动路径，并通过 DX12/Vulkan 图像测试。
用户此前已在 RTX 3070 Ti Laptop 8 GB 上确认 -8 的 `dxgi.dll` 在悟空中正常工作。
这是功能验证反馈，不是新的性能基准。文件名不会为未集成帧生成的游戏添加该功能，
也不会增加 DX11 DLSSG 支持。回退时请关闭游戏，移走安装的桥接文件并恢复备份。
