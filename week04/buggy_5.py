# -*- coding: utf-8 -*-
"""
buggy_5.py  ―  '앞 행 대비 가격 변화'가 큰 행 찾기

정제한 price를 앞뒤로 비교하며 급변 지점을 찾으려 한다.
데이터에는 이상치(-4500, 9999999)도 섞여 있어 변화폭이 튀는 구간이 있다.
그런데 반복문이 끝까지 가지 못하고 죽는다.

[과제] Traceback으로 예외 타입을 확인하라(힌트: 반복문 경계).
       print 디버깅이 500줄 출력을 뒤져야 한다면,
       디버거의 '조건부 중단점'(예: 조건식  i >= len(prices) - 2)을 걸어
       문제의 반복 지점에서 곧바로 멈춰 원인을 관찰한 뒤 수정하라.
"""
import pandas as pd

def load_prices(path):
    df = pd.read_csv(path, encoding="utf-8")
    
    # price 컬럼 전처리 (쉼표, 단위 '원', 공백 제거)
    df["price"] = (df["price"].astype(str)
                              .str.replace(",", "")
                              .str.replace("원", "")
                              .str.strip())
    df["price"] = pd.to_numeric(df["price"], errors="coerce").fillna(0)
    
    # FIXED: 999,999 및 음수 등 비현실적 극단 이상치를 0으로 정제하여 데이터 왜곡 방지
    prices = df["price"].apply(lambda x: 0 if x >= 100000 or x < 0 else x).tolist()
    return prices

def find_big_jumps(prices, threshold=10000):
    jumps = []
    # FIXED: range(len(prices)-1)로 변경하여 prices[i + 1] 참조 시 IndexError 발생 방지
    for i in range(len(prices) - 1):
        diff = prices[i + 1] - prices[i]
        if abs(diff) >= threshold:
            jumps.append((i, prices[i], prices[i + 1], diff))
    return jumps

if __name__ == "__main__":
    prices = load_prices("dirty_sales.csv")
    jumps = find_big_jumps(prices)
    print(f"급변 지점 {len(jumps)}건")
    for row in jumps[:10]:
        print(row)