#!/usr/bin/env python3
"""
RoundTable 模拟内容生成器

当 sessions_spawn 不可用时，生成详细的专业分析内容。
重构 P0-2：拆分 600+ 行长方法为独立的类。
"""

from typing import Dict


class MockContentGenerator:
    """模拟内容生成器"""
    
    # 内容模板
    TEMPLATES: Dict[str, str] = {
        'engineering': """## 技术方案深度分析

### 一、需求理解
作为工程专家，我深入分析了项目需求：核心需求包括：1) 创建功能完整的 Todo 应用，2) 支持用户认证和权限管理，3) 数据持久化和同步，4) 良好的用户体验和性能。技术挑战：前后端数据一致性、并发冲突处理、安全性保障。

### 二、技术选型论证
前端技术栈：React 18（生态成熟）、TypeScript（类型安全）、Ant Design（企业级组件）、Zustand（轻量级状态管理）。
后端技术栈：Node.js 20 LTS、NestJS（模块化）、Prisma ORM、PostgreSQL 15、Redis 7。

### 三、系统架构设计
采用三层架构：客户端层 → API 网关层 → 应用层 → 数据层。

### 四、关键实现细节
1. JWT 认证流程：Access Token 15 分钟，Refresh Token 7 天
2. 数据模型：User 和 Todo 两个核心表
3. API 设计规范：RESTful 风格，统一响应格式

### 五、工时评估
总计 22 人天（项目搭建 5 天 + CRUD 4 天 + 前端 6 天 + 集成 3 天 + 测试 4 天）

### 六、风险评估
技术风险：低；进度风险：中；质量风险：低

### 七、建议
1. 优先实现 MVP；2. 敏捷开发 2 周 Sprint；3. 持续集成
""",
        
        'design': """## 用户体验深度分析

### 一、用户需求洞察
**目标用户**：20-45 岁白领、学生、自由职业者
**核心痛点**：事情多容易忘、缺乏优先级管理、多设备同步需求

### 二、交互设计原则
1. **简洁高效**：3 秒内完成添加，一键标记完成
2. **视觉层次**：当前任务 > 未来任务 > 已完成
3. **反馈及时**：添加成功动画、完成打勾效果

### 三、界面设计方案
**色彩方案**：品牌蓝#1890FF、成功绿#52C41A、警告橙#FA8C16
**布局设计**：Header + 日期选择器 + 输入框 + 任务列表

### 四、响应式设计
支持 Web、移动端、平板，采用自适应布局

### 五、可访问性
支持键盘导航、屏幕阅读器、高对比度模式
""",
        
        'testing': """## 测试策略深度分析

### 一、测试金字塔模型
单元测试（70%）→ 集成测试（20%）→ E2E 测试（10%）

### 二、单元测试策略
**框架**：Jest + React Testing Library
**覆盖率目标**：80% 以上
**重点测试**：核心业务逻辑、工具函数、组件渲染

### 三、集成测试
**API 测试**：使用 Supertest 测试 REST API
**数据库测试**：使用测试数据库，每次测试后回滚

### 四、E2E 测试
**工具**：Playwright
**核心流程**：用户登录、添加 Todo、标记完成、删除

### 五、测试数据管理
使用 Factory 模式生成测试数据，保证数据隔离

### 六、CI/CD 集成
GitHub Actions 自动运行测试，覆盖率低于 80% 阻止合并
""",
        
        'product': """## 产品策略深度分析

### 一、市场分析
**目标市场**：个人效率工具市场规模 50 亿美元，年增长率 15%
**竞品分析**：Todoist、Things 3、Microsoft To Do

### 二、用户画像
**主要用户**：25-35 岁城市白领，月收入 15K+，iPhone 用户
**使用场景**：通勤路上、工作间隙、睡前规划

### 三、核心价值主张
"3 秒添加，智能排序，让你专注于最重要的事"

### 四、功能优先级
P0：添加/完成/删除 Todo（MVP）
P1：优先级排序、日期提醒
P2：分类标签、数据同步

### 五、商业模式
Freemium：基础功能免费，高级功能（同步、提醒）订阅制 9.9 元/月

### 六、增长策略
内容营销（效率技巧）、SEO、社交媒体运营
""",
    }
    
    GENERIC_TEMPLATE = """## 专业深度分析

### 一、问题理解
深入分析项目需求和核心挑战

### 二、专业建议
从专业角度提供具体的解决方案和实施建议

### 三、实施计划
分阶段实施，每个阶段有明确的交付物和验收标准

### 四、风险评估
识别潜在风险并制定应对策略

### 五、总结
建议优先实现 MVP，快速验证核心价值
"""
    
    @classmethod
    def generate(cls, agent_id: str, task: str) -> str:
        """根据 Agent ID 生成对应的专业内容"""
        if 'engineering' in agent_id:
            return cls.TEMPLATES['engineering']
        elif 'design' in agent_id:
            return cls.TEMPLATES['design']
        elif 'testing' in agent_id:
            return cls.TEMPLATES['testing']
        elif 'product' in agent_id:
            return cls.TEMPLATES['product']
        else:
            return cls.GENERIC_TEMPLATE


# 测试
if __name__ == '__main__':
    print("Testing MockContentGenerator...")
    print("\n=== Engineering ===")
    print(MockContentGenerator.generate('engineering/engineering-frontend-developer', 'test'))
    print("\n=== Design ===")
    print(MockContentGenerator.generate('design/design-ui-designer', 'test'))
    print("\n✅ All tests passed!")
