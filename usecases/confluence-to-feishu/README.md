# Confluence to Feishu Notifications

[English](README.md)

---

## Introduction

This workflow receives Confluence activity events via Dify's built-in Webhook Start node and sends rich interactive notification cards to Feishu (Lark). It uses Confluence Automation rules to push webhook payloads, and Dify code nodes to route events and build Feishu cards.

## Features

### Notification Types

| Event | Recipient | Card Style | Description |
|---|---|---|---|
| 📢 **@Mention** | Mentioned user | Blue card | Someone mentions you in a page or blog post |
| 💬 **Comment** | Page owner | Green card | Someone comments on your page (with comment preview) |
| ✏️ **Page Edited** | Page owner | Turquoise card | Someone edits your page |
| 🔄 **Ownership Transfer** | New owner + Old owner | Orange card | Page ownership is transferred (both parties notified) |

### Smart Filtering

- **Self-action suppression**: If you comment on or edit your own page, no notification is sent — avoids unnecessary noise
- Notifications are always sent to the **page owner**, not the person who performed the action
- Ownership transfer is the exception: both old and new owners are notified

### Rich Feishu Cards

All notifications are sent as interactive Feishu cards with:
- Page title with clickable link
- Actor information (who performed the action)
- Action buttons (View Page, View Comment, etc.)
- Timestamp footer

## Workflow Structure

```
Webhook Start → Code (event router) → IF/ELSE (event type branching)
    → Code (build mention card) → Feishu Send
    → Code (build comment card) → IF/ELSE (skip self-action) → Feishu Send
    → Code (build page edited card) → IF/ELSE (skip self-action) → Feishu Send
    → Code (build owner changed card) → Feishu Send (new owner) + Feishu Send (old owner)
```

1. **Webhook Start**: Dify built-in `trigger-webhook` node receives the raw JSON payload
2. **Code Node (Event Router)**: Extracts `event_type` from the payload
3. **IF/ELSE Branching**: Routes to the matching code node based on event type
4. **Code Nodes (Card Builders)**: Build Feishu interactive card JSON and determine the recipient
5. **IF/ELSE Filter**: For comment and edit events, checks if the email output is non-empty (skips when actor == page owner)
6. **Feishu Send**: Sends the card to the recipient via Feishu Bot Message

## Configuration

### Dependencies

- `langgenius/feishu_message` - Feishu message plugin

### Step 1: Import Workflow

Import `workflow.yml` into your Dify instance.

### Step 2: Configure Feishu

Configure the Feishu message plugin with your Feishu Bot credentials.

### Step 3: Configure Confluence Automation

In your Confluence instance, create Automation rules that send webhooks to the Dify workflow's webhook URL. Use the JSON templates in `confluence-automation-templates/` as the request body.

Create 4 Automation rules:

| Confluence Trigger | Template File | `event_type` Value |
|---|---|---|
| User mentioned | `mention.json` | `mention` |
| Comment created | `comment.json` | `comment` |
| Page updated | `page_edited.json` | `page_edited` |
| Page owner changed | `page_owner_changed.json` | `page_owner_changed` |

For each rule:
1. Set the trigger condition in Confluence Automation
2. Add a **Send web request** action
3. Set the URL to the Dify workflow's webhook URL
4. Set Content-Type to `application/json`
5. Paste the corresponding JSON template as the request body

### Confluence Automation Templates

The `confluence-automation-templates/` folder contains JSON payload templates using Confluence smart values (e.g., `{{page.title}}`, `{{user.emailAddress}}`). Each template includes an `event_type` field that the workflow uses to route events to the correct card builder.

## Notes

- No Confluence API credentials are required — all data comes from the webhook payload sent by Confluence Automation
- Email addresses from Confluence are used to match Feishu users (requires email match between Atlassian and Feishu accounts)
- Card content is built entirely in code nodes using the Feishu interactive card JSON format

## License

This project uses the Apache License 2.0.
