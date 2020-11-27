# #그리디 01.모험가길드

# #내가 푼 답
# # 정당성 : 모험가의 공포도 중 가장 큰 값부터 그룹을 지어 n에서 제거해나가면 여행을 떠날 수 있는 그룹 수의 최댓값을 구할 수 있을 것.
n = int(input())
scared_point = list(map(int,input().split()))

scared_point = list(set(scared_point))
scared_point.sort()
max_index = len(scared_point) - 1
group = 0


while n != 0:
  n -= scared_point[max_index - group]
  group += 1
print(group)

# #모범답안
# # 정당성 :  항상 최소한의 모험가의 수만 포함하여 그룹을 결성 하면 최대한 많은 그룹이 구성된다.
n = int(input())
data = list(map(int,input().split()))
data.sort()

result = 0 # 총 그룹의수
count = 0 #현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
  count += 1 # 현재 그룹에 해당 모험가를 포함시키기
  if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
    result += 1 # 총 그룹의 수 증가시키기
    count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) #총 그룹의 수 출력

#개선사항: 합리적인 알고리즘을 떠올리도록 해야함