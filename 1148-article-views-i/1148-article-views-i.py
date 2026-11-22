import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    new_df=views['author_id']==views['viewer_id']
    return views.loc[new_df,['author_id']].drop_duplicates().rename(columns={"author_id":"id"}).sort_values(by="id")