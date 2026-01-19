# Telegram Bot Setup Guide

## 1. 봇 생성

1. Telegram에서 [@BotFather](https://t.me/BotFather) 검색
2. `/newbot` 명령 입력
3. 봇 이름 입력 (예: "My Claude Notifier")
4. 봇 사용자명 입력 (예: "my_claude_notifier_bot", `_bot`으로 끝나야 함)
5. **Bot Token** 복사 (예: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)

## 2. Chat ID 확인

### 방법 A: 개인 채팅

1. 생성한 봇에게 아무 메시지 발송
2. 브라우저에서 접속:
   ```
   https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
   ```
3. JSON 응답에서 `"chat":{"id":123456789}` 찾기
4. 숫자가 Chat ID

### 방법 B: 그룹 채팅

1. 봇을 그룹에 추가
2. 그룹에서 아무 메시지 발송
3. 위 URL 접속하여 Chat ID 확인 (그룹은 음수: `-123456789`)

## 3. 환경 변수 설정

```bash
# ~/.zshrc 또는 ~/.bashrc에 추가
export TELEGRAM_BOT_TOKEN="1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"
export TELEGRAM_CHAT_ID="123456789"
```

저장 후:
```bash
source ~/.zshrc  # 또는 source ~/.bashrc
```

## 4. 테스트

```bash
python3 ~/.claude/skills/telegram-notifier/scripts/send_telegram.py "테스트" "설정 완료!"
```

텔레그램으로 메시지가 오면 성공입니다.
