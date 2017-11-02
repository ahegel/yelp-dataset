# -*- coding: utf-8 -*-

import json
import os
import pandas as pd
import ast


business_file = '/data/business.json'
review_file = '/data/review.json'
user_file = '/data/user.json'
tip_file = '/data/tip.json'
checkin_file = '/data/checkin.json'

# BUSINESS.JSON
business_data = []
print 'Reading business.json'
with open(os.path.dirname(__file__) + business_file) as f:
    for line in f:
        business_data.append(json.loads(line))
business_df = pd.DataFrame.from_dict(business_data)
business_sample = business_df[business_df['city'].str.contains('leveland')]
print 'Creating business_sample.json'
with open('business_sample.json', 'w') as f:
    business_sample.to_json(f, orient='records', lines=True)
# now that sample file is made, get list of business id's from it
# convert into a dict with values as keys for fast searching
print 'Getting business_ids'
business_ids = pd.Series(business_sample['business_id'].index.values, index=business_sample['business_id']).to_dict()

# REVIEW.JSON
review_data = []
print 'Reading review.json'
with open(os.path.dirname(__file__) + review_file) as f:
    for line in f:
        newline = ast.literal_eval(line)  # read the line (str) as a dict
        if newline['business_id'] in business_ids:
            review_data.append(json.loads(line))
review_df = pd.DataFrame.from_dict(review_data)
# get list of business id's from business.json and only keep reviews of those businesses
# would normally write it with to_json but it's too big to fit in memory, so write it line by line
print 'Creating review_sample.json line by line'
for row in review_df.iterrows():
    with open('review_sample.json', 'a') as f:
        line = row[1].to_json(f)
        f.write('\n')
# now that sample file is made, get list of user id's from it
# convert into a dict with values as keys for fast searching
print 'Getting user_ids'
user_ids = pd.Series(review_df['user_id'].index.values, index=review_df['user_id']).to_dict()

# USER.JSON
user_data = []
with open(os.path.dirname(__file__) + user_file) as f:
    for line in f:
        newline = ast.literal_eval(line)  # read the line (str) as a dict
        if newline['user_id'] in user_ids:
            user_data.append(json.loads(line))
user_df = pd.DataFrame.from_dict(user_data)
print 'Creating user_sample.json'
with open('user_sample.json', 'w') as f:
    user_df.to_json(f, orient='records', lines=True)

# TIP.JSON
tip_data = []
print 'Reading tip.json'
with open(os.path.dirname(__file__) + tip_file) as f:
    for line in f:
        newline = ast.literal_eval(line)
        if newline['business_id'] in business_ids:
            tip_data.append(json.loads(line))
tip_df = pd.DataFrame.from_dict(tip_data)
print 'Creating tip_sample.json'
with open('tip_sample.json', 'w') as f:
    tip_df.to_json(f, orient='records', lines=True)

# CHECKIN.JSON
checkin_data = []
print 'Reading checkin.json'
with open(os.path.dirname(__file__) + checkin_file) as f:
    for line in f:
        newline = ast.literal_eval(line)
        if newline['business_id'] in business_ids:
            checkin_data.append(json.loads(line))
checkin_df = pd.DataFrame.from_dict(checkin_data)
print 'Creating checkin_sample.json'
with open('checkin_sample.json', 'w') as f:
    checkin_df.to_json(f, orient='records', lines=True)
