# Slack Trigger News Researcher

[English](README.md) | [简体中文](README.zh-Hans.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md)

---

## Introduction

This is an intelligent Slack bot workflow that intelligently routes to different processing flows based on user question types when users @ mention the bot in Slack. Supports casual chat, tech news queries, and handling unanswerable questions.

## Features

- 🔔 **Slack Trigger**: Responds to Slack App Mention events
- 🧠 **Smart Classification**: Uses question classifier to determine user intent
- 💬 **Casual Chat**: Friendly daily conversation bot (Jasper)
- 📰 **News Research**: Uses Agent and tools for tech news search
- ⚠️ **Graceful Handling**: Provides friendly prompts when questions cannot be answered

## Workflow Structure

```
Slack Trigger → Question Classifier → [3 branches]
                                    ├─ Casual Chat → LLM → Slack Webhook
                                    ├─ Tech News Inquiry → Agent → Slack Webhook
                                    └─ Unanswerable → LLM → Slack Webhook
```

### Node Description

1. **Slack Trigger (App Mention)**
   - Listens for @ mention events in Slack
   - Extracts user message text

2. **Question Classifier**
   - Uses GPT-4o-mini to classify user questions
   - Three categories:
     - **Casual Chat**: Daily conversation, greetings, small talk
     - **Tech News Inquiry**: Tech news queries, latest updates
     - **Unanswerable**: Questions that cannot be accurately answered

3. **Casual Chat Branch**
   - Uses GPT-4o-mini for daily conversation
   - Bot name: Jasper
   - Friendly daily communication style

4. **Tech News Inquiry Branch**
   - Uses Agent (GPT-5.1) for news research
   - Available tools:
     - Google Search: Web search
     - Yahoo Finance News: Stock news
     - Current Time: Get current time

5. **Unanswerable Branch**
   - Uses GPT-4o-mini to handle unanswerable questions
   - Friendly explanation and guidance for rephrasing

## Configuration

### Dependencies

- `langgenius/slack:0.0.4` - Slack integration plugin
- `langgenius/openai:0.2.7` - OpenAI model plugin

### Environment Variables

No additional environment variables required.

### Tool Configuration

1. **Google Search**
   - Used to search web content
   - Supports language and country code configuration

2. **Yahoo Finance News**
   - Fetches stock-related news
   - Parameter: `symbol` (stock ticker)

3. **Current Time**
   - Gets current time
   - Used to judge news timeliness

4. **Slack Incoming Webhook**
   - Requires 3 Webhook URLs (corresponding to 3 branches)
   - Sends processing results back to Slack

## Usage

1. Import this workflow DSL file into Dify
2. Configure Slack App Mention trigger (requires setup in Slack app)
3. Configure 3 Slack Incoming Webhook URLs (corresponding to 3 branches)
4. Adjust Agent instructions and tool configuration as needed
5. Save and enable the workflow
6. Test by @ mentioning the bot in Slack

## Customization

### Modify Classifier Categories

Modify `classes` and `instruction` in the Question Classifier node:

```yaml
classes:
  - id: '1'
    name: Casual Chat — everyday conversation...
  - id: '2'
    name: Tech News Inquiry — asking about current technology...
  - id: '3'
    name: Unanswerable (Insufficient Information)...
```

### Modify Agent Instructions

Modify behavior rules in the Agent node's `instruction` parameter:

```yaml
instruction:
  type: constant
  value: |
    Your custom instructions here...
```

### Modify Bot Name and Style

Modify in each LLM node's system prompt:

```yaml
prompt_template:
  - role: system
    text: 'Your name is Jasper. Your role is...'
```

## Notes

- Requires App Mention event subscription configuration in Slack app
- Ensure all 3 Slack Webhook URLs are correctly configured
- Agent model requires API access permissions
- Recommend adjusting classification logic and response style according to actual usage scenarios
- Empty or blank messages have special handling logic

## License

This project uses the Apache License 2.0.
