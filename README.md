# Telegram Notifier for Claude Code

Claude Code 작업 완료 또는 사용자 입력 대기 시 텔레그램으로 자동 알림을 보내는 스킬입니다.

## 설치

### 1. 텔레그램 봇 생성

1. Telegram에서 **@BotFather** 검색
2. `/newbot` 명령 입력
3. 봇 이름 입력 (예: "Claude Notifier")
4. 봇 사용자명 입력 (`_bot`으로 끝나야 함)
5. 발급된 **Bot Token** 복사

### 2. Chat ID 확인

1. 생성한 봇에게 아무 메시지 발송
2. 브라우저에서 접속:
   ```
   https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
   ```
3. JSON 응답에서 `"chat":{"id":123456789}` 부분의 숫자가 Chat ID

### 3. 환경 변수 설정

`~/.zshrc` 또는 `~/.bashrc`에 추가:

```bash
export TELEGRAM_BOT_TOKEN="1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"
export TELEGRAM_CHAT_ID="123456789"
```

적용:
```bash
source ~/.zshrc
```

### 4. Claude Code Hooks 설정

`~/.claude/settings.json`에 hooks 추가:

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

## 사용법

### 자동 알림

설정 완료 후 Claude Code가 다음 상황에서 자동으로 텔레그램 알림을 발송합니다:

| 상황 | 설명 |
|------|------|
| 작업 완료 | 요청한 작업이 완료되었을 때 |
| 사용자 입력 대기 | 추가 정보나 확인이 필요할 때 |
| 오류 발생 | 작업 중 오류가 발생했을 때 |

### 수동 알림 테스트

```bash
python3 ~/.claude/skills/telegram-notifier/scripts/send_telegram.py "제목" "메시지 내용"
```

## 파일 구조

```
~/.claude/skills/telegram-notifier/
├── SKILL.md                    # 스킬 정의
├── README.md                   # 이 문서
├── scripts/
│   └── send_telegram.py        # 텔레그램 발송 스크립트
└── references/
    └── setup-guide.md          # 상세 설정 가이드
```

## 문제 해결

| 문제 | 해결 방법 |
|------|----------|
| 알림이 오지 않음 | `echo $TELEGRAM_BOT_TOKEN` 으로 환경 변수 확인 |
| 권한 오류 | 봇에게 먼저 메시지를 보냈는지 확인 |
| Hook 미작동 | `~/.claude/settings.json` JSON 문법 오류 확인 |
| 그룹 채팅 알림 안됨 | Chat ID가 음수인지 확인 (그룹은 `-123456789` 형식) |

## 환경 변수

| 변수명 | 설명 | 예시 |
|--------|------|------|
| `TELEGRAM_BOT_TOKEN` | BotFather에서 발급받은 토큰 | `1234567890:ABC...` |
| `TELEGRAM_CHAT_ID` | 알림 받을 채팅 ID | `123456789` |
