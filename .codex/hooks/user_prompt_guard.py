import json
import sys


def main():
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError:
        event = {}

    guardrails = "\n".join(
        [
            "HASSION project guardrails:",
            "- Maintain a premium, minimal B2B OEM leather goods website tone.",
            "- Avoid Alibaba, Taobao, export-template, or generic catalog styling.",
            "- Read AGENTS.md before making website changes.",
            "- Do not do broad polish passes without a plan and approval.",
            "- Keep each change narrow and controlled.",
            "- Protect contact form logic, FormSubmit action/hidden fields, _next, thanks.html, WhatsApp URLs, and product image paths.",
            "- Do not commit or push unless explicitly requested.",
            "- After edits, show exact files changed, git status, and diff summary.",
        ]
    )

    output = {
        "hookSpecificOutput": {
            "hookEventName": event.get("hook_event_name", "UserPromptSubmit"),
            "additionalContext": guardrails,
        }
    }
    print(json.dumps(output))


if __name__ == "__main__":
    main()
