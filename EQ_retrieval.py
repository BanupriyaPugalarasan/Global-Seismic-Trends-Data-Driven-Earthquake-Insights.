# %%
pip install pandas

# %%
import requests
import pandas as pd
from datetime import datetime

url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

all_records = []
start_year = 2021   # last 5 years
end_year = 2025

for year in range(start_year, end_year + 1):
    for month in range(1, 13):
        start_date = f"{year}-{month:02d}-01"
        if month == 12:
            end_date = f"{year+1}-01-01"
        else:
            end_date = f"{year}-{month+1:02d}-01"

        params = {
            "format": "geojson",
            "starttime": start_date,
            "endtime": end_date,
            "minmagnitude": 3
        }

        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"⚠️ Failed for {start_date}: {response.text[:200]}")
            continue

        try:
            data = response.json()
        except Exception as e:
            print(f"⚠️ JSON error for {start_date}: {e}")
            continue

        for f in data["features"]:
            p = f["properties"]
            g = f["geometry"]["coordinates"]
            all_records.append({
                "id": f.get("id"),
                "time": pd.to_datetime(p.get("time"), unit="ms"),
                "updated": pd.to_datetime(p.get("updated"), unit="ms"),
                "latitude": g[1] if g else None,
                "longitude": g[0] if g else None,
                "depth_km": g[2] if g else None,
                "mag": p.get("mag"),
                "magType" : p.get("magType"),
                "place": p.get("place"),
                "status" : p.get("status"),
                "tsunami": p.get("tsunami"),
                "alert": p.get("alert"),
                "felt": p.get("felt"),
                "cdi": p.get("cdi"),
                "mmi": p.get("mmi"),
                "sig": p.get("sig"),
                "net": p.get("net"),
                "code": p.get("code"),
                "ids": p.get("ids"),
                "sources": p.get("sources"),
                "types": p.get("types"),
                "nst": p.get("nst"),
                "dmin": p.get("dmin"),
                "rms": p.get("rms"),
                "gap": p.get("gap"),
                "type": p.get("type")


                })

df = pd.DataFrame(all_records)

# %%
df

# %%
df.info() # to get data type

# %%
df.shape # rows and columns counts

# %%
df.head() # first 5 rows

# %%
df["place"]

# %%
df["place"]=df["place"].str.extract(r"(?:,\s*)?([^,]+)$")[0]

# %%
df["place"].value_counts()

# %%
df["alert"].isnull().sum() #this col has null.

# %%
df["alert"].value_counts()

# %%
df["alert"]=df["alert"].fillna(df["alert"].mode()[0])#nan values fillna.mode()

# %%
df["alert"].value_counts()

# %%
df["magType"]

# %%
df["magType"].value_counts() #there is no null .

# %%
df["magType"]=df["magType"].str.lower() #changing all string are lowercase.

# %%
df["status"].value_counts() #there is no null and 2unique row (reviewed,automatic)

# %%
df["status"]=df["status"].str.lower() #changing all string are lowercase.

# %%
df["type"]=df["type"].str.lower() #changing all string are lowercase.

# %%
df["type"] # there is no null ,but type and magtype are same

# %%
df["net"]=df["net"].str.lower() #changing all string are lowercase.
df["sources"]=df["sources"].str.lower() #changing all string are lowercase.
df["types"]=df["types"].str.lower() #changing all string are lowercase.

# %%
df.info()

# %%
df["sources"].value_counts() #there is no null

# %%
df["sources"]=df["sources"].str.strip(',') # removing the , in the string

# %%
df["sources"]

# %%
df["types"] #there is no null

# %%
df["types"]=df["types"].str.strip(',')# removing the , in the string

# %%
df["types"].value_counts()

# %%
df["ids"]=df["ids"].str.strip(',')# removing the , in the string

# %%
df["ids"]

# %%
df.info()

# %%
df["mag"]

# %%
df["mag"].unique()

# %%
df["depth_km"].unique()

# %%
df

# %%
df["nst"]

# %%
df["nst"]=df["nst"].fillna(df["nst"].median())


# %%
df["nst"]

# %%
df["dmin"]

# %%
df["dmin"]=df["dmin"].fillna(df["dmin"].median())

# %%
df["dmin"]

# %%
df["rms"]

# %%
df["rms"]=df["rms"].fillna(df["rms"].mean())

# %%
df["rms"].value_counts()

# %%
df["gap"]=df["gap"].fillna(df["gap"].median())

# %%
df["gap"]

# %%
df["sig"]

# %%
df["alert"]=df["alert"].str.lower()

# %%
df["felt"]

# %%
df["felt"]=df["felt"].fillna(df["felt"].median())

# %%
df["felt"]

# %%
df["cdi"]

# %%
df["cdi"]=df["cdi"].fillna(df["cdi"].median())

# %%
df["cdi"]

# %%
df["mmi"]

# %%
df["mmi"]=df["mmi"].fillna(df["mmi"].median())

# %%
df["mmi"]

# %%
df.info()

# %%
df["year"]=df["time"].dt.year
df["month"]=df["time"].dt.month
df["day"]=df["time"].dt.day
df["day_of_week"]=df["time"].dt.day_name()

# %%
df

# %%
def earthquake_flag(depth_km):
  if depth_km <=300:
    return "shallow"
  else:
    return "deep"

# %%
df["earthquake_flag"]=df["depth_km"].apply(earthquake_flag)

# %%
df

# %%
def mag_thresholds(mag):
  if mag<=5:
    return "strong"
  else:
    return "destructive"

# %%
df["mag_flag"]=df["mag"].apply(mag_thresholds)

# %%
df

# %%
df.info()

# %%
df.to_csv("Cleaned_earthquake_dataset.csv", index = False)

# %%
import os
os.listdir()

# %%



