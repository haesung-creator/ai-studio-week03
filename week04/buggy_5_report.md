
## 1. 진단 보고 (진단 3단계 루틴)

* **① 무엇이 (예외 타입 및 메시지):**
  * `IndexError: list index out of range`
* **② 어디서 (파일·줄·코드):**
  * `buggy_5.py` 파일 내 `find_big_jumps` 함수 16번째 줄 `diff = prices[i + 1] - prices[i]`
* **③ 왜 (변수 상태 근거 및 이상치 원인):**
  * `for i in range(len(prices)):` 루프에서 `i`가 리스트의 마지막 인덱스(`len(prices) - 1`)에 다다랐을 때, `prices[i + 1]` 구문이 유효 범위를 벗어난 인덱스(`len(prices)`)에 접근하려고 시도하여 `IndexError`가 발생함.
  * 추가적으로 `dirty_sales.csv` 내에 `999,999`와 같이 비현실적인 극단 이상치가 존재하는 경우 탐지 로직을 왜곡하므로 사전 정제가 필요함.