# DLL / ASI 安装 — 310.9.1-11

从[发布页](https://github.com/SilyNoMeta/dlssg_for_sm86/releases/tag/v310.9.1-11)下载 **dlssg-310.9.1-11-win64.zip**。需要可选面板时，使用 [包内可选 ReShade 面板](reshade-controls.zh-CN.md)。

关闭游戏并备份要替换的文件。仅将**一个**引擎与 `dlssg_sm86.ini` 放在实际游戏程序旁（《黑神话：悟空》：`b1/Binaries/Win64`），并在游戏中开启 DLSS FG。

| 方式 | 安装 |
|---|---|
| version 代理 | 直接放入我们的 `version.dll`；游戏必须加载该名称。 |
| DXGI 代理 | 将同一文件改名为 `dxgi.dll`，无需 ASI 加载器。 |
| Ultimate ASI Loader | 将 [UAL x64](https://github.com/ThirteenAG/Ultimate-ASI-Loader) 作为 `version.dll`，把我们的文件改名为 `dxgi.asi`。 |

这些名称使用相同引擎。INI 始终叫 `dlssg_sm86.ini`，放在引擎旁。不要把桥接文件改名为 `nvngx_dlssg.dll`。如果 ReShade 或其他模组占用代理名称，请选择空闲的加载方式；我们的 DXGI 代理转发到 Windows，不会自动串联其他 DXGI 模组。

UAL 可通过 `InitializeASI` 加载其他 ASI 文件名；隔离加载测试已验证 `dlssg_sm86.asi`。不调用此导出的加载器请使用 `dxgi.asi`。放在 ASI 子目录时，INI 也放在插件旁。REFramework 可保留自己的 `dinput8.dll`。

可选 `DLSSGControls.addon64` 与本 DLL/ASI 配合使用。升级前移除旧独立引擎 `DLSSG.addon64`。保留 ReShade 和无关 NR add-on，并仅安装一个 MFG 兼容引擎。

**从 FSR FG 切换到 DLSS FG？** 如果选项已改变但帧生成仍未启动，请保存 DLSS FG 选项，完全退出游戏后重新启动再测试。一次测试中重启恢复了帧生成；不保证无需重启即可切换帧生成提供方。

## 配置与验证

默认跟随游戏，`MaxInterpolatedFrames=5` 表示最高 X6，仍受插件能力限制。参见[控制、迁移、日志和遥测](live-controls.zh-CN.md)。手动编辑 INI 后重启；实时快捷键请使用 ReShade 面板。仅用 DLL 的快捷键在《黑神话：悟空》中失败，尚不能作为已验证的替代方案。原生动态需要兼容 DX12，固定控制可用于已识别 DX12/Vulkan 路径。

日志开启时，`proxy_attached`、`dxgi_attached` 或 `asi_attached` 标识加载，`installed_310_9_1` 标识运行库处理。`sl_native_dynamic_accepted` 仅表示 SDK 接受，并不证明驱动采用了目标。NVIDIA 全局或游戏级动态目标覆盖可优先。可用的 NVIDIA 水印可显示 `Dyn DRV` 和当前/最大倍率；本包不会自动开启水印。

加载成功不等于生成帧已经显示。回退时关闭游戏，仅移除本项目引擎并恢复备份。游玩不需要 CUDA toolkit 或编译工具。
