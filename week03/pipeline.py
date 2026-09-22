import pandas as pd

# 1. RAW_DATA.csv 파일 로드 (CP949 인코딩 지정)
file_path = "RAW_DATA.csv"
df = pd.read_csv(file_path, encoding="cp949")

# 2. 로드 직후 데이터의 크기(행, 열) 및 기본 정보 확인
print("=== 1. 데이터 크기 (행, 열) ===")
print(df.shape)

print("\n=== 2. 데이터 컬럼 및 타입 정보 ===")
df.info()

print("\n=== 3. 상위 5개 행 미리보기 ===")
print(df.head())