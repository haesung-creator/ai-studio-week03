def calculator(a, b, op):
	if op == "+":
		return a + b
	elif op == "-":
		return a - b
	elif op == "*":
		return a * b
	elif op == "/":
		if b == 0:
			return "Error"
		return a / b
	return "Error"


#최소 2가지 입력 테스트
print("1) calculator 테스트:")
print(calculator(10, 3, "/")) #3.333...
print(calculator(5, 0, "/")) #Error

def format_receipt(name, price):
	return f"[{name}] 가격: {price:,}원"

#최소 2가지 입력 테스트
print("\n2) format_receipt 테스트:")
print(format_receipt("라떼", 5500)) # [라떼] 가격: 5,500원
print(format_receipt("아메리카노", 4000)) # [아메리카노] 가격: 4,000원


def filter_over(numbers,  threshold):
	result = []
	for num in numbers:
		if num > threshold:
			result.append(num)
	return result
	return result

#최소 2가지 입력 테스트
print("\n3 filter_over 테스트:")
print(filter_over([10,25,3,40],20)) # [25,40]
print(filter_over([1,5,8,12,15],10)) # [12,15]

