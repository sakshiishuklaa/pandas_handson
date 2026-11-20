import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    new_df=pd.merge(left=customers,right=orders,left_on = 'id',right_on='customerId' ,how = 'left')
    neww = new_df["customerId"].isna()
    return new_df.loc[neww, ["name"]].rename(columns={"name": "Customers"})