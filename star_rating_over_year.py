""" 
author: Ryan LaRue; rml5169
"""

import mysql.connector as connection
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from credentials import ip, user, pwd, db_name

try:
    # establish db connection
    db = connection.connect(host=ip, user=user, password=pwd, database=db_name)
    query = "SELECT  MONTH(date), avg(star_rating) from review GROUP BY MONTH(date) ORDER BY MONTH(date);"

    # perform db query
    df = pd.read_sql(query, db)

    # df.to_csv('output.csv')

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug',
              'Sept', 'Oct', 'Nov', 'Dec']
    plt.plot(months, df['avg(star_rating)'])

    plt.xlabel("Month of the Year (Numeric)")
    plt.ylabel("Average Star Rating")
    plt.title("Month of the Year vs Average Star Rating")
    # plt.xticks(1)
    plt.show()

# close the connection at the end or if something goes wrong
except Exception as e:
    db.close()
    print(str(e))
finally:
    db.close()
