import datetime

import pandas as pd
import streamlit as st
import tweepy

from tweepy_df import tweets2df

# DataFrameをCSVに変換するための関数
@st.experimental_memo
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

# CSV出力結果を初期化
csv_df_filtered = ''
csv_df = ''

# 認証情報を格納
consumer_key = st.secrets['consumer_key']
consumer_secret = st.secrets['consumer_secret']
access_token = st.secrets['access_token']
access_token_secret = st.secrets['access_token_secret']

# 認証オブジェクトの生成
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)


st.title('30日間のTweet検索App')
st.text('直近30日間のツイートから特定のキーワードに合致するものを抽出するアプリです。')
# API実行時の設定をユーザーから取得するフォーム
st.subheader('検索設定')
st.write('下記の設定を入力して、「実行」ボタンをクリックしてください。')

# 最低フォロワー数による絞り込みの有無
follower_filter = 0
follower_filter = st.checkbox(label='最低フォロワー数による絞り込み')
if follower_filter:
    filter_num = st.select_slider(label='最低フォロワー数', options=[50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000, 3000, 5000, 10000, 20000, 30000, 50000, 100000])

# ユーザー設定フォーム
with st.form('scrape_option_form'):
    search_keyword = st.text_input(label='検索キーワード')
    results_number = st.slider(label='検索結果の取得数（10〜100）', min_value=10, max_value=100)
    st.info('検索結果の取得数には月間上限があるので、多量の実行にはご注意ください。\
            「実行」ボタンを押すたびに実行した取得数が上積みされる形でカウントされていきます。')

    # API検索の実行
    submitted = st.form_submit_button("実行")
    if submitted:
        try:
            if search_keyword and follower_filter:
                hit_tweets = api.search_30_day(label='30daysSearch', query=search_keyword, maxResults=results_number)
                tweets = tweets2df(hit_tweets)
                # DFをフィルタリングして再代入
                tweets_filtered = tweets.loc[:][tweets.loc[:, 'followers_num'] > filter_num]
                # フィルタリングした結果を表示                
                st.subheader('実行結果: フィルタリング後の最大10行を表示')
                st.dataframe(tweets_filtered.head(10))
                with st.expander("フィルタリング後のすべての検索結果をチェック"):
                    st.dataframe(tweets_filtered)
                # CSVとして保存
                csv_df_filtered = convert_df(tweets_filtered)
            elif search_keyword:
                hit_tweets = api.search_30_day(label='30daysSearch', query=search_keyword, maxResults=results_number)
                tweets = tweets2df(hit_tweets)
                # 結果を表示                
                st.subheader('実行結果: 最初の10行のみ')
                st.dataframe(tweets.head(10))
                with st.expander("すべての検索結果をチェック"):
                    st.dataframe(tweets)
                # CSVとして保存
                csv_df = convert_df(tweets)
            else:
                st.write('検索キーワードを入力してください。')
        except:
            st.write('Unexpeted Error.')

# CSVダウンロードボタン
if csv_df_filtered:
    st.download_button(
        label="CSVとして保存",
        data=csv_df_filtered,
        file_name=f'tweets_{search_keyword}_filtered_{filter_num}.csv',
        mime='text/csv',
        key='download-csv'
    )
elif csv_df:
    st.download_button(
        label="CSVとして保存",
        data=csv_df,
        file_name=f'tweets_{search_keyword}.csv',
        mime='text/csv',
        key='download-csv'
    )
