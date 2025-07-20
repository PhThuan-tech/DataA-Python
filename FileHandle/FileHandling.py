"""
Doc file co nhieu kieu:
 w  : chi viet
 r  : chi doc
 r+ va w+ : doc + viet file
 rb : doc file duoi dang ma nhi phan
 rb+ : doc va viet duoi dang ma nhi phan
.... con nhieu kieu khac nx
"""
"""

# in ra noi dung file
file = open("PythonText","r")
content = file.read()
print(content)
file.close()

# viet them vao file da co
file1 = open("PythonText", "w")
file1.write("Dong nay la thu 7")
file1.close()

"""

# xu dung khoi lenh with .. as : tranh bi loi khi quen chua cau lenh close() cuoi doan code
with open("PythonText", "r") as file:
    content = file.read()
    print(content)



