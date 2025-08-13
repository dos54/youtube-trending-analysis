import numpy as np
import pandas as pd
import json
from util import print_question_and_answer

num_questions = 0

df = pd.read_csv('data/raw/USvideos.csv')

# Q1: What are the top 5 categories by video count?

top5categories = (
  df['category_id']
  .value_counts()
  .rename_axis('category_id')
  .reset_index(name='count')
  .head(5)
)

with open('data/raw/US_category_id.json', 'r') as f:
  data = json.load(f)

id_map = {item['id']: item['snippet']['title'] for item in data['items']}

top5categories["category_name"] = top5categories['category_id'].astype(str).map(id_map)

num_questions = print_question_and_answer("What are the top 5 categories by video count?",
                          top5categories[['category_name', 'count']],
                          num_questions
                          )


# Q2: What are the top 5 channels by video count?
top_channels = (
  df['channel_title']
  .value_counts()
  .reset_index()
  .head(5)
)

num_questions = print_question_and_answer('What are the top 5 channels by video count?\n', top_channels, num_questions)

# Q3: What % of videos have comments disabled?
comments_disabled = (~df['comments_disabled']).sum()
total_videos = len(df)
comments_enabled_percent = f'{100 * (comments_disabled/total_videos):.1f}%'
num_questions = print_question_and_answer('What percentage of videos have comments enabled?', f'{comments_enabled_percent} of videos have comments enabled', num_questions)


# Q4: What's the average title length of trending videos?

avg_title_length = df['channel_title'].fillna('').str.len().mean()

num_questions = print_question_and_answer('What\'s the average title length of trending videos?', f'{avg_title_length:.1f} characters on average', num_questions)
