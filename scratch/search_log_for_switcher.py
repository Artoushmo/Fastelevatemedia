import json

log_path = "/Users/v/.gemini/antigravity/brain/ab575514-3844-46a3-9db4-a110ad8d87b9/.system_generated/logs/transcript.jsonl"

print("Searching transcript for language switcher occurrences...")

with open(log_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            step = json.loads(line)
            idx = step.get("step_index")
            content = str(step)
            if "EN (US)" in content or "NL (Dutch)" in content:
                print(f"Step {idx}: Type={step.get('type')}, Source={step.get('source')}")
                # Print a bit of content if it's user input
                if step.get('type') == 'USER_INPUT':
                    print("USER INPUT:", step.get('content'))
                elif "tool_calls" in step:
                    # check if replace_file_content or write_to_file is called
                    for tc in step["tool_calls"]:
                        method = tc.get("method")
                        if "replace_file_content" in method or "write" in method:
                            print(f"  Tool Call: {method}")
                            args = tc.get("arguments", {})
                            if isinstance(args, dict):
                                target = args.get("TargetContent", "") or args.get("ReplacementContent", "")
                                if target:
                                    print("  Target/Replacement preview:")
                                    print(target[:300])
        except Exception as e:
            pass
