<div align="center">

<h1>DLSS Frame Generation</h1>
<p>按自己的方式设置帧生成，现在可直接通过 ReShade 实时调整。</p>
<p><img alt="310.9.1-11" src="https://img.shields.io/badge/release-310.9.1--11-76b900?style=flat-square"> <img alt="Windows x64" src="https://img.shields.io/badge/Windows-x64-238636?style=flat-square"> <img alt="DX12 and Vulkan" src="https://img.shields.io/badge/API-DX12%20%2B%20Vulkan-30363d?style=flat-square"></p>
<p><strong><a href="https://github.com/SilyNoMeta/dlssg_for_sm86/releases/download/v310.9.1-11/dlssg-310.9.1-11-win64.zip">下载 310.9.1-11</a></strong></p>
<p><a href="README.en.md">English</a> · <a href="README.fr.md">Français</a> · <a href="README.zh-CN.md">简体中文</a></p>

</div>

---


**310.9.1-11 将引擎保留在提前加载的 DLL 中，ReShade 改为可选控制面板。** 可以只用 DLL，也可以添加面板，在游戏中调整设置。旧独立 add-on 在部分游戏中加载过晚。基于 [sdli1995 的原始项目](https://github.com/sdli1995/dlssg_for_sm86)。

## 一个下载包，可搭配或不搭配 ReShade

ZIP 包含 **`version.dll`**、**`dlssg_sm86.ini`**、可选面板 **`DLSSGControls.addon64`** 及使用文档。

| 使用方式 | 操作方法 |
|---|---|
| **不使用 ReShade** | 安装 DLL 和 INI，手动编辑 INI 后重启游戏以应用更改。 |
| **使用 ReShade** | 安装相同文件及 add-on。ReShade 需支持完整 add-on，面板可调整倍率及兼容的 DMFG 设置、录制快捷键，并将这些设置保存到 INI。 |

面板仅覆盖部分 INI 设置：优化开关、倍率上限、日志和遥测仍需手动编辑并重启。本包不附带 ReShade 或 OptiScaler。没有 ReShade 时，add-on 不会使用，DLL 仍提供帧生成。升级时只移除本项目旧 `DLSSG.addon64`，保留 ReShade 和其他 add-on。

关闭游戏并备份文件，安装到实际游戏可执行文件旁（《黑神话：悟空》：`b1/Binaries/Win64`），然后在游戏中开启 DLSS 帧生成。只安装一份本项目引擎，并按下方迁移说明保留自己的 INI。


[DLL / ASI 安装](docs/install-loaders.zh-CN.md) · [ReShade 安装与面板](docs/reshade-controls.zh-CN.md)

## 可以做什么

| 功能 | 实际用途 |
|---|---|
| **X2–X6** | 在已加载插件支持范围内选择固定倍率。X4 是一张渲染帧加三张生成帧。 |
| **原生 Dynamic MFG** | 指定目标，让 NVIDIA 在兼容的 **DX12** 集成中自动调整倍率。 |
| **实时控制** | 游戏中请使用 ReShade 面板调整设置。仅使用 DLL 时，快捷键目前在《黑神话：悟空》中失效，尚不能作为可靠的替代方案。 |
| **DX12 + Vulkan** | 共用兼容引擎与正确的运动时序。Vulkan 固定控制需要识别到 Streamline 路径；原生动态仅限 DX12。 |
| **RTX 30 / RTX 40** | SM86、SM89 内核，已有 RTX 3070 Ti Laptop 8 GB 和 RTX 4090 用户反馈。**RTX 20 / SM75 仍为实验支持，尚未在实体 Turing 显卡测试。** |
| **可选遥测** | 为兼容工具提供 CPU 源帧提交速率，OptiScaler 状态见下方。 |

倍率越高不一定越好：响应性仍取决于渲染帧率，运动伪影也可能增加。游戏必须已有 DLSS FG 集成；本项目不会为任意游戏添加 FG，也不提供 DX11 后端。直接 NGX 集成仍由游戏控制。本版本不声称获得新的 FPS 基准结果。

## 按自己的需要配置 INI

```ini
[FrameGeneration]
MaxInterpolatedFrames=5
ForceMultiplier=0
DynamicMFG=0
DynamicTargetFPS=0
```

- **`MaxInterpolatedFrames`** 表示生成帧数量：**1–5 对应 X2–X6**，默认 5。设为 1 仍保留 X2 及必要补丁。
- **`ForceMultiplier`** 使用显示倍率：0 跟随游戏，2–6 请求固定倍率，仍受上限约束。
- **`DynamicMFG=1`** 请求原生动态模式。**`DynamicTargetFPS`** 可设 1–1000，0 使用显示目标。没有预设目标帧率。
- **`[Logging] Enabled=0`** 关闭本项目日志，默认 1；已有日志不会删除。
- **`[Telemetry] Enabled=1`** 开启源帧速率遥测，默认 0。

**升级：**将 `MaxMultiplier=M` 替换为 `MaxInterpolatedFrames=M-1`，例如 6 变成 5。旧上限键不再读取。`ForceMultiplier` 含义不变。`[Hotkeys]` 的动态动作叫 `ActivateDynamicMFG`；启动开关 `DynamicMFG` 保留在 `[FrameGeneration]`。

手动编辑 INI 后重启。ReShade 的 **Apply for this session** 仅本次有效；**Apply & save settings** 保存模式与目标。点击 **Record** 录制组合键，再用 **Save keyboard shortcuts** 独立保存快捷键。默认：**Ctrl+F2–F6** 对应 X2–X6，**Ctrl+F10** 启用动态模式，**Ctrl+F11** 跟随游戏，**Ctrl+F12** 恢复 INI 设置。所有绑定均可修改或禁用。 [完整控制与按键语法](docs/live-controls.zh-CN.md)。

**目标被忽略？** NVIDIA 的全局或游戏级 **Override DLSSG Target Frame Rate** 可覆盖已被 Streamline 接受的目标。希望由面板控制时，请禁用相关覆盖项并重启游戏。它与普通 FPS 限制器、VSync 是不同设置。DMFG 目标不是严格帧率上限。动态快捷键使用 INI 中保存的目标；若要通过快捷键复用面板目标，请先保存设置。

## 四项可选优化

在 `[Optimizations]` 中均默认开启（1）；设为 0 并重启可进行比较。收益取决于负载，可能较小。即使全部关闭，时序修正仍然生效。

| 键 | 作用 |
|---|---|
| `HardwareBilinear` | 重建阶段使用硬件过滤，参考[原项目选项](https://github.com/sdli1995/dlssg_for_sm86/blob/main/docs/NATIVE_INI.md)，可能产生细微像素差异。 |
| `Conv13SharedInput` | 在 GPU 共享内存中复用卷积输入。 |
| `Conv0SharedInput` | 对另一卷积使用共享输入复用。 |
| `ResidualVectorLoads` | 对残差卷积的内存读取进行分组。 |

Ada 使用同一 FP16 模型及 SM89 编译，不包含 FP8/INT8 加速或更小模型。[技术历史与验证](docs/research.zh-CN.md)。

## DLSS 画质：应用、验证、保存

可选面板现提供 **DLAA、Quality、Balanced、Performance、Ultra Performance** 和 **50–100% 自定义滑块**。这些控件主要用于注入 DLSS 后游戏没有提供画质菜单的情况。**如果游戏已有 DLSS 画质或渲染比例设置，请优先使用游戏菜单。**

先为当前会话应用比例。连续八帧成功的 DLSS 计算使用请求分辨率后，才能点击 **Save render scale**。被忽略的请求无法通过面板或 API 保存。实际输入/输出尺寸与请求值分开显示。关闭覆盖始终可以保存；手动修改 INI 会绕过验证。能否实时应用取决于游戏。[分辨率控制与恢复](docs/super-resolution.zh-CN.md)。

## 实验性画质选项

INI 提供三个独立选项，**默认均关闭**：

| 键 | 作用 |
|---|---|
| `[Quality] QualityValidWarp=1` | 增加已接受重投影颜色候选的权重，尝试保留细小细节。 |
| `[Experimental] BlackwellBlend=1` | 使用从 Blackwell 移植的混合内核。 |
| `[Experimental] BlackwellScatter=1` | 使用从 Blackwell 移植的中间帧运动散射内核。 |

Blackwell 表示内核来源，并非要求使用 Blackwell 显卡；提供 SM75、SM86、SM89 版本。选项可组合使用，修改后须完整重启，也可能增加拖影或降低稳定性。Wukong 实验中曾出现间歇性 GPU 挂起；如需保持原有路径，请关闭这些选项。不承诺普遍的画质或 FPS 提升。

本版本仍内置 NVIDIA **310.9.1** FG 运行库和适配后的内核，并不宣称支持十四个提供方版本、自动 UIR 解锁、DirectInput8 代理或 Proton。

## OptiScaler 与配套工具

**OptiScaler 支持仍在等待 [PR #1156](https://github.com/optiscaler/OptiScaler/pull/1156)。** 本包包含数据提供端，但 OptiScaler 必须包含该改动才能读取。仅开启 INI 不会更新旧版本。数据是 CPU 源帧提交速率，不是 GPU 完成速率或输入延迟。可用时，我们的 ReShade 面板也能独立显示它。

新手可以先用 **[RHI](https://github.com/RankFTW/RHI)** 管理 DLSS 与配套工具，再使用上方下载链接。测试者反馈与 ShortFuse 的 [DLSS Tool](https://discord.com/channels/1408098019194310818/1543975158937821315) 和 [Patched DLSS-NR for RTX20/30/40](https://discord.com/channels/1408098019194310818/1543976771920330884) 配合良好，也可通过 RHI 安装。它们的 NR 支持与本项目的 FG 兼容范围不同。欢迎给 [RHI](https://github.com/RankFTW/RHI) 和 [ShortFuse RenoDX](https://github.com/clshortfuse/renodx) 点星支持！

## 版本与反馈

| 版本 | 区别 |
|---|---|
| **[310.9.1-11](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-11)** | 推荐：提前加载的 DLL 与可选 ReShade 面板；增强加载路由对覆盖层拦截的兼容性。 |
| [310.9.1-10](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-10) | 旧独立 ReShade 引擎；建议迁移到 DLL + 控制面板以提高启动可靠性。 |
| [310.9.1-9](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-9) | 首次提供原生动态 / X6，使用旧 INI 上限语法。 |
| [310.9.1-8](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-8) | 可重命名的通用 DLL，已修正 X2–X4。 |
| [310.9.1-7](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-7) | 首次修正 MFG 运动，仅 `version.dll`。 |

-0 至 -6 因 MFG 运动错误已撤下。《黑神话：悟空》基准图表上的白色矩形仍是已知问题。实时控制与动态目标切换已在该游戏获得用户确认，但不代表所有游戏均已验证。Linux/Proton、DXVK 尚未验证。

[提交反馈](https://github.com/SilyNoMeta/dlssg_for_sm86/issues) 时请附 GPU/显存、驱动、游戏/API、已加载 Streamline 版本、安装方式、INI 和 NR 设置。欢迎更多配置，尤其 RTX 20 用户测试。

---

Credits: [sdli1995](https://github.com/sdli1995/dlssg_for_sm86) · [Coldwood1026](https://github.com/Coldwood1026/dlssg_for_sm75) · [RTX40MFG-Unlock](https://github.com/dashdogy/RTX40MFG-Unlock) · [MFGAdaUnlock-RenoDx](https://github.com/mavismmg/MFGAdaUnlock-RenoDx) · Tony Joaca (DLSSG-Transfusion) · [Matias Lombo](https://github.com/matiasLombo/mfg-unlock) · [ReShade](https://reshade.me/) · [Ultimate ASI Loader](https://github.com/ThirteenAG/Ultimate-ASI-Loader). [Third-party notices](THIRD_PARTY_NOTICES.txt) · [Checksums](SHA256SUMS.txt)
