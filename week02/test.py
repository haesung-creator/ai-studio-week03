import sys

# 방법 A: 리스트 컴프리헨션 (대괄호 [ ] 사용)
# 👉 1천만 개를 메모리에 '즉시' 다 만들어 올림 (약 85MB 차지)
squares_list = [x * x for x in range(10_000_000)]
print("리스트 메모리 크기:", sys.getsizeof(squares_list))   # 약 89,095,160 바이트

# 방법 B: 제너레이터 표현식 (소괄호 ( ) 사용)
# 👉 값을 직접 만들지 않고, '만드는 규칙(공식)'만 기억함 (약 200바이트 고정!)
squares_gen = (x * x for x in range(10_000_000))
print("제너레이터 메모리 크기:", sys.getsizeof(squares_gen))    # 약 200 바이트

def read_sales(path):
    """대용량 판매 로그 파일을 메모리 과부하 없이 한 줄씩 읽어오는 제너레이터 함수"""
    with open(path, encoding="utf-8") as f:
        for line in f:                       # 파일 객체 f 자체가 이터레이터 역할 수행
            item, price = line.strip().split(",")
            yield item, int(price)           # return이 아니라 yield로 '한 건만' 내어주고 대기!

# 사용할 때는 일반 for문과 똑같이 사용합니다. 전체 파일이 메모리에 안 올라갑니다!
total = 0
for item, price in read_sales("sales_log.csv"):
   total += price