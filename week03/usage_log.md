# 3주차 과제 AI 어시스턴트 활용 기록

## 1. 사용 일시 및 모델
- 일시: 2026년 9월 22일
- 활용 도구: Gemini (AI 어시스턴트)

## 2. 질의 내용 (Prompt) 및 답변 결과
- **프롬프트 1**: 
  "RAW_DATA.csv 파일을 읽을 때 FileNotFoundError가 발생하고 인코딩 문제가 발생해. 해결 방법 알려줘."
- **채택 내용**: 
  작업 디렉토리 위치를 `week03`으로 이동하고 `pd.read_csv("RAW_DATA.csv", encoding="cp949")` 옵션을 적용함.
- **프롬프트 2**: 
  "단가 열의 콤마 제거, 파생 열 생성, groupby 월별 집계 및 assert 검증 코드를 작성해 줘."
- **채택 내용**: 
  `pd.to_numeric`과 `astype("Int64")`를 활용한 단가 정제, `dt.month`를 활용한 월 추출, `assert raw_total == summary_total` 검증 로직 반영.

## 3. 검증 및 결과
- 파이프라인 스크립트 실행 후 `Monthly_Report.xlsx` 파일 생성 확인.
- 생성된 엑셀 파일 내 '월별카테고리요약', '카테고리별합계' 2개 시트 정상 저장 확인.
- `assert` 단언문을 통과하여 원본 및 집계표 간의 총매출 수치 일치 확인.