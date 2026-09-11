import json

log_path = r"C:\Users\HP\.gemini\antigravity-ide\brain\6c3f4803-40db-48f8-afd0-9c19e0452aef\.system_generated\logs\transcript_full.jsonl"
with open(log_path, "r", encoding="utf-8") as f:
    for idx, line in enumerate(f):
        data = json.loads(line)
        calls = data.get("tool_calls")
        if calls:
            for c in calls:
                if c.get("name") == "replace_file_content":
                    print(f"=== Call at index {idx} ===")
                    print("TargetFile:", c.get("args").get("TargetFile"))
                    print("TARGET CONTENT:\n" + c.get("args").get("TargetContent"))
                    print("\nREPLACEMENT CONTENT:\n" + c.get("args").get("ReplacementContent"))
                    print("="*80)
