""" 
author: Ryan LaRue; rml5169
"""

import mysql.connector


database = mysql.connector.connect(host="129.21.100.38", user="CSCI620",
                                   password="CSCI620_5")


cursor = database.cursor()

cursor.execute("USE `amazon reviews`")
cursor.execute("SELECT * FROM review")

for line in cursor:
    print(line)