n = int(input()) #학생수
score_list = list(map(int, input().split()))#점수
# print(score_list)

answer = max(score_list)- min(score_list)
print(answer)