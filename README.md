# Factory Boy Study

<img alt="Python" src ="https://img.shields.io/badge/Python-3776AB.svg?&style=for-the-badge&logo=Python&logoColor=white"/>
<img alt="Pytest" src ="https://img.shields.io/badge/Pytest-0A9EDC.svg?&style=for-the-badge&logo=Pytest&logoColor=white"/>
<img alt="Docker" src ="https://img.shields.io/badge/Docker-2496ED.svg?&style=for-the-badge&logo=Docker&logoColor=white"/>
<img alt="Django" src ="https://img.shields.io/badge/Django-092E20.svg?&style=for-the-badge&logo=Django&logoColor=white"/>
<img alt="PostgreSQL" src ="https://img.shields.io/badge/PostgreSQL-4169E1.svg?&style=for-the-badge&logo=PostgreSQL&logoColor=white"/>

ORM-Based Fixtures Manager 도구인 `factory-boy` 학습 프로젝트 입니다.

### 프로젝트 목표

1. json 기반의 Fixtures 를 사용하지 않고 ORM 기반의 Fixture 생성 방법을 익힌다.
2. Fixture 를 생성해 본다.
3. N:1 관계의 Fixture 를 생성해 본다.
4. 1:1 관계의 Fixture 를 생성해 본다.
5. M:N 관계의 Fixture 를 생성해 본다.

## 도커

본 프로젝트는 Docker 를 통해 장고 환경을 구성했습니다. 프로젝트 구성을 몰라도 아래 명령어로 손쉽게 프로젝트 환경을 실행 할 수 있습니다.

```shell
docker-compoe -f local.yml up -d
```

## 환경변수

본 프로젝트는 로컬에서의 환경을 별도로 지원하기 위해 `DJANGO_READ_DOT_ENV_FILE` 환경 변수를 지원합니다. 따라서 아래 작업을 통해 로컬에서 또한 작업이 가능합니다

1. DJANGO_READ_DOT_ENV_FILE 환경변수를 `True` 값으로 설정해줍니다.

```shell
export DJANGO_READ_DOT_ENV_FILE=True
```

2. project root 디렉토리에 .env 파일을 생성합니다.

```shell
touch .env 
```

3. 필요한 환경 변수를 채워줍니다.

|idx|변수|자료형|디폴트|설명|
|---|---|---|---|---|
|1|DJANGO_READ_DOT_ENV_FILE|`bool`|`False`|프로젝트 루트 디렉토리의 `.env` 파일을 찾아 환경변수를 다시 씁니다.|
|2|DJANGO_SECRET_KEY|`string`|`django-secret-key`|장고 비밀키를 입력 받습니다.|
|3|DJANGO_DEBULG|`bool`|`True`|장고 서버의 디버그 모드를 결정합니다.|
|4|DATABASE_URL|`string`|`None`|장고 서버의 디폴트 데이터베이스 연결 정보를 입력받습니다.|

4.로컬에서 장고 서버를 동작 합니다.

```shell
python manage.py runserver
```

## 테스트

테스트는 pytest 모듈을 기반으로 다양한 플러그인으로 구성했습니다.

```text
plugin list
- pytest
- pytest-django
- pytest-cov
```

### pytest

도커를 통해 손쉽게 pytest 를 구동할 수 있습니다.

```shell
docker-compose -f local.yml run --rm django pytest
```

`.env` 가 준비되어 있다면 로컬에서도 수행할 수 있습니다.

```shell
pytest
```

### Coverage

도커를 통해 손쉽게 커버리지를 측정할 수 있습니다.

```shell
docker-compose -f local.yml run --rm django pytest --cov
```

`.env` 가 준비되어 있다면 로컬에서도 수행할 수 있습니다.

 ```shell
 pytest --cov
 ```