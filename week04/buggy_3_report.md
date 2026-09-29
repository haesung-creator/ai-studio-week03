
## 1. 진단 보고 (진단 3단계 루틴)

* **① 무엇이 (예외 타입 및 메시지):**
  * `AttributeError: 'NoneType' object has no attribute 'groupby'` 
* **② 어디서 (파일·줄·코드):**
  * `buggy_3.py` 파일 내 `main` 함수 28번째 줄 `result = df.groupby("category")["revenue"].sum()`
* **③ 왜 (변수 상태 근거 및 전파 원인 역추적):**
  * `main()` 함수에서 `df.groupby()`를 호출할 때 변수 `df`에 `None` 값이 저장되어 있어 속성 참조 에러가 발생함.
  * 호출 스택을 역추적해보면, 에러 원인은 `main()`이 아니라 `load_and_clean()` 함수에 있음. `load_and_clean()` 함수 내에서 price, quantity, revenue 컬럼 정제를 모두 마쳤으나, `return df` 구문을 누락하여, 함수 종료 시 `None`이 반환(전파)되었기 때문임.
