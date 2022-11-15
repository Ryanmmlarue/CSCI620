import mysql.connector
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random


database = mysql.connector.connect(host="172.101.146.227", user="CSCI620",
                                   password="CSCI620")


cursor = database.cursor()

cursor.execute("USE `amazon_reviews`")

cursor.execute("SELECT product.category, COUNT(product.category) AS num_cat "
               "FROM product "
               "GROUP BY product.category "
               "ORDER BY num_cat")

labels = []
data = []
for line in cursor:
    labels.append(line[0].replace("_", " "))
    data.append(line[1])

plt.bar(labels, data)
plt.title('Total Purchase of Each Category')
plt.xlabel('Categories')
plt.xticks(rotation = 90, fontsize = 8)
plt.ylabel('Number of Purchases')
plt.tight_layout()
plt.show()

total = sum(data)
for i in range(len(data)):
    data[i] = (data[i]/total)*100
colors = random.choices(list(mcolors.CSS4_COLORS.values()),k = 36)
plt.pie(data, colors= colors)
plt.legend(labels = ['%s, %1.1f %%' % (l, s) for l, s in zip(labels,data)], loc='center left',
           bbox_to_anchor=(-0.4, 0.5), fontsize = 8)
plt.show()
