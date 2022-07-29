
specital_col = ['private_number', 'name', 'email', 'phone_number']

mod_dtypes = {'임시일련번호': 'int64',
 '주민등록번호': 'object',
 '혈액형': 'object',
 '은행': 'object',
 '근무년수': 'object',
 '인센티브': 'int64',
 '소유차량': 'object',
 '적금': 'int64',
 '성별': 'object',
 '신장': 'int64',
 '주거형태': 'object',
 '자녀수': 'object',
 '추가컬럼1': 'object',
 '추가컬럼2': 'object',
 '추가컬럼3': 'object',
 '추가컬럼4': 'object',
 '추가컬럼5': 'int64',
 '추가컬럼6': 'object',
 '추가컬럼7': 'object',
 '추가컬럼8': 'object'}

intersection_list = list(set(specital_col) & set(mod_dtypes.values()))

if len(intersection_list) != 0:
    print("공통 요소: ", intersection_list)
else:
    print("공통 요소가 존재하지 않습니다.")