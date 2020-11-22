# IT WORKS - COOL

# Looking at tweets from the 2020 election

from wordcloud import WordCloud, STOPWORDS
import csv

with open('./data_twitter/hashtag_donaldtrump.csv', encoding = 'utf8') as f:
    rows = csv.reader(f)
    headers = next(rows)
    print(headers)
    text = ""
    for row in rows:
        text_list = str(row[3])
        text.append(text_list)
    print(len(text))


