# Confluence to Feishu Notifications

[English](README.md)

---

## Introduction

This workflow receives Confluence activity events via Dify's built-in Webhook Start node and sends rich interactive notification cards to Feishu (Lark). It uses Confluence Automation rules to push webhook payloads, and Dify code nodes to route events and build Feishu cards.

## Features

- 📢 **@Mention Notifications**: Get notified when someone mentions you in a page or blog post
- 💬 **Comment Notifications**: Get notified when comments are added to pages
- ✏️ **Page Edit Notifications**: Get notified when pages are created or updated
- 🔄 **Ownership Transfer Notifications**: Get notified when page ownership changes (notifies both old and new owner)
- 🎨 **Rich Feishu Cards**: Interactive cards with page links, actor info, and action buttons

## Workflow Structure

```
Webhook Start → Code (event router) → IF/ELSE branching
    → Code (build mention card) → Feishu Send
    → Code (build comment card) → Feishu Send
    → Code (build page edited card) → Feishu Send
    → Code (build owner changed card) → Feishu Send (new owner) + Feishu Send (old owner)
```

1. **Webhook Start**: Dify built-in `trigger-webhook` node receives the raw JSON payload
2. **Code Node (Event Router)**: Extracts `event_type` from the payload
3. **IF/ELSE Branching**: Routes to the matching code node based on event type
4. **Code Nodes (Card Builders)**: Build Feishu interactive card JSON for each event type
5. **Feishu Send**: Sends the card to the recipient via Feishu Bot Message

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
