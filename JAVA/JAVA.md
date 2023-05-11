# JAVA 정리   
## JAVA란?   
+ JAVA는 웹 애플리케이션 코딩에서 널리 사용되는 프로그래밍 언어이다.   
+ JAVA는 그 자체 플랫폼으로 사용할 수 있는 다중 플랫폼, 객체 지향 및 네트워크 중심 언어이다.   
* * *
# JAVA의 용도   
## 1.게임 개발
+ 많은 모바일, 컴퓨터 및 비디오 게임과 기계 학습, 가상현실과 같은 기술이 통합된 최신 게임도 JAVA로 작성된다.
## 2.클라우드 컴퓨팅
+ JAVA는 분산 클라우드 기반 애플리케이션에 적합하다.
## 3.빅데이터
+ JAVA는 복잡한 데이터 집합과 방대한 데이터를 처리할 수 있는 데이터 처리 엔진에 사용된다.

이외에도 여러가지 방면으로 사용된다.
* * *
# JAVA 문법

## 자료형
### JAVA의 자료형은 Primitive type(기본 자료형)과 Reference type(참조 자료형)으로 나뉜다.

## Primitive type의 종류
+ short, int, long, float, double, char, boolean, byte 등이 있다.   
## Reference type의 종류
+ Reference type은 위의 Primitive type의 자료형을 제외한 모든 자료형이다.   

## 조건문
+ if / else if / else 구조   
+ switch문을 사용할 때에는 소괄호에 파라미터를 넣어주며 각각의 케이스 별 기능을 구현할 수 있다.switch를 사용한 예시는 아래의 코드가 있다.
<pre><code>   
import java.util.Scanner;   
public class Main    
    public static void main(String[] args)    
        Scanner sc = new Scanner(System.in);   
        String score = sc.next();   
   
        switch(score)   
            case "A":   
                System.out.println("A등급입니다.");   
                break;   
            case "B":   
                System.out.println("B등급입니다.");   
                break;   
            case "C":   
                System.out.println("C등급입니다.");   
                break;   
            default:   
                System.out.println("D등급 이하 입니다.");   
                break;   
           
          
</code></pre>

## 반복문
+ for 반복문은 자바스크립트와 형태가 비슷하다.for 문을 사용한 예시는 아래의 코드가 있다.
+ <pre><code>for( int i = 0 ; i < 100; i++)</code></pre>   
+ for each 반복문은 python에서 주로 쓰이는 반복문의 형식이다.for each를 사용하는 예시는 아래의 코드가 있다.
+ <pre><code>public class Main 
    public static void main(String[] args) 
        // write your code here
        String[] days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};

        for (String day : days)
            System.out.println(day);
        
    
</code><pre>