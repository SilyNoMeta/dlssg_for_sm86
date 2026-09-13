# ReShade 控制面板 — 310.9.1-11

安装 **version.dll + DLSSGControls.addon64 + dlssg_sm86.ini**，并使用支持完整 add-on 的 ReShade。统一 ZIP 已包含这三个项目文件。DLL 提前加载兼容性引擎，小型 add-on 提供界面。仅安装面板无法解锁 FG。

关闭游戏并备份要替换的文件。若安装过本项目旧 **DLSSG.addon64**，请移除它；保留 ReShade 和其他 NR add-on。仅保留一个引擎。INI 始终放在引擎旁，即使 ASI 加载器使用子目录。

ReShade 使用 `dxgi.dll` 时，本项目引擎可使用 `version.dll`，此组合无需 Ultimate ASI Loader。名称冲突或 ASI 安装方式请参见[加载指南](install-loaders.zh-CN.md)。不再推荐独立引擎包，因为部分游戏在 ReShade 加载 add-on 前已初始化 DLSS。

## 生成设置

先在游戏中启用 FG，再打开 ReShade 的 **DLSSG Live Controls**。
选择已保存设置、跟随游戏、固定倍率或动态 MFG。原生动态模式需要兼容的 DX12 集成。

- **Apply for this session**：仅应用到当前运行。
- **Apply & save settings**：应用并把模式和目标 FPS 保存到 dlssg_sm86.ini，下次启动仍有效。
- 已接受表示最后一次 SDK 提交，不代表测量到了瞬时动态倍率。如果一直等待，
  在游戏 FG 菜单中应用一次设置。
- 默认跟随游戏，不强制目标 FPS，也不绑定默认快捷键。

## 快捷键

在下方点击操作旁的 **Record**，按下 Ctrl+Alt+F8 等组合键。Escape 取消录制。
也可直接编辑文本；清空表示禁用。点击 **Save keyboard shortcuts** 保存并立即启用，
无需重启。此按钮不保存生成设置。无效组合或重复快捷键会被拒绝，不会部分写入。
录制或编辑时暂停现有快捷键；按住的键需要释放后才能再次触发。

修饰键为 Ctrl、Alt、Shift、Win。支持 F1–F24、A–Z、0–9，以及
Insert/Delete/Home/End/PageUp/PageDown/Space/Tab/Enter/Escape、方向键，或 Windows
虚拟键码 0xNN。录制不常见的键时会使用虚拟键码。

## INI

MaxInterpolatedFrames 是唯一上限键：1..5 对应 X2..X6，默认 5。
ForceMultiplier 使用显示倍率：0 跟随游戏，2..6 强制 X2..X6。
[FrameGeneration] 的 DynamicMFG 和 DynamicTargetFPS 控制启动设置；
[Hotkeys] 的 ActivateDynamicMFG 仅定义快捷键。
四个优化开关、倍率上限、日志和遥测仍需编辑 INI 后重启。
面板保存会保留其他节，并通过临时副本替换文件；写入失败时保留旧文件及运行设置。

## 仅测试 OptiScaler 计数器

使用包含 [PR #1156](https://github.com/optiscaler/OptiScaler/pull/1156) 的 OptiScaler 构建。发布时该 PR 仍待审核，本包不附带修改版 OptiScaler，仅改 INI 不会更新旧版。先设置 **FG Output = None**，再设置
**FG Input = None**，保持游戏内 FG 开启。不要为显示计数器选择 Nukem's 等替代引擎。

1. 本项目 INI 中设置 [Telemetry] Enabled=1，保存并重启。
2. 展开 OptiScaler 右侧 **FPS Overlay**。
3. 勾选 **FPS Overlay Enabled**，选择 **Overlay Type = Simple**。
4. 点击 **Save Settings**；如果后端改动仍在等待，重启游戏。

观察两个 FPS 数字及 **DLSSG source telemetry** 标签。第二个数字是 CPU 源帧提交速率，
第一个仍为 OptiScaler 原有计数器。设置窗口底部的图表不是这个 overlay。
动态模式不能简单除以配置的最大倍率。没有第二个数字表示数据缺失、过时、歧义或
未观察到支持的集成，不表示零 FPS。数据有效时，本项目面板也可显示源帧速率。

## 验证范围

使用 ReShade 6.8.0 验证独立加载与两次设备生命周期，设置持久化、写入错误和快捷键冲突检查通过。真实 Streamline DX12/Vulkan 命令测试通过，但这些命令测试不显示生成帧。原生动态仅限 DX12；界面测试中的 DX11 主机不代表支持 DX11 FG。用户在 RTX 3070 Ti Laptop 8 GB 的《黑神话：悟空》中确认独立控制、按键录制和动态目标切换正常。这不是性能基准或所有游戏验证。RTX 20 仍属实验支持。

## 动态目标与保存设置

NVIDIA 全局或游戏级 **Override DLSSG Target Frame Rate** 可覆盖面板目标。禁用相关覆盖并重启，才能由面板控制。普通 FPS 限制器与 VSync 是不同设置。动态快捷键使用 INI 中保存的目标；用 Apply & save settings 保存后才能通过快捷键复用。参见 [INI 参考](live-controls.zh-CN.md)。

## DLSS 渲染分辨率

[DLSS 渲染分辨率](super-resolution.zh-CN.md)
