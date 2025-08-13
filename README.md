# Overview


This dataset includes statistics about the trending YouTube video statistics. You can find it [here](https://www.kaggle.com/datasets/datasnaek/youtube-new).

This software should help creators (or people that are just interested!) to learn some new facts about the trending category on YouTube.


[Software Demo Video](https://youtu.be/23dAjZHkDbc)

# Data Analysis Results

If you want more up-to-date data, the source code that was used to generate the data file can be found [on github here](https://github.com/mitchelljy/Trending-YouTube-Scraper).
This analysis covered the default dataset found at the prior link, so it is out of date and only includes ~6 months of data.

Question 1: What are the top 5 categories in the Trending tab by view count?
Answer (in order): Entertainment, Music, Howto & Style, Comedy, People & Blogs

Question 2: What are the top 5 channels by video count?
Answer:

| #  | Channel Title                          | Count |
|----|----------------------------------------|-------|
| 1  | ESPN                                   | 203   |
| 2  | The Tonight Show Starring Jimmy Fallon | 197   |
| 3  | TheEllenShow                           | 193   |
| 4  | Vox                                    | 193   |
| 5  | Netflix                                | 193   |

Question 3: What percentage of videos in the trending tab have comments enabled?
Answer: 98.5% of videos have comments enabled

Question 4: What's the average title length of trending videos?
Answer: 12.8 characters on average

# Development Environment

Languages used: Python
Libraries: Pandas

Make sure that you have Pandas installed to run this script.

# Useful Websites

* [Kaggle.com](https://www.kaggle.com/) has some great, free to use data sets.
* [Pandas documentation](https://pandas.pydata.org/docs/index.html) is a great place to get started with Pandas.

# Future Work

* I would like to incorporate the data scraper, to automatically get the most up-to-date data for analysis.
