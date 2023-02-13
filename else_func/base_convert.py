#10진법까지
def base_conv(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]

print(base_conv(123, 3)) #11120
print(base_conv(16, 3)) #121
print(base_conv(27, 3)) #1000
print(base_conv(13124, 3)) #200000002

#15진법까지 고려 (0 ~ A ~ F)
def base_conv_expn(n, q):
    num = '0123456789ABCDEF'
    rev_base = ''
    
    if n == 0:
        return '0'

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(num[mod])

    return rev_base[::-1]

print(base_conv_expn(15, 15)) #11120

