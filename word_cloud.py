from google.colab import drive
import pandas as pd
import os
from nltk.corpus import stopwords
import nltk
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

drive.mount('/content/gdrive')
stop = stopwords.words('english')

dir = '/content/gdrive/Shareddrives/CSCI 620/Project/output/'
files = os.listdir(dir)
review= []
for file_ in files:
  data = pd.read_csv(dir + file_ + '/review.tsv', index_col = False, sep="\t", skipinitialspace=True)
  data = data[data['body'].notna()]
  data['body'] = data['body'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
  review.append(data['body'].values)

flat_list = [item for sublist in review for item in sublist]

text = (' ').join(flat_list)

text = re.sub('<[^<]+?>', '', text)

flat_list = text.split()

word_could_dict=Counter(flat_list)
wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(word_could_dict)

plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()