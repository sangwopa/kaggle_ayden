import random
import datetime

#생년, 성별을 인수로 받아 임의의 주민등록번호 생성
def make_private_num(age, gen):
    if len(age) == 1:
        age = "0" + str(age)
    if gen >= 1 and gen<= 2:
        year = "19" + str(age)
    else:
        year = "20" + str(age)
        
    test_date1, test_date2 = datetime.date(int(year), 1, 1), datetime.date(int(year), 12, 31)

    time_between_dates = test_date2 - test_date1

    days_between_dates = time_between_dates.days

    random_number_of_days = random.randrange(days_between_dates)

    random_date = test_date1 + datetime.timedelta(days=random_number_of_days)
    
    return str(age) + str(random_date)[5:7] + str(random_date)[8:10] + '-' + str(gen) + str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
