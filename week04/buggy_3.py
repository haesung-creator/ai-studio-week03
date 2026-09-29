# -*- coding: utf-8 -*-
"""
buggy_3.py  ―  데이터 로드 후 카테고리별 집계

load_and_clean()으로 데이터를 읽어 정제한 뒤,
그 결과를 groupby로 집계하려 한다.
그런데 집계 단계에서 이상한 에러가 난다.

[과제] Traceback의 예외 타입을 확인하고,
       'NoneType ...' 메시지가 가리키는 '이 변수를 만든 직전 단계'를
       역추적하여 원인 함수를 찾아 수정하라.
"""
import pandas as pd

def load_and_clean(path):
    df = pd.read_csv(path, encoding="utf-8")
    
    # price 컬럼 숫자로 정제
    df["price"] = (df["price"].astype(str)
                              .str.replace(",", "")
                              .str.replace("원", "")
                              .str.strip())
    df["price"] = pd.to_numeric(df["price"], errors="coerce").fillna(0)
    
    # FIXED: quantity 컬럼 쉼표/공백 전처리, 수치형 변환 및 결측치 보정
    qty_clean = df["quantity"].astype(str).str.replace(",", "").str.strip()
    df["quantity"] = pd.to_numeric(qty_clean, errors="coerce").fillna(0)
    
    df["revenue"] = df["price"] * df["quantity"]
    
    # FIXED: AttributeError(NoneType) 전파 원인 해결 - 정제된 데이터프레임(df) 반환 구문 추가
    return df

def main():
    df = load_and_clean("dirty_sales.csv")
    # FIXED: load_and_clean에서 정상 df가 반환되어 groupby() 정상 실행 가능
    result = df.groupby("category")["revenue"].sum()
    print(result)

if __name__ == "__main__":
    main()