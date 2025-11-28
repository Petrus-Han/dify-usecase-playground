# Slack Trigger News Researcher

[English](README.md) | [简体中文](README.zh-Hans.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md)

---

## 簡介

這是一個智能 Slack 機器人工作流，當使用者在 Slack 中 @ 提及機器人時，會根據使用者的問題類型智能路由到不同的處理流程。支援日常聊天、科技新聞查詢和無法回答問題的處理。

## 功能特性

- 🔔 **Slack 觸發**：響應 Slack App Mention 事件
- 🧠 **智能分類**：使用問題分類器判斷使用者意圖
- 💬 **日常聊天**：友好的日常對話機器人（Jasper）
- 📰 **新聞研究**：使用 Agent 和工具進行科技新聞搜尋
- ⚠️ **優雅處理**：無法回答時給出友好提示

## 工作流結構

```
Slack Trigger → Question Classifier → [3個分支]
                                    ├─ Casual Chat → LLM → Slack Webhook
                                    ├─ Tech News Inquiry → Agent → Slack Webhook
                                    └─ Unanswerable → LLM → Slack Webhook
```

### 節點說明

1. **Slack Trigger (App Mention)**
   - 監聽 Slack 中的 @ 提及事件
   - 提取使用者訊息文字

2. **Question Classifier**
   - 使用 GPT-4o-mini 對使用者問題進行分類
   - 三個分類：
     - **Casual Chat**：日常對話、問候、閒聊
     - **Tech News Inquiry**：科技新聞查詢、最新資訊
     - **Unanswerable**：無法準確回答的問題

3. **Casual Chat 分支**
   - 使用 GPT-4o-mini 進行日常對話
   - 機器人名稱：Jasper
   - 友好的日常交流風格

4. **Tech News Inquiry 分支**
   - 使用 Agent（GPT-5.1）進行新聞研究
   - 可用工具：
     - Google Search：網頁搜尋
     - Yahoo Finance News：股票新聞
     - Current Time：獲取當前時間

5. **Unanswerable 分支**
   - 使用 GPT-4o-mini 處理無法回答的問題
   - 友好地解釋原因並引導使用者重新提問

## 設定說明

### 依賴插件

- `langgenius/slack:0.0.4` - Slack 整合插件
- `langgenius/openai:0.2.7` - OpenAI 模型插件

### 環境變數

無需額外環境變數。

### 工具設定

1. **Google Search**
   - 用於搜尋網頁內容
   - 支援語言和國家代碼設定

2. **Yahoo Finance News**
   - 獲取股票相關新聞
   - 參數：`symbol`（股票代碼）

3. **Current Time**
   - 獲取當前時間
   - 用於判斷新聞時效性

4. **Slack Incoming Webhook**
   - 需要設定 3 個 Webhook URL（對應 3 個分支）
   - 將處理結果發送回 Slack

## 使用方法

1. 在 Dify 中匯入此工作流 DSL 檔案
2. 設定 Slack App Mention 觸發器（需要在 Slack 應用中設定）
3. 設定 3 個 Slack Incoming Webhook URL（分別對應 3 個分支）
4. 根據需要調整 Agent 的指令和工具設定
5. 儲存並啟用工作流
6. 在 Slack 中 @ 提及機器人進行測試

## 自訂設定

### 修改分類器類別

在 Question Classifier 節點中修改 `classes` 和 `instruction`：

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

在 Agent 節點的 `instruction` 參數中修改行為規則：

```yaml
instruction:
  type: constant
  value: |
    Your custom instructions here...
```

### 修改機器人名稱和風格

在各個 LLM 節點的 system prompt 中修改：

```yaml
prompt_template:
  - role: system
    text: 'Your name is Jasper. Your role is...'
```

## 注意事項

- 需要在 Slack 應用中設定 App Mention 事件訂閱
- 確保 3 個 Slack Webhook URL 都已正確設定
- Agent 使用的模型需要 API 存取權限
- 建議根據實際使用場景調整分類邏輯和響應風格
- 空訊息或空白訊息會有特殊處理邏輯

## 授權許可

本專案採用 Apache License 2.0。

