import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:

    new_df=users['mail']
    filtered_df=new_df.str.match(r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$', na=False)
    last_df=users[filtered_df]
    return last_df