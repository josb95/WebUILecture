# a = set()
# a = {'bsd', 'asd', 'geg', 'jwa', 'zsdf', 'saw', 'awb'}
# print(a)
# a = sorted(a)
# print(a)






# counter_list = list()

# counter_list.append('abc')
# counter_list.append('bcd')
# counter_list.append('cde')

# print(counter_list)
# del counter_list
# try:
#     print(counter_list)
# except NameError:
#     print("정의되지 않은 변수가 호출되었습니다.")


test_dict = {'abc': 3, 'bbc': 2, 'cbc': 2}
print(test_dict)
print(test_dict['abc'])
for i in test_dict:
    key = i
    value = test_dict[i]
    print("key : {}, value : {}".format(key, value) )
