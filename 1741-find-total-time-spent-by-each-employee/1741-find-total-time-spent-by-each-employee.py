import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees["total_time"] = employees["out_time"] - employees["in_time"]
    grouped = employees.groupby(["event_day", "emp_id"], as_index=False)["total_time"].sum()
    return grouped.rename(columns={"event_day": "day"})[["day", "emp_id", "total_time"]]