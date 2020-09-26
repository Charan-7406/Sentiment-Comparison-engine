import tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
import preprocessor as p
import re
import matplotlib.pyplot as plt

#add your own keys
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN =""
ACCESS_TOKEN_SECRET=""

auth = tweepy.OAuthHandler(consumer_key = CONSUMER_KEY,consumer_secret = CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)

def perc_response(a):
  p_a = 100 * (len(a) / 57)
  return round(p_a, 2)

search_input = input("Enter your first keyword/hash you want to analyze:")
search_input1 = input("Enter your second keyword/hash you want to analyze:")

all_tweets = []
for tweet in tweepy.Cursor(api.search, q=search_input, tweet_mode='extended', lang="en", result_type='recent').items(57):
  all_tweets.append(tweet.full_text)

tweets_clean = []
for tweet in all_tweets:
    tweet = p.clean(tweet)
    tweet = ' '.join(re.sub(':', ' ', tweet).split())
    tweets_clean.append(tweet)

positive_l = []
negative_l = []
neutral_l = []

for tweet in tweets_clean:
  if analyser.polarity_scores(tweet).get('compound') >= 0.05:
    positive_l.append(tweet)
  elif analyser.polarity_scores(tweet).get('compound') <= -0.05:
    negative_l.append(tweet)
  else:
    neutral_l.append(tweet)

positive = perc_response(positive_l)
negative = perc_response(negative_l)
neutral = perc_response(neutral_l)

# For the second hash word
all_tweets1 = []
for tweet in tweepy.Cursor(api.search, q=search_input1, tweet_mode='extended', lang="en", result_type='recent').items(57):
  all_tweets1.append(tweet.full_text)

tweets_clean1 = []
for tweet in all_tweets1:
  tweet = p.clean(tweet)
  tweet = ' '.join(re.sub(':', ' ', tweet).split())
  tweets_clean1.append(tweet)

positive_l1 = []
negative_l1 = []
neutral_l1 = []
for tweet in tweets_clean1:
  if analyser.polarity_scores(tweet).get('compound') >= 0.05:
    positive_l1.append(tweet)
  elif analyser.polarity_scores(tweet).get('compound') <= -0.05:
    negative_l1.append(tweet)
  else:
    neutral_l1.append(tweet)

positive1 = perc_response(positive_l1)
negative1 = perc_response(negative_l1)
neutral1 = perc_response(neutral_l1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 10))  # ax1,ax2 refer to your two pies
labels = ['Positive', 'negative', 'neutral']
values = [positive, negative, neutral]
colors = ['green', 'red', 'yellow']
explode = (0, 0.1, 0.1)
ax1.pie(values, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90) # plot first pie
ax1.set_title('Peoples sentiment on the topic '+search_input+' is:')

labels1 = ['Positive', 'negative', 'neutral']
values1 = [positive1, negative1, neutral1]
colors = ['green', 'red', 'yellow']
explode = (0, 0.1, 0.1)
ax2.pie(values1, labels=labels1, colors=colors,explode=explode, autopct='%1.1f%%', shadow=True,startangle=90)  # plot second pie
plt.title('Peoples sentiment on the topic ' + search_input1 + ' is:')

if (positive > positive1):
  print("Based on the sentiment's analyzed for the above keyword/hash submitted: ")
  print(f'{search_input} is better than {search_input1}.')
else:
  print("Based on the sentiment's analyzed for the above keyword/hash submitted: ")
  print(f'{search_input1} is better than {search_input}.')

#plotting
plt.show()