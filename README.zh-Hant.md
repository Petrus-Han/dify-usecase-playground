# Dify Use Case Playground

> 🎯 真實場景的 Dify 工作流 DSL 範例和用例集合

[English](README.md) | [简体中文](README.zh-Hans.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md)

---

## 專案簡介

**Dify Use Case Playground** 是一個個人開源專案，收集了實用的 Dify 工作流 DSL 範例和用例。本倉庫旨在為使用 Dify 工作流引擎構建生產級工作流提供學習資源和參考。

## 內容說明

本倉庫包含：

- 📋 **工作流 DSL 檔案** (`.yml`) - 可直接匯入 Dify 的完整工作流定義
- 📖 **文件說明** (`README.md`) - 每個用例的詳細說明
- 🎨 **最佳實踐** - 真實場景的模式和解決方案

## 特性

- ✅ 生產級工作流
- ✅ 完整的文件說明
- ✅ 易於匯入和自訂
- ✅ 真實場景用例
- ✅ 最佳實踐和模式
- 🔒 **安全保護**：透過 CI/CD 自動掃描敏感資訊

## 用例列表

### 🤖 自動化

- **[每日新聞推送到 Slack](./usecases/daily-news-slack/)** - 使用定時觸發器自動將每日新聞推送到 Slack 頻道

### 💬 聊天機器人和助手

- **[Slack 觸發新聞研究助手](./usecases/slack-news-researcher/)** - 具有問題分類和新聞研究能力的智能 Slack 機器人

## 快速開始

1. **瀏覽用例**
   - 查看 `usecases/` 目錄
   - 每個用例都有自己的資料夾，包含 `workflow.yml` 和 `README.md`

2. **匯入工作流**
   - 開啟 Dify 控制台
   - 從用例資料夾匯入 `.yml` 檔案
   - 按照用例 README 中的設定說明進行操作

3. **自訂**
   - 根據需求修改工作流
   - 更新設定參數
   - 測試並部署

## 目錄結構

```
.
├── README.md                 # 本檔案（英文）
├── README.zh-Hans.md         # 簡體中文
├── README.zh-Hant.md         # 繁體中文
├── README.ja.md              # 日文
├── LICENSE                   # Apache 2.0 授權許可
├── .gitignore               # Git 忽略規則
├── .gitleaks.toml          # 敏感資訊掃描設定
├── .github/
│   └── workflows/
│       ├── secret-scanning.yml      # CI/CD 敏感資訊掃描工作流
│       └── code-language-check.yml  # CI/CD 語言檢查工作流
└── usecases/                 # 用例集合
    ├── daily-news-slack/
    │   ├── workflow.yml      # 工作流 DSL 檔案
    │   └── README.md         # 用例文件（英文）
    └── slack-news-researcher/
        ├── workflow.yml      # 工作流 DSL 檔案
        └── README.md         # 用例文件（英文）
```

## 環境要求

- [Dify](https://github.com/langgenius/dify) 平台存取權限
- 所需的插件和 API 金鑰（參見各用例的 README）

## 安全說明

🔒 **本倉庫使用自動化的敏感資訊掃描**，防止意外提交敏感資訊：

- **CI/CD 整合**：GitHub Actions 工作流會在每次推送和拉取請求時自動掃描敏感資訊
- **使用的工具**：
  - [Gitleaks](https://github.com/gitleaks/gitleaks) - 全面的金鑰檢測
  - 自訂模式匹配常見敏感資料
- **檢查內容**：API 金鑰、令牌、密碼、Webhook URL、AWS 金鑰、Slack 令牌等

**重要提示**：請勿提交敏感資訊，如 API 金鑰、令牌或憑證。請使用環境變數或安全的設定管理方式。

## 程式碼語言要求

🌐 **本專案保持國際化定位。**

- ✅ **程式碼檔案可以包含中文或其他語言** - 鼓勵用於國際化（i18n）支援
- ✅ Dify 工作流檔案中的 i18n 欄位（`zh_Hans`, `zh_Hant`, `ja_JP`, `pt_BR` 等）完全支援
- ✅ **Git 提交資訊必須使用英文** - 以保持國際化專案定位
- ✅ **Pull request 標題和描述必須使用英文** - 便於全球協作
- 📖 文件檔案提供多種語言版本（英文、簡體中文、繁體中文、日文）

**注意**：CI 檢查會強制要求 git 提交資訊和 PR 內容使用英文，但允許程式碼檔案中使用任何語言以支援國際化。

## 貢獻

這是一個個人專案，但歡迎建議和回饋！你可以：

- 提交 issue 報告問題或提出功能請求
- 提交 pull request 進行改進
- 分享你自己的用例

## 授權許可

本專案採用 Apache License 2.0 - 詳見 [LICENSE](LICENSE) 檔案。

---

## 作者

個人專案 by [@petrus](https://github.com/petrus)

---

**注意**：本倉庫作為個人學習和參考資源維護。用例基於真實場景，可能需要根據你的具體需求進行自訂。

