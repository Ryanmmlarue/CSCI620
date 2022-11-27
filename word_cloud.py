from google.colab import drive
drive.mount('/content/gdrive')

import pandas as pd
import os
dir = '/content/gdrive/Shareddrives/CSCI 620/Project/output/'
files = os.listdir(dir)
review= []
for file_ in files:
  data = pd.read_csv(dir + file_ + '/review.tsv', index_col = False, sep="\t")
  review.append(data['body'].values)

flat_list = [item for sublist in review for item in sublist]

from collections import Counter
word_could_dict=Counter(flat_list)
wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(word_could_dict)

plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()