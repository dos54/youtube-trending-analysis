# Overview

{Important!  Do not say in this section that this is college assignment.  Talk about what you are trying to accomplish as a software engineer to further your learning.}

{Provide a description of the data set that you are analyzing.  Include the link of where you obtained the data.}
This dataset includes statistics about the trending YouTube video statistics. You can find it [here](https://www.kaggle.com/datasets/datasnaek/youtube-new).

{Describe your purpose for writing this software to analyze the data.}
This software should help creators (or people that are just interested!) to learn some new facts about the trending category on YouTube.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the data set, the questions and answers, the code running and a walkthrough of the code.}

[Software Demo Video](https://youtu.be/23dAjZHkDbc)

# Data Analysis Results

{List the questions and the answers you found by doing this analysis.}
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

{Describe the tools that you used to develop the software}
For this project I used Pandas, a data analysis tool for Python
{Describe the programming language that you used and any libraries.}
Languages used: Python
Libraries: Pandas

# Useful Websites

{Make a list of websites that you found helpful in this project}

* [Kaggle.com](https://www.kaggle.com/) has some great, free to use data sets.
* [Pandas documentation](https://pandas.pydata.org/docs/index.html) is a great place to get started with Pandas.

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}

* I would like to incorporate the data scraper, to automatically get the most up-to-date data for analysis.
