# 适用于 SM86 的 DLSSG 310.9.1

[English](README.md) | 简体中文 | [Français](README.fr.md)

面向 NVIDIA SM86 显卡的实验性 DLSS 帧生成 **310.9.1** 适配版本，基于
[sdli1995/dlssg_for_sm86](https://github.com/sdli1995/dlssg_for_sm86) 的工作。
安装时只需复制一个文件：**`version.dll`**。


**推荐从这里开始：[310.9.1-6 — DX12 + Vulkan + 可配置优化](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/download/v310.9.1-6/dlssg-sm86-310.9.1-6-win64.zip)。**
一个 `version.dll` 包含两种 API 路径和全部四项已发布优化。
ZIP 内含可选的 `dlssg_sm86.ini`，四项优化默认全部开启。
下方配置可重现此前版本的内核组合，无需反复替换 DLL。
本版本仍为实验预发布；版本号更高不保证 FPS 更高。

## 选择版本

所有版本均使用 DLSSG 310.9.1，只需安装一个 `version.dll`。
**请在相同场景中尝试各版本，保留最适合自己的版本。**
版本号更高并不保证 FPS 更高或体验更好。

| 版本 / 下载 | 主要区别 | 预期效果 |
|---|---|---|
| [310.9.1-0](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-0) | 基础版本，手动双线性插值。 | 用于对比图像重建效果。 |
| [310.9.1-1](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-1) | 最终重建使用硬件双线性过滤。 | 可能存在细微像素差异；用户反馈有小幅改善。 |
| [310.9.1-2](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-2) | 包含 `-1`，并在一个卷积中复用 FP16 输入。 | 一位用户已在游戏中试用；未报告明显画面问题，性能改善难以判断。 |
| [310.9.1-3](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-3) | 包含 `-2`，并在第二个重建卷积中复用 FP16 输入。 | 离线图像与 `-2` 一致；尚未确认 GPU 总耗时有稳定改善。 |
| [310.9.1-4](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-4) | 包含 `-3`，并在两个残差卷积中使用向量化输入读取。 | 离线图像与 `-2` 一致；GPU 总耗时变化较小且存在波动。 |
| [310.9.1-5](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-5) | 使用 `-4` 内核，通过可选 INI 开关控制四项优化。 | 默认图像处理路径与 `-4` 相同，便于对比此前版本的内核组合。 |
| [310.9.1-6](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-6) | **统一 DirectX 12 + Vulkan**，提供四项 INI 开关。 | 推荐起始包；默认内核与 `-4`/`-5` 相同，新增 Vulkan 路径。 |

双线性优化借鉴原项目的 [HardwareBilinear](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff44a9c08f9841fa605e7b7160f79ccd2c40/docs/NATIVE_INI.md) 选项，与 `-0` 相比可能出现轻微像素差异。
后续内存读取优化保留 FP16 运算。**这些发布版本均未使用 FP8 或 INT8。**

目前测试设备为一台 **RTX 3070 Ti Laptop、8 GB 显存的笔记本**，驱动 616.92。
早期 DX12 版本已有《黑神话：悟空》和《幻兽帕鲁》的用户反馈。
相同 Vulkan 实现与内核的诊断预览版已有《无人深空》X2/X3/X4 成功运行反馈。
该预览版额外记录诊断日志。跨版本受控游戏基准测试仍在进行，不承诺整体性能提升。

更换 DLL 或设置前请退出游戏。在相同设置下比较画质、响应、流畅度和 FPS。

### 可选配置（`-5` / `-6`）

将 `dlssg_sm86.ini` 放在 `version.dll` 旁，将值设为 `1`（开启）或 `0`（关闭），
然后完全重启游戏。没有 INI 文件或缺少某项设置时，该项默认开启。
这是本桥接实现的配置，不会读取原项目原生宿主的 INI。

```ini
[Optimizations]
HardwareBilinear=1
Conv13SharedInput=1
Conv0SharedInput=1
ResidualVectorLoads=1
```

| 选项 | 作用 |
|---|---|
| `HardwareBilinear` | 最终重建使用硬件双线性过滤，可能出现细微像素差异。 |
| `Conv13SharedInput` | 在共享内存中复用一个卷积的 FP16 输入。 |
| `Conv0SharedInput` | 在第二个重建卷积中复用 FP16 输入。 |
| `ResidualVectorLoads` | 在两个残差卷积中使用向量化输入读取。 |

INI 对两种 API 的优化均有效。DX12 或 Vulkan 由游戏选择，INI 不提供 API 切换。
这些开关不选择 X2/X3/X4，也不控制独立的 Neural Rendering / NR Cost Scaler 模组。

用于对比的内核组合（图像处理路径相同，但 DLL 文件本身不同）：

| 配置 | HardwareBilinear | Conv13SharedInput | Conv0SharedInput | ResidualVectorLoads |
|---|---:|---:|---:|---:|
| `-0` | 0 | 0 | 0 | 0 |
| `-1` | 1 | 0 | 0 | 0 |
| `-2` | 1 | 1 | 0 | 0 |
| `-3` | 1 | 1 | 1 | 0 |
| `-4` | 1 | 1 | 1 | 1 |

实际分发的 DLL 已重新通过两种 API 的离线检查，包括全部 16 种 INI
组合和附带的 INI 文件。Vulkan X2/X3/X4、历史重置与恢复以及 DX12 对比均通过。
输出图像与各自参考路径一致，加载和缓存检查也已通过。
这些检查不保证所有游戏兼容，也不代表 FPS 一定提高。

## 运行要求

- Windows x64、Direct3D 12 或原生 Vulkan 游戏，以及提供 NGX 和所需 API 扩展的 NVIDIA 驱动。
- SM86 显卡（GeForce RTX 30 系列）。已在配备 RTX 3070 Ti Laptop（**8 GB 显存**）的笔记本上使用 616.92 驱动测试；该驱动版本不是最低版本要求。
- 游戏须集成 DLSS 帧生成，并能够加载 `version.dll` 代理。
- X2、X3、X4 是否可选取决于游戏提供的选项。
- 游玩时无需安装 Python 或 CUDA Toolkit。

`-6` 提供 DirectX 12 和原生 Vulkan 路径；此前 `-0` 至 `-5` 包仅支持 DX12。
Vulkan 游戏或其集成层必须已提供 NGX 帧生成输入、所需扩展和图像呈现调度。
仅复制本 DLL 不能为任意 Vulkan 游戏添加帧生成。
本版本未支持或验证 DX11、Linux/Proton、DXVK、SM75/RTX 20 及其他代理文件名。
自定义 Vulkan 函数解析路径仍待验证。


## 安装与更新

### 新手推荐：RHI 与 ShortFuse 工具

**推荐新手使用 [RHI — ReShade HDR Installer](https://github.com/RankFTW/RHI)**
安装和管理配套工具。RHI 的 DLSS 管理界面提供 ShortFuse DLSS Tool 和 NR Cost Scaler。
请按 RHI 针对游戏的说明操作，然后按下方步骤安装本版本的 `version.dll`。

根据测试用户对早期版本的反馈，这些版本与
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
3. 将本版本的 `version.dll` 复制到实际负责渲染的 EXE 旁。对于《黑神话：悟空》，路径为 `b1/Binaries/Win64`，与 `b1-Win64-Shipping.exe` 同目录。《无人深空》使用 `Binaries`，放在 `NMS.exe` 旁。
4. 启动游戏并启用 DLSS 帧生成。建议先使用 X2，再在同一运动场景中比较 X3/X4。

`-5` 和 `-6` 支持可选 INI；请参阅上方配置说明。不会读取原项目原生宿主的 INI。
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
| 无人深空（Vulkan） | 此 Vulkan 路径的诊断预览版已有 X2/X3/X4 成功反馈；该笔记本上的 FPS 提升幅度有限。 |

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

Vulkan 日志中的 `vulkan_backend_active` 与 `vulkan_kernel_launches` 可确认
后端执行，但不是显示 FPS 测量。Toxic Commando 尚未验证。
反馈时请说明实际使用的 API 及帧生成选项是否可用。

若帧生成选项未出现，请检查 EXE 目录和 `dlssg3109.log`。修改文件前先退出游戏。
若日志报告缓存损坏，可将 `%LOCALAPPDATA%/DLSSG-SM86` 下对应的子目录移走，
下次启动时会重新创建。

卸载时，只移除本版本的 `version.dll`，并恢复此前备份的文件（如有）。
使用该缓存的游戏全部退出后，也可移除日志和 DLSSG-SM86 缓存。

报告问题时，请提供游戏、显卡、驱动和所选倍率；分享日志前请检查其中的个人路径。

## 版本与致谢

`310.9.1-6` 使用 310.9.1 运行时。DLL 校验值见 `SHA256SUMS.txt`。

感谢 [sdli1995](https://github.com/sdli1995/dlssg_for_sm86) 的原始项目和 SM86 工作。
另见[第三方声明](THIRD_PARTY_NOTICES.txt)。
