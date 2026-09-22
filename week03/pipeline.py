import pandas as pd

# ==========================================
# [Step 1] 원시 데이터 로드 및 확인
# ==========================================
file_path = "RAW_DATA.csv"
df = pd.read_csv(file_path, encoding="cp949")

print("=== [1] 데이터 로드 완료 (행, 열) ===")
print(df.shape)

# ==========================================
# [Step 2] 데이터 정제 및 파생 열 생성
# ==========================================
# 1. '단가' 열의 콤마 제거 및 정수(Int64) 타입 변환
df["단가"] = pd.to_numeric(
    df["단가"].astype(str).str.replace(",", "", regex=False), 
    errors="coerce"
).astype("Int64")

# 2. '매출액' 파생 열 생성 (단가 × 수량)
df["매출액"] = df["단가"] * df["수량"]

# 3. '주문일자' 날짜 타입 변환 및 '월' 파생 열 추출
df["주문일자"] = pd.to_datetime(df["주문일자"])
df["월"] = df["주문일자"].dt.month

print("\n=== [2] 정제 후 상위 5개 행 미리보기 ===")
print(df.head())

print("\n=== [2] 컬럼 정보 확인 (매출액, 월 추가 확인) ===")
df.info()

import pandas as pd

# ==========================================
# [Step 1] 원시 데이터 로드 및 확인
# ==========================================
file_path = "RAW_DATA.csv"
df = pd.read_csv(file_path, encoding="cp949")

print("=== [1] 데이터 로드 완료 (행, 열) ===")
print(df.shape)

# ==========================================
# [Step 2] 데이터 정제 및 파생 열 생성
# ==========================================
# 1. '단가' 열의 콤마 제거 및 정수(Int64) 타입 변환
df["단가"] = pd.to_numeric(
    df["단가"].astype(str).str.replace(",", "", regex=False), 
    errors="coerce"
).astype("Int64")

# 2. '매출액' 파생 열 생성 (단가 × 수량)
df["매출액"] = df["단가"] * df["수량"]

# 3. '주문일자' 날짜 타입 변환 및 '월' 파생 열 추출
df["주문일자"] = pd.to_datetime(df["주문일자"])
df["월"] = df["주문일자"].dt.month

# ==========================================
# [Step 3] groupby 그룹화 및 집계표 생성
# ==========================================
# 1. 월별 × 카테고리별 매출 총합·평균·거래건수 집계
monthly_summary = (
    df.groupby(["월", "카테고리"])["매출액"]
    .agg(총매출="sum", 평균매출="mean", 거래건수="count")
    .reset_index()
)

# 2. 카테고리별 총매출 집계 및 내림차순 정렬
category_summary = (
    df.groupby("카테고리")["매출액"]
    .sum()
    .reset_index(name="총매출")
    .sort_values(by="총매출", ascending=False)
)

print("\n=== [3] 월별 카테고리 요약 (상위 5행) ===")
print(monthly_summary.head())

print("\n=== [3] 카테고리별 총매출 (내림차순 정렬) ===")
print(category_summary)