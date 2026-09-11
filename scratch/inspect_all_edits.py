import os, json, glob

brain_dir = r"C:\Users\HP\.gemini\antigravity-ide\brain"
conv_dirs = sorted(glob.glob(os.path.join(brain_dir, "*")), key=os.path.getmtime)

for cd in conv_dirs:
    log_file = os.path.join(cd, ".system_generated", "logs", "transcript_full.jsonl")
    if not os.path.exists(log_file):
        continue
    print(f"\n============================== CONVERSATION {os.path.basename(cd)} ==============================")
    with open(log_file, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            try:
                data = json.loads(line)
                t = data.get("type")
                if t == "USER_INPUT":
                    print(f"\n[USER_INPUT step={data.get('step_index')}] line={idx}")
                    print(data.get("content", ""))
                elif t == "PLANNER_RESPONSE":
                    calls = data.get("tool_calls")
                    if calls:
                        for c in calls:
                            name = c.get("name")
                            if name in ("replace_file_content", "multi_replace_file_content", "write_to_file"):
                                print(f"[FILE_EDIT step={data.get('step_index')}] {name} on {c.get('args', {}).get('TargetFile')}")
                                if name == "replace_file_content":
                                    print("  TargetContent:", repr(c.get('args', {}).get('TargetContent')[:150]))
                                    print("  ReplacementContent:", repr(c.get('args', {}).get('ReplacementContent')[:150]))
            except Exception as e:
                pass
