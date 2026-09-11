# 面向 SM86 的 DLSSG 310.9.1

[English](README.md) | 简体中文 | [Français](README.fr.md)

基于 [sdli1995/dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86) 的实验性 **DLSS Frame Generation 310.9.1**
SM86/RTX 30 适配。一个 **`version.dll`** 包含 **DirectX 12 + Vulkan**、
MFG 时间位置修正和四项可选优化。

## 下载 310.9.1-7

**[下载 DLL 和可选 INI](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/download/v310.9.1-7/dlssg-sm86-310.9.1-7-win64.zip)** · [版本说明](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-7)

目前只保留此版本。**此前 -0 至 -6 已撤下：虽然 FPS 较高，其 X3/X4
生成图像的运动位置可能都接近两张真实图像的中点。** 在每帧移动 8 像素的测试中，
旧 X4 输出约为 4/4/4 像素，修正后为 2/4/6。使用 **RTX 3070 Ti Laptop、8 GB**、
驱动 616.92 的用户确认《黑神话：悟空》X4 明显更加流畅。这是正确性修复，
不承诺提高 FPS。悟空基准图表的白色矩形仍存在；赛博朋克和鬼武者仍待确认。

即使关闭全部 INI 优化，时间修正也始终生效。
详见[技术发现、方法和结果](docs/research.zh-CN.md)。

## 安装

1. 关闭游戏，备份现有 `version.dll` 和 `dlssg_sm86.ini`。
2. 将 `version.dll` 放在实际渲染程序旁：悟空为 `b1/Binaries/Win64`，
   无人深空为 `Binaries`。
3. 可将 `dlssg_sm86.ini` 放在同一目录，重启并比较 X2/X3/X4。

如果其他模组占用了 `version.dll`，请先处理冲突；本代理不会链式加载其他代理。
不要将本文件改名为 `dxgi.asi` 或 `nvngx_dlssg.dll`。
**ASI loader 配置仍在测试中。** 回退时关闭游戏并恢复备份文件。

需要 Windows x64、SM86 GPU 和游戏现有的 DLSS FG 集成。Vulkan 游戏还需提供
NGX 扩展和帧呈现机制。复制 DLL 无法为任意游戏添加 FG。DX11、Linux/Proton、
DXVK、RTX 20 和其他代理文件名未验证。游玩无需安装 Python/CUDA。
616.92 是已测试驱动，并非最低版本要求。

## 可选优化

```ini
[Optimizations]
HardwareBilinear=1
Conv13SharedInput=1
Conv0SharedInput=1
ResidualVectorLoads=1
```

| 选项 | 作用 |
|---|---|
| `HardwareBilinear` | 最终重建使用硬件过滤，可能出现细微像素差异；相关原项目选项为 [HardwareBilinear](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff44a9c08f9841fa605e7b7160f79ccd2c40/docs/NATIVE_INI.md)。 |
| `Conv13SharedInput` | 在共享内存中复用一个卷积的 FP16 输入。 |
| `Conv0SharedInput` | 在第二个重建卷积中复用 FP16 输入。 |
| `ResidualVectorLoads` | 对两个残差卷积使用向量化输入读取。 |

`1` 开启，`0` 关闭；文件或键缺失时默认为 `1`。修改后须重启游戏。
设置适用于两种 API，不选择 X2/X3/X4，也不控制 Neural Rendering / NR Cost Scaler。
本代理读取自己的 `[Optimizations]` 配置，不读取原生提供程序的配置段。
全部关闭时仍使用修正后的参考内核，不会恢复旧版本缺陷。
本版本不含 FP8、INT8 或降低神经网络质量的选项。

## 配套工具与游戏反馈

**建议新手使用 [RHI](https://github.com/RankFTW/RHI) 管理配套工具**，遵照其说明操作，再安装此 FG DLL。
笔记本测试用户反馈与 [ShortFuse DLSS Tool](https://discord.com/channels/1408098019194310818/1543975158937821315) 和
[Patched DLSS-NR for RTX20/30/40](https://discord.com/channels/1408098019194310818/1543976771920330884) 配合良好，后者也可通过 RHI 安装。
Discord 链接可能要求加入服务器。NR 补丁名称中的 GPU 范围不会扩大本 FG 代理的 SM86 支持范围。
请给 **[RHI](https://github.com/RankFTW/RHI)** 和 **[ShortFuse RenoDX](https://github.com/clshortfuse/renodx)** 点 Star，支持作者。

| 游戏 | 验证情况 |
|---|---|
| 黑神话：悟空 / DX12 | 用户确认修正后的 X4 明显更流畅；基准图表仍为白色。 |
| 幻兽帕鲁 | 旧版本已有良好反馈；修正版需重新测试。 |
| 无人深空 / Vulkan | 旧诊断预览版 X2/X3/X4 可运行；修正版已通过离线 Vulkan 检查，游戏内待复测。 |
| 赛博朋克 / 鬼武者 | 原问题来自 RTX 3060 Ti 8 GB；修正版在这些游戏中尚未确认。 |

目前主要数据来自一台**笔记本**，不能代表桌面 GPU。欢迎[提交其他配置反馈](https://github.com/SilyNoMeta/dlssg_for_sm86/issues)：
GPU/显存、驱动、游戏/API、分辨率、倍数、NR/Cost Scaler 设置、运动画质和响应感受。
[历史帕鲁截图与 RHI 配置](GALLERY.zh-CN.md) 展示 X2，不代表本次修正版，
也不能确认 Cost Scaler 的准确数值。

## 诊断与致谢

DLL 内嵌未修改的 NVIDIA 310.9.1 运行时和 SM86 内核。运行时经校验后缓存于
`%LOCALAPPDATA%/DLSSG-SM86/<SHA256>/`；内核始终内嵌。日志为代理旁的 `dlssg3109.log`。
Vulkan 日志事件证明后端执行，不测量显示 FPS。损坏缓存会被拒绝；关闭游戏后，
可将对应缓存子目录移走以便重新生成。

感谢 [sdli1995](https://github.com/sdli1995/dlssg_for_sm86) 和 Michael Robles 的
[RTX40MFG-Unlock 时间修正](https://github.com/dashdogy/RTX40MFG-Unlock/blob/cf99204a00ce015a24c4c2be4082170b65e2fed1/source/native/midpoint_fix.cpp)（MIT）。
详见[第三方声明](THIRD_PARTY_NOTICES.txt)和 `SHA256SUMS.txt`。
