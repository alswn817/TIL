# TIL   

* * *
# JavaScript란?   
+ JavaScript는 개발자가 대화식 웹 페이지를 만들기 위해 사용하는 프로그래밍 언어이다.클라이언트 측 스크립팅 언어로서 JavaScript는 월드 와이드 웹의 핵심 기술 중 하나이다.

## 문법   
+ JavaScript는 대소문자를 구별하며 유니코드 문자셋을 이용한다. 예를 들면, Früh(독일어)을 변수명으로 사용할 수 있다.
```JavaScript
var 갑을 = "병정";
var Früh = "foobar";
```

## 주석   
```Javascript
// 한 줄 주석

/* 더 긴
 * 여러 줄 주석.
 */

/* 그러나 /*가 중첩된 주석은 사용할 수 없다. */ SyntaxError */
```

## 선언   
+ var - 변수 선언. + 동시에 값을 초기화 함.   
+ let - 블록 스코프 지역 변수 선언. + 동시에 값을 초기화.   
+ const - 블록 스코프 읽기 전용 상수 선언.   
* * *
* 스코프: 함수가 실행될때, 함수 내에서 변수에 대한 접근이 어떻게 되든지를 나타내는 용어
* 블록 스코프: 블록 {}이 생성될 때마다 새로운 스코프가 형성되는 것

## 변수   
+ 애플리케이션에서 값에 상징적인 이름으로 변수 사용. 변수명은 식별자라고 불림.   

+ JavaScript 식별자는 문자, 밑줄 (_) 혹은 달러 기호 ($)로 시작해야 하는 반면 이후는 숫자 (0–9)이다.   

+ JavaScript는 대소문자를 비교하기 때문에 문자는 대문자와 소문자까지 모두 포함한다.   

+ ISO 8859-1 혹은 Unicode 문자(가령 å 나 ü)도 식별자에 사용할 수 있다.   

```
예시 :  Number_hits, temp99, $credit 및 _name 등
```

## 변수 할당   
+ 지정된 초기 값 없이 var 혹은 let 문을 사용해서 선언된 변수는 undefined 값을 갖는다.(선언되지 않은 변수에 접근을 시도하는 경우 ReferenceError 예외가 발생.)

```JavaScript
var a;
console.log('a 값은 ' + a); // a 값은 undefined

console.log('b 값은 ' + b); // b 값은 undefined
var b;

console.log('c 값은 ' + c); // Uncaught ReferenceError: c is not defined

let x;
console.log('x 값은 ' + x); // x 값은 undefined

console.log('y 값은 ' + y); // Uncaught ReferenceError: y is not defined
let y;
```

## 변수 호이스팅
+ JavaScript 변수의 특이한 점은 예외를 받지 않고도 나중에 선언된 변수를 참조할 수 있다는 것이다..

+ 이 개념은 호이스팅(hoisting)으로 알려져 있다. JavaScript 변수가 어떤 의미에서 함수나 문의 최상단으로 "올려지는" (혹은 "끌어올려지는") 것을 말한다. 하지만 끌어올려진 변수는 undefined 값을 반환한다. 그래서 심지어 이 변수를 사용 혹은 참조한 후에 선언 및 초기화하더라도, 여전히 undefined를 반환한다.