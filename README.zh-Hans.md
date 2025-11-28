# Dify Use Case Playground

> 🎯 真实场景的 Dify 工作流 DSL 示例和用例集合

[English](README.md) | [简体中文](README.zh-Hans.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md)

---

## 项目简介

**Dify Use Case Playground** 是一个个人开源项目，收集了实用的 Dify 工作流 DSL 示例和用例。本仓库旨在为使用 Dify 工作流引擎构建生产级工作流提供学习资源和参考。

## 内容说明

本仓库包含：

- 📋 **工作流 DSL 文件** (`.yml`) - 可直接导入 Dify 的完整工作流定义
- 📖 **文档说明** (`README.md`) - 每个用例的详细说明
- 🎨 **最佳实践** - 真实场景的模式和解决方案

## 特性

- ✅ 生产级工作流
- ✅ 完整的文档说明
- ✅ 易于导入和自定义
- ✅ 真实场景用例
- ✅ 最佳实践和模式
- 🔒 **安全保护**：通过 CI/CD 自动扫描敏感信息

## 用例列表

### 🤖 自动化

- **[每日新闻推送到 Slack](./usecases/daily-news-slack/)** - 使用定时触发器自动将每日新闻推送到 Slack 频道

### 💬 聊天机器人和助手

- **[Slack 触发新闻研究助手](./usecases/slack-news-researcher/)** - 具有问题分类和新闻研究能力的智能 Slack 机器人

## 快速开始

1. **浏览用例**
   - 查看 `usecases/` 目录
   - 每个用例都有自己的文件夹，包含 `workflow.yml` 和 `README.md`

2. **导入工作流**
   - 打开 Dify 控制台
   - 从用例文件夹导入 `.yml` 文件
   - 按照用例 README 中的设置说明进行操作

3. **自定义**
   - 根据需求修改工作流
   - 更新配置参数
   - 测试并部署

## 目录结构

```
.
├── README.md                 # 本文件（英文）
├── README.zh-Hans.md         # 简体中文
├── README.zh-Hant.md         # 繁体中文
├── README.ja.md              # 日文
├── LICENSE                   # Apache 2.0 许可证
├── .gitignore               # Git 忽略规则
├── .gitleaks.toml          # 敏感信息扫描配置
├── .github/
│   └── workflows/
│       ├── secret-scanning.yml      # CI/CD 敏感信息扫描工作流
│       └── code-language-check.yml  # CI/CD 语言检查工作流
└── usecases/                 # 用例集合
    ├── daily-news-slack/
    │   ├── workflow.yml      # 工作流 DSL 文件
    │   └── README.md         # 用例文档（英文）
    └── slack-news-researcher/
        ├── workflow.yml      # 工作流 DSL 文件
        └── README.md         # 用例文档（英文）
```

## 环境要求

- [Dify](https://github.com/langgenius/dify) 平台访问权限
- 所需的插件和 API 密钥（参见各用例的 README）

## 安全说明

🔒 **本仓库使用自动化的敏感信息扫描**，防止意外提交敏感信息：

- **CI/CD 集成**：GitHub Actions 工作流会在每次推送和拉取请求时自动扫描敏感信息
- **使用的工具**：
  - [Gitleaks](https://github.com/gitleaks/gitleaks) - 全面的密钥检测
  - 自定义模式匹配常见敏感数据
- **检查内容**：API 密钥、令牌、密码、Webhook URL、AWS 密钥、Slack 令牌等

**重要提示**：请勿提交敏感信息，如 API 密钥、令牌或凭证。请使用环境变量或安全的配置管理方式。

## 代码语言要求

🌐 **本项目保持国际化定位。**

- ✅ **代码文件可以包含中文或其他语言** - 鼓励用于国际化（i18n）支持
- ✅ Dify 工作流文件中的 i18n 字段（`zh_Hans`, `zh_Hant`, `ja_JP`, `pt_BR` 等）完全支持
- ✅ **Git 提交信息必须使用英文** - 以保持国际化项目定位
- ✅ **Pull request 标题和描述必须使用英文** - 便于全球协作
- 📖 文档文件提供多种语言版本（英文、简体中文、繁体中文、日文）

**注意**：CI 检查会强制要求 git 提交信息和 PR 内容使用英文，但允许代码文件中使用任何语言以支持国际化。

## 贡献

这是一个个人项目，但欢迎建议和反馈！你可以：

- 提交 issue 报告问题或提出功能请求
- 提交 pull request 进行改进
- 分享你自己的用例

## 许可证

本项目采用 Apache License 2.0 - 详见 [LICENSE](LICENSE) 文件。

---

## 作者

个人项目 by [@petrus](https://github.com/petrus)

---

**注意**：本仓库作为个人学习和参考资源维护。用例基于真实场景，可能需要根据你的具体需求进行自定义。

