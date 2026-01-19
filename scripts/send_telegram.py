#!/usr/bin/env python3
"""Send Telegram notification via Bot API."""

import os
import sys
import urllib.request
import urllib.parse
import json

def send_telegram(title: str, message: str) -> bool:
    """Send a message to Telegram."""
    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")

    if not bot_token or not chat_id:
        print("Error: TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID not set", file=sys.stderr)
        return False

    # Format message
    text = f"🤖 *Claude Code*\n\n*{title}*\n{message}"

    # Prepare API request
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }).encode("utf-8")

    try:
        req = urllib.request.Request(url, data=data)
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read().decode("utf-8"))
            if result.get("ok"):
                print("Notification sent successfully")
                return True
            else:
                print(f"API error: {result}", file=sys.stderr)
                return False
    except Exception as e:
        print(f"Failed to send notification: {e}", file=sys.stderr)
        return False


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: send_telegram.py <title> <message>", file=sys.stderr)
        sys.exit(1)

    title = sys.argv[1]
    message = sys.argv[2]

    success = send_telegram(title, message)
    sys.exit(0 if success else 1)
