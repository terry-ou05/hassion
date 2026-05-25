import json
import os
import subprocess
import sys


def run_git(args, cwd):
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
    except Exception as exc:
        return f"Unable to run git {' '.join(args)}: {exc}"

    output = (result.stdout or result.stderr).strip()
    return output if output else "(no output)"


def main():
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError:
        event = {}

    cwd = event.get("cwd") or "."
    if not os.path.isdir(cwd):
        cwd = "."
    status = run_git(["status", "--short"], cwd)
    diff_stat = run_git(["diff", "--stat"], cwd)

    checklist = "\n".join(
        [
            "HASSION final checklist:",
            "- Confirm exact files changed.",
            "- Confirm protected FormSubmit, _next, thanks.html, WhatsApp URLs, and product image paths are unchanged unless requested.",
            "- Confirm no commit or push was made unless explicitly requested.",
            "",
            "git status --short:",
            status,
            "",
            "git diff --stat:",
            diff_stat,
        ]
    )

    print(json.dumps({"systemMessage": checklist}))


if __name__ == "__main__":
    main()
