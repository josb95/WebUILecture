# a = set()
# a = {'bsd', 'asd', 'geg', 'jwa', 'zsdf', 'saw', 'awb'}
# print(a)
# a = sorted(a)
# print(a)

counter_list = list()

counter_list.append('abc')
counter_list.append('bcd')
counter_list.append('cde')

print(counter_list)
del counter_list
try:
    print(counter_list)
except NameError:
    print("정의되지 않은 변수가 호출되었습니다.")
