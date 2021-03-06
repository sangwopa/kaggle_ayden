import random

#한글 이름 생성
def randomKoreanLastName():
    lst_nm_idx1 = ['김', '이', '박', '최', '정']
    lst_nm_idx2 = ['강', '조', '윤', '장', '임', '한', '오', '서', '신', '권', '황', '안', '송'
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
    if random.choices(range(2))[0] == 1:
        con_tmp = random.choices(lst_nm_idx2)[0]
    else:
        con_tmp = random.choices(lst_nm_idx1, weights=(21,14,8,4,4), k=1)[0]
    
    return con_tmp

def randomKoreanFirstName(size : int):
    nm_idx = ''.join(['가각간갈감갑강개객갱갹거건걸검겁게격견결겸경계고곡곤골공곶과곽관괄광괘괴괵굉교구국군굴궁권궐궤귀규균귤극근글금급긍기긴길김끽나낙난날남납낭내녀녁년념녑녕노농뇌뇨누눈눌뉴뉵능니닉닐다단달담답당대댁덕도독돈돌동두둔둘득등라락란랄람랍랑래랭'
            ,'략량려력련렬렴렵령례로록론롱뢰료룡루류륙륜률륭륵름릉리린림립마막만말망매맥맹멱면멸명몌모목몰몽묘무묵문물미민밀박반발방배백번벌범법벽변별병보복본볼봉부북분불붕비빈빙사삭산살삼삽상새색생서석선설섬섭성세소속손솔송쇄쇠수숙순술숭쉬슬습승시'
            ,'식신실심십쌍씨아악안알암압앙애액앵야약양어억언얼엄업에엔여역연열염엽영예오옥온올옹와완왈왕왜외요욕용우욱운울웅원월위유육윤율융은을음읍응의이익인일임입잉자작잔잠잡장재쟁저적전절점접정제조족존졸종좌죄주죽준줄중즉즐즙증지직진질짐집징차착'
            ,'찬찰참창채책처척천철첨첩청체초촉촌총촬최추축춘출충췌취측층치칙친칠침칩칭쾌타탁탄탈탐탑탕태택탱터토톤통퇴투퉁특틈파판팔패팽퍅편폄평폐포폭표품풍피픽필핍하학한할함합항해핵행향허헌헐험혁현혈혐협형혜호혹혼홀홍화확환활황회획횡효후훈훌훙훤훼휘휴휼흉흑흔흘흠흡흥희히힐'])
    
    return ''.join(random.choice(nm_idx) for _ in range(size))

def randomKoreanFullName():
    return randomKoreanLastName() + randomKoreanFirstName(2)