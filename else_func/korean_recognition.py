import re

#한글로만 이루어진 문자열인지 확인
def iskorean(text):    
    hanCount = re.compile(u'[\u3130-\u318F\uAC00-\uD7A3]+')
    
    con = []
    
    for i in text:
        con_tmp = bool(hanCount.match(i))
        con.append(con_tmp)
        
    if False in con:
        return False
    else:
        return True