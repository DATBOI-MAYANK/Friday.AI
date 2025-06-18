import re
import time
import subprocess

NOTIFY_CMD = ["notify-send"]
MAX_DELAY = 300  # optional safety: max 5 minutes

def parse_and_notify(response: str) -> bool:
    match = re.search(r"\(notify,(\d+)\)\s*(.+)", response, re.DOTALL)
    if match:
        delay = min(int(match.group(1)), MAX_DELAY)
        message = match.group(2).strip()

        try:
            time.sleep(delay)
            subprocess.run(NOTIFY_CMD + [message], check=True)
            print(f"[Notification sent after {delay} seconds]: {message}")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to send notification.")
    return False
