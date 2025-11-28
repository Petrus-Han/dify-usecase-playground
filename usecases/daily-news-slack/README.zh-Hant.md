# Daily News for Slack Channel

[English](README.md) | [简体中文](README.zh-Hans.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md)

---

## 簡介

這是一個自動化工作流，每天定時獲取最新新聞並發送到 Slack 頻道。工作流使用定時觸發器，結合 Agent 和工具節點，實現新聞的自動採集和推送。

## 功能特性

- ⏰ **定時觸發**：每天自動執行（預設 UTC 時間 9:00，可設定時區）
- 📰 **新聞獲取**：使用 Yahoo Finance News 工具獲取股票相關新聞
- 🤖 **智能 Agent**：使用 Claude Opus 4 模型進行新聞分析和處理
- 📤 **Slack 推送**：透過 Slack Incoming Webhook 發送訊息到指定頻道

## 工作流結構

```
Schedule Trigger → Agent → Slack Webhook
```

1. **Schedule Trigger**：定時觸發器，每天執行一次
2. **Agent**：智能代理，負責：
   - 獲取當前時間
   - 使用 Yahoo Finance News 工具搜尋新聞
   - 分析和整理新聞內容
3. **Slack Webhook**：將處理後的新聞發送到 Slack 頻道

## 設定說明

### 依賴插件

- `langgenius/slack:0.0.4` - Slack 整合插件

### 環境變數

無需額外環境變數。

### 工具設定

1. **Yahoo Finance News**
   - 用於獲取股票代碼相關的新聞
   - 參數：`symbol`（股票代碼，如 NVDA、TSLA）

2. **Current Time**
   - 獲取當前時間，用於判斷新聞時效性
   - 時區：UTC（可設定）

3. **Slack Incoming Webhook**
   - 需要設定 Slack Webhook URL
   - 訊息內容來自 Agent 的輸出

## 使用方法

1. 在 Dify 中匯入此工作流 DSL 檔案
2. 設定 Slack Incoming Webhook URL
3. 根據需要調整定時觸發器的執行時間
4. 修改 Agent 的查詢內容（預設查詢 NVDA 和 TSLA 的新聞）
5. 儲存並啟用工作流

## 自訂設定

### 修改查詢內容

在 Agent 節點的 `query` 參數中修改預設查詢：

```yaml
query:
  type: constant
  value: What's the latest on NVDA and TSLA today?
```

### 修改執行時間

在 Schedule Trigger 節點中修改 `cron_expression` 和 `timezone`：

```yaml
cron_expression: 0 9 * * *  # 每天 9:00 UTC
timezone: America/New_York   # 時區設定
```

## 注意事項

- 確保已安裝並設定 Slack 插件
- Webhook URL 需要正確設定，否則訊息無法發送
- Agent 使用的模型需要 API 存取權限
- 建議根據實際需求調整新聞查詢範圍和頻率

## 授權許可

本專案採用 Apache License 2.0。

