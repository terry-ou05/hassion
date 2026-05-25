import json
import re
import sys


DANGEROUS_PATTERNS = [
    (re.compile(r"\bgit\s+push\b", re.I), "git push is blocked unless explicitly requested."),
    (re.compile(r"\bgit\s+commit\b", re.I), "git commit is blocked unless explicitly requested."),
    (re.compile(r"\bgit\s+reset\s+--hard\b", re.I), "git reset --hard is blocked."),
    (re.compile(r"\bgit\s+clean\b(?=.*-[a-z]*f)(?=.*-[a-z]*d)", re.I), "git clean -fd is blocked."),
    (re.compile(r"\brm\s+-(?:rf|fr)\b", re.I), "rm -rf is blocked."),
]

PROTECTED_TERMS = ["formsubmit.co", "_next", "thanks.html", "wa.me", "whatsapp"]


def flatten_strings(value):
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        strings = []
        for item in value.values():
            strings.extend(flatten_strings(item))
        return strings
    if isinstance(value, list):
        strings = []
        for item in value:
            strings.extend(flatten_strings(item))
        return strings
    return []


def main():
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError:
        event = {}

    tool_input = event.get("tool_input", {})
    haystack = "\n".join(flatten_strings(tool_input))

    for pattern, reason in DANGEROUS_PATTERNS:
        if pattern.search(haystack):
            print(json.dumps({"decision": "block", "reason": reason}))
            return

    lowered = haystack.lower()
    mentioned = [term for term in PROTECTED_TERMS if term in lowered]
    if mentioned:
        warning = (
            "HASSION guardrail: this tool input mentions protected website terms "
            f"({', '.join(mentioned)}). Verify these are intentionally unchanged unless "
            "the user explicitly requested the change."
        )
        print(
            json.dumps(
                {
                    "hookSpecificOutput": {
                        "hookEventName": event.get("hook_event_name", "PreToolUse"),
                        "additionalContext": warning,
                    }
                }
            )
        )
        return

    print("{}")


if __name__ == "__main__":
    main()
