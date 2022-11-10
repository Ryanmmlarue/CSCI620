""" 
author: Ryan LaRue; rml5169
"""

import mysql.connector as connection
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ip = "172.29.224.1"
user = "CSCI620"
pwd = "CSCI620"
db_name = 'amazon_reviews'

try:
    # establish db connection
    db = connection.connect(host=ip, user=user, password=pwd, database=db_name)
    query = "SELECT helpful_votes, avg(length(body)) as avg_length FROM " \
        "review GROUP BY helpful_votes;"

    # perform db query
    df = pd.read_sql(query, db)
    print(df)

    # df.to_csv('output.csv')

    # get regression line
    m, b = np.polyfit(df['helpful_votes'], df['avg_length'], 1)

    # plot data
    plt.scatter(df['helpful_votes'], df['avg_length'], s=5)
    plt.plot(df['helpful_votes'], m * df['helpful_votes'] + b, color='red')

    # add plot labels and display
    plt.xlabel("Helpful Votes Count")
    plt.ylabel("Average Review Length")
    plt.title("Helpful Votes Count vs Average Review Length")
    plt.show()

# close the connection at the end or if something goes wrong
except Exception as e:
    db.close()
    print(str(e))
finally:
    db.close()
