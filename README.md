# Namseoul Project (server side)

> This is API server code of Namseoul Project



## API Structure

* /message





## Database

* For local namseoul_mb4

    ```sql
    CREATE DATABASE namseoul_mb4
      DEFAULT CHARACTER SET utf8mb4
      DEFAULT COLLATE utf8mb4_unicode_ci;
    ```

* with docker

    ```shell
    docker run -dit --restart unless-stopped --name db -e MYSQL_ROOT_PASSWORD=something -p 3306:3306 mysql:5.7.21 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
    ```

* Data Migration for Django

    ```bash
    ./manage.py migrate
    ```



## deploy 관련

uWsgi and Nginx 는 알아서 하세요



#### linux 관련 업데이트(개발 모듈 설치)

> 이걸 먼저해야 나중에 python mysqlclient를 설치할 수 있음

```shell
sudo apt-get update
sudo apt-get upgrade
```

```shell
sudo apt-get install gcc libmysqlclient-dev libxml2-dev libxslt1-dev python-dev
```



#### Annaconda 설치

http://docs.anaconda.com/anaconda/install/linux/ 참고

* Download (다운로드 폴더 만들고 진행하는 것이 좋음)

  ```shell
  curl -O https://repo.anaconda.com/archive/Anaconda3-4.4.0-Linux-x86_64.sh
  ```

* SHA256 checksum 해제

  ```
  sha256sum Anaconda3-4.4.0-Linux-x86_64.sh
  ```

* Anaconda Script 실행

  ```
  bash Anaconda3-4.4.0-Linux-x86_64.sh
  ```

* 설치 경로
  해당 계정의 홈디렉토리(~)에 설치해야 그 계정이 사용가능

* .bashrc 에 자동으로 추가하는 옵션 꼭 사용

* test

  ```shell
  conda list -envs
  ```



### Anaconda3-5.3.0 setting 변경(uwsgi 관련 에러 해결)

> 그냥 Anaconda3-4.4.0 쓰는 것을 추천

```shell
conda config --add channels conda-forge
```

```shell
conda install uwsgi
```

> 이결 해야 나중에 pip로 uwsgi 설치 가능 (anaconda3-5.~~ 관련 오류임)



#### conda env 만들기 & 적용하기

```shell
conda create --name my_env python=3.6.2
```

```shell
source activate my_env
or
conda activate my_env
```



#### Auto ENV 적용하기

https://github.com/kennethreitz/autoenv 참고

```shell
$ git clone git://github.com/kennethreitz/autoenv.git ~/.autoenv
$ echo 'source ~/.autoenv/activate.sh' >> ~/.bashrc
```

이후 `.env` 파일을 작성하면 된다.

> .env in project folder

```
source activate my_env
```

