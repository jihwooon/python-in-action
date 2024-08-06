print('hello')

print('a bunch of words')

print('hello ' + 'there')

print('-' * 30)

print('' * 30)

upper = 'hello'.upper()
print(upper)

strip = '    abc'.strip()
print(strip)

abc__strip = 'abc'.strip('a')
print(abc__strip)

abca__strip = 'abca'.strip('a')
print(abca__strip)

count = 'abc'.count('a')
print(count)

aaabcaa__count = 'aaabcaa'.count('a')
print(aaabcaa__count)

ababa__count = 'ababa'.count('aba')
print(ababa__count)

dollars = 250
dollars + 1
print(dollars) # 251를 기대 했지만 250이 출력 된다.

dollars = dollars + 1
print(dollars) # 결과를 보존하고 있어 할당문이 필요하다.
