Poll_pre 
pollpjct : userapp, adminapp 구조로 구성 


pollpjct2 : userapp, adminapp 로그인 기능 (django.contrib.auth 아니고 자체 구현한 간단한 로그인 기능) 


#### reference
112269075.5.jpg : 투표 결과 지역별 시각화 예시 
선거인명부 서식.pdf : 선거인명부 DB 구성 예시 


pollpjct1.pdf : 기획 단계 1차 스케치 (* Diagram 막 그림, 악필, 무질서함 *)


pollpjct2.pdf : 기획 단계 2차 스케치


poll.pages : 기획 단계 메모 (오프라인으로 할지 온라인으로 할지 둘 차이, 공통점, 기능, etc)






#### D1 2022/3/20~3/30 : 기획 
* 기능, 구조, etc (userapp, adminapp, pollpjct하고 함수 이름 정도)

#### D2 2022/4/12 : userapp, adminapp 로그인 (기능 X (userapp/models.py 커스텀 유저 모델만 조금), 템플릿 O)
* userapp/templates/home.html : 사진 & 버튼(누르면 userlogin으로 넘어감) 
* adminapp/templates/adminlogin.html
