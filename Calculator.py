s = input()
dct_1 = {v: k for k, v in enumerate('один два три четыре пять шесть семь восемь девять десять одиннадцать двенадцать тринадцать четырнадцать пятнадцать шестнадцать семнадцать восемнадцать девятнадцать'.split(), 1)}
dct_10 = {v: 10*k for k, v in enumerate(' двадцать тридцать сорок пятьдесят шестьдесят семьдесят восемьдесят девяносто'.split(), 2)}
dct_100 = {v: 100*k for k, v in enumerate('сто двести триста четыреста пятьсот шестьсот семьсот восемьсот девятьсот'.split(), 1)}
dct_1000 = {v: 1000*k for k, v in enumerate('одна тысяча,две тысячи,три тысячи,четыре тысячи,пять тысяч,шесть тысяч,семь тысяч,восемь тысяч,девять тысяч'.split(','), 1)}
dct_ = {'плюс': '+', 'минус': '-', 'умножить': '*'}
dct = {**dct_1, **dct_10, **dct_100, **dct_1000, **dct_}
d = 0
for elem in s.split():
    if type(dct[elem]) == int:
        d += dct[elem]
    else:
        res = d
        op = dct[elem]
        d = 0
 
if op == '+':
    res += d 
elif op == '-':
    res -= d 
else:
    res *= d 
 
dct_text = {v: k for k, v in dct.items()}
 
txt = []
if res < 0:
    txt.append('минус')
    res *= -1
elif res == 0:
    txt.append('ноль')
 
k = 1000
while k:
    if res > k-1:
        if res > 20:
            txt.append(dct_text[res//k*k])
            res %= k 
        else:
            txt.append(dct_text[res])
            k = 0
    k //= 10
 
print(' '.join(txt))