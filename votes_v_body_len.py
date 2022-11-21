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
    query = "SELECT helpful_votes, length(body) as length FROM " \
        "review GROUP BY helpful_votes;"

    # perform db query
    df = pd.read_sql(query, db)
    df.dropna(inplace=True)
    print(df)

    # df.to_csv('output.csv')

    # get regression line
    m, b = np.polyfit(df['length'], df['helpful_votes'] , 1)

    # plot data
    plt.scatter(df['length'], df['helpful_votes'], s=5)
    plt.plot(df['length'], m * df['length'] + b, color='red')

    # add plot labels and display
    plt.ylabel("Helpful Votes Count")
    plt.xlabel("Review Length")
    plt.title("Review Length vs Helpful Votes Count")
    plt.show()

# close the connection at the end or if something goes wrong
except Exception as e:
    db.close()
    print(str(e))
finally:
    db.close()
