# Slack Trigger News Researcher

[English](README.md) | [简体中文](README.zh-Hans.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md)

---

## 简介

这是一个智能 Slack 机器人工作流，当用户在 Slack 中 @ 提及机器人时，会根据用户的问题类型智能路由到不同的处理流程。支持日常聊天、科技新闻查询和无法回答问题的处理。

## 功能特性

- 🔔 **Slack 触发**：响应 Slack App Mention 事件
- 🧠 **智能分类**：使用问题分类器判断用户意图
- 💬 **日常聊天**：友好的日常对话机器人（Jasper）
- 📰 **新闻研究**：使用 Agent 和工具进行科技新闻搜索
- ⚠️ **优雅处理**：无法回答时给出友好提示

## 工作流结构

```
Slack Trigger → Question Classifier → [3个分支]
                                    ├─ Casual Chat → LLM → Slack Webhook
                                    ├─ Tech News Inquiry → Agent → Slack Webhook
                                    └─ Unanswerable → LLM → Slack Webhook
```

### 节点说明

1. **Slack Trigger (App Mention)**
   - 监听 Slack 中的 @ 提及事件
   - 提取用户消息文本

2. **Question Classifier**
   - 使用 GPT-4o-mini 对用户问题进行分类
   - 三个分类：
     - **Casual Chat**：日常对话、问候、闲聊
     - **Tech News Inquiry**：科技新闻查询、最新资讯
     - **Unanswerable**：无法准确回答的问题

3. **Casual Chat 分支**
   - 使用 GPT-4o-mini 进行日常对话
   - 机器人名称：Jasper
   - 友好的日常交流风格

4. **Tech News Inquiry 分支**
   - 使用 Agent（GPT-5.1）进行新闻研究
   - 可用工具：
     - Google Search：网页搜索
     - Yahoo Finance News：股票新闻
     - Current Time：获取当前时间

5. **Unanswerable 分支**
   - 使用 GPT-4o-mini 处理无法回答的问题
   - 友好地解释原因并引导用户重新提问

## 配置说明

### 依赖插件

- `langgenius/slack:0.0.4` - Slack 集成插件
- `langgenius/openai:0.2.7` - OpenAI 模型插件

### 环境变量

无需额外环境变量。

### 工具配置

1. **Google Search**
   - 用于搜索网页内容
   - 支持语言和国家代码配置

2. **Yahoo Finance News**
   - 获取股票相关新闻
   - 参数：`symbol`（股票代码）

3. **Current Time**
   - 获取当前时间
   - 用于判断新闻时效性

4. **Slack Incoming Webhook**
   - 需要配置 3 个 Webhook URL（对应 3 个分支）
   - 将处理结果发送回 Slack

## 使用方法

1. 在 Dify 中导入此工作流 DSL 文件
2. 配置 Slack App Mention 触发器（需要在 Slack 应用中设置）
3. 配置 3 个 Slack Incoming Webhook URL（分别对应 3 个分支）
4. 根据需要调整 Agent 的指令和工具配置
5. 保存并启用工作流
6. 在 Slack 中 @ 提及机器人进行测试

## 自定义配置

### 修改分类器类别

在 Question Classifier 节点中修改 `classes` 和 `instruction`：

```yaml
classes:
  - id: '1'
    name: Casual Chat — everyday conversation...
  - id: '2'
    name: Tech News Inquiry — asking about current technology...
  - id: '3'
    name: Unanswerable (Insufficient Information)...
```

### 修改 Agent 指令

在 Agent 节点的 `instruction` 参数中修改行为规则：

```yaml
instruction:
  type: constant
  value: |
    Your custom instructions here...
```

### 修改机器人名称和风格

在各个 LLM 节点的 system prompt 中修改：

```yaml
prompt_template:
  - role: system
    text: 'Your name is Jasper. Your role is...'
```

## 注意事项

- 需要在 Slack 应用中配置 App Mention 事件订阅
- 确保 3 个 Slack Webhook URL 都已正确配置
- Agent 使用的模型需要 API 访问权限
- 建议根据实际使用场景调整分类逻辑和响应风格
- 空消息或空白消息会有特殊处理逻辑

## 许可证

本项目采用 Apache License 2.0。

