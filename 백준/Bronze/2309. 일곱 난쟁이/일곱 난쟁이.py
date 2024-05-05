def after_two_sum(lists, target):
    del_num =[]
    for i in range(8):
        for j in range(i+1, 9):
            if lists[i] + lists[j]==target:
                del_num.append(lists[i])
                del_num.append(lists[j])
                ans = [i for i in lists if i not in del_num]
                return ans
short_nine = []
for i in range(9):
    height = int(input())
    short_nine.append(height)
    
tot_sum = sum(short_nine) 
find_sum = tot_sum -100 #제외할 두명의 합

answer = after_two_sum(short_nine, find_sum)
for i in sorted(answer):
    print(i)