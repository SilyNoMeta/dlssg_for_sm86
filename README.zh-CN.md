<div align="center">

# 适用于 RTX 20 / 30 的 DLSS 帧生成

**最高 X6 的多帧生成、更稳定的界面与更清晰的细节——有无 ReShade 均可使用。**

<a href="https://github.com/SilyNoMeta/dlssg_for_sm86/releases/download/v0.3.5-3/DLSSG-RTX20-30-v0.3.5-3-clean-win64.zip"><img alt="下载 0.3.5-3" src="https://img.shields.io/badge/%E4%B8%8B%E8%BD%BD-0.3.5--3-76b900?style=for-the-badge&logo=nvidia&logoColor=white"></a>

<img alt="Windows x64" src="https://img.shields.io/badge/Windows-x64-0078D4?style=flat-square&logo=windows&logoColor=white"> <img alt="DX12 与 Vulkan" src="https://img.shields.io/badge/API-DX12%20%7C%20Vulkan-30363d?style=flat-square"> <img alt="RTX 30" src="https://img.shields.io/badge/RTX%2030-%E6%94%AF%E6%8C%81-76b900?style=flat-square"> <img alt="RTX 20" src="https://img.shields.io/badge/RTX%2020-%E5%AE%9E%E9%AA%8C%E6%80%A7-d29922?style=flat-square"> <img alt="NVIDIA FG 310.9.1" src="https://img.shields.io/badge/NVIDIA%20FG-310.9.1-555?style=flat-square">

[English](README.en.md) · [Français](README.fr.md) · [简体中文](README.zh-CN.md) · [安装指南（英文）](docs/INSTALL.en.md) · [发布说明](RELEASE-NOTES.md)

</div>

> [!IMPORTANT]
> 实验性项目。仅适用于本身已提供 **DLSS 帧生成** 的游戏，不会解锁游戏插件本身不支持的功能。

## ✨ 0.3.5-3 新内容

| | 您将注意到的变化 |
|---|---|
| 🧭 **界面更稳定** | 在未向 DLSS 帧生成提供干净场景画面的游戏中（例如 **Crimson Desert**），小地图、计量条和文字在生成帧上不再闪烁或拖影。 |
| 🪟 **半透明面板更干净** | 半透明面板和小地图后面不再出现重影或背景扭曲（例如 **Cyberpunk 2077**）。 |
| 🪄 **全自动** | 无需新设置。在 DX12 下使用默认的 `UIRecomposition=1` 即生效。已正确处理界面的游戏不受影响。 |

## 🚀 快速开始

1. 关闭游戏，备份将被替换的文件。
2. 将 **`version.dll`** 复制到游戏渲染主程序旁。
3. 从 `config/d3d12`、`config/vulkan-sm86` 或 `config/vulkan-sm75` 复制 **`dlssg_sm86.ini`**，并将我们的配置段合并到 **`ReShade.ini`**（即使不使用 ReShade 也请保留此文件，其中保存我们的设置）。
4. 如需实时面板和快捷键：安装支持完整插件功能的 ReShade 6.8，并加入 `optional-panel/DLSSG-SM86-75-COMPANION.addon64`。
5. 在游戏中开启 DLSS 帧生成。

Vulkan 还需要对应版本的 NVIDIA 运行库，请参阅[安装指南](docs/INSTALL.en.md)。

## 🎛️ 功能

| | |
|---|---|
| **X2 – X6** | 跟随游戏设置，或选择固定倍数。X4 = 1 帧渲染 + 3 帧生成。 |
| **动态模式（DX12）** | 设定目标帧率，由 NVIDIA 在兼容游戏中自动调整生成数量。 |
| **自适应模式（Vulkan）** | 倍数根据帧率与目标在 X2 至 X6 之间调整。 |
| **画质** | 围栏、电线和植被更清晰，生成帧上的界面更稳定。 |
| **实时控制** | 通过 ReShade 面板或 Ctrl+F2…F12 按游戏修改并保存设置。 |
| **DLSS 渲染比例** | 从 DLAA 到超级性能或自定义比例，保存前会进行校验。 |
| **游戏专项修复** | REANIMAL 的 DLSS 启用、FINAL FANTASY VII REBIRTH 的识别处理、Black Myth: Wukong 的启动问题。 |

<details>
<summary><b>⚙️ 设置</b></summary>

`dlssg_sm86.ini`（修改后需重启游戏）：

```ini
[FrameGeneration]
Optimized=1            ; 优化内核与画质改进（0 = 参考内核）
MaxGeneratedFrames=5   ; 插件支持时最高 X6
```

`ReShade.ini`（未安装 ReShade 时同样使用）：

```ini
[DLSSG-SM86-75-COMPANION]
Multiplier=0           ; 0 = 跟随游戏，2-6 = 固定倍数
Dynamic=0              ; 1 = 动态（DX12）/ 自适应（Vulkan）
TargetFPS=0            ; 0 = 显示器刷新率，否则为目标值（非硬性上限）
UIRecomposition=1      ; 自动界面处理（0 = 跟随游戏，2 = 强制）
```

快捷键（需面板）：**Ctrl+F2–F6** X2–X6 · **Ctrl+F10** 自动模式 · **Ctrl+F11** 跟随游戏 · **Ctrl+F12** 恢复已保存设置。

</details>

<details>
<summary><b>🔌 代理文件名</b></summary>

同一文件可按游戏实际加载的名称重命名，只安装一份。

| 名称 | 适用情况 |
|---|---|
| `version.dll` | 首选，包括 Unreal Engine 4/5 |
| `dinput8.dll` | 使用 DirectInput8 的游戏 |
| `dxgi.dll` | 较早加载 DXGI 的游戏——切勿覆盖已有的 ReShade `dxgi.dll` |
| `winmm.dll` | 使用 WinMM 的游戏 |
| 任意 `.asi` 名称 | 配合 ASI 加载器 |

</details>

<details>
<summary><b>⬆️ 从旧版本升级</b></summary>

替换 `version.dll`，用新的可选面板替换旧的伴随插件（或直接移除），并移走旧的 `DLSSG-SM86-75-RUNTIME.dll`。切勿同时启用两个版本的插件。release 11 设置的迁移方法见[安装指南](docs/INSTALL.en.md#upgrading)。

</details>

## 🎮 实机测试

**Crimson Desert · Cyberpunk 2077 · FINAL FANTASY VII REBIRTH · Onimusha: Way of the Sword · Bodycam · REANIMAL（试玩版）**——RTX 3070 Ti Laptop，DX12。其他游戏及 RTX 20 硬件表现可能不同，欢迎反馈。

## 📦 版本

| 版本 | |
|---|---|
| [**0.3.5-3**](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v0.3.5-3) | 当前版本：更稳定的界面与干净的半透明面板，基于集成引擎与可选面板。 |
| [310.9.1-11](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-11) · [-10](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-10) · [-9](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-9) · [-8](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-8) · [-7](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-7) | 已归档的上一代版本，使用其自身的文件布局与设置。 |

## 💬 反馈

请[提交 issue](https://github.com/SilyNoMeta/dlssg_for_sm86/issues)，并附上 GPU 与驱动版本、游戏与 API、代理文件名、两个 INI 文件以及 `DLSSG-SM86-75-runtime.log`。

---

<div align="center">

基于 [sdli1995 / dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86)（upstream 0.3.5）· 包含改编自 [Tony Joaca / DLSSG-Transfusion](https://github.com/TonyJoaca/DLSSG-Transfusion) 的工作（MIT）<br>
感谢 [Coldwood1026](https://github.com/Coldwood1026/dlssg_for_sm75)、[Matias Lombo](https://github.com/matiasLombo/mfg-unlock) 与 [ReShade](https://reshade.me/)<br>
[第三方声明](THIRD_PARTY_NOTICES.txt) · [校验和](SHA256SUMS.txt) · 与 NVIDIA 无关

</div>
