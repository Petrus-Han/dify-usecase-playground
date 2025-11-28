# Slack Trigger News Researcher

[English](README.md) | [简体中文](README.zh-Hans.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md)

---

## 概要

これは、Slack でユーザーがボットを @ メンションしたときに、ユーザーの質問タイプに基づいて異なる処理フローにインテリジェントにルーティングするインテリジェントな Slack ボットワークフローです。カジュアルなチャット、技術ニュースのクエリ、回答不可能な質問の処理をサポートします。

## 機能

- 🔔 **Slack トリガー**: Slack App Mention イベントに応答
- 🧠 **スマート分類**: 質問分類器を使用してユーザーの意図を判断
- 💬 **カジュアルチャット**: フレンドリーな日常会話ボット（Jasper）
- 📰 **ニュースリサーチ**: Agent とツールを使用して技術ニュースを検索
- ⚠️ **優雅な処理**: 質問に答えられない場合にフレンドリーなプロンプトを提供

## ワークフロー構造

```
Slack Trigger → Question Classifier → [3つのブランチ]
                                    ├─ Casual Chat → LLM → Slack Webhook
                                    ├─ Tech News Inquiry → Agent → Slack Webhook
                                    └─ Unanswerable → LLM → Slack Webhook
```

### ノード説明

1. **Slack Trigger (App Mention)**
   - Slack の @ メンションイベントをリッスン
   - ユーザーメッセージテキストを抽出

2. **Question Classifier**
   - GPT-4o-mini を使用してユーザーの質問を分類
   - 3つのカテゴリ：
     - **Casual Chat**: 日常会話、挨拶、雑談
     - **Tech News Inquiry**: 技術ニュースのクエリ、最新情報
     - **Unanswerable**: 正確に答えられない質問

3. **Casual Chat ブランチ**
   - GPT-4o-mini を使用して日常会話を実行
   - ボット名: Jasper
   - フレンドリーな日常コミュニケーションスタイル

4. **Tech News Inquiry ブランチ**
   - Agent（GPT-5.1）を使用してニュースリサーチを実行
   - 利用可能なツール：
     - Google Search: ウェブ検索
     - Yahoo Finance News: 株式ニュース
     - Current Time: 現在時刻を取得

5. **Unanswerable ブランチ**
   - GPT-4o-mini を使用して答えられない質問を処理
   - フレンドリーに理由を説明し、ユーザーに再質問を促す

## 設定

### 依存関係

- `langgenius/slack:0.0.4` - Slack 統合プラグイン
- `langgenius/openai:0.2.7` - OpenAI モデルプラグイン

### 環境変数

追加の環境変数は不要です。

### ツール設定

1. **Google Search**
   - ウェブコンテンツを検索するために使用
   - 言語と国コードの設定をサポート

2. **Yahoo Finance News**
   - 株式関連のニュースを取得
   - パラメータ: `symbol`（株式ティッカー）

3. **Current Time**
   - 現在時刻を取得
   - ニュースの時効性を判断するために使用

4. **Slack Incoming Webhook**
   - 3つの Webhook URL が必要（3つのブランチに対応）
   - 処理結果を Slack に送信

## 使用方法

1. このワークフロー DSL ファイルを Dify にインポート
2. Slack App Mention トリガーを設定（Slack アプリで設定が必要）
3. 3つの Slack Incoming Webhook URL を設定（それぞれ3つのブランチに対応）
4. 必要に応じて Agent の指示とツール設定を調整
5. ワークフローを保存して有効化
6. Slack でボットを @ メンションしてテスト

## カスタマイズ

### 分類器カテゴリの変更

Question Classifier ノードで `classes` と `instruction` を変更：

```yaml
classes:
  - id: '1'
    name: Casual Chat — everyday conversation...
  - id: '2'
    name: Tech News Inquiry — asking about current technology...
  - id: '3'
    name: Unanswerable (Insufficient Information)...
```

### Agent 指示の変更

Agent ノードの `instruction` パラメータで動作規則を変更：

```yaml
instruction:
  type: constant
  value: |
    Your custom instructions here...
```

### ボット名とスタイルの変更

各 LLM ノードの system prompt で変更：

```yaml
prompt_template:
  - role: system
    text: 'Your name is Jasper. Your role is...'
```

## 注意事項

- Slack アプリで App Mention イベントサブスクリプションの設定が必要
- 3つの Slack Webhook URL がすべて正しく設定されていることを確認
- Agent モデルには API アクセス権限が必要
- 実際の使用シナリオに応じて分類ロジックと応答スタイルを調整することを推奨
- 空のメッセージや空白メッセージには特別な処理ロジックがあります

## ライセンス

このプロジェクトは Apache License 2.0 を使用しています。

