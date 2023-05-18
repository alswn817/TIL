# TIL

* * *

## 리스트   
```py
std = ['hello', 'hi', '안녕', 5]
print(std[1:])
 ```

### 인덱스 찾기   
```py
std = ['hello', 'hi', '안녕', 5]
print(std.index(5)) 
```

### 리스트 길이 구하기   
```py
cafe = ["아메리카노", "카페라떼", "바닐라라뗴", "요거트"]
print(len(cafe)) #len() : 리스트 길이 반환
```

### 데이터 추가   
1. append() : 리스트 맨 뒤에 값이 추가
2. insert() : 원하는 위치에 값이 추가

```py
cafe.append("프라푸치노")
cafe.append("레몬에이드")
print(cafe)
```

```py
cafe.insert(0,"에스프레소")
cafe.insert(5,"블루베리 요거트")
print(cafe)
```

### 데이터 할당(값 바꾸기)   
```py
cafe[4] = "플레인요거트"
print(cafe)
```

### 데이터 삭제   
1. del 명령 -> 인덱스로 제거
2. pop() -> 인덱스로 제거
3. remove - > 값으로 제거

```py
del cafe[-1]
print(cafe)
```

```py
cafe.pop(0)
print(cafe)
```

```py
cafe.remove("바닐라라뗴")
print(cafe)
```

```py
print("라떼" in cafe) # 결과값: False
print("라뗴" not in cafe) # 결과값: True
```

# 리스트 연결   

### 메뉴 합치기   
```py
cafe.extend(bakery) # cafe와 bakery
print(cafe)
```

### 정렬   
```py
cafe.sort() 
print(cafe)
```
