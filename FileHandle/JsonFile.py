# import thu vien json de su dung : khac vs Java phai cai them Dependency
import json     # doi tuong trong python -> du lieu Json
from xml.etree.ElementTree import indent

# cac thao tac voi file json : doc, sua, them, xoa

# thao tac lay du lieu cua doi tuong chuyen sang file json
# json.dump(<doi tuong>, <file can chuyen>,<chuyen theo ascci>, <thut dau dong = >)
# thuoc tinh doi tuong nen sap xephop li ko in thieu
thuan = {"Name" : "thuan", "ID" : "24022461", "School" : "UET"}

with open("DataJS.json","w", encoding='utf-8') as file:
  json.dump(thuan,file,ensure_ascii=False,sort_keys=True,indent=4)

# gio in file Json vua tao thoang qua load
with open("DataJS.json","r",encoding='utf-8') as file:
  data = json.load(file)
print(data)


# neu nhieu doi tuong hon thi dung tuple trong list
users = [
  {"Name" : "Thuan", "ID" : "120", "School" : "UET"},
  {"Name" : "Ha", "ID" : "222", "School" : "AJC"},
  {"Name" : "Cam", "ID" : "233", "School" : "Duma"}
]

with open("DataJS.json","w", encoding='utf-8') as file:
  json.dump(users,file,ensure_ascii=False,sort_keys=True,indent=4)