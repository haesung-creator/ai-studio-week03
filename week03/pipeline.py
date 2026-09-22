import pandas as pd

# ==========================================
# [Step 1] 원시 데이터 로드 및 확인 (Commit 1)
# ==========================================
file_path = "RAW_DATA.csv"
df = pd.read_csv(file_path, encoding="cp949")

print("=== [Step 1] 데이터 로드 완료 ===")
print(f"데이터 크기 (행, 열): {df.shape}")


# ==========================================
# [Step 2] 데이터 정제 및 파생 열 생성 (Commit 2)
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

print("=== [Step 2] 데이터 정제 및 파생 열 생성 완료 ===")


# ==========================================
# [Step 3] groupby 그룹화 및 집계표 생성 (Commit 3)
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

print("=== [Step 3] groupby 집계표 생성 완료 ===")


# ==========================================
# [Step 4] 교차 검증 및 Excel 저장 (Commit 4)
# ==========================================
# 1. 원본 매출액 총합과 집계표 총매출 합 교차 검증 (assert)
raw_total = df["매출액"].sum()
summary_total = monthly_summary["총매출"].sum()

assert raw_total == summary_total, f"매출 총합 불일치 에러! (원본: {raw_total}, 집계: {summary_total})"
print(f"[검증 성공] 원본 데이터 총매출({raw_total:,}원)과 집계표 총매출 합계가 완벽히 일치합니다.")

# 2. Excel 저장 (시트 2개 구성, index=False 적용)
output_file = "Monthly_Report.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    monthly_summary.to_excel(writer, sheet_name="월별카테고리요약", index=False)
    category_summary.to_excel(writer, sheet_name="카테고리별합계", index=False)

print(f"=== [Step 4] '{output_file}' 자동 저장 완료! ===")