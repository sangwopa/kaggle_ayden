import pandas as pd
import random
import numpy as np
import re
from collections import Counter

FIRST_NAME1 = ['김', '이', '박', '최', '정']
FIRST_NAME2 = ['강', '조', '윤', '장', '임', '한', '오', '서', '신', '권', '황', '안', '송'
                , '전', '홍', '유', '고', '문', '양', '손', '배', '조', '백', '허', '유', '남'
                , '심', '노', '정', '하', '곽', '성', '차', '주', '우', '구', '신', '임', '전'
                , '민', '유', '류', '나', '진', '지', '엄', '채', '원', '천', '방', '공', '강'
                , '현', '함', '변', '염', '양', '변', '여', '추', '노', '도', '소', '신', '석'
                , '선', '설', '마', '길', '주', '연', '방', '위', '표', '명', '기', '반', '라'
                , '왕', '금', '옥', '육', '인', '맹', '제', '모', '장', '남궁', '탁', '국'
                , '여', '진', '어', '은', '편', '구', '용', '유', '예', '경', '봉', '정'
                , '석', '사', '부', '황보', '가', '복', '태', '목', '진', '형', '계', '최'
                , '피', '두', '지', '감', '장', '제갈', '음', '빈', '동', '온', '사공', '호'
                , '경', '범', '전', '선우', '좌', '설', '팽', '승', '간', '하', '상', '시'
                , '갈', '서문', '진']

#데이터 숫자형 치환
def return_numcol(columns, dtypes):
    
    num_columns = [x for x in columns.tolist() if (('int' in dtypes[x]) or ('float' in dtypes[x]))]
    
    return num_columns

#데이터 범주형 치환
def return_catcol(columns, dtypes):
    
    cat_columns = [x for x in columns.tolist() if ((dtypes[x] == 'object') or (dtypes[x] == 'bool'))]
    
    return cat_columns

#한글 이름 인식
def compute_name_recognition(self, data):
    if (not self.iskorean(data)) or (not ((len(data)>=2) and (len(data)<=5))):
        return False

    if (not ((data[0] in FIRST_NAME1) or (data[:2] in FIRST_NAME1))) and (not ((data[0] in FIRST_NAME2) or (data[:2] in FIRST_NAME2))):
        return False
    
    return True




    
    
    
    

