# 幻兽帕鲁：DLSSG、Neural Rendering 与 RHI

[English](GALLERY.en.md) | 简体中文 | [Français](GALLERY.fr.md) · [安装说明](README.zh-CN.md)

用户在配备 **RTX 3070 Ti Laptop、8 GB 显存的笔记本电脑**上提供的截图。
游戏顶部显示 **DLSSG 310.9.1、D3D12、X2**；可见的 NR 指示器显示 **DLSSNR 310.8.0**。
帧生成与 Neural Rendering 是独立组件，版本号也各自独立。

这些截图展示两者同时运行及画面差异，并非受控基准测试：镜头、动画和特效会变化。
静态截图不能证明运动流畅度或 FPS。DLSSG 横幅中的 `224Hz` 不是 FPS 测量值。

## NR 开启，完整处理分辨率

NR 指示器显示 `ON | 2560x1440`。这是所提供截图中较清晰的完整分辨率 NR 示例；
画面没有显示 Cost Scaler 开关的状态。

![幻兽帕鲁中 DLSSG 310.9.1 X2 与 DLSSNR 310.8.0 ON，NR 分辨率为 2560x1440](screenshots/palworld-nr-full.png)

## NR 开启，降低处理分辨率

NR 指示器显示 `ON | 1484x834`，说明 NR 处理分辨率降低。
用户记得曾将 NR Cost Scaler 设为约 `0.50`，但截图中无法看到具体数值，
因此不将此图标注为已确认的 `0.50` 测试。

![幻兽帕鲁中 DLSSG X2 与 NR ON，NR 分辨率为 1484x834](screenshots/palworld-nr-reduced.png)

## 用户对比中的 NR 关闭状态

NR 指示器不再显示，而 DLSSG 310.9.1 X2 仍然可见。
用户将此图作为关闭 NR 的对比。镜头与前两张相近，但并非完全相同。

![幻兽帕鲁中未显示 NR 指示器，DLSSG X2 仍然可见](screenshots/palworld-nr-off.png)

## Palworld 的 RHI 配置

面板选中了 **DLSS Tool (ShortFuse)**，并将 **NR Cost Scaler** 标记为已安装。
没有显示 Cost Scaler 的具体数值。这是管理器中的设置；上文列出的实际运行版本
来自游戏内指示器。尤其不能把 RHI 显示的 NR `0.0.0` 当作游戏中实际使用的 NR 版本。

![RHI 的 Palworld 配置，显示 DLSS Tool ShortFuse 和已安装的 NR Cost Scaler](screenshots/rhi-palworld.jpg)

安装时可从 [RHI](https://github.com/RankFTW/RHI) 入手。欢迎为该项目及
[ShortFuse 的 RenoDX](https://github.com/clshortfuse/renodx) 点亮 GitHub Star ⭐，支持作者。
