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


def _build_card(header_title, body_line, page, actor, old_owner, new_owner, space, time):
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
            "text": {"tag": "lark_md", "content": body_line},
        },
    ]

    if space:
        elements.append({
            "tag": "div",
            "text": {"tag": "lark_md", "content": f"Space: {space}"},
        })

    elements.append({"tag": "hr"})
    elements.append({
        "tag": "action",
        "actions": [
            {
                "tag": "button",
                "text": {"tag": "plain_text", "content": "View Page"},
                "url": page.get("url", ""),
                "type": "primary",
            }
        ],
    })
    elements.append({
        "tag": "note",
        "elements": [
            {"tag": "plain_text", "content": f"{time}  ·  Confluence Notification"},
        ],
    })

    return {
        "config": {"wide_screen_mode": True},
        "header": {
            "title": {"tag": "plain_text", "content": header_title},
            "template": "orange",
        },
        "elements": elements,
    }


def main(payload: str) -> dict:
    data = json.loads(payload) if isinstance(payload, str) else payload
    if "body" in data and "method" in data:
        data = data["body"]

    page = data.get("page", {})
    actor_email = data.get("actor", {}).get("email", "Unknown")
    old_owner_email = data.get("owner", {}).get("old", {}).get("email", "Unknown")
    new_owner_email = data.get("owner", {}).get("new", {}).get("email", "Unknown")
    time = _format_time(data.get("time", ""))

    actor = _name_from_email(actor_email)
    old_owner = _name_from_email(old_owner_email)
    new_owner = _name_from_email(new_owner_email)

    space_name = page.get("space_name", "")
    space_key = page.get("space_key", "")
    space = f"{space_name} ({space_key})" if space_name and space_key else space_name or space_key

    card_new = _build_card(
        header_title="🔄 You are the new page owner",
        body_line=f"**{actor}** assigned you as the owner\nPrevious owner: {old_owner}",
        page=page, actor=actor, old_owner=old_owner, new_owner=new_owner, space=space, time=time,
    )

    card_old = _build_card(
        header_title="🔄 Page ownership transferred",
        body_line=f"**{actor}** transferred ownership to **{new_owner}**",
        page=page, actor=actor, old_owner=old_owner, new_owner=new_owner, space=space, time=time,
    )

    return {
        "new_owner_email": new_owner_email,
        "new_owner_content": json.dumps(card_new, ensure_ascii=False),
        "old_owner_email": old_owner_email,
        "old_owner_content": json.dumps(card_old, ensure_ascii=False),
    }
