# discord.py

다기능 Discord 봇: 자가진단 자동화, 역할 관리, 자연어 처리를 지원합니다.

## 개요

discord.py는 Python의 discord.py 라이브러리를 사용하여 제작된 다목적 Discord 봇입니다. 학생들을 위한 COVID-19 자가진단 자동화, 음성 채널 기반 역할 자동 부여, 환영 메시지, 메시지 관리, 자연어 처리 등 다양한 기능을 제공합니다.

## 주요 기능

- **자가진단 자동화**: Selenium으로 교육부 자가진단 시스템 자동 처리
- **역할 자동 부여**: 특정 음성 채널 입장 시 역할 자동 지급
- **환영 메시지**: 신규 멤버 입장 시 자동 환영
- **메시지 관리**: 대량 메시지 삭제 기능
- **봇 자동 퇴장**: 음성 채널에 혼자 남은 봇 자동 퇴장
- **자연어 처리**: KoNLPy를 이용한 한국어 텍스트 분석
- **Google Sheets 연동**: 사용자 정보 저장 및 관리

## 기술 스택

- **discord.py** - Discord 봇 라이브러리
- **Selenium** - 웹 자동화
- **KoNLPy (Okt)** - 한국어 형태소 분석
- **gspread** - Google Sheets API
- **oauth2client** - Google API 인증

## 설치 및 실행

### 사전 요구사항

- Python 3.7 이상
- Chrome 브라우저
- ChromeDriver
- Google Sheets API 인증 파일 (`usekey.json`)

### 1. 저장소 클론

```bash
git clone https://github.com/herbpot/discord.py.git
cd discord.py
```

### 2. 의존성 설치

```bash
pip install -r requirements.txt
```

**requirements.txt 내용:**
```
discord.py
selenium
webdriver-manager
gspread
oauth2client
konlpy
```

### 3. 설정

1. Discord 봇 토큰 설정 (코드 마지막 줄)
```python
bot.run("YOUR_DISCORD_TOKEN")
```

2. Google Sheets API 인증 파일 (`usekey.json`) 준비

3. Google Sheets URL 설정 (코드 159번 줄)

### 4. 실행

```bash
python auto_cleanBot.py
```

## 주요 명령어

| 명령어 | 사용법 | 설명 |
|--------|--------|------|
| `help` | `-help` | 기능 도움말 |
| `helpc` | `-helpc` | 명령어 리스트 |
| `chelp` | `-chelp <명령어>` | 특정 명령어 사용법 |
| `selfinfo` | `-selfinfo 이름 지역 학교급 학교이름 생일 비밀번호` | 자가진단 정보 저장 |
| `selfstart` | `-selfstart 이름` | 자가진단 시작 |
| `setchannel` | `-setchannel 역할 [제외역할] [부여역할]` | 역할 부여 채널 설정 |
| `setchannel` | `-setchannel 환영` | 환영 메시지 채널 설정 |
| `setlist` | `-setlist [역할/환영]` | 설정 확인 |
| `delmsg` | `-delmsg <개수>` | 메시지 삭제 |
| `version` | `-version` | 봇 버전 확인 |
| `ping` | `-ping` | 핑 확인 |

## 기능 상세 설명

### 1. 자가진단 자동화

Selenium을 사용하여 교육부 자가진단 시스템(hcs.eduro.go.kr)에 자동으로 로그인하고 설문을 제출합니다.

#### 사용법

1. **정보 저장**
```
-selfinfo 홍길동 경기도 고등학교 ○○고등학교 051231 1234
```

2. **자가진단 실행**
```
-selfstart 홍길동
```

#### 처리 과정

```python
1. 학교 검색 및 선택
2. 이름/생년월일 입력
3. 비밀번호 입력
4. 설문 자동 체크 (증상 없음)
5. 제출 완료
```

### 2. 역할 자동 부여

특정 음성 채널에 입장한 사용자에게 자동으로 역할을 부여합니다.

#### 설정

```
-setchannel 역할 @학생역할 @인증완료
```

- 음성 채널에 입장한 상태에서 명령어 실행
- `@학생역할`: 이 역할이 있으면 제외
- `@인증완료`: 부여할 역할

### 3. 환영 메시지

새로운 멤버가 서버에 입장하면 자동으로 환영 메시지를 보냅니다.

```
-setchannel 환영
```

출력 예시:
```
@새회원님이 달 저편에 새롭게 착륙하셨습니다 모두 환영해 주세요
```

### 4. 메시지 대량 삭제

```
-delmsg 50
```

최근 50개의 메시지를 삭제합니다 (관리자 권한 필요).

## Google Sheets 연동

### 데이터 구조

| 이름 | 지역 | 학교급 | 학교이름 | 생일 | 비밀번호 |
|------|------|--------|----------|------|----------|
| 홍길동 | 경기도 | 고등학교 | ○○고등학교 | 051231 | 1234 |

### 코드 예시

```python
scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
]
credentials = ServiceAccountCredentials.from_json_keyfile_name('usekey.json', scope)
gc = gspread.authorize(credentials)
doc = gc.open_by_url(spreadsheet_url)
worksheet = doc.worksheet('시트1')
```

## 자동 기능

### 1. 음성 채널 봇 자동 퇴장

음성 채널에 봇만 남으면 자동으로 퇴장:

```python
@bot.event
async def on_voice_state_update(member, before, after):
    if len(before.channel.members) == 1:
        if before.channel.members[0].bot:
            await before.channel.members[0].move_to(None)
```

### 2. 역할 자동 부여

지정된 음성 채널에 입장 시 역할 자동 지급:

```python
if after.channel == rolegiver_dic[guild_id][0]:
    for people in after.channel.members:
        # 제외 역할이 없으면 역할 부여
        await people.add_roles(give_role)
```

## 자연어 처리 (NLP)

KoNLPy Okt를 사용한 간단한 텍스트 분석:

```python
class natural():
    def __init__(self):
        self.okt = Okt()

    def text_process(self, text):
        text_nouns = self.okt.nouns(text)
        for i in range(len(text_nouns)):
            self.text_dic[text_nouns[i]] = True

    def check(self):
        if self.text_dic['뭐']:
            return '지금은 탄생중'
```

## 보안 고려사항

### 민감 정보 관리

```python
# .env 파일 사용 권장
import os
from dotenv import load_dotenv

load_dotenv()
bot.run(os.getenv('DISCORD_TOKEN'))
```

### Google Sheets 인증

```python
# usekey.json을 .gitignore에 추가
echo "usekey.json" >> .gitignore
```

## 주의사항

⚠️ **자가진단 자동화**는 교육 목적으로만 사용하세요. 실제 증상이 있을 경우 반드시 직접 작성하세요.

⚠️ **Discord 토큰**을 GitHub에 업로드하지 마세요.

⚠️ **Google Sheets 인증 파일**을 공유하지 마세요.

## 트러블슈팅

### ChromeDriver 오류

```python
# webdriver-manager 사용 (자동 업데이트)
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    executable_path=ChromeDriverManager().install()
)
```

### Selenium 타임아웃

```python
# 대기 시간 조정
driver.implicitly_wait(10)
time.sleep(3)
```

### Discord 권한 오류

봇에 다음 권한 부여 필요:
- Manage Roles
- Manage Messages
- Manage Channels
- Send Messages
- Embed Links

## 버전 히스토리

- **v2.2.4**: 현재 버전
  - 자가진단 자동화
  - 역할 자동 부여
  - 환영 메시지
  - NLP 기능

## 향후 계획

- [ ] 자가진단 일정 예약 (cron)
- [ ] 웹 대시보드
- [ ] 다국어 지원
- [ ] 로그 시스템
- [ ] 명령어 cooldown
- [ ] 데이터베이스 연동
- [ ] Slash Commands 지원

## 참고 자료

- [discord.py 문서](https://discordpy.readthedocs.io/)
- [Selenium 문서](https://selenium-python.readthedocs.io/)
- [gspread 문서](https://docs.gspread.org/)

## 라이선스

교육 목적으로 작성된 프로젝트입니다.

## 면책 조항

이 봇의 자가진단 자동화 기능은 교육 및 학습 목적으로 제공됩니다. 실제 사용 시 발생하는 문제에 대한 책임은 사용자에게 있습니다.
