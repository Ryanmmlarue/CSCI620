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
    query = "SELECT star_rating, SUM(CASE WHEN verified_purchase = 1 THEN 1 " \
            "ELSE 0 END) AS Purchase, SUM(CASE WHEN verified_purchase = 0 " \
            "THEN 1 ELSE 0 END) AS NoPurchase from review GROUP BY star_rating"

    # perform db query
    df = pd.read_sql(query, db)

    stars = np.array(df['star_rating'])
    purchased = np.array(df['Purchase'])
    NoPurchase = np.array(df['NoPurchase'])
    width = 0.35
    x = np.arange(len(stars))

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, purchased, width, label='Purchased')
    rects2 = ax.bar(x + width / 2, NoPurchase, width, label='No Purchase')

    ax.set_ylabel('Instances')
    ax.set_title('Star Ratings Purchased vs Not Purchased')
    ax.set_xticks(x, stars)
    ax.legend()

    fig.tight_layout()
    plt.show()

# close the connection at the end or if something goes wrong
except Exception as e:
    db.close()
    print(str(e))
finally:
    db.close()