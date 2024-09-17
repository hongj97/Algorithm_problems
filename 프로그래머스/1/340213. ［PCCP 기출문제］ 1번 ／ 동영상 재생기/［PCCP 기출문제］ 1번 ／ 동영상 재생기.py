#video_len: 동영상의 길이, pos: 직전의 재생위치, op_start, op_end: 오프닝 시작/끝나는 시각
#commands: 사용자의 입력
def min2sec(time:str):
    m, s = list(map(int, time.split(':')))
    total_s = m*60 +  s
    return total_s

def solution(video_len, pos, op_start, op_end, commands):
    answer = '' #사용자의 입력이 끝난 후 동영상 위치(mm:ss)
    pos_sec = min2sec(pos)
    
    #오프닝 건너뛰기
    if min2sec(op_start)<=pos_sec<=min2sec(op_end):
        pos_sec = min2sec(op_end)
    
    result_sec = pos_sec
    for command in commands:
        if command == "prev":   #10초 전으로 이동
            result_sec = result_sec - 10
            if result_sec < 10: # 처음 위치로 이동 
                result_sec = 0
        elif command == "next": #10초 후로 이동
            result_sec = result_sec + 10
            if (min2sec(video_len) - result_sec) < 10  : #남은 시간이 10초 미만
                result_sec = min2sec(video_len)
        # print(f"{command}, {result_sec}")
        
        # 오프닝 건너뛰기
        if min2sec(op_start)<=result_sec<=min2sec(op_end):
            result_sec = min2sec(op_end)
    
    a_min = str(result_sec//60)
    if len(a_min) ==1:
        a_min = "0" + a_min
    a_sec = str(result_sec % 60)
    if len(a_sec) ==1:
        a_sec = "0" + a_sec
    # print(a_min, a_sec)
    answer = a_min+":"+a_sec
    return answer