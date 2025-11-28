# Daily News for Slack Channel

[English](README.md) | [简体中文](README.zh-Hans.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md)

---

## 概要

これは、毎日最新のニュースを取得して Slack チャンネルに送信する自動化ワークフローです。ワークフローはスケジュールトリガーを使用し、Agent とツールノードを組み合わせて、ニュースの自動収集と配信を実現します。

## 機能

- ⏰ **スケジュールトリガー**: 毎日自動実行（デフォルト UTC 9:00、タイムゾーン設定可能）
- 📰 **ニュース取得**: Yahoo Finance News ツールを使用して株式関連のニュースを取得
- 🤖 **スマート Agent**: Claude Opus 4 モデルを使用してニュースの分析と処理を実行
- 📤 **Slack 配信**: Slack Incoming Webhook を介して指定されたチャンネルにメッセージを送信

## ワークフロー構造

```
Schedule Trigger → Agent → Slack Webhook
```

1. **Schedule Trigger**: 毎日1回実行されるスケジュールトリガー
2. **Agent**: 以下の責任を持つインテリジェントエージェント：
   - 現在時刻の取得
   - Yahoo Finance News ツールを使用したニュース検索
   - ニュースコンテンツの分析と整理
3. **Slack Webhook**: 処理されたニュースを Slack チャンネルに送信

## 設定

### 依存関係

- `langgenius/slack:0.0.4` - Slack 統合プラグイン

### 環境変数

追加の環境変数は不要です。

### ツール設定

1. **Yahoo Finance News**
   - 株式ティッカーシンボルに関連するニュースを取得するために使用
   - パラメータ: `symbol`（株式ティッカー、例: NVDA、TSLA）

2. **Current Time**
   - ニュースの時効性を判断するために現在時刻を取得
   - タイムゾーン: UTC（設定可能）

3. **Slack Incoming Webhook**
   - Slack Webhook URL の設定が必要
   - メッセージコンテンツは Agent の出力から取得

## 使用方法

1. このワークフロー DSL ファイルを Dify にインポート
2. Slack Incoming Webhook URL を設定
3. 必要に応じてスケジュールトリガーの実行時間を調整
4. Agent のクエリ内容を変更（デフォルトは NVDA と TSLA のニュースをクエリ）
5. ワークフローを保存して有効化

## カスタマイズ

### クエリ内容の変更

Agent ノードの `query` パラメータでデフォルトクエリを変更：

```yaml
query:
  type: constant
  value: What's the latest on NVDA and TSLA today?
```

### 実行時間の変更

Schedule Trigger ノードで `cron_expression` と `timezone` を変更：

```yaml
cron_expression: 0 9 * * *  # 毎日 9:00 UTC
timezone: America/New_York   # タイムゾーン設定
```

## 注意事項

- Slack プラグインがインストールされ、設定されていることを確認
- Webhook URL が正しく設定されている必要があります。そうでない場合、メッセージを送信できません
- Agent モデルには API アクセス権限が必要
- 実際のニーズに応じてニュースクエリの範囲と頻度を調整することを推奨

## ライセンス

このプロジェクトは Apache License 2.0 を使用しています。

