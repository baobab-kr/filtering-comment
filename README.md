<div align="center">
  <h3 align="center">Baobab Filtering Comment API</h3>

  <p align="center">
    바오밥 서비스의 댓글 필터링 API를 제공합니다. <br/> 
    한정적인 Azure 리소스 비용으로 인해 비활성화 되어있는 경우 사용이 제한될 수 있습니다. <br/>
    <br />
    <a href="https://github.com/baobab-kr/filtering-comment"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#">View Demo</a>
    ·
    <a href="https://github.com/baobab-kr/filtering-comment/issues">Report Bug</a>
    ·
    <a href="https://github.com/baobab-kr/filtering-comment/issues">Request Feature</a>
  </p>
</div>


## Installation

해당 섹션에서는 API 서버를 로컬에 설치하는 방법을 안내합니다. <br/>
이미 도커 엔진이 로컬 PC에 설치되어 있음을 가정하에 제작되었습니다. <br/>

- Clone the repo  
   ```sh
   git clone https://github.com/baobab-kr/blog-service.git
   ```
- Docker Container build and Run  
   ```sh
   docker build -t filtering-api-test:v0.0.1 .
   docker run -p 5000:5000 --name=filtering-api filtering-api-test:v0.0.1
   ```
<br/>

## How to Test

컨테이너를 동작 시킨 후 Postman을 이용하여 https://localhost:3000/predict 끝점을 통해 테스트해 보실 수 있습니다. <br/>
<br/>
<br/>

## Environment Table

| Variable           | dev | qa/prod |  Example                 | Explanation                                                                         |
| ------------------ | :-: | :-----: | :-----------------------: | ----------------------------------------------------------------------------------- |
| JAVA_HOME           | ✅  |   ✅    | /usr/lib/jvm/java-1.7-openjdk/jre | Konlpy를 사용하기 위해 JDK를 설치합니다.  |