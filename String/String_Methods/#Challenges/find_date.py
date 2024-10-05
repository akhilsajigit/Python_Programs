date = input("Enter the date[dd/mm/yy] : ")
x = date.split('/')
print(f"""
Day : {x[0]}
Month : {x[1]}
Year : {x[2]}
""")
print(type(x))