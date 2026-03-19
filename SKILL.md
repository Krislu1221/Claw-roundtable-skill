# RoundTable Skill - 多 Agent 深度讨论系统

## 📋 技能说明

RoundTable 是一个多专家 Agent 讨论系统，模拟真实的圆桌会议场景。每个 Agent 从不同专业角度（技术、体验、测试等）提供独立观点，经过 5 轮深度讨论后形成完善的方案。

### 版本
**0.9.0** - 基于真实测试优化（2026-03-19）

### 作者
Krislu <krislu666@foxmail.com>

### 核心价值
- **深度讨论**：5 轮渐进式讨论（R1-R5）
- **多专家视角**：工程专家 + 体验专家 + 测试专家
- **质量保证**：相互引用、批判思维、辩论完善
- **用户友好**：实时进度通知、完整报告输出

### 触发词
说出以下任意词汇即可激活 RoundTable：
- `RoundTable`
- `圆桌会议`
- `圆桌讨论`
- `多 Agent 讨论`
- `多专家讨论`
- `深度讨论`

### 适用场景
✅ 技术方案设计
✅ 架构决策评估
✅ 代码审查
✅ 产品方案讨论
❌ 简单问题查询
❌ 需要立即回答

---

## 🚀 快速开始

### 基础用法

**中文**:
```
请你 RoundTable 讨论一下：智能待办应用技术方案
```

**英文**:
```
Please RoundTable this topic: Smart Todo App Technical Architecture
```

**代码方式**:
```python
from roundtable_engine import RoundTableEngine

# 创建引擎
engine = RoundTableEngine("智能客服系统技术方案")

# 运行（自动发送确认和进度通知）
success = await engine.run("user_channel")
```

### 完整示例

```python
import asyncio
from roundtable_engine import RoundTableEngine

async def main():
    # 创建 RoundTable 引擎
    engine = RoundTableEngine(
        topic="智能客服系统技术方案",
        mode="pre-ac"  # pre-ac: AC 前讨论，post-ac: AC 后审查
    )
    
    # 运行完整流程
    # user_channel: 用户通知渠道（飞书聊天 ID 等）
    success = await engine.run("user_channel")
    
    if success:
        print("🎉 RoundTable 成功完成！")
    else:
        print("❌ RoundTable 被取消或失败")

asyncio.run(main())
```

---

## ⚙️ 配置说明

### 统一配置

```python
# 所有轮次统一配置
TIMEOUT_SECONDS = 300  # 超时时间（5 分钟，最大允许时间）
MAX_RETRIES = 2        # 超时重试次数
MODE = "quality"       # 质量优先，非速度优先
```

### 轮次说明

| 轮次 | 名称 | 参与 Agent | 说明 | 预计耗时 |
|------|------|-----------|------|---------|
| **R1** | 独立方案 | 工程/体验/测试专家 | 各自阐述观点 | 3-5 分钟 |
| **R2** | 相互引用 | 工程/体验/测试专家 | 引用他人 + 补充 | 3-5 分钟 |
| **R3** | 深度分析 | 工程/体验/测试专家 | 批判思维 + 评价 | 5-8 分钟 |
| **R4** | 辩论完善 | 工程/体验/测试专家 | 辩论 + 完善方案 | 5-8 分钟 |
| **R5** | 总结报告 | Host（主持人） | 汇总所有结论 | 3-5 分钟 |
| **总计** | - | - | - | **15-30 分钟** |

---

## 📬 通知机制

### 1. 确认请求

```
🔄 RoundTable 多 Agent 深度讨论

讨论主题：智能客服系统技术方案

📋 讨论说明：
- 参与 Agent：工程专家 + 体验专家 + 测试专家
- 讨论轮次：5 轮深度讨论（R1-R5）
- 预计耗时：15-30 分钟
- 输出内容：完整技术方案 + 多方观点 + 行动建议

⚠️ 请注意：
- RoundTable 适合需要深度分析的场景
- 如果您需要快速回答，请使用普通对话
- 讨论过程中您可以随时查看进度

请确认您的需求：
回复"确认"开始 RoundTable 深度讨论
回复"快速"获取简要方案（<1 分钟）
```

### 2. 开始通知

```
🚀 RoundTable 已启动

主题：智能客服系统技术方案
状态：R1 轮讨论中（1/5）
参与：工程专家 · 体验专家 · 测试专家
预计：15-30 分钟

您可以在讨论过程中随时查看进度，
完成时会收到最终报告通知。
```

### 3. 进度更新（每轮完成）

```
📊 RoundTable 进度更新

当前：R2 轮完成（2/5）
进度：████████░░░░░░░░ 40%
已完成：工程专家，体验专家，测试专家
已耗时：8.5 分钟
预计剩余：12-20 分钟

点击查看当前讨论内容 →
```

### 4. 完成通知

```
✅ RoundTable 讨论完成

主题：智能客服系统技术方案
总耗时：23.5 分钟
讨论轮次：R1-R5（完整 5 轮）
输出内容：技术方案 + 安全建议 + 体验优化

📄 查看完整报告：
http://localhost:8080

[打开报告] [下载 PDF] [分享给团队]
```

---

## 🔧 高级用法

### 自定义通知渠道

```python
from roundtable_notifier import RoundTableNotifier

notifier = RoundTableNotifier("讨论主题")

# 发送确认请求
confirmed = await notifier.send_confirmation_request("feishu_chat_id")

# 发送进度更新
await notifier.send_progress_update(
    user_channel="feishu_chat_id",
    round_num=2,
    completed_agents=["工程专家", "体验专家"]
)

# 发送完成通知
await notifier.send_completion_notification(
    user_channel="feishu_chat_id",
    report_url="http://localhost:8080"
)
```

### 并行执行优化

```python
# RoundTable 引擎默认并行执行所有 Agent
# 实际执行时间 = max(Agent1, Agent2, Agent3)
# 而非串行执行时间 = Agent1 + Agent2 + Agent3

# 示例：
# 工程专家 (35s) ─┐
# 体验专家 (52s)   ┼─→ 收集结果 → 52 秒
# 测试专家 (120s)─┘
```

### 超时重试机制

```python
# 自动重试配置
MAX_RETRIES = 2  # 超时后重试 2 次

# 执行流程：
# 1. 第一次执行（300 秒超时）
# 2. 超时 → 等待 5 秒 → 重试 1
# 3. 超时 → 等待 5 秒 → 重试 2
# 4. 仍超时 → 启用降级方案
```

---

## 📊 输出格式

### 讨论报告（Markdown）

```markdown
# RoundTable 讨论报告

## 基本信息
- 主题：智能客服系统技术方案
- 模式：pre-ac
- 时间：2026-03-17 14:25 - 14:50
- 参与 Agent：工程专家，体验专家，测试专家

## R1: 独立方案

### 工程专家 - 技术方案
React 18 + NestJS + PostgreSQL + Redis...

### 体验专家 - 用户体验方案
用户画像 + 交互流程 + 色彩方案...

### 测试专家 - 测试策略
测试金字塔 + 覆盖率目标 + CI/CD...

## R2: 相互引用

### 工程专家 - 引用体验专家观点
同意用户体验方案，补充技术实现细节...

## R5: 总结报告

### 核心决策
1. 技术栈：React 18 + NestJS + PostgreSQL
2. 体验保障：SSE 流式输出 + 转接优化
3. 测试策略：覆盖率>80% + 自动化测试

### 行动项
- [ ] 搭建 NestJS 项目框架
- [ ] 实现 SSE 流式输出
- [ ] 配置测试环境
```

### 前端查看器

访问 `http://localhost:8080` 查看：
- 项目卡片切换
- 消息展开/折叠
- 搜索功能
- 导出 Markdown

---

## ⚠️ 注意事项

### 1. 耗时说明
- **超时时间** = 最大允许时间（保险丝）
- **实际耗时** = Agent 实际执行时间
- Agent 30 秒完成 → 30 秒后继续
- Agent 300 秒未完成 → 触发重试

### 2. 适用场景
- ✅ 需要多方观点的复杂问题
- ✅ 需要深度分析的技术方案
- ✅ 需要权衡利弊的架构决策
- ❌ 简单问题查询
- ❌ 需要立即回答的场景

### 3. 用户期望管理
- 明确告知 15-30 分钟耗时
- 提供"快速回答"备选方案
- 实时进度通知减少焦虑
- 支持用户中途查看

---

## 📁 文件结构

```
roundtable-skill/
├── SKILL.md                    # 技能说明（本文件）
├── __init__.py                 # 模块导出
├── roundtable_engine.py        # 执行引擎
├── roundtable_notifier.py      # 通知模块
├── agent_selector.py           # Agent 选择器
├── clawhub.json                # ClawHub 配置
├── prompts/
│   ├── framework.md            # 提示词框架
│   └── README.md               # 提示词说明
├── templates/
│   ├── software-development.md # 软件开发模板
│   ├── product-planning.md     # 产品规划模板
│   └── business-research.md    # 商业研究模板
└── roundtable-viewer/          # 前端查看器
    ├── index.html
    ├── data.json
    └── assets/
```

---

## 🔗 相关链接

- ClawHub: `https://clawhub.com/skills/roundtable-skill` *(待上线)*
- 文档：`https://docs.openclaw.ai/skills/roundtable` *(待上线)*
- 示例：`https://github.com/openclaw/roundtable-examples` *(待上线)*

---

## 📝 更新日志

### v0.9.0 (2026-03-19) - 基于真实测试优化
- ✅ 完整 5 轮流程（R1-R5）
- ✅ 强制批判深度（5 风险 +3 缺陷）
- ✅ 方案动态演进（R4 标注修改）
- ✅ 分歧明确裁决（R5 必须裁决）
- ✅ 产出可直接执行（周级计划 + 风险预案）
- ✅ 触发词识别（RoundTable/圆桌会议/圆桌讨论等）
- ✅ 真实子 Agent 调用（sessions_spawn）
- ✅ 上下文传递（每轮注入完整历史）

### v0.1.0 (2026-03-17) - 初始版本
- ✅ 基础 RoundTable 框架
- ✅ 3 专家角色定义
- ✅ 5 轮讨论流程
- ✅ 前端查看器

---

*RoundTable - 让决策更完善，让讨论更深入*
