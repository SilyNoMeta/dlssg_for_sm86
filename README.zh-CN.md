# 适用于 SM86 的 DLSSG 310.9.1

[English](README.md) | 简体中文 | [Français](README.fr.md)

面向 NVIDIA SM86 显卡的实验性 DLSS 帧生成 **310.9.1** 适配版本，基于
[sdli1995/dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86) 的工作。
安装时只需复制一个文件：**`version.dll`**。

[下载 310.9.1-1 版本](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-1)

## 310.9.1-1 更新内容

本次更新在最终图像重建阶段启用**硬件双线性过滤**，用硬件过滤的纹理读取
替代手动双线性插值，以减少计算工作。这是一条近似采样路径，生成帧的像素
可能与 310.9.1-0 略有不同。

其优化思路与原项目的
[`HardwareBilinear` 选项](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff4/docs/NATIVE_INI.md)
相同，但实现针对本项目的 310.9.1 桥接架构进行了适配。本版本**始终启用**
该路径，没有 INI 开关。如需恢复此前的采样方式，请使用
[310.9.1-0](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-0)。

测试用户在配备 RTX 3070 Ti Laptop、8 GB 显存的笔记本上反馈有**轻微的主观改善**。
目前尚未确认可重复的整体性能提升，效果取决于游戏和场景。欢迎其他配置的反馈。
X2/X3/X4 已通过离线检查。合成图像中的微小差异并不保证所有游戏、运动场景或 HDR
下的画质均相同。

## 运行要求

- Windows x64、Direct3D 12 游戏，以及提供 NGX/NVAPI 接口的 NVIDIA 驱动。
- SM86 显卡（GeForce RTX 30 系列）。已在配备 RTX 3070 Ti Laptop（**8 GB 显存**）的笔记本上使用 616.92 驱动测试；该驱动版本不是最低版本要求。
- 游戏须集成 DLSS 帧生成，并能够加载 `version.dll` 代理。
- X2、X3、X4 是否可选取决于游戏提供的选项。
- 游玩时无需安装 Python 或 CUDA Toolkit。

本版本不提供 SM75/RTX 20 路由、Vulkan 支持或其他文件名的代理 DLL。

## 安装与更新

### 新手推荐：RHI 与 ShortFuse 工具

**推荐新手使用 [RHI — ReShade HDR Installer](https://github.com/RankFTW/RHI)**
安装和管理配套工具。RHI 的 DLSS 管理界面提供 ShortFuse DLSS Tool 和 NR Cost Scaler。
请按 RHI 针对游戏的说明操作，然后按下方步骤安装本版本的 `version.dll`。

根据测试用户的反馈，本版本与
**[ShortFuse 的 DLSS Tool](https://discord.com/channels/1408098019194310818/1543975158937821315)**
及其 **[Patched DLSS-NR for RTX20/30/40](https://discord.com/channels/1408098019194310818/1543976771920330884)**
配合使用效果很好，也可通过 [RHI](https://github.com/RankFTW/RHI) 安装这些配套工具。
访问上述 Discord 链接可能需要先加入对应服务器。

NR 补丁名称中的 RTX20/30/40 指该配套工具的支持范围；本帧生成桥接版本仍面向
SM86/RTX 30。兼容性反馈仅代表已测试的配置。

**欢迎为 [RHI](https://github.com/RankFTW/RHI) 和
[ShortFuse 的 RenoDX](https://github.com/clshortfuse/renodx) 仓库点亮 Star ⭐，支持作者！**

### 安装帧生成桥接 DLL

1. 完全退出游戏。
2. 备份现有的 `version.dll`。如果其他 Mod 使用该文件名，请勿覆盖；本版本不支持代理链式加载。
3. 将本版本的 `version.dll` 复制到实际负责渲染的 EXE 旁。对于《黑神话：悟空》，路径为 `b1/Binaries/Win64`，与 `b1-Win64-Shipping.exe` 同目录。
4. 启动游戏并启用 DLSS 帧生成。建议先使用 X2，再在同一运动场景中比较 X3/X4。

无需 INI 文件。本版本不读取上游原生宿主的设置，包括 `HardwareBilinear`。
请勿将本 DLL 重命名为 `nvngx_dlssg.dll`，也不要用它替换游戏原有的 NVIDIA DLL。

若从最初的双组件 310.9.1 包升级，请将旧 `version.dll` 和 `dlssg3109` 文件夹
备份到游戏目录之外。新版本只需一个 DLL。

## 工作方式

代理内嵌未经修改的 NVIDIA 310.9.1 运行时和 SM86 内核资源。首次使用时，
运行时会自动解压到 `%LOCALAPPDATA%/DLSSG-SM86/<SHA256>/nvngx_dlssg.dll`，
通过校验后复用缓存。内核直接从 DLL 资源读取；损坏的缓存会被拒绝。
诊断日志为代理旁的 `dlssg3109.log`。

这一架构不同于上游的 310.1 原生宿主。上游的设置、性能数据及显卡路由不代表本版本。
安装本版本不会自动更改全局驱动设置或开启 DLSS 指示器。

## 游戏反馈与限制

以下反馈均来自同一台配备 **RTX 3070 Ti Laptop、8 GB 显存的笔记本电脑**，不能视为桌面显卡的测试结果。

| 游戏 | 用户反馈 |
|---|---|
| 黑神话：悟空 | X2 体验良好，X3 可以接受；X4 能运行，但流畅度体感较差。 |
| 幻兽帕鲁（Palworld） | 运行良好，包括 X4；X4 下画质明显下降。 |

这些是用户反馈，并非受控基准测试，也不保证所有配置均兼容。
显示帧率更高不一定意味着响应更快；也应比较运动中的伪影和帧间隔稳定性。
目前尚未确定所报告 X4 画面问题的具体原因。

**欢迎其他配置的用户提供反馈！** 请注明显卡、显存、笔记本或台式机型号、
驱动、游戏版本、输出分辨率及 X2/X3/X4 模式。使用 Neural Rendering 时，
请同时提供 NR 版本和 NR Cost Scaler 设置。除了 FPS，也请描述画质和响应体验，
最好在同一场景中比较。欢迎通过 [GitHub Issues](https://github.com/SilyNoMeta/dlssg_for_sm86/issues) 分享结果。

[查看《幻兽帕鲁》截图与 RHI 配置](GALLERY.zh-CN.md)：展示 NR 开启/关闭及完整/降低的 NR 处理分辨率。
所提供的游戏截图均显示 X2；尚未确认 Cost Scaler 的具体数值。

## 排障与卸载

若帧生成选项未出现，请检查 EXE 目录和 `dlssg3109.log`。修改文件前先退出游戏。
若日志报告缓存损坏，可将 `%LOCALAPPDATA%/DLSSG-SM86` 下对应的子目录移走，
下次启动时会重新创建。

卸载时，只移除本版本的 `version.dll`，并恢复此前备份的文件（如有）。
使用该缓存的游戏全部退出后，也可移除日志和 DLSSG-SM86 缓存。

报告问题时，请提供游戏、显卡、驱动和所选倍率；分享日志前请检查其中的个人路径。

## 版本与致谢

`310.9.1-1` 使用 310.9.1 运行时。DLL 校验值见 `SHA256SUMS.txt`。

感谢 [sdli1995](https://github.com/sdli1995/dlssg_for_sm86) 的原始项目和 SM86 工作。
另见[第三方声明](THIRD_PARTY_NOTICES.txt)。
