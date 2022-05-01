from itertools import count

from pwn import *

dictionary = {'零': 0,
              '一': 1,
              '二': 2,
              '三': 3,
              '四': 4,
              '五': 5,
              '六': 6,
              '七': 7,
              '八': 8,
              '九': 9,
              '十': 10,
              '十一': 11,
              '十二': 12,
              '十三': 13,
              '十四': 14,
              '十五': 15,
              '十六': 16,
              '十七': 17,
              '十八': 18,
              '十九': 19,
              '减': '-',
              '加': '+',
              '模数': 'abs'}

dictionary1 = {0: '零',
               1: '一',
               2: '二',
               3: '三',
               4: '四',
               5: '五',
               6: '六',
               7: '七',
               8: '八',
               9: '九',
               10: '十',
               11: '十一',
               12: '十二',
               13: '十三',
               14: '十四',
               15: '十五',
               16: '十六',
               17: '十七',
               18: '十八',
               19: '十九',
               20: '二十'}

s = connect('91.238.230.93', 8080)
s.recvline()

for _ in count():
    print(s.recvline().decode())
    Str = s.recvline().decode()

    if '减' in Str:
        x = dictionary[Str[2]]
        y = dictionary[Str[4]]
        z = abs(x - y)
    elif '加' in Str:
        x = dictionary[Str[0]]
        y = dictionary[Str[2]]
        z = x + y
    else:
        print(Str)
        print(Str.encode())
        s.interactive()
        break

    z = dictionary1[z]
    print(f'{_}) {Str[:-1]}:  {z}')
    print()
    s.sendline(z.encode())
