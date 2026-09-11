import json

log_path = r"C:\Users\HP\.gemini\antigravity-ide\brain\6c3f4803-40db-48f8-afd0-9c19e0452aef\.system_generated\logs\transcript_full.jsonl"
with open(log_path, "r", encoding="utf-8") as f:
    for idx, line in enumerate(f):
        data = json.loads(line)
        calls = data.get("tool_calls")
        if calls:
            for c in calls:
                name = c.get("name")
                if "replace" in name or "write" in name:
                    print(f"--- Line {idx} Step {data.get('step_index')} Tool {name} ---")
                    args = c.get("args")
                    print("TargetFile:", args.get("TargetFile"))
                    print("StartLine:", args.get("StartLine"), "EndLine:", args.get("EndLine"))
                    print("TargetContent:\n", args.get("TargetContent"))
                    print("ReplacementContent:\n", args.get("ReplacementContent"))
                    print("="*60)
