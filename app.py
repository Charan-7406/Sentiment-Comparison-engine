# Importing required libraries
import streamlit as st
import tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
import preprocessor as p
import re
import matplotlib.pyplot as plt
from streamlit import caching
caching.clear_cache()


@st.cache()
def perc_response(a):
    p_a = 100 * (len(a) / 61)
    return round(p_a, 2)


st.set_option('deprecation.showPyplotGlobalUse', False)


CONSUMER_KEY = "DdNtxsyingxVz1oZKYs1HNzV7"
CONSUMER_SECRET = "r1nRXAi1PCIxGRbLqw65OoC606PLdQIGqZOAppxPMYK73IlM58"
ACCESS_TOKEN ="1285509929856495618-YVjTWTsYZD3c2p6PK2qAnKbtqcH0Ja"
ACCESS_TOKEN_SECRET="IA4ej6Im7GZHupSan2lovPIssIDuaqhPu5ASDPokvwZqC"

auth = tweepy.OAuthHandler(consumer_key = CONSUMER_KEY,consumer_secret = CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)

def about():
    st.write(
        '''
        **Sentiment comparison engine **.
        NLP plays a major role in this sentiment comparison engine project.
        First using the library 'tweepy' we obtain tweets realted to the keywords that is submitted and then the tweets are preprocessed.
        Then using sentiment analysis i.e. vadersentiment we get the scores for the tweet.
        Sentiment Analysis is the process of ‘computationally’ determining whether a piece of writing is positive, negative or neutral.
        It’s also known as opinion mining, deriving the opinion or attitude of a speaker.
        VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media.
        Based on the positive scores obtained, we understand which is the better keyword/topic .


        The 2 important libraries used here are:
            1. tweepy
            2. vadersentimet 

Read more :point_right:https://blog.quantinsti.com/vader-sentiment/
        ''')

def main():
    st.title("Sentiment Comparison App : ")
    activities = ["Home", "Know more"]
    choice = st.sidebar.selectbox("About:", activities)

    if choice == "Home":

        st.write("Go to the About section from the sidebar to learn more about the project")
        search_input = st.text_input("Enter your first keyword/hash you want to analyze:")
        search_input1 = st.text_input("Enter your second keyword/hash you want to analyze:")
        if search_input and search_input1 is not None:
            if st.button("Analyze"):
                # For the first hash word
                all_tweets = []
                for tweet in tweepy.Cursor(api.search, q=search_input, tweet_mode='extended', lang="en", result_type='recent').items(61):
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
                for tweet in tweepy.Cursor(api.search, q=search_input1, tweet_mode='extended', lang="en", result_type='recent').items(61):
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
                st.pyplot()

                if (positive > positive1):
                    st.subheader("Based on the sentiment's analyzed for the above keyword/hash submitted: ")
                    st.success(f'**{search_input}** is better than **{search_input1}**.')
                else:
                    st.subheader("Based on the sentiment's analyzed for the above keyword/hash submitted: ")
                    st.success(f'**{search_input1}** is better than **{search_input}**.')

    elif choice == "Know more":
        about()

if __name__ == "__main__":
    main()

