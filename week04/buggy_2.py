# -*- coding: utf-8 -*-
"""
buggy_2.py  ―  카테고리별 매출 집계 (pandas 버전)

dirty_sales.csv를 pandas로 읽어 카테고리별 매출 합계를 구하려 한다.
그런데 실행하자마자 죽는다.

[과제] Traceback을 얻어 예외 타입을 확인하고,
       '원인을 데이터에서 직접 확인'한 뒤(힌트: 실제 컬럼명이 무엇인가?)
       코드를 수정하라.
"""
import pandas as pd

def load(path):
    df = pd.read_csv(path, encoding="utf-8")
    return df

def summarize(df):
    # FIXED: 쉼표(,) 제거 및 숫자(int) 형변환으로 문자열 반복 연산 오류 해결 (ValueError/KeyError 방지)
    price_clean = df["price"].astype(str).str.replace(",", "").str.replace("원", "").str.strip()
    df["price_clean"] = pd.to_numeric(price_clean, errors="coerce").fillna(0).astype(int)
    
    # FIXED: 수량 컬럼 정수 형변환
    df["quantity_clean"] = pd.to_numeric(df["quantity"], errors="coerce").fillna(0).astype(int)

    # FIXED: 숫자 간 곱셈으로 파생 컬럼 생성
    df["매출액"] = df["price_clean"] * df["quantity_clean"]
    
    # FIXED: 실제 CSV의 영문 컬럼명 'category' 기반 그룹화
    return df.groupby("category")["매출액"].sum()

if __name__ == "__main__":
    df = load("dirty_sales.csv")
    result = summarize(df)
    print(result)
