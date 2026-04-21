import numpy as np

def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    avg = total / len(numbers)
    return avg

data = [10, 20, 30, 40, 50]

# 수정된 부분: f-string을 사용하여 문자열과 숫자를 함께 출력
print(f"평균값은: {calculate_average(data)}")
