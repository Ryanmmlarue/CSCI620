""" 
author: Ryan LaRue; rml5169
"""
import mysql.connector as connection
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from Project.credentials import ip, user, pwd, db_name

try:
    # establish db connection
    db = connection.connect(host=ip, user=user, password=pwd, database=db_name)
    query = "SELECT star_rating, count(star_rating) FROM review GROUP BY star_rating ORDER BY star_rating;"

    # perform db query
    df = pd.read_sql(query, db)

    # df.to_csv('output.csv')

    plt.bar(df['star_rating'], df['count(star_rating)'], width=0.4)

    plt.xlabel("Star Rating")
    plt.ylabel("Number of Instances")
    plt.title("Star Rating Distribution")
    plt.show()

# close the connection at the end or if something goes wrong
except Exception as e:
    db.close()
    print(str(e))
finally:
    db.close()