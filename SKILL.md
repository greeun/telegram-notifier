---
name: telegram-notifier
description: Send Telegram notifications when tasks complete or user input is needed. Use when setting up notifications, configuring telegram alerts, or when user says "telegram notify", "send telegram", "notify me".
---

# Telegram Notifier

Claude Code 작업 완료 또는 사용자 입력 필요 시 텔레그램으로 알림을 보냅니다.

## Quick Start

### 1. 환경 변수 설정

```bash
# ~/.zshrc 또는 ~/.bashrc에 추가
export TELEGRAM_BOT_TOKEN="your_bot_token"
export TELEGRAM_CHAT_ID="your_chat_id"
```

봇 토큰/채팅 ID가 없다면: [references/setup-guide.md](references/setup-guide.md) 참조

### 2. Claude Code Hooks 설정

`~/.claude/settings.json`에 추가:

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/skills/telegram-notifier/scripts/send_telegram.py \"$CLAUDE_NOTIFICATION_TITLE\" \"$CLAUDE_NOTIFICATION_MESSAGE\""
          }
        ]
      }
    ]
  }
}
```

## 알림 발생 시점

Claude Code는 다음 상황에서 Notification hook을 트리거합니다:

| 상황 | 알림 제목 예시 |
|------|---------------|
| 작업 완료 | "Task completed" |
| 사용자 입력 대기 | "Waiting for input" |
| 오류 발생 | "Error occurred" |

## 수동 알림 테스트

```bash
python3 ~/.claude/skills/telegram-notifier/scripts/send_telegram.py "테스트" "메시지 내용"
```

## Troubleshooting

| 문제 | 해결 |
|-----|-----|
| 알림 안 옴 | `echo $TELEGRAM_BOT_TOKEN` 확인 |
| 권한 오류 | 봇이 채팅방에 추가되었는지 확인 |
| Hook 미작동 | `~/.claude/settings.json` 문법 확인 |
