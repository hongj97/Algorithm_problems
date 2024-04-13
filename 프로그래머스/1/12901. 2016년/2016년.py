import datetime 

def solution(a, b):
    answer = ''
    days = ['MON','TUE','WED','THU','FRI','SAT', 'SUN']
    dt_date = datetime.date(2016,a, b).weekday()
    # print(dt_date)
    answer = days[dt_date]
    return answer