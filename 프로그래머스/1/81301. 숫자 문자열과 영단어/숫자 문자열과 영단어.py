def solution(s):
    answer = 0
    convert_dict = {"zero":"0", "one":"1", "two":
"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    
    for k in convert_dict.keys():
        if k in s:
            s= s.replace(k, convert_dict[k])
        if s.isdigit():
            break
    answer = int(s)
    return answer