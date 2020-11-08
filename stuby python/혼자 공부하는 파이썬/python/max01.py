max_value = 0
a = 0
b = 0

# 어차피 앞뒤가 같아서 "100 // 2"까지 반복하게 했습니다.
# 그냥 range(1, 100 + 1) 했어도 문제 없습니다.
for i in range(1, 100 + 1):
    j = 100 - i
  
    # 이전 절의 최대값 구하는 문제와 차이 없음
    current = i * j
    if max_value < current:
        a = i
        b = j
        max_value = current

print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))
