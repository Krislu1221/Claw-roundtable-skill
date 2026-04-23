# RoundTable Skill v2.0 - 多专家 Agent 深度讨论系统

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/Krislu1221/Claw-roundtable-skill)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)

> 模拟真实圆桌会议，异构模型路由 + MMR 意图解析 + 收敛控制，产生可执行方案

---

## 📋 技能说明

**RoundTable v2.0** 是一个通用的多 Agent 讨论引擎，支持**异构模型路由**（不同角色配置不同模型）和**收敛控制**。

系统通过 Maximal Marginal Relevance (MMR) 从 170+ 专家库中动态匹配 diverse experts，防止"回音室效应"。支持本地模型配置 (`local_models.json`) 和公开配置 (`roundtable_config.yaml`) 两种模式。

---

## 🎯 核心升级 (v2.0)

| 特性 | v0.9.0 | v2.0 |
|------|--------|------|
| 专家匹配 | 固定 5 角色 | **170+ 专家库动态匹配** |
| 模型路由 | 单一模型 | **异构路由 (MiniMax 创意/GLM 逻辑)** |
| 收敛控制 | 固定 5 轮 | **语义收敛引擎，自动停止** |
| 意图解析 | 关键词 | **MMR 多样性选择** |
| 配置安全 | 扫描环境变量 | **显式配置文件，零环境扫描** |

---

## 🚀 适用场景

### ✅ 推荐使用
- 复杂项目前期的头脑风暴
- 技术方案设计和架构决策
- 产品方案讨论和 MVP 定义
- 项目后期的优化和合规审查
- 需要多方观点的复杂问题
- 需要深度分析的技术方案
- 需要权衡利弊的架构决策

### ❌ 不推荐使用
- 简单问答（直接问主 Agent）
- 代码生成（使用 Auto-Coding v3）
- 需要即时响应的场景
- 单次工具调用即可解决的任务

---

## 🏗️ 架构设计

### 1. 意图解析器 (MMR)
```python
def parse(self, input_text: str, top_k=3):
    # 1. 关键词评分
    # 2. MMR 选择（最大化相关性，最小化专家间相似度）
    # 3. 返回 diverse 专家列表 + 模糊度评分
```

### 2. 自适应模型路由器
```python
class ModelRouter:
    def get_model_for_role(self, capability: str) -> str:
        # 根据能力标签匹配最佳模型
        # 创意 → MiniMax, 逻辑 → GLM/Qwen
```

### 3. 收敛引擎
```python
def check(self, history, current_round, max_rounds):
    if current_round >= max_rounds: return "FORCE_ARBITRATE"
    if "consensus" in recent_turns: return "STOP"
    return "CONTINUE"
```

---

## 📦 使用方式

### 触发词
- RoundTable
- 圆桌会议 / 圆桌讨论
- 多 Agent 讨论 / 多专家讨论

### 配置要求
- **本地开发**: 使用 `local_models.json` 定义模型阵容
- **开源部署**: 使用 `roundtable_config.yaml`（零环境扫描）
- **降级模式**: 无配置时自动切换为单模型多角色模式

---

## ⚠️ 注意事项

1. **Token 消耗**: 多 Agent 讨论会消耗成倍 Token，请根据任务复杂度选择
2. **模型配置**: 强烈建议配置多模型阵容以获得最佳效果
3. **收敛控制**: 系统会自动检测语义重复并提前终止，无需担心无限循环
4. **用户参与**: 讨论过程中可插入补充意见增强讨论质量

---

## 📁 文件结构

```
roundtable-skill/
├── SKILL.md              # 技能核心定义
├── core/
│   ├── model_router.py   # 自适应模型路由器
│   ├── intent_parser.py  # MMR 意图解析器
│   ├── prompt_builder.py # 提示词构建器
│   └── convergence.py    # 收敛控制引擎
├── local_models.json     # 本地模型配置（可选）
└── roundtable_config.yaml # 公开配置文件（可选）
```

---

## 👤 作者

Kris Lu <krislu666@foxmail.com>

## 📄 许可

MIT License

---

**更新日期**: 2026-04-23
