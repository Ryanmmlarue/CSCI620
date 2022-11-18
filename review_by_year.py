import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

database = mysql.connector.connect(host="172.101.146.227", user="CSCI620",
                                   password="CSCI620")


cursor = database.cursor()

cursor.execute("USE `amazon_reviews`")

cursor.execute("SELECT DATE_FORMAT(review.date, '%Y') AS date, "
               "COUNT(review.review_id) AS total "
               "FROM review "
               "GROUP BY DATE_FORMAT(review.date, '%Y') "
               "ORDER BY date ASC")
year = []
count = []
for line in cursor:
    year.append(int(line[0]))
    count.append(line[1])

plt.plot(year, count)
plt.xticks(np.arange(2005, 2015+1, step=1))
plt.xticks(rotation = 90, fontsize = 8)
plt.title('Number of Reviews Per Year')
plt.xlabel('Year')
plt.ylabel('Reviews')
plt.show()