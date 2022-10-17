""" 
author: Ryan LaRue; rml5169
"""

import os
import pandas as pd

subdirs = os.listdir('./output')

buys = []
gives = []
has = []
product = []
review = []
user = []

for subdir in subdirs:
    tables = os.listdir('./output/' + subdir)

    buys.append(pd.read_csv('./output/' + subdir + '/' + tables[0], sep="\t"))
    gives.append(pd.read_csv('./output/' + subdir + '/' + tables[1], sep="\t"))
    has.append(pd.read_csv('./output/' + subdir + '/' + tables[2], sep="\t"))
    product.append(pd.read_csv('./output/' + subdir + '/' + tables[3],
                               sep="\t"))
    review.append(pd.read_csv('./output/' + subdir + '/' + tables[4], sep="\t"))
    user.append(pd.read_csv('./output/' + subdir + '/' + tables[5], sep="\t"))

print(len(buys))


aggregate_buys = pd.concat(buys).drop_duplicates()
aggregate_gives = pd.concat(gives, axis=0).drop_duplicates()
aggregate_has = pd.concat(has, axis=0).drop_duplicates()
aggregate_product = pd.concat(product, axis=0).drop_duplicates()
aggregate_review = pd.concat(review, axis=0).drop_duplicates()
aggregate_user = pd.concat(user, axis=0).drop_duplicates()

print(aggregate_buys)
print(aggregate_gives)
print(aggregate_has)
print(aggregate_product)
print(aggregate_review)
print(aggregate_user)

print('writing buys_a')
aggregate_buys.to_csv('./agg/buys_a.tsv', sep='\t', index=False)
print('writing gives_a')
aggregate_gives.to_csv('./agg/gives_a.tsv', sep='\t', index=False)
print('writing gives_a')
aggregate_has.to_csv('./agg/has_a.tsv', sep='\t', index=False)
print('writing product')
aggregate_product.to_csv('./agg/product.tsv', sep='\t', index=False)
print('writing review')
aggregate_review.to_csv('./agg/review.tsv', sep='\t', index=False)
print('writing user')
aggregate_user.to_csv('./agg/user.tsv', sep='\t', index=False)
