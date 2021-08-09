hand_1=['J', 'A', 'A', '2']
hand_2=['9', '6', 'K', 'A', '5', 'J']

# sum1 = 0
# sum2 = 0

len1 = len(hand_1) - 1
len2 = len(hand_2) - 1

while len1 >= 0:
    if hand_1[len1] == 'A':
        hand_1.pop(len1)
        hand_1.append('A')
    len1 -= 1

while len2 >= 0:
    if hand_2[len2] == 'A':
        hand_2.pop(len2)
        hand_2.append('A')
    len1 -= 1

print(hand_1)
print(hand_2)

# for i in hand_1:
#     if i == 'K' or i == 'Q' or i == 'J':
#         i = 10
#     if i == 'A' and sum1 <= 10:     
#         sum1 += 11
#     elif i == 'A' and sum1 > 10:
#         sum1 += 1
#     else:
#         sum1 += int(i)

# for i in hand_2:
#     if i == 'K' or i == 'Q' or i == 'J':
#         i = 10
#     if i == 'A' and sum2 <= 10:
#         sum2 += 11
#     elif i == 'A' and sum2 > 10:
#         sum2 += 1
#     else:
#         sum2 += int(i)


