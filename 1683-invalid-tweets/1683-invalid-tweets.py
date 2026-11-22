import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    new_df=tweets["content"].str.len()>15
    return tweets.loc[new_df,['tweet_id']]