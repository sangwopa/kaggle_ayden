# 파일 이름 분할
def split_file_name(fileNm):
    con = []
    stts = 0
    str1, str2, str3 = '', '', ''
    for i in range(len(fileNm)):
        if stts == 0:
            if fileNm[i].isdigit():
                stts = 1
                str2 += fileNm[i]
            else:
                str1 += fileNm[i]
        elif stts == 1:
            if not fileNm[i].isdigit():
                str3 = fileNm[i:]
                con.extend([str1, str2, str3])
                break
            else:
                str2 += fileNm[i]
    
    if str3 == '':
        con.extend([str1, str2, str3])
                
    return con

def solution(files):
    tmp = [split_file_name(i) for i in files]
    
    # 다중 리스트 정렬
    # 이전 기준 중복일 경우 고려하려면 튜플 안 x[i] 추가
    # +면 오름차순, -면 내림차순
    # 아래 함수는 0 index 오름차순, 1 index 내림차순
    tmp.sort(key=lambda x: (x[0].lower(), -int(x[1])))

    return [''.join(i) for i in tmp]


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))