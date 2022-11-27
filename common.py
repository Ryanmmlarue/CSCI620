from google.colab import drive
import pandas as pd
from collections import Counter
import os
from matplotlib import pyplot as plt

drive.mount('/content/gdrive')

dir = '/content/gdrive/Shareddrives/CSCI 620/Project/output/'
files = os.listdir(dir)
title= []
for file_ in files:
  data = pd.read_csv(dir + file_ + '/product.tsv', index_col = False, sep="\t")
  title.append(data['title'].values)


flat_list = [item for sublist in title for item in sublist]


c = Counter(flat_list)

y = [count for tag, count in c.most_common(20)]
x = [tag for tag, count in c.most_common(20)]

plt.bar(x, y, color='crimson')
plt.title("Top Products sold")
plt.ylabel("Total purchase numbers")
plt.xticks(rotation=90)
for i, (tag, count) in enumerate(c.most_common(20)):
    plt.text(i, count, f' {count} ', rotation=90,
             ha='center', va='top' if i < 10 else 'bottom', color='white' if i < 10 else 'black')
plt.show()