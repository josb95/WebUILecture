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
    print(rack)
    s.add_rack(rack[0], rack[1], rack[2], rack[3], rack[4])

cur.close()
con.close()

print(s.Rack_A)
print(s.Rack_B.name)
print(s.Rack_B.stuff)
print(s.Rack_B.quantity)
print(s.Rack_B.col)
print(s.Rack_B.row)
