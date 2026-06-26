# 시스템 허브 (정적 사이트)

QR로 여는 작은 도구들을 한곳에 모은 정적 사이트입니다. 서버가 필요 없어 GitHub Pages에 그대로 올리면 됩니다.
각 "시스템"은 systems 폴더 안의 독립된 디렉터리이고, 디렉터리를 추가하면 허브에 자동으로 나타납니다.

## 구조
```
index.html                      허브(시스템 목록)
shared/
  theme.css                     공통 디자인
  discover.js                   폴더 자동 인식 도우미
systems/
  registry.json                 (자동) 시스템 목록
  sound/                        [시스템] 소리 재생
    index.html
    system.json                 허브에 표시될 제목/설명/아이콘/색
    sounds/
      manifest.json             (자동) 사운드 목록
      animal/ inst/ nature/ fx/ melody/  *.mp3
  qr/                           [시스템] QR 생성
    index.html
    system.json
.github/workflows/build.yml     registry/manifest 자동 갱신
```

## 새 시스템 추가하기
1. `systems/<이름>/` 폴더를 만듭니다.
2. 그 안에 `index.html`(페이지)과 `system.json`을 넣습니다.
   ```json
   { "title": "표시 이름", "desc": "한 줄 설명", "icon": "🎲", "color": "#4FD6B8", "order": 3 }
   ```
3. push 하면 허브 목록에 자동으로 추가됩니다. (허브 코드는 수정 불필요)
   - 페이지에서 공통 디자인을 쓰려면: `<link rel="stylesheet" href="../../shared/theme.css">`
   - 폴더 자동 인식이 필요하면: `<script src="../../shared/discover.js"></script>` 후 `Discover.listFiles("폴더")`

## 소리 추가/변경 (소리 재생 시스템)
- `systems/sound/sounds/<카테고리>/` 폴더에 mp3 파일만 넣고 push 하면 자동 인식됩니다.
- 화면에는 확장자를 뺀 **파일명**이 그대로 표시됩니다. 예) `호랑이.mp3` → "호랑이"
- 새 카테고리는 폴더를 만들고 `systems/sound/index.html` 의 CATS 배열에 한 줄 추가하면 됩니다.

## 동작 방식
- GitHub Pages에서는 저장소 파일 트리를 읽어 폴더 내용을 **실시간** 반영합니다(폴더에 넣고 push하면 끝).
- 깃헙이 아닌 환경에서는 registry.json / manifest.json 을 사용하며, build.yml 액션이 push 때마다 자동 생성합니다.

## 배포 (GitHub Pages)
1. github.com에서 Public 저장소 생성
2. 이 폴더 전체(.github 포함)를 업로드 후 commit
3. Settings → Pages → Source: Deploy from a branch, Branch: main / (root) → Save
4. 1~2분 후: https://아이디.github.io/저장소이름/

## 로컬 미리보기
```
python3 -m http.server
# http://localhost:8000 접속
```

동봉된 mp3는 데모용 합성음입니다. 실제 음원으로 교체해서 쓰세요.
