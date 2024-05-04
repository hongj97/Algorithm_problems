a, b, v = map(int, input().split())

status = 0
#(up-down)으로 (전체 일수-1)만큼 올라감
#마지막날은 up
tot_day = (v-a) // (a-b)
if (v-a) % (a-b) != 0:
    tot_day += 1
#print(tot_day)
day = tot_day +1
print(day)
