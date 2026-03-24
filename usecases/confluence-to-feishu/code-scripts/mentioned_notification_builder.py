import json


def _name_from_email(email: str) -> str:
    """Extract display name from email: peter.han@dify.ai -> Peter Han"""
    local = email.split("@")[0] if "@" in email else email
    parts = local.replace("_", ".").replace("-", ".").split(".")
    return " ".join(p.capitalize() for p in parts if p)


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
                "text": {
                    "tag": "lark_md",
                    "content": f"**📄 {content_type}:** [{title}]({url})",
                },
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
