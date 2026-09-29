# -*- coding: utf-8 -*-
"""
buggy_1.py  ―  판매 데이터 매출 집계 (csv 모듈 버전)

dirty_sales.csv를 한 줄씩 읽어 '매출액 = 단가 x 수량'을 누적한다.
잘 돌아가는 것처럼 보이지만, 어떤 행에서 갑자기 멈춘다.

[과제] 이 스크립트를 실행해 Traceback을 얻고,
       진단 3단계 루틴(무엇이 / 어디서 / 왜)으로 원인을 특정한 뒤
       전처리로 해결하라. (힌트: 예외 타입은 무엇인가?)
"""
import csv

def calc_total(path):
    total = 0
    normal_prices = {}

    # 1. 정상 단가표 수집 (1차 순회)
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            product = row["product"]
            # FIXED: 천 단위 쉼표(,), 단위('원')를 제거하고 양끝 공백(.strip())을 지워 ValueError 방지
            raw_price = row["price"].replace(",", "").replace("원", "").strip()
            
            # FIXED: 공백/빈값이 아니고 순수 숫자인 경우, 음수(-4700 등)는 abs()로 절댓값 변환하여 양수 단가만 보존
            if raw_price and raw_price.lstrip('-').isdigit():
                price_val = abs(int(raw_price))
                if product not in normal_prices and price_val > 0:
                    normal_prices[product] = price_val

    # 2. 실제 매출 계산 (2차 순회)
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            product = row["product"]
            # FIXED: 쉼표, 단위, 공백 2차 전처리
            raw_price = row["price"].replace(",", "").replace("원", "").strip()

            # FIXED: 공백/빈 문자열("")이거나 숫자가 아닌 경우 1차에서 수집한 normal_prices 정상 단가 참조
            if not raw_price or not raw_price.lstrip('-').isdigit():
                price = normal_prices.get(product, 0)
            else:
                # FIXED: int 형변환 및 음수 단가(-4500 등)의 절댓값(abs) 변환으로 누적 연산 오류 방지
                price = abs(int(raw_price))

            qty = int(row["quantity"])
            total += price * qty

    return total

if __name__ == "__main__":
    total = calc_total("./week04/dirty_sales.csv")
    print(f"총 매출액: {total:,}원")