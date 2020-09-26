# Sentiment-Comparison-engine
Nlp plays a major role in this project. Based on the keywords given as inputs , tweets based on the keyword are searched, preprocessed and then sentiment analysis is carried out on them to give us a brief idea on which topic/keyword has more positive responses.

# System requirements
 A laptop with python installed and running would be sufficeint.
 
 # Libraries required
* tweepy
* vaderSentiment
* tweet-preprocessor
* matplotlib
* streamlit (used for the deployment of the model)

# About the project:
 NLP plays a major role in this sentiment comparison engine project.
 First using the library 'tweepy' we obtain tweets realted to the keywords that is submitted and then the tweets are preprocessed.
 Then using sentiment analysis i.e. vadersentiment we get the scores for the tweet.
 Sentiment Analysis is the process of ‘computationally’ determining whether a piece of writing is positive, negative or neutral.
 It’s also known as opinion mining, deriving the opinion or attitude of a speaker.
 VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media.
 Based on the positive scores obtained, we understand which is the better keyword/topic.
 
  # This reprository contains:
 * 2 pickle files which has all unique words coverted into numbers or tokens and vice versa.
 * cap_model50.h5 which is the trained model.
 * app.py which is the program which will be deployed on heroku.
 * Proj_imgcap notebook file which is the Jupyter notebook consisting of the implimented program.
 * The remaing files such as setup.sh, requirements.txt, Procfile are used when deploying the model on heroku. 
 

 
