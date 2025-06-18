import re
import time
import subprocess

def parse_and_notify(response):
    match = re.search(r"\(notify,(\d+)\)\s*(.+)", response, re.DOTALL)
    if match:
        delay = int(match.group(1))
        message = match.group(2).strip()
        time.sleep(delay)
        subprocess.run(["notify-send", message])
        print(f"[Notification sent after {delay} seconds]: {message}")
        return True
    return False
