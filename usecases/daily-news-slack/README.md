# Daily News for Slack Channel

[English](README.md) | [简体中文](README.zh-Hans.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md)

---

## Introduction

This is an automated workflow that fetches the latest news daily and sends it to a Slack channel. The workflow uses scheduled triggers combined with Agent and tool nodes to achieve automatic news collection and delivery.

## Features

- ⏰ **Scheduled Trigger**: Automatically executes daily (default UTC 9:00, configurable timezone)
- 📰 **News Retrieval**: Uses Yahoo Finance News tool to fetch stock-related news
- 🤖 **Smart Agent**: Uses Claude Opus 4 model for news analysis and processing
- 📤 **Slack Delivery**: Sends messages to specified channels via Slack Incoming Webhook

## Workflow Structure

```
Schedule Trigger → Agent → Slack Webhook
```

1. **Schedule Trigger**: Scheduled trigger that executes once daily
2. **Agent**: Intelligent agent responsible for:
   - Getting current time
   - Searching news using Yahoo Finance News tool
   - Analyzing and organizing news content
3. **Slack Webhook**: Sends processed news to Slack channel

## Configuration

### Dependencies

- `langgenius/slack:0.0.4` - Slack integration plugin

### Environment Variables

No additional environment variables required.

### Tool Configuration

1. **Yahoo Finance News**
   - Used to fetch news related to stock ticker symbols
   - Parameter: `symbol` (stock ticker, e.g., NVDA, TSLA)

2. **Current Time**
   - Gets current time for judging news timeliness
   - Timezone: UTC (configurable)

3. **Slack Incoming Webhook**
   - Requires Slack Webhook URL configuration
   - Message content comes from Agent output

## Usage

1. Import this workflow DSL file into Dify
2. Configure Slack Incoming Webhook URL
3. Adjust scheduled trigger execution time as needed
4. Modify Agent query content (default queries NVDA and TSLA news)
5. Save and enable the workflow

## Customization

### Modify Query Content

Modify the default query in the Agent node's `query` parameter:

```yaml
query:
  type: constant
  value: What's the latest on NVDA and TSLA today?
```

### Modify Execution Time

Modify `cron_expression` and `timezone` in the Schedule Trigger node:

```yaml
cron_expression: 0 9 * * *  # Daily at 9:00 UTC
timezone: America/New_York   # Timezone setting
```

## Notes

- Ensure Slack plugin is installed and configured
- Webhook URL must be correctly configured, otherwise messages cannot be sent
- Agent model requires API access permissions
- Recommend adjusting news query scope and frequency according to actual needs

## License

This project uses the Apache License 2.0.
