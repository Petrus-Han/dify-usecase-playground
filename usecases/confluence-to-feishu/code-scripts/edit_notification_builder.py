import json


def _name_from_email(email: str) -> str:
    local = email.split("@")[0] if "@" in email else email
    parts = local.replace("_", ".").replace("-", ".").split(".")
    return " ".join(p.capitalize() for p in parts if p)


def _format_time(raw: str) -> str:
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
    actor_email = data.get("actor", {}).get("email", "Unknown")
    owner_email = data.get("owner", {}).get("email", "")
    if actor_email == owner_email:
        return {"email": "", "content": ""}
    actor = _name_from_email(actor_email)
    owner = _name_from_email(owner_email) if owner_email else ""
    time = _format_time(data.get("time", ""))

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
                "content": f"Edited by **{actor}**" + (f"  ·  Owner: {owner}" if owner else ""),
            },
        },
        {"tag": "hr"},
        {
            "tag": "action",
            "actions": [
                {
                    "tag": "button",
                    "text": {"tag": "plain_text", "content": "View Page"},
                    "url": page.get("url", ""),
                    "type": "primary",
                }
            ],
        },
        {
            "tag": "note",
            "elements": [
                {"tag": "plain_text", "content": f"{time}  ·  Confluence Notification"},
            ],
        },
    ]

    card = {
        "config": {"wide_screen_mode": True},
        "header": {
            "title": {"tag": "plain_text", "content": "✏️ Confluence Page Edited"},
            "template": "turquoise",
        },
        "elements": elements,
    }

    return {
        "email": owner_email,
        "content": json.dumps(card, ensure_ascii=False),
    }
