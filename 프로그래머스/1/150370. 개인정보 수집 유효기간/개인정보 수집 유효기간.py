def after_ymd(ymd_list, plus_month):
    year, month, day =ymd_list
    after_month = month + plus_month
    if after_month > 12:
        after_month = after_month - 12*(after_month//12)
        year = year + (month+plus_month)//12
        #after_month가 12로 나눠떨어지는 경우
        if after_month % 12==0:
            after_month = 12
            year = year - 1 
    #보관가능 마지막 날
    if day-1==0:
        day = 28
        after_month = after_month-1
        if after_month ==0:
            after_month =12
            year = year-1
    else:
        day = day-1    
    # print("수집일자: ", ymd_list)        
    # print("마지막날: ", year, after_month, day)
    return [year, after_month, day]

def compare_date(today, after):
    #after가 today보다 크다면 true
    t_y, t_m, t_d = today
    a_y, a_m, a_d = after
    if a_y > t_y:   #나중연도가 크다면
        return False
    elif a_y==t_y and a_m > t_m: #연도같지만 나중월이 크다면
        return False
    elif a_y==t_y and a_m==t_m and a_d >= t_d: #연도 월이 같지만 나중일이 같거나 크다면
        return False
    else:
        return True

def solution(today, terms, privacies):
    answer = []
    ymd = list(map(int, today.split('.'))) #year month day (today)
    terms_dict = {term.split(' ')[0]:int(term.split(' ')[1]) for term in terms}
    # print("오늘: ", ymd)
    for i in range(len(privacies)):
        term = privacies[i][-1] #유효기간
        p_term = terms_dict[term] #약관
        p_ymd = list(map(int, privacies[i][:-2].split('.')))
        # print(p_ymd, p_term)
        
        after_date = after_ymd(p_ymd, p_term)
        if compare_date(ymd, after_date): #유효기간이 지났다면
            answer.append(i+1)
    # print(answer)
    return answer