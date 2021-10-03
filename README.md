# factory_boy_study
 장고의 Fixture 기반 테스트에서 ORM기반 Fixture를 만들기 위해 factory_boy를 사용하려 한다.
 
# run server
```shell
docker-compose -f local.yml up -d
```
- 접속정보 : localhost:8000
- 데이터베이스 볼륨 : 도커 볼륨 사용
- 서버 데몬 : uvicorn + watchgod 리로드 지원