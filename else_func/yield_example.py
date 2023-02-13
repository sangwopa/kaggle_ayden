import time

def return_abc():
  alphabets = []
  for ch in "ABC":
    time.sleep(1)
    alphabets.append(ch)
  return alphabets

# 3초 후에 A,B,C 한번에 출력
for ch in return_abc():
    print(ch)
  
def yield_abc():
    for ch in "ABC":
        time.sleep(1)
        yield ch

# 1초 마다 A,B,C 차례로 출력
for ch in yield_abc():
    print(ch)