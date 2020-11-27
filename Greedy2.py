# 그리디 2. 곱하기 혹은 더하기

# #정당성 : 문자가 연산시 숫자 중 0,1이 있다면 덧셈 나머지는 곱셈을 해야 가장 큰 수를 만들 수 있다.

num = input()
lst = []
result = 0

for i in num:
  lst.append(int(i))

for i in lst:
  if i == 0 or i == 1 or result == 0:
    result += i
  else:
    result *= i
print(result)

# #모범답안

# #정당성 : 두 수에 대하여 연산을 수행할 때, 두 수 중에서 하나라도 1이하인 경우에는 더하며, 두 수가 모두 2이상인 경우에는 곱하면 된다.

data = input()

#첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
  #두 수 중에서 하나라도 0 혹은 1인 경우, 곱하기보다는 더하기 수행
  num = int(data[i])
  if num <= 1 or result <= 1:
    result += num
  else:
    result *= num
print(result)

# # 개선사항: 알고리즘을 떠올렸다면 그것을 유의하며 코드르 짜야함.