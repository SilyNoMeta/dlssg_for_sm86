# 实时控制与 INI 参考 — 310.9.1-11

统一 ZIP 包含 DLL/ASI 引擎及可选 ReShade 面板。不使用 ReShade 时，手动编辑 INI 并重启。将 `dlssg_sm86.ini` 放在引擎旁，先在游戏中开启 FG。RTX 20 尚无实体 Turing 测试，仍属实验支持。

## 默认快捷键与自定义

**已知限制：** 当前版本在《黑神话：悟空》的实机测试中，虽然成功读取了按键绑定，仅用 DLL 的快捷键仍未生效。自动化测试不能证明游戏中的按键检测有效。实时调整请使用 ReShade 面板；仅用 DLL 时请编辑 INI 后重启。下列语法说明已实现的接口，并不保证所有游戏都能识别快捷键。

默认使用 **Ctrl+F2 至 Ctrl+F6** 请求 X2–X6，**Ctrl+F10** 启用动态模式，
**Ctrl+F11** 跟随游戏，**Ctrl+F12** 恢复 INI 设置。可修改任意绑定，留空即禁用：

| 项目 | 操作 |
|---|---|
| `ForceX2` … `ForceX6` | 请求固定倍率，不超过 INI 和已加载插件的上限。 |
| `RestoreINI` | 恢复启动时读取的固定倍率、动态模式和目标帧率。 |
| `FollowGame` | 跟随游戏自己的选择，包括原生动态模式，忽略本项目的 INI 强制设置。 |
| `ActivateDynamicMFG` | 使用 INI 的 `DynamicTargetFPS` 请求原生动态模式，仅适用于兼容的 DX12 集成。 |

下一版压缩包的默认配置：

```ini
[Hotkeys]
ForceX2=Ctrl+F2
ForceX3=Ctrl+F3
ForceX4=Ctrl+F4
ForceX5=Ctrl+F5
ForceX6=Ctrl+F6
ActivateDynamicMFG=Ctrl+F10
FollowGame=Ctrl+F11
RestoreINI=Ctrl+F12
```

用 `+` 连接修饰键和**一个普通键**。名称不区分大小写，忽略名称前后的空格。
修饰键：`Ctrl`、`Alt`、`Shift`、`Win`。普通键：`F1`–`F24`、`A`–`Z`、`0`–`9`、
`Insert`、`Delete`、`Home`、`End`、`PageUp`、`PageDown`、`Space`、`Tab`、`Enter`、
`Escape`、`Up`、`Down`、`Left`、`Right`、`Backspace`、`Pause`。INI 中使用这些英文名称。
也接受两位十六进制 Windows 虚拟键码，例如 `0x41` 表示 A，参见
[Microsoft 虚拟键码表](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes)。
字母按 Windows 虚拟键处理，请根据自己的键盘布局检查结果。

修饰键必须完全匹配，`F8` 与 `Ctrl+F8` 不同。按住不会重复触发。
仅在游戏处于前台时工作；按住键切回游戏不会触发。无效组合会禁用；重复绑定会禁用
所有冲突项目。快捷键不会拦截游戏或其他工具的输入，因此请避开已有快捷键。
建议使用组合键；单个字母在游戏聊天或其他面板中输入时也可能触发。

修改绑定后重启一次。使用快捷键不会写回 INI；如果游戏定期提交 FG 选项，则不需要重启。

## ReShade 面板或快捷键

需要游戏内面板时，使用 **ReShade 控制包**，其中包含引擎 DLL 和 `DLSSGControls.addon64`。参见[面板指南](reshade-controls.zh-CN.md)。add-on 控制 DLL，并不替代 DLL。

面板分别提供 **Apply for this session**、**Apply & save settings** 和 **Save keyboard shortcuts**。成功保存会更新 INI 和本次运行所用的已保存设置。`RestoreINI` 恢复这些设置，不会重新读取手动编辑的文件。`ActivateDynamicMFG` 使用 INI 中保存的目标；若想通过该快捷键复用会话目标，请先保存。

请求在游戏下一次提交 Streamline FG 选项时应用。若一直等待，在游戏菜单应用一次 FG 设置。SDK 接受请求不代表驱动实际采用了目标或生成帧已显示。Vulkan 固定控制需要识别到 Streamline 路径；原生动态仅限兼容 DX12。直接 NGX 路径仍由游戏控制。面板不会修改 NR、Reflex、VSync 或 NVIDIA 配置。

## 设置生成帧数上限

`[FrameGeneration]` 中的 `MaxInterpolatedFrames` 表示**生成帧**数量。
加上一张渲染帧，就是显示的倍率。

| MaxInterpolatedFrames | 最高模式 |
|---|---|
| 1 | X2 |
| 2 | X3 |
| 3 | X4 |
| 4 | X5 |
| 5 | X6 |

缺省或无效时使用 **5**。已加载的插件仍可能限制最高倍率。
1 保留 X2 以及必需的兼容性与时序修正。
`ForceMultiplier` 仍使用显示倍率：`4` 请求 X4，`0` 跟随游戏。

**迁移：**将 `MaxMultiplier=M` 改为 `MaxInterpolatedFrames=M-1`。
例如 `MaxMultiplier=6` 改为 `MaxInterpolatedFrames=5`。旧键不再读取。
同时将 `[Hotkeys] DynamicMFG` 改名为 `ActivateDynamicMFG`。
保留 `[FrameGeneration]` 中、`DynamicTargetFPS` 旁的 `DynamicMFG`，它控制启动时的模式；
`ActivateDynamicMFG` 仅用于设置可选快捷键。

## 可选的源帧遥测

```ini
[Telemetry]
Enabled=1
```

默认 `0`；修改后重启。DLL 在约半秒的窗口内测量成功提交到 Streamline 的不同源帧，
同一帧的重复调用只计一次。这是 CPU 提交速率，不是 GPU 完成速率或输入延迟。
过时或存在歧义的数据不会显示。没有拦截 Streamline 常量的直接 NGX 集成不受支持。

OptiScaler 需要包含 [PR #1156](https://github.com/optiscaler/OptiScaler/pull/1156) 的构建；发布时该 PR 仍待上游审核。此 ZIP 不附带修改版 OptiScaler。仅启用 INI 键不能让旧版本读取接口。支持后，第二个 FPS 数字使用源帧速率；由 OptiScaler 管理的 FG 后端仍使用原显示路径。ReShade 面板也能独立显示该速率。[计数器配置](standalone-reshade.zh-CN.md)。

## 关闭本项目日志

```ini
[Logging]
Enabled=0
```

修改后重启。默认是 `1`；`0` 停止创建或追加 `dlssg3109.log`，但保留已有文件。
因此旧日志存在并不代表仍在记录。其他工具或 NVIDIA 的日志不受影响。
收集问题报告前请重新开启日志。

## 动态目标与 INI 不一致？

除普通 FPS 限制和 VSync 外，还应检查 NVIDIA 全局和游戏配置中的
**DLSSG 动态目标覆盖设置**。它们是不同选项。即使 Streamline 接受了请求，
驱动覆盖仍可能更改目标。修改前备份配置，只调整相关覆盖项，不要重置无关设置。


开启日志时，`hotkey_bindings_loaded` 表示有效绑定数量。`hotkey_action_triggered=0` 对应 ForceX2（1–4 对应 X3–X6）。`live_multiplier_requested` 表示请求已排队，`sl_forced_multiplier_accepted` 表示 Streamline 已接受；仍需检查实际输出帧。若只绑定 F4，在 `[Hotkeys]` 中填写 `ForceX2=F4` 并重启。
