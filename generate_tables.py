""" 
author: Ryan LaRue; rml5169
"""

import pandas as pd
import time

import os

def make_directory(dir_name):
    dir = os.path.dirname(__file__)
    path = os.path.join(dir, 'output', dir_name)
    os.mkdir(path)
    return path

def extract_path(file_name):
    tokens = file_name.split('.')
    file = tokens[1].split('/')
    return file[-1]

def generate_tables(file_name, rows):
    df = pd.read_csv(file_name, sep='\t', on_bad_lines='skip', nrows=rows)
    df = df.rename(columns=
                   {'customer_id': 'user_id',
                    'review_headline': 'headline',
                    'review_date': 'date',
                    'review_body': 'body',
                    'product_category': 'category',
                    'product_title': 'title',
                    'product_parent': 'parent'
                    }
                   )

    df = df.replace({'verified_purchase': {'Y': 1, 'N': 0}})
    df = df.replace({'vine': {'Y': 1, 'N': 0}})

    name = extract_path(file_name)

    path = make_directory(name)

    # create User table
    user = df['user_id'].drop_duplicates()
    user.to_csv(path + '/user.tsv', sep='\t', index=False)

    # create Review table
    review = df[['review_id', 'star_rating', 'helpful_votes', 'total_votes',
                 'vine', 'verified_purchase', 'headline', 'body',
                 'date']].drop_duplicates()
    review.to_csv(path + '/review.tsv', sep='\t', index=False)

    # create Product table
    product = df[['product_id', 'parent', 'title', 'category']].drop_duplicates()
    product.to_csv(path + '/product.tsv', sep='\t', index=False)

    # create GivesA table
    gives_a = df[['user_id', 'review_id']]
    gives_a.to_csv(path + '/gives_a.tsv', sep='\t', index=False)

    # create HasA table
    has_a = df[['review_id', 'product_id']]
    has_a.to_csv(path + '/has_a.tsv', sep='\t', index=False)

    # create BuysA table
    buys_a = df[['user_id', 'product_id']]
    buys_a.to_csv(path + '/buys_a.tsv', sep='\t', index=False)


def process_file(file_path):
    start = time.time()
    generate_tables('./data/' + file_path, 50000)
    end = time.time()
    print('Processed', file_path, 'after', end-start, 'seconds')


tsvs = os.listdir('./data')

for tsv in tsvs:
    process_file(tsv)






