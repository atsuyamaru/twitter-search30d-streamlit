import pandas as pd

def tweets2df(hit_tweets):
    """
    Create pandas DataFrame from the hit keywords.
    Pass the hit_tweets object created from tweepy library.
    Return the DataFrame object. 
    """

    # 値（リスト）の中身が空の辞書を作成
    tweets_container = {'user_id': [], 'screen_name': [], 'profile_name': [], 'followers_num': [], 'tweet_date': [], 'tweet_text': []}

    # 1つずつ行データをリストに追加
    for hit_tweet in hit_tweets:
        user_id, screen_name, profile_name, followers_num, tweet_date, tweet_text = \
            hit_tweet.user.id, hit_tweet.user.screen_name, \
            hit_tweet.user.name, hit_tweet.user.followers_count, hit_tweet.created_at, hit_tweet.text
        tweets_container['user_id'].append(user_id)
        tweets_container['screen_name'].append(screen_name)
        tweets_container['profile_name'].append(profile_name)
        tweets_container['followers_num'].append(followers_num)
        tweets_container['tweet_date'].append(tweet_date.strftime('%Y-%m-%d'))
        tweets_container['tweet_text'].append(tweet_text.replace("\n", ""))
    
    tweets = pd.DataFrame(tweets_container)
    return tweets