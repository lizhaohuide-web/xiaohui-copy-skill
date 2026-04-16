# 🛠️ Xiaohui Copy Skill (Skill Factory Pro)

一个**进阶版 AI Skill 克隆与定制工厂**。它不仅能复制代码，更能通过“业务场景挖掘”和“自动化验证”，将现有 Skill 重构为开箱即用的生产级工具。

## ✨ 核心特性

| 特性 | 描述 |
| :--- | :--- |
| 🤝 **顾问模式** | 深度解剖原版，按 P0/P1/P2 优先级输出定制项。通过场景化提问，将你的“业务痛点”自动转化为技术方案。 |
| ⚡ **专家模式** | 跳过繁琐交互，直接接收技术参数指令，秒级完成代码重构与文档更新。 |
| 🧪 **自动化验证** | 生成后自动执行 `bash -n` / `py_compile` 语法检查与冒烟测试（Smoke Test），拒绝交付“半成品”。 |
| 🗝️ **环境依赖清单** | 自动识别所需 API Key/环境变量，附带获取指南，配置透明化。 |
| 🔄 **动态降级策略** | 内置备选方案推荐，确保主模型/Key 不可用时仍有路可走。 |
| 🛡️ **安全隔离** | 所有操作均在独立目录进行，**绝不污染原版 Skill**。 |

## 📦 目录结构
```text
xiaohui-copy-skill/
├── SKILL.md              # 核心 Prompt 与工作流定义
├── scripts/
│   └── clone_skill.py    # 底层克隆、文件复制与参数 Patch 脚本
└── README.md             # 本说明文档
```

## 🚀 快速开始

### 1. 安装
将本仓库克隆或复制到你的 Hermes / OpenClaw Skills 目录中：
```bash
# 假设你的 skills 目录在 ~/.hermes/skills/
git clone https://github.com/<你的用户名>/xiaohui-copy-skill.git ~/.hermes/skills/xiaohui-copy-skill
```

### 2. 触发使用
在 AI 对话中直接发送以下指令即可激活：
- `分析一下 [目标Skill名称]`
- `基于 [目标Skill名称] 克隆一个新 skill`
- `用专家模式，把 [目标Skill名称] 改成 [新名字]，参数A改成X...`

### 3. 工作流演示

**🤝 顾问模式 (默认)**
> **你**: 分析一下 `baoyu-imagine`。
> **AI**: 📋 生成《baoyu-imagine 解剖报告》...
> 🔥 P0 痛点: 每次都要手动输入 `--ar 3:4`。
> 🗣️ 提问: 你平时主要用它做什么业务？
> **你**: 做公众号封面，觉得调尺寸太麻烦。
> **AI**: 方案已锁定：比例强制 21:9，自动注入留白咒语。确认执行？
> **你**: 执行。
> **AI**: ✅ 已生成 `wechat-cover-master`，并通过语法检查！

**⚡ 专家模式**
> **你**: 用专家模式，把 `baoyu-imagine` 改成 `nano-simple`，默认 1:1。
> **AI**: ✅ 收到。已跳过访谈，直接重构并运行语法检查... 🧪 验证通过，交付完成！

## 🛠️ 开发说明
本 Skill 依赖于 `patch` 机制与脚本替换。AI 会调用内置的 `clone_skill.py` 执行以下操作：
1. 隔离复制源目录
2. 读取目标文件
3. 执行字符串级替换 (Replacements)
4. 重写 `SKILL.md` 中的 Prompt 与 Workflow

## 📝 License
MIT
