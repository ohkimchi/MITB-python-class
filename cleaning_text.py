# -*- coding: utf-8 -*-
import json
import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np

pd.set_option('display.max_rows', 5000000)
pd.set_option('display.max_columns', 5000000)
pd.set_option('display.width', 10000000)

# Next we will read the data in into an array that we call tweets.
# dir = '/Users/bigmac/PycharmProjects/MITB-python-class/max-test.txt'
dir = '/Users/bigmac/PycharmProjects/MITB-python-class/actors_data.txt'
tweets_data_path = dir

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
print(len(tweets_data))
tweets = pd.DataFrame()


# Func to extract info from dic
def extract_dic_key(string):
    lst = []
    for t in tweets_data:
        lst.append(t[string])
    return lst


# Find all the dict_keys
list_of_keys = list(tweets_data[0].keys())
list_of_relevant_fields = ['text'] # column of 'text'
for i in list_of_relevant_fields:
    tweets[i] = extract_dic_key(i)
# print(pd.DataFrame(tweets))

# Convert df to csv. Don't forget to add '.csv' at the end of the path
tweets.to_csv(r'tweet_text_list.csv', index=None, header=True)

# Create charts

"""
Mining the data
"""


# Function to for text. True if text is foud
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False


movie_list = ['Vagabond', 'Wine Country', 'Always Be My Maybe', 'The Man Without Gravity', 'See You Yesterday',
              'The Wandering Earth', 'Tall Girl', 'Sex Education', 'When the camellia blooms',
              'Interior Design Masters']
# To find word in text
for i in movie_list:
    tweets[i] = tweets['text'].apply(lambda tweet: word_in_text(i, tweet))

# Calculate number of tweets
print(tweets['Vagabond'].value_counts())
# print(tweets['Vagabond'].value_counts()[True])
print(tweets['Wine Country'].value_counts())
print(tweets['Always Be My Maybe'].value_counts())
print(tweets['The Man Without Gravity'].value_counts())
print(tweets['See You Yesterday'].value_counts())
print(tweets['The Wandering Earth'].value_counts())
print(tweets['Tall Girl'].value_counts())
print(tweets['Sex Education'].value_counts())
print(tweets['When the camellia blooms'].value_counts())
print(tweets['Interior Design Masters'].value_counts())


"""
Target relevant tweets
"""


# Plot graph


"""
Extracting links from the relevants tweets
"""


# retrieve links to programming tutorials
# def extract_link(text):
#     regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
#     match = re.search(regex, text)
#     if match:
#         return match.group()
#     return ''
#
#
# tweets['link'] = tweets['text'].apply(lambda tweet: extract_link(tweet))
#
# # Create new Dataframe containing relevant tweets
# tweets_relevant = tweets[tweets['relevant'] == True]
# tweets_relevant_with_link = tweets_relevant[tweets_relevant['link'] != '']
#
# print(tweets_relevant_with_link[tweets_relevant_with_link['python'] == True]['link'])
# print(tweets_relevant_with_link[tweets_relevant_with_link['javascript'] == True]['link'])
# print(tweets_relevant_with_link[tweets_relevant_with_link['ruby'] == True]['link'])
