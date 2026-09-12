# 时间正确性与已集成优化

## 310.9.1-10：同一引擎，两种安装方式

两个包均包含相同的 NVIDIA 310.9.1 运行库和已修正多架构内核包。DLL 是已测试的常规引擎；独立 add-on 将该引擎与 ReShade 面板链接。SM86 内核保持与 -9 相同，增加同一 FP16 模型的 SM89 编译及实验性 SM75 路径，尚无实体 Turing 验证。下方历史章节对应各自原始版本，并非新的性能测量。

实时请求在游戏下一次 Streamline 选项提交时应用。设置保存与快捷键保存独立；文件替换失败时保留旧文件及状态。Record 使用 ReShade 自己的输入 API，因为菜单捕获键盘时会屏蔽普通 Win32 按键轮询。

Streamline 接受的目标仍可能被 NVIDIA 全局/游戏级动态目标覆盖。用户确认移除该覆盖后，《黑神话：悟空》的目标切换恢复正常。本 add-on 不会自动重置 NVIDIA 配置。

遥测测量约半秒内成功提交的不同源帧，而非 GPU 完成速率或延迟。[OptiScaler PR #1156](https://github.com/optiscaler/OptiScaler/pull/1156) 添加读取端，发布时仍待审核。[控制指南](live-controls.zh-CN.md) · [验证范围](validation-summary.json)。

## -9 及更早版本的历史记录


2026-09-11 · 310.9.1-9 · [English](research.en.md) / [Français](research.fr.md) / [简体中文](research.zh-CN.md)

## -9 新增：更高倍率与原生 Dynamic MFG

提供程序上限可配置为五张生成帧，即总倍率 X6。同一时间修正按 t=i/(n+1)
放置第 i 张生成帧，也适用于 X5/X6。提高上限不会扩展旧版 Streamline 插件
中的数组；固定覆盖仍受已识别插件版本及其报告能力的限制。

原生 Dynamic MFG 使用 Streamline 的 eDynamic 选项及目标帧率，不另建帧呈现
调节循环。启用需要已知 ABI、本项目适配的提供程序、DX12 和肯定的动态能力
报告。游戏关闭 FG 时仍保持关闭。动态不可用或被拒绝时，可在支持范围内回退
到所配置固定倍率。游戏已选择的原生动态模式会被保留。

### 为什么报告了支持，却仍未启用？

游戏可能在视图 0 调用 GetState，却在视图 1 调用 SetOptions。最初实现将系统
能力存于每个视图中，导致第二个视图等待第一个视图已经获取的能力。修复后跨
视图共享系统能力，但帧呈现计数、fence 和启用状态仍各自独立。提供程序、设备
或 API 变化，以及成功关闭时，能力缓存被清空；后来的明确否定报告覆盖此前的
肯定结果。版本化副本保护旧结构体，也不会额外调用 GetState 消耗游戏的呈现计数。

### 此二进制文件的验证依据

- 213 项控制/ABI 断言，包含旧版 Options/State 缓冲区保护。
- 16 个 DX12/Vulkan 固定倍率 GPU 用例，覆盖 X5/X6 及优化开关。
- 10 个真实 Streamline 场景，包含初始实现的预期失败对照和修复后的能力共享。
- 四组 Vulkan X2–X6 切换序列，每组仅显式创建一次 feature；合成测试图中的
  时间位置误差小于 0.403 像素。
- RTX 3070 Ti Laptop 8 GB、驱动 616.92 上的游戏内功能报告：自动 X3/X4/X5
  切换、动态水印以及被接受的 130 FPS 目标请求。

该报告不提供新的 FPS/延迟基准或长时间稳定性结果。Vulkan 切换用例检查图像
内容，不检查 swapchain 呈现或内部内存分配成本。Streamline 2.14.1 在 Vulkan
下报告不支持原生动态，这与 [NVIDIA 指南](https://github.com/NVIDIA-RTX/Streamline/blob/v2.14.1/docs/ProgrammingGuideDLSS_G.md#63-enabling-dynamic-multi-frame-generation)
一致。本版本未包含独立的 Vulkan 自适应控制器。

控制设计参考了 [mavismmg / ImDreamt 的 MFGAdaUnlock-RenoDx](https://github.com/mavismmg/MFGAdaUnlock-RenoDx)，
固定提交为 7e613b2aadffe936f2ea19df9c71931bbbbae2e6。发行包保留其 MIT 署名及
Streamline 头文件声明。

以下章节保留此前时间修正和加载测试的历史范围，不代表已重新测量 -9 的所有配置。

## 观察与假设

[Issue #2](https://github.com/SilyNoMeta/dlssg_for_sm86/issues/2) 报告 RTX 3060 Ti 8 GB 在 X4
虽有 160–170 FPS，却不够流畅。维护者在悟空中也发现类似现象。
假设是生成图像的内容未按正确时间推进，而非单纯帧数不足。

测试使用 640×360 场景，每张真实图像水平移动 8 像素，运动向量已知、深度固定。
红色渐变提供独立于参考 DLL 的位移测量。首帧重置历史并排除计分，随后测量三组，
避开边缘、渐变回绕和 UI。

| X4 来源 | 生成 1 | 生成 2 | 生成 3 |
|---|---:|---:|---:|
| 预期 | 2 px | 4 px | 6 px |
| 原生 310.1，HardwareBilinear=1 | ~2 px | ~4 px | ~6 px |
| 旧 310.9.1 基线 | ~4 px | ~4 px | ~4 px |
| 修正后的 310.9.1-7 | ~2 px | ~4 px | ~6 px |

旧输出并非完全相同的字节副本：哈希不同，但运动都停留在中点附近。
此前参考路径使用相同的 MFG 解锁方式，可能共享缺陷。因此哈希一致性检查和更高的
FPS 都不足以证明独立的时间正确性或流畅度。

## 原因与修正

本 SM86 适配所用的 SM89 PTX，在 `Kernel_EstimateIntermMvecsScatter`（k46）中
有 104 次将运动向量乘以 0.5 的操作。仅解锁主机端生成帧数，并不会让这些操作使用
正确的逐帧时间。对生成索引 i、生成数量 n，t=i/(n+1)：修正将前 52 个因子替换为
1−t，后 52 个替换为 t。半像素坐标偏移保持不变。实现参考 Michael Robles 的
[RTX40MFG-Unlock 修正](https://github.com/dashdogy/RTX40MFG-Unlock/blob/cf99204a00ce015a24c4c2be4082170b65e2fed1/source/native/midpoint_fix.cpp)（MIT），并验证输入代码的准确身份。

每个包含 148 个键的内核包仅修改一个键。参考包和优化包均包含此修正，INI 无法关闭。
X2 的 t=0.5，因此关闭全部优化时，修正后的 X2 输出与旧基线逐字节一致。
模型、权重和 FP16 精度没有降低。

## 验证范围与限制

-7 的时间修正在 RTX 3070 Ti Laptop 8 GB、驱动 616.92 上检查了 52 个离线 GPU 用例：49 个预期成功，
3 个用于发现旧版 X3/X4 缺陷的预期失败，其中包含 UI 场景。覆盖 DX12/Vulkan X4
的全部 16 种 INI 组合、两种 API 下全开/全关的 X2/X3、1280×720、向左移动和
HUDLess/UIAlpha。相同配置的修正版 DX12/Vulkan 输出逐字节一致。
位移容差为 0.5 像素，因为 RGBA8 量化使 X3 三等分位置即使在原版中也有约 0.34 像素
误差；旧缺陷约为 X3 1.33 像素、X4 2 像素。还检查了内嵌资源、冷/并发/热缓存和
损坏缓存拒绝。[结构化验证摘要](validation-summary.json)。

离线测试不测量游戏呈现，也不覆盖所有遮挡、摄像机运动、UI 格式和游戏集成。
随后所有者确认，该 -7 二进制文件在悟空 X4 中明显更加流畅。
本发布版本的 Vulkan 游戏测试仍待确认。
悟空基准图表的白色矩形仍存在，合成 UI 场景未复现，因此不声称本次修复了该症状。

## DLL 中包含的优化

| INI 选项 | 机制 | 结果与限制 |
|---|---|---|
| HardwareBilinear | k60 最终重建使用硬件采样，参考原项目 [HardwareBilinear](https://github.com/sdli1995/dlssg_for_sm86/blob/5f62ff44a9c08f9841fa605e7b7160f79ccd2c40/docs/NATIVE_INI.md)。 | 可能有细微像素差异；先前用户感知提升很小，不保证整体提升。 |
| Conv13SharedInput | 在共享内存复用 k13 的 FP16 输入。 | 已测试情形保持算术结果；不能单独归因游戏 FPS 收益。 |
| Conv0SharedInput | k0 使用共享输入邻域，保留 Tensor Core 运算顺序。 | 一次同步独立测试为 0.792384→0.698168 ms（−11.89%）；完整 1440p X4 测量接近无变化。 |
| ResidualVectorLoads | k5/k11 使用协作向量读取，保留运算和屏障。 | 独立测试分别为 −2.84% / −6.20%；整体运行时间变化小且不一致。 |

这些内核测试早于时间修正，代表特定工作负载下的局部开销，不代表 -7 的游戏 FPS 提升。
此前输出等价测试有助于验证优化算术，但不足以验证 MFG 运动。本版本不含 FP8、INT8、
LZ4 或更小神经网络。比较选项时始终使用同一修正路径，并在每次修改后重启游戏。

## 加载 DLL 不等于启动桥接

原始 -7 二进制文件仅在名称为 `version.dll` 时自动启动。ASI 加载器可以成功加载
重命名后的 DLL，但桥接仍未初始化。这个问题与 X3/X4 时间插值错误是独立缺陷。

-8 在同一个二进制文件中提供统一且幂等的入口：`version.dll` 转发版本信息函数；
`dxgi.asi` 在加载时启动，同时导出 `InitializeASI`；`dxgi.dll` 转发真实的
Windows DXGI 导出函数。Ultimate ASI Loader 也会为其他名称的 `.asi`
调用 `InitializeASI`，因此启动不再依赖 `dxgi.asi` 这个特殊文件名。

使用 UAL 时，`version.dll` 是加载器，`dxgi.asi` 是桥接文件，两者不同。
只应安装一份桥接文件。配置始终使用桥接文件旁的 `dlssg_sm86.ini`，不随名称改变。

DXGI 代理通过系统目录的绝对路径加载真实库，避免递归加载自身。转发保留
整数、浮点和栈参数，直接返回 Windows COM 对象。真实 DXGI 延迟到首次导出
调用时加载，在本项目的 `DllMain` 之外执行；Microsoft 指出
[在 DllMain 中创建 factory 会失败](https://learn.microsoft.com/en-us/windows/win32/api/dxgi/nf-dxgi-createdxgifactory)。
模块句柄通过原子操作发布，处理首次并发调用且不累积多余引用。
导出名称和序号与测试系统比较，实际 factory 创建另行验证。

**-8 压缩包只提供一个 `version.dll`，改名即可使用这些模式。**
20 个 DXGI 导出、三种 factory API、首次并发调用、静态导入、版本函数转发
和真实 UAL 启动均通过自动检查。四个 X4 用例（DX12 下三种文件名及 Vulkan
下 `dxgi.dll`）中，每个用例的 12 张输出均与标准 -7 逐字节一致。
随后用户在 RTX 3070 Ti Laptop 8 GB 上确认 `dxgi.dll` 在悟空中正常工作。
这是功能验证，不是新的 FPS 基准，也不代表所有游戏均已验证。
仅出现启动日志并不能证明游戏正在显示生成的帧。

## 两种图形 API，共用同一组内核

两个后端均保留 310.9.1 的宿主计算图和权重。DX12 拦截 NvAPI 计算内核创建，
Vulkan 适配 NVX CUDA 模块创建及启动调用。两者都使用同一组修正内核包中的
已验证 SM86 映像。API 适配方式不同，神经网络运算和时间修正保持一致。
运动、深度资源与帧呈现仍由游戏提供；重命名 DLL 不能补上游戏缺失的集成，
也不会增加 DX11 后端。

## 可追溯性

-9 `version.dll` SHA256：`114004043035c3f8f91b1b8909bdb8b7e68fa36394aeb339c339e30042684561`。
这就是获得本次游戏内动态验证的二进制文件，未重新构建。内嵌运行库与两个修正
内核包均与 -8 相同；新增工作在于宿主端帧生成控制与能力处理。改名不会改变
哈希。以上点名游戏的历史结果仍归属于其原始版本。-0 至 -6 已撤下。
发行包仅附公开技术摘要，不包含开发日志或测试程序。参见[验证范围](validation-summary.json)。
