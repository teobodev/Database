# ██████╗  █████╗ ██╗  ██╗ █████╗ ██████╗ ██╗██████╗ 
# ██╔══██╗██╔══██╗██║  ██║██╔══██╗██╔══██╗██║██╔══██╗
# ██████╦╝███████║███████║██║  ██║██║  ██║██║██████╔╝
# ██╔══██╗██╔══██║██╔══██║██║  ██║██║  ██║██║██╔══██╗
# ██████╦╝██║  ██║██║  ██║╚█████╔╝██████╔╝██║██║  ██║
# ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝

# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# 🌐 https://github.com/teobodev/Database/blob/main/LICENSE
# 👤 https://t.me/baxa_akee_2602

# identity your massage id


name = input("What is the name: ")
surname = input("What is the surname: ")
year = input("Enter the year: ")
date = input("Date of birth: ")
something_add = input('Do you want to add others informations? (y/n)')


import sqlite3 as sql
import time as tm

con = sql.connect('database.db')

c = con.cursor()

c.execute(f"""CREATE TABLE IF NOT EXISTS information (ism TEXT, familiya TEXT, year INTERGER, birthday TEXT)""")
c.execute(f"""INSERT INTO information VALUES ('{name}', '{surname}', {year}, {date})""")

while something_add == "y":
    name = input("What is the name: ")
    surname = input("What is the surname: ")
    year = input("Enter the year: ")
    date = input("Date of birth: ")
    something_add = input('Do you want to add others informations? (y/n)')
    c.execute(f"""INSERT INTO information VALUES ('{name}', '{surname}', {year}, {date})""")
if something_add == "n":
    print("Thank you for giving information!")
    


con.commit()
con.close()
