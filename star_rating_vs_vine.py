""" 
author: Ryan LaRue; rml5169
"""
import mysql.connector as connection
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ip = "172.30.64.1"
user = "CSCI620"
pwd = "CSCI620"
db_name = 'amazon_reviews'

try:
    # establish db connection
    db = connection.connect(host=ip, user=user, password=pwd, database=db_name)
    vine_query = "SELECT AVG(star_rating) FROM review WHERE vine = 1;"
    no_vine_query = "SELECT AVG(star_rating) FROM review WHERE vine = 0;"

    # perform db query
    vine_df = pd.read_sql(vine_query, db)
    no_vine_df = pd.read_sql(no_vine_query, db)

    print('Average Star Rating For Vine Reviews:', vine_df['AVG(star_rating)'].iloc[0])
    print('Average Star Rating For Non-Vine Reviews:',no_vine_df['AVG(star_rating)'].iloc[0])

    # df.to_csv('output.csv')

# close the connection at the end or if something goes wrong
except Exception as e:
    db.close()
    print(str(e))
finally:
    db.close()