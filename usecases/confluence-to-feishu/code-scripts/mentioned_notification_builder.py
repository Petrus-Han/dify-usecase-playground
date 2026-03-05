import json


def _name_from_email(email: str) -> str:
    """Extract display name from email: peter.han@dify.ai -> Peter Han"""
    local = email.split("@")[0] if "@" in email else email
    parts = local.replace("_", ".").replace("-", ".").split(".")
    return " ".join(p.capitalize() for p in parts if p)


def _format_time(raw: str) -> str:
    """Format ISO time to readable: 2026-03-04T10:00:45.5+0000 -> 2026-03-04 10:00 UTC"""
    if not raw:
        return ""
    try:
        date_part = raw[:10]
        time_part = raw[11:16] if len(raw) > 16 else ""
        return f"{date_part} {time_part} UTC" if time_part else date_part
    except Exception:
        return raw


def main(payload: str) -> dict:
    data = json.loads(payload) if isinstance(payload, str) else payload
    if "body" in data and "method" in data:
        data = data["body"]

    page = data.get("page", {})
    blogpost = data.get("blogpost", {})
    mentions = data.get("mentions", {})
    if blogpost.get("title"):
        title, url, content_type = blogpost["title"], blogpost.get("url", ""), "Blog Post"
        author_email = blogpost.get("author", "") or "Someone"
    else:
        title, url, content_type = page.get("title", "Untitled"), page.get("url", ""), "Page"
        author_email = page.get("author", "") or "Someone"
    author = _name_from_email(author_email)

    email = mentions.get("email", "Unknown")
    time = _format_time(data.get("time", ""))

    card = {
        "config": {"wide_screen_mode": True},
        "header": {
            "title": {"tag": "plain_text", "content": "📢 Confluence Mention"},
            "template": "blue",
        },
        "elements": [
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": f"**{author}** mentioned you in a {content_type}",
                },
            },
            {"tag": "hr"},
            {
                "tag": "div",
                "fields": [
                    {"is_short": True, "text": {"tag": "lark_md", "content": f"**📄 {content_type}**\n[{title}]({url})"}},
                    {"is_short": True, "text": {"tag": "lark_md", "content": f"**🕐 Time**\n{time}"}},
                ],
            },
            {"tag": "hr"},
            {
                "tag": "action",
                "actions": [
                    {
                        "tag": "button",
                        "text": {"tag": "plain_text", "content": f"View {content_type}"},
                        "url": url,
                        "type": "primary",
                    }
                ],
            },
            {
                "tag": "note",
                "elements": [
                    {"tag": "plain_text", "content": "Confluence → Dify Notification"},
                ],
            },
        ],
    }

    return {
        "email": email,
        "content": json.dumps(card, ensure_ascii=False),
    }
