import re
import time
import subprocess

NOTIFY_CMD = ["notify-send"]
MAX_DELAY = 300  # seconds

def parse_and_notify(response: str) -> bool:
    print("[DEBUG] Raw LLM response:", repr(response))

    match = re.search(r"\(notify,(\d+)\)\s*(.+)", response, re.DOTALL)
    if match:
        delay = min(int(match.group(1)), MAX_DELAY)
        message = match.group(2).strip()

        print(f"[DEBUG] Parsed Notify: delay={delay}, message={message}")
        time.sleep(delay)
        subprocess.run(NOTIFY_CMD + [message], check=True)
        print(f"[✅ Notification sent after {delay} seconds]: {message}")
        return True
    else:
        print("⚠️ No valid notify pattern matched.")
        return False
