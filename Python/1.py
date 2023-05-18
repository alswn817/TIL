# 리스트
# std = ['hello', 'hi', '안녕', 5]
# print(std[1:])

# 인덱스 찾기
# std = ['hello', 'hi', '안녕', 5]
# print(std.index(5))

# 리스트 길이 구하기
# cafe = ["아메리카노", "카페라떼", "바닐라라뗴", "요거트"]
# print(len(cafe)) #len() : 리스트 길이 반환, #4

# 데이터 추가
# 1. append() : 리스트 맨 뒤에 값이 추가
# 2. insert() : 원하는 위치에 값이 추가

# cafe.append("프라푸치노")
# cafe.append("레몬에이드")
# print(cafe)

# cafe.insert(0,"에스프레소")
# cafe.insert(5,"블루베리 요거트")
# print(cafe)

# 데이터 할당(값 바꾸기)
# cafe[4] = "플레인요거트"
# print(cafe)

# 데이터 삭제
# 1. del 명령 -> 인덱스로 제거
# 2. pop() -> 인덱스로 제거
# 3. remove - > 값으로 제거

# del cafe[-1]
# print(cafe)

# cafe.pop(0)
# print(cafe)

# cafe.remove("바닐라라뗴")
# print(cafe)

# print("라떼" in cafe) # 결과값: False
# print("라뗴" not in cafe) # 결과값: True



# menu = ["비빔밥", "삼겹살", "제육볶음"]
# order = input("주문 입력: ")
# if (order in menu):
#     print("주문 완료")
# else:
#     print("메뉴판에 없음")

# bakery = ["스콘", "케이크", "샌드위치"]
# print(len(bakery)) # 메뉴 개수 출력

# bakery.insert(0, "약과") # 약과 추가
# print(bakery)

# bakery.extend(["햄치즈 샌드위치", "에그샐러드 샌드위치", "닭가슴살 샌드위치"]) # 여러 메뉴 추가
# print(bakery)

# bakery[3] = "불고기 샌드위치" # 샌드위치 값을 불고기 샌드위치로 변경
# print(bakery)

# bakery.remove("스콘") # 스콘을 제거
# print(bakery)



# 5월 17일
# 리스트 연결
# cafe.extend(bakery) # cafe와 bakery 메뉴 합치기
# print(cafe)

# cafe.sort() # 정렬 
# print(cafe)

# for i in range(10, 51, 10):
#    print(i, end='')

# coding = ["파이썬", "C", "C++", "c#", "JAVA"]
# for i in coding:
#     print(i, end = '')

# student = int(input("학생 수 입력 : "))
# score_list = []
# for i in range(student):
#     score = int(input(f"[i+1]번 점수 입력하세요 : "))
#     score_list.append(score)
# print()
# print(f"{student}명의 점수 : ", score_list)
# print(f"{student}명의 최대 점수 : ", max(score_list))
# print(f"{student}명의 최소 점수 : ", min(score_list))
# print(f"{student}명의 점수 합계 : ", sum(score_list))
# print(f"{student}명의 평균 : {sum(score_list)/student : .2f}")

# a = [10, 20, 30, 40, 50]
# print(a)
# print(min(a))
# print(max(a))
# rint(sum(a))
# print(sum(a)/len(a))

# a = input("학생 수 입력 : ")
# student = [a]
# b=1
# for i in range:
#     score=input(f"{b}번 점수 입력 : ")
#     b+=1

# from random import*
# lotto=[]
# while len(lotto)<6:
#     x=randint(1, 45)
#     # 로또번호가 리스트에 없을 경우에만 추가
#     if x not in lotto:
#         lotto.append(x)
# lotto.sort()
# print("컴퓨터 로또 입력 : ", lotto)