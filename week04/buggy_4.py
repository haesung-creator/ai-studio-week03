# -*- coding: utf-8 -*-
"""
buggy_4.py  ―  총 매출액 집계 (에러 없이 '조용히' 틀리는 스크립트)

이 스크립트는 에러 없이 잘 돌아가고, 그럴듯한 숫자를 출력한다.
하지만 그 숫자는 '틀렸다'.

[과제] 이 스크립트는 예외를 던지지 않는다. 대신
       (1) info()/describe()로 데이터 상태를 먼저 세어 보고
       (2) '무엇이 틀렸는지 어떻게 알아챘는지'를 서술한 뒤
       (3) 결측 규모를 보고하고 처리 방법을 선택·적용하여
           올바른 총매출을 산출하라.
       (힌트: 가격 결측은 몇 건인가? 음수 가격과 9999999 같은 값은 정상인가?)
"""
import pandas as pd

def main():
    df = pd.read_csv("dirty_sales.csv", encoding="utf-8")

    # FIXED: price 컬럼 쉼표, '원', 공백 전처리 후 수치형 변환
    df["price_clean"] = (df["price"].astype(str)
                                   .str.replace(",", "")
                                   .str.replace("원", "")
                                   .str.strip())
    df["price_clean"] = pd.to_numeric(df["price_clean"], errors="coerce")

    # FIXED: quantity 컬럼 전처리
    df["quantity_clean"] = (df["quantity"].astype(str)
                                         .str.replace(",", "")
                                         .str.strip())
    df["quantity_clean"] = pd.to_numeric(df["quantity_clean"], errors="coerce")

    # FIXED: 결측치 규모 사전 진단 및 기록
    price_nan_count = df["price_clean"].isna().sum()
    qty_nan_count = df["quantity_clean"].isna().sum()
    print(f"[진단] price 결측치: {price_nan_count}건, quantity 결측치: {qty_nan_count}건")

    # FIXED: 결측치 발생 시 상품(product)별 대표 단가로 보정하여 NaN에 의한 매출 유실 방지
    product_price_map = df.groupby("product")["price_clean"].transform("median")
    df["price_filled"] = df["price_clean"].fillna(product_price_map).fillna(0)
    df["quantity_filled"] = df["quantity_clean"].fillna(1) # 수량 결측은 기본값 1 적용

    # FIXED: 보정된 수치형 데이터 간 곱셈 연산으로 revenue 계산
    df["revenue"] = df["price_filled"] * df["quantity_filled"]

    total = df["revenue"].sum()
    avg_price = df["price_filled"][df["price_filled"] > 0].mean()

    print(f"총 매출액: {total:,.0f}원")
    print(f"평균 단가: {avg_price:,.0f}원")

if __name__ == "__main__":
    main()