import json

log_path = r"C:\Users\HP\.gemini\antigravity-ide\brain\6c3f4803-40db-48f8-afd0-9c19e0452aef\.system_generated\logs\transcript_full.jsonl"
with open(log_path, "r", encoding="utf-8") as f:
    for idx, line in enumerate(f):
        data = json.loads(line)
        calls = data.get("tool_calls")
        if calls:
            for c in calls:
                if c.get("args", {}).get("TargetFile") == "c:/Users/HP/Downloads/willbridge-estate-template/blog.html":
                    print(f"=== Tool Call at line {idx} ===")
                    print("START LINE:", c.get("args").get("StartLine"), "END LINE:", c.get("args").get("EndLine"))
                    print("--- TARGET ---")
                    print(c.get("args").get("TargetContent"))
                    print("--- REPLACEMENT ---")
                    print(c.get("args").get("ReplacementContent"))
