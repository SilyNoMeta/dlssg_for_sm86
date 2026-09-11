<div align="center">

<h1>DLSS Frame Generation<br>让 RTX 30 系列生成更多帧</h1>
<p>更多画面，更流畅的运动，让倍率随游戏负载而变。</p>
<p>
<img alt="版本 310.9.1-9" src="https://img.shields.io/badge/release-310.9.1--9-76b900?style=flat-square">
<img alt="Windows x64" src="https://img.shields.io/badge/Windows-x64-238636?style=flat-square">
<img alt="DirectX 12 和 Vulkan" src="https://img.shields.io/badge/API-DX12%20%2B%20Vulkan-30363d?style=flat-square">
<img alt="SM86" src="https://img.shields.io/badge/GPU-SM86-30363d?style=flat-square">
</p>
<p><strong><a href="https://github.com/SilyNoMeta/dlssg_for_sm86/releases/download/v310.9.1-9/dlssg-sm86-310.9.1-9-win64.zip">下载 310.9.1-9</a></strong> · <a href="RELEASE-NOTES.md">版本更新</a> · <a href="docs/install-loaders.zh-CN.md">安装指南</a></p>
<p><a href="README.en.md">English</a> · <a href="README.fr.md">Français</a> · <strong>简体中文</strong></p>

</div>

---

在兼容的 **Ampere SM86 / RTX 30 系列** GPU 上使用 **DLSS Frame Generation 310.9.1**。本实验性适配基于 [sdli1995 的原项目](https://github.com/sdli1995/dlssg_for_sm86)，修正多帧生成的运动位置，提供可选优化，并将 **DirectX 12 与 Vulkan** 支持集成到一个 DLL 中。

**-9 新增：** 最高 **X6** 固定倍率、**兼容 DX12 集成中的原生 Dynamic MFG**，以及一个可自行编辑的 INI。游戏仍需已经集成 DLSS 帧生成。

## 能带来什么？

| 功能 | 游戏中的实际作用 |
|---|---|
| **选择 X2 至 X6** | 在已加载插件支持的范围内，为每张渲染帧生成更多中间帧。X4 表示一张渲染帧加三张生成帧。 |
| **让 Dynamic MFG 自动选择** | 为 NVIDIA 运行库设置你希望的目标，让它随负载调整倍率。需要兼容的 DX12 Streamline 集成与驱动。 |
| **让运动均匀推进** | 中间帧处于运动路径的不同位置。时间修正解决旧版“FPS 很高，观感却不流畅”的 MFG 问题，并始终生效。 |
| **支持 DX12 和 Vulkan** | 两者使用同一套修正后的 SM86 内核。固定 X5/X6 取决于游戏插件；原生动态模式仅支持 DX12。 |
| **适配已有模组** | 保留 `version.dll`，改名为 `dxgi.dll`，或作为 ASI 插件加载。同一个文件，同一套功能。 |
| **自行选择优化** | 四项 GPU 优化可在 INI 中独立开关。游玩不需要编译工具或安装 CUDA。 |

更多生成帧可以改善视觉流畅度，但 **X6 并不一定最好**。操作响应仍取决于实际渲染帧率，更高倍率也可能让画面瑕疵更明显。建议从 X2 或 X3 开始，在运动场景中比较。

## 开始使用

1. **下载并解压**[发布 ZIP](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/download/v310.9.1-9/dlssg-sm86-310.9.1-9-win64.zip)。
2. **关闭游戏并备份**将被替换的文件。将 `version.dll` 和 `dlssg_sm86.ini` 放在实际游戏可执行文件旁。《黑神话：悟空》的位置为 `b1/Binaries/Win64`。
3. **在游戏中启用 DLSS 帧生成。** 随包 INI 保留游戏的模式选择，并在集成支持时允许最高 X6。
4. **编辑 INI**，在兼容游戏中选择固定倍率或启用动态。修改配置后重启游戏。

> **第一次使用 DLSS 模组？** [RHI](https://github.com/RankFTW/RHI) 可帮助管理 DLSS 版本及配套工具。按其指南操作，再按上面的步骤安装本项目 DLL。

已经使用其他模组？请选择一种加载方式：

| 安装文件 | 使用场景 |
|---|---|
| `version.dll` | 默认的直接加载方式。 |
| `dxgi.dll` | 将同一个 DLL 改名后通过 DXGI 直接加载，无需 ASI Loader。 |
| `dxgi.asi` | 改名后使用 [Ultimate ASI Loader x64](https://github.com/ThirteenAG/Ultimate-ASI-Loader) 加载。加载器本身可占用 `version.dll`。 |

**只安装一份本项目 DLL。** 配置名称始终为 `dlssg_sm86.ini`，放在本项目 DLL/ASI 旁。保留已有的 ReShade 等代理文件；[安装指南](docs/install-loaders.zh-CN.md) 介绍共存、其他 ASI 名称及回退方法。不要将本文件改名为 `nvngx_dlssg.dll`。

## 按你的习惯设置

用文本编辑器打开本项目 DLL 旁的 **`dlssg_sm86.ini`**。填入自己需要的值，保存后**重启游戏**。随包配置为：

```ini
[FrameGeneration]
MaxMultiplier=6
ForceMultiplier=0
DynamicMFG=0
DynamicTargetFPS=0
```

| 参数 | 应填写什么 |
|---|---|
| `MaxMultiplier` | 倍率上限，**2 至 6**。实际加载的插件必须支持所请求倍率。 |
| `ForceMultiplier` | **0** 让游戏选择；**2 至所设上限** 请求对应固定倍率。 |
| `DynamicMFG` | **1** 在兼容的 DX12 集成中请求原生动态；**0** 表示本 DLL 不主动请求动态。 |
| `DynamicTargetFPS` | **0** 以显示器刷新率为目标。使用动态模式时，也可填写**自己希望的目标 FPS**（1–1000 的整数）。 |

**想固定 X5？** 设置 `MaxMultiplier=6`、`ForceMultiplier=5`、`DynamicMFG=0`。需要 X2、X3、X4 或 X6 时，改为对应倍率即可。

**想自动调整？** 设置 `DynamicMFG=1`，并选择自己的 `DynamicTargetFPS`。`ForceMultiplier=0` 时，回退使用游戏选择。也可指定固定回退，例如 `ForceMultiplier=4`，在动态不可用且固定覆盖受支持时生效。

目标**不保证实际 FPS 恒定**；VSync 可能优先生效。游戏中必须启用 FG，但菜单不必出现“Dynamic”选项。这些设置不会为游戏菜单添加按钮。

原生动态需要**兼容的 DX12 Streamline 集成与驱动**。固定覆盖也需要已识别的 Streamline 路径；直接使用 NGX 的集成仍由游戏控制。**Vulkan** 请使用固定模式，原生动态在该 API 上未启用。游戏自身选择的原生动态模式会被保留，即使本 DLL 未主动请求动态。

**保留旧 INI？** 加入上述配置节即可使用这些控制项。缺少该节时，默认 `MaxMultiplier=4`，其余三项为 `0`。随包新 INI 明确允许 X6，同时保留游戏的模式选择。

## 四项小优化，自由选择

默认全部开启。将某项设为 `0` 后重启即可比较。收益可能较小，并取决于实际负载。

| INI 设置 | 改变了什么 |
|---|---|
| `HardwareBilinear` | 最终重建使用 GPU 硬件过滤，可能产生细微像素差异。参考原项目的 [HardwareBilinear 选项](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff44a9c08f9841fa605e7b7160f79ccd2c40/docs/NATIVE_INI.md)。 |
| `Conv13SharedInput` | 在 GPU 快速共享内存中复用一个卷积的输入数据。 |
| `Conv0SharedInput` | 将共享输入复用应用到另一个重建卷积。 |
| `ResidualVectorLoads` | 合并两个残差卷积中的内存读取。 |

它们位于 `[Optimizations]`，对两种 API 均生效。省略的优化键默认为 `1`。全部关闭也会保留时间修正。这些选项不控制 Neural Rendering 或 NR Cost Scaler；不包含 FP8/INT8 模式或缩小的神经网络模型。

## 兼容性与配套工具

**Windows x64 · 兼容的 SM86 GPU · 游戏已有 DLSS FG 集成。** 运动/深度信息与帧呈现由游戏提供。本 DLL 无法为任意游戏添加 FG，也不提供 DX11 后端。Linux/Proton、DXVK 和 RTX 20 未验证。

原生 Dynamic MFG 已有 **RTX 3070 Ti Laptop、8 GB 显存**、驱动 **616.92** 上的游戏内功能确认。这是一台笔记本的结果，不代表所有 RTX 30 显卡或游戏。该驱动版本是测试环境，并非最低要求。高倍率与动态模式取决于**实际加载的 Streamline 插件及驱动**，而不只是 DLL 文件名。

测试者还报告，本项目与 **[ShortFuse 的 DLSS Tool](https://discord.com/channels/1408098019194310818/1543975158937821315)** 及 **[Patched DLSS-NR for RTX20/30/40](https://discord.com/channels/1408098019194310818/1543976771920330884)** 配合良好，这些工具也可通过 RHI 获取。NR 补丁的 GPU 支持范围不等于本 FG 桥接的支持范围。Discord 链接可能需要先加入服务器。

如果这些工具对你有帮助，请为 **[RHI](https://github.com/RankFTW/RHI)** 和 **[ShortFuse 的 RenoDX](https://github.com/clshortfuse/renodx)** 点亮一颗 Star。它们让安装管理方便了许多。

## 应该尝试哪个版本？

| 版本 | 主要区别 | 适合用途 |
|---|---|---|
| **[310.9.1-9](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-9)** | 兼容 DX12 集成中的动态模式、固定 X5/X6、INI 控制、通用加载。 | **从这里开始。** 包含此前修正及四项优化。 |
| [310.9.1-8](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-8) | 修正后的 X2–X4，支持 `version.dll` / `dxgi.dll` / ASI。 | 比较或回退到没有新增 MFG 控制的版本。 |
| [310.9.1-7](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-7) | 首个修正 MFG 运动的版本；仅支持 `version.dll`。 | 对比时间修正的历史版本。 |

-0 至 -6 因 MFG 运动错误而撤下。《黑神话：悟空》基准图表上的白色矩形仍是独立的已知问题。

## 深入了解 · 帮助改进

[技术说明](docs/research.zh-CN.md) 介绍时间修正、视图间能力共享修复、验证范围及尚未测量的项目。排查问题可参考[日志指南](docs/install-loaders.zh-CN.md#配置与检查)。NVIDIA 水印可用时，`Dyn DRV` 表示驱动动态模式；`4x/6x` 表示当前 X4、上限 X6。

**欢迎其他配置的测试反馈。** 请提供 GPU/显存、驱动、游戏/API、实际加载的 Streamline 版本、分辨率、INI 设置，以及 NR/Cost Scaler 设置。描述运动观感及响应，FrameView/PresentMon 记录尤其有帮助。[提交反馈 →](https://github.com/SilyNoMeta/dlssg_for_sm86/issues)

---

基于 [sdli1995/dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86)。感谢 [Michael Robles / RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock) 的时间修正、[mavismmg / ImDreamt 的 MFGAdaUnlock-RenoDx](https://github.com/mavismmg/MFGAdaUnlock-RenoDx) 提供的扩展/动态 MFG 参考，以及 [Ultimate ASI Loader](https://github.com/ThirteenAG/Ultimate-ASI-Loader) 的 ASI 加载支持。NVIDIA 运行库与资源保留其原有权利。[第三方声明](THIRD_PARTY_NOTICES.txt) · [校验值](SHA256SUMS.txt)
