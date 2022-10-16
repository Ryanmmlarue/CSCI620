""" 
author: Ryan LaRue; rml5169
"""

import pandas as pd

def generate_tables(file_name):
    df = pd.read_csv(file_name, sep='\t', on_bad_lines='skip')
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

    # create User table
    user = df['user_id'].drop_duplicates()
    user.to_csv('./output/user.tsv', sep='\t', index=False)

    # create Review table
    review = df[['review_id', 'star_rating', 'helpful_votes', 'total_votes',
                 'vine', 'verified_purchase', 'headline', 'body', 'date']]
    review.to_csv('./output/review.tsv', sep='\t', index=False)

    # create Product table
    product = df[['product_id', 'parent', 'title', 'category']].drop_duplicates()
    product.to_csv('./output/product.tsv', sep='\t', index=False)

    # create GivesA table
    gives_a = df[['user_id', 'review_id']]
    gives_a.to_csv('./output/gives_a.tsv', sep='\t', index=False)

    # create HasA table
    has_a = df[['review_id', 'product_id']]
    has_a.to_csv('./output/has_a.tsv', sep='\t', index=False)

    # create BuysA table
    buys_a = df[['user_id', 'product_id']]
    buys_a.to_csv('./output/buys_a.tsv', sep='\t', index=False)


file_path = 'amazon_reviews_multilingual_US_v1_00.tsv'

generate_tables('./data/' + file_path)
