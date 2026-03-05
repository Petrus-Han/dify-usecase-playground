import json


def main(payload: str) -> dict:
    data = json.loads(payload) if isinstance(payload, str) else payload
    if "body" in data and "method" in data:
        data = data["body"]
    return {"result": data.get("event_type", "unknown")}
