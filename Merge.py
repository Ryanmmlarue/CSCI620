"""
author: Ryan Jiau; rsj7519
"""

import pandas as pd
import os
from fnmatch import fnmatch

table1 = []
table2 = []
table3 = []
table4 = []
table5 = []
table6 = []

root = 'output'
pattern1 = "*buys_a.tsv"
pattern2 = "*gives_a.tsv"
pattern3 = "*has_a.tsv"
pattern4 = "*product.tsv"
pattern5 = "*review.tsv"
pattern6 = "*user.tsv"

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern1):
            xpath = os.path.join(path, name)
            data = pd.read_table(xpath)
            data.head()
            table1.append(data)
        elif fnmatch(name, pattern2):
            xpath = os.path.join(path, name)
            data = pd.read_table(xpath)
            data.head()
            table2.append(data)
        elif fnmatch(name, pattern3):
            xpath = os.path.join(path, name)
            data = pd.read_table(xpath)
            data.head()
            table3.append(data)
        elif fnmatch(name, pattern4):
            xpath = os.path.join(path, name)
            data = pd.read_table(xpath)
            data.head()
            table4.append(data)
        elif fnmatch(name, pattern5):
            xpath = os.path.join(path, name)
            data = pd.read_table(xpath)
            data.head()
            table5.append(data)
        elif fnmatch(name, pattern6):
            xpath = os.path.join(path, name)
            data = pd.read_table(xpath)
            data.head()
            table6.append(data)

for x in table1:
    concate_data1 = pd.concat(table1)
    concate_data1.head()

concate_data1.to_csv("merged/buys_a.tsv", sep="\t", index=False)

for x in table2:
    concate_data2 = pd.concat(table2)
    concate_data2.head()

concate_data2.to_csv("merged/gives_a.tsv", sep="\t", index=False)

for x in table3:
    concate_data3 = pd.concat(table3)
    concate_data3.head()

concate_data3.to_csv("merged/has_a.tsv", sep="\t", index=False)

for x in table4:
    concate_data4 = pd.concat(table4)
    concate_data4.head()

concate_data4 = concate_data4.drop_duplicates(subset=["product_id"], keep='first')
concate_data4.to_csv("merged/product.tsv", sep="\t", index=False)

for x in table5:
    concate_data5 = pd.concat(table5)
    concate_data5.head()

concate_data5 = concate_data5.drop_duplicates(subset=["review_id"], keep='first')
concate_data5.to_csv("merged/review.tsv", sep="\t", index=False)

for x in table6:
    concate_data6 = pd.concat(table6)
    concate_data6.head()

concate_data6 = concate_data6.drop_duplicates(subset=["user_id"], keep='first')
concate_data6.to_csv("merged/user.tsv", sep="\t", index=False)
