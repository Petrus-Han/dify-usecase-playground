# Daily News for Slack Channel

[English](README.md) | [简体中文](README.zh-Hans.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md)

---

## 简介

这是一个自动化工作流，每天定时获取最新新闻并发送到 Slack 频道。工作流使用定时触发器，结合 Agent 和工具节点，实现新闻的自动采集和推送。

## 功能特性

- ⏰ **定时触发**：每天自动执行（默认 UTC 时间 9:00，可配置时区）
- 📰 **新闻获取**：使用 Yahoo Finance News 工具获取股票相关新闻
- 🤖 **智能 Agent**：使用 Claude Opus 4 模型进行新闻分析和处理
- 📤 **Slack 推送**：通过 Slack Incoming Webhook 发送消息到指定频道

## 工作流结构

```
Schedule Trigger → Agent → Slack Webhook
```

1. **Schedule Trigger**：定时触发器，每天执行一次
2. **Agent**：智能代理，负责：
   - 获取当前时间
   - 使用 Yahoo Finance News 工具搜索新闻
   - 分析和整理新闻内容
3. **Slack Webhook**：将处理后的新闻发送到 Slack 频道

## 配置说明

### 依赖插件

- `langgenius/slack:0.0.4` - Slack 集成插件

### 环境变量

无需额外环境变量。

### 工具配置

1. **Yahoo Finance News**
   - 用于获取股票代码相关的新闻
   - 参数：`symbol`（股票代码，如 NVDA、TSLA）

2. **Current Time**
   - 获取当前时间，用于判断新闻时效性
   - 时区：UTC（可配置）

3. **Slack Incoming Webhook**
   - 需要配置 Slack Webhook URL
   - 消息内容来自 Agent 的输出

## 使用方法

1. 在 Dify 中导入此工作流 DSL 文件
2. 配置 Slack Incoming Webhook URL
3. 根据需要调整定时触发器的执行时间
4. 修改 Agent 的查询内容（默认查询 NVDA 和 TSLA 的新闻）
5. 保存并启用工作流

## 自定义配置

### 修改查询内容

在 Agent 节点的 `query` 参数中修改默认查询：

```yaml
query:
  type: constant
  value: What's the latest on NVDA and TSLA today?
```

### 修改执行时间

在 Schedule Trigger 节点中修改 `cron_expression` 和 `timezone`：

```yaml
cron_expression: 0 9 * * *  # 每天 9:00 UTC
timezone: America/New_York   # 时区设置
```

## 注意事项

- 确保已安装并配置 Slack 插件
- Webhook URL 需要正确配置，否则消息无法发送
- Agent 使用的模型需要 API 访问权限
- 建议根据实际需求调整新闻查询范围和频率

## 许可证

本项目采用 Apache License 2.0。

