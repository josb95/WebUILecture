from flask import Flask, render_template, jsonify
import time
import cx_Oracle as ora
import WareHouse.Storage as WS
import pandas as pd


s = WS.Storage(9, 5)

con = ora.connect("stock/1234@localhost:1521/orcl")


cur = con.cursor()
sql = "select * from rack"
temp = cur.execute(sql)

df_rack = pd.read_sql(sql, con=con)

for i in range(8):
    rack = cur.fetchone()
    # print(rack)
    s.add_rack(rack[0], rack[1], rack[2], rack[3], rack[4])

cur.close()
con.close()

# print(s.Rack_A)
# print(s.Rack_B.name)
# print(s.Rack_B.stuff)
# print(s.Rack_B.quantity)
# print(s.Rack_B.col)
# print(s.Rack_B.row)

# print(s.Rack_A)
s.Rack_A.add_Stuff('1', 'abc')
s.Rack_A.add_Stuff('2', 'abc')
s.Rack_B.add_Stuff('3', 'abc')
s.Rack_B.add_Stuff('4', 'bbc')  # 불일치
s.Rack_C.add_Stuff('5', 'bbc')
s.Rack_C.add_Stuff('6', 'bbc')
s.Rack_E.add_Stuff('7', 'cbc')
s.Rack_E.add_Stuff('8', 'cbc')
# s.Rack_A.remove_Stuff('2')
s.Rack_B.remove_Stuff('3')
print(s.Rack_B.stuff)

# s.Rack_A.remove_Stuff_byName('abc')
# s.Rack_B.remove_Stuff_byName('abc')

# s.Rack_A.add_Stuff('3', 'abc')
# print(s.Rack_A.quantity)
s.calculate_Stock()
print(s.stock_dict)
s.update_Stock()

# print(s.Stock_A.name, s.Stock_A.quantity)
# print(s.Stock_B.name, s.Stock_B.quantity)
# print(s.Stock_C.name, s.Stock_C.quantity)
# print()
# print(s.stock_list[0].name, s.stock_list[0].quantity)
# print(s.stock_list[1].name, s.stock_list[1].quantity)
# print(s.stock_list[2].name, s.stock_list[2].quantity)

# 불량 확인
# print(s.Rack_A.stuff_list[0].isBad)
# print(s.Rack_A.stuff_list[1].isBad)
# print(s.Rack_B.stuff_list[0].isBad)
# print(s.Rack_C.stuff_list[0].isBad)
# print(s.Rack_C.stuff_list[1].isBad)
# print(s.Rack_E.stuff_list[0].isBad)
# print(s.Rack_E.stuff_list[1].isBad)


# Stock Setting 테스트
s.insert_Setting_Stock('abc', 2)
s.insert_Setting_Stock('bbc', 2)
s.insert_Setting_Stock('cbc', 2)

print(s.stock_setting_dict)

s.update_Setting_Stock('abc', 3)

print(s.stock_setting_dict)

s.delete_Setting_Stock('bbc')

print(s.stock_setting_dict)
