import pandas as pd
import snscrape.modules.twitter as sntwitter

tweets_list2 = []

for i, tweet in enumerate(
        sntwitter.TwitterSearchScraper('Minecraft', top='true').get_items()):
    if i > 10:
        break
    tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

for x in tweets_df2["Text"]:
    print("\n -------------------------------------")
    print(x)