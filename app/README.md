# 유튜브 백엔드 구현

## 1. REST API

### (1) 모델 구조

1. User (Custom)

- email
- password
- nickname
- is_business(boolean) : personal, business

2. Video

- title
- link
- description
- category
- views_count
- thumbnail
- video_uploaded_url(S3)
- video_file(FileField)
- User: FK

3. Likes/Dislike

- User:FK
- Video:FK
  Video: Like / Dislike(1:N)

4. Comment

- User:FK
- Video:FK
- like
- dislike

5. Subcription

- User:FK => subscriber (구독한) -> 내가 구독한 사람
- User:FK => subscribed_to (구독을 당한) -> 나를 구독한 사람

6. Notification

- User:FK
- message
- is_read

7. Common

- created_at
- updated_at

8. Chatting (예정)

- User:FK (nickname)

## 수업진행

- 1일차: project Settings (Docker => Django, Github => Github Actions(CI))
- 2일차:
  - project Settings (PostgreSQL)
  - 연결 하는 부분 작업 (DB 컨테이너가 준비될 때 까지 Django 커멘드 명령을 통해서 DB 연결 재시도)
  - CustomUser Model
    - 왜 커스텀 유저 모델을 사용하는가?
      - 장고의 유저 모델을 상속 받아서 기존에 구현된 기능을 내가 직접 구현하지 않아도 되기 때문에 (패스워드 해싱화 유저 필드, 체크 등 커스텀유저모델에 들어있어.)
      - 장고의 공식 문서에서 강력히 추천한다.
