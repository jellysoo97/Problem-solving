# 손익분기점
# A: 고정비용 / B: 노트북 한대의 가변비용 / C: 노트북 가격
# 손익분기점 = A + B * N < C * N 되는 시점
# 손익분기점 존재하지 않으면(0보다 작거나 같으면) -1 출력

a, b, c = list(map(int, input().split()))

if c - b <= 0:
  print(-1)
else:
  print(int(a / (c-b)) + 1)