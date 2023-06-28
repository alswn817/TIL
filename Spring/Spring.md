# TIL

## Spring
### Spring의 빌드 관리 도구
+ MAVEN - 작업 의존성 그래프를 기반
+ GRADLE - 고정적이고 선형적인 단계의 모델을 기반

### Library
+ 스트링 부트 라이브러리와 테스트 라이브러리
##### 스프링 부트 라이브러리
+ spring-boot-starter-tomcat : 웹서버
+ spring-webmvc : 스프링 웹 MVC(웹 계층에 서블릿(Servlet) API를 기반으로 클라이언트의 요청을 처리하는 모듈)
+ spring-boot-starter-thymeleaf : 타임리프 템플릿 엔진
+ spring-boot-starter(공통) : 스프링 부트 + 스프링 코어 + 로깅
	+ spring-boot
		+ spring-core
	+ spring-boot-starter-logging
		+ logback,slf4j

#### 테스트 라이브러리
+ spring-boot-starter-test
	+ junit : 테스트 프레임워크 / junit 5을 많이 사용함
	+ mockito : 목 라이브러리
	+ assertj : 테스트 코드를 좀 더 편하게 작성하게 도와주는 라이브러리
	+ spring-test : 스프링 통합 테스트 지원

### View 환경 설정
+ spring-boot에서는 Welocome page 기능을 제공한다.
    + statoc/index.html을 올리면 Welcome Page 기능을 제공한다.

### 빌드 후 실행
1 ``` ./gradlew build ```
2 ``` cd build/libs ```
3 ``` java -jar hello-spring=0.0.1-SNAPSHOT.jar```

### 정적 컨텐츠
+ 정적 컨텐츠 - 실시간으로 변경할 필요 없는 데이터

### MVC와 템플릿 엔진
+ MVC(Model, View, Controller)
+ 웹브라우저에서 링크 넘김-> 내장 tomcat 서버가 스프링 컨테이너에서 메소드 호출->
받은 모델을 viewResolver로 넘김.타임레프 템플릿 엔진이 렌더링 후 -> 웹브라우저

### API
+ @ResponseBody 사용
	+ HTTPㅇ,; BODY에 문자 내용을 직접 반환
	+ 'viewResolver' 대신 'HttpMessageConverter'가 동작
	+ 기본 문자처리 : 'StringHttpMessageConverter'
	+ 기본 객체처리 : 'MappingJackson2HttpMessageConverter' (Jason을 Jackson으로 변경함)
	+ byte 처리 등등 기타 여러 HttpMessageConverter가 기본 등록 되어있음