import json


def _name_from_email(email: str) -> str:
    local = email.split("@")[0] if "@" in email else email
    parts = local.replace("_", ".").replace("-", ".").split(".")
    return " ".join(p.capitalize() for p in parts if p)


def main(payload: str) -> dict:
    data = json.loads(payload) if isinstance(payload, str) else payload
    if "body" in data and "method" in data:
        data = data["body"]

    page = data.get("page", {})
    comment = data.get("comment", {})

    owner_email = page.get("owner", "Unknown")
    actor_email = comment.get("author", "Unknown")
    if actor_email == owner_email:
        return {"email": "", "content": ""}
    actor = _name_from_email(actor_email)
    body = comment.get("body", "")
    if len(body) > 200:
        body = body[:200] + "..."
    elements = [
        {
            "tag": "div",
            "text": {
                "tag": "lark_md",
                "content": f"**[{page.get('title', 'Untitled')}]({page.get('url', '')})**",
            },
        },
        {
            "tag": "div",
            "text": {
                "tag": "lark_md",
                "content": f"Comment by **{actor}**",
            },
        },
    ]

    if body:
        elements.append({
            "tag": "div",
            "text": {"tag": "lark_md", "content": f"> {body}"},
        })

    elements.append({"tag": "hr"})

    actions = []
    if page.get("url"):
        actions.append({
            "tag": "button",
            "text": {"tag": "plain_text", "content": "View Page"},
            "url": page["url"],
            "type": "primary",
        })
    if comment.get("url"):
        actions.append({
            "tag": "button",
            "text": {"tag": "plain_text", "content": "View Comment"},
            "url": comment["url"],
            "type": "default",
        })
    if actions:
        elements.append({"tag": "action", "actions": actions})

    elements.append({
        "tag": "note",
        "elements": [
            {"tag": "plain_text", "content": "Confluence Notification"},
        ],
    })

    card = {
        "config": {"wide_screen_mode": True},
        "header": {
            "title": {"tag": "plain_text", "content": "💬 Confluence Comment"},
            "template": "green",
        },
        "elements": elements,
    }

    return {
        "email": owner_email,
        "content": json.dumps(card, ensure_ascii=False),
    }
