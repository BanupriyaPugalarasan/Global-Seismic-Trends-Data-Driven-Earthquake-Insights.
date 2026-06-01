# %% [markdown]
# pip install pymysql ---->run this in Terminal page

# %%
import pymysql
import pandas as pd

# %%
conn = pymysql.connect(
    host = "127.0.0.1",
    user = "root",
    password="Banu@2026sql"
  )

# %%
cursor = conn.cursor()

# %%
# CREATE DATABASE
cursor.execute("CREATE DATABASE EQ_dataset;")

# %%
#READ CSV FILE
df=pd.read_csv(r"c:\Users\HP\Downloads\Cleaned_earthquake_dataset.csv")

# %%
print(df.head())

# %%
print(df.shape)

# %%
cursor.execute("USE EQ_dataset")

# %%
#CREATE TABLE Earthquake_data
cursor.execute("""
CREATE TABLE Earthquake_data(
    id VARCHAR(100),
    time DATETIME(3),
    updated DATETIME(3),
    latitude FLOAT,
    longitude FLOAT,
    depth_km FLOAT,
    mag FLOAT,
    magType VARCHAR(50),
    place VARCHAR(225),
    status VARCHAR(50),
    tsunami INT,
    alert VARCHAR(10),
    Felt FLOAT,
    cdi FLOAT,
    mmi FLOAT,
    sig INT,
    net VARCHAR(100),
    code VARCHAR(100),
    ids VARCHAR(225),
    sources VARCHAR(225),
    types TEXT,
    nst FLOAT,
    dmin FLOAT,
    rms FLOAT,
    gap FLOAT,
    type VARCHAR(100),
    year INT(4),
    month INT(2),
    day INT(2),
    day_of_week VARCHAR(20),
    earthquake_flag VARCHAR(20),
    mag_flag VARCHAR(20)
)
               """)


# %%
#insert values into table
sql="""INSERT INTO earthquake_data(
    id,time,updated,latitude,longitude,depth_km,mag,magType,place,status,
    tsunami,alert,felt,cdi,mmi,sig,net,code,ids,sources,
    types,nst,dmin,rms,gap,type,year,month,day,day_of_week,
    earthquake_flag,mag_flag
    )
    VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    )
"""

# %%
for row in df.itertuples(index=False):
    cursor.execute(sql, tuple(row))

conn.commit()


# %%
cursor.execute("select * from earthquake_data;")
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)

# %% [markdown]
# Analyst Tasks

# %%
# Magnitude & Depth
#1.Top 10 strongest earthquakes(mag)
cursor.execute("""SELECT id,place,mag 
              FROM earthquake_data  
              ORDER BY mag DESC
              LIMIT 10;""")

data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)

# %%
#2.Top 10 deepest eqrthquakes(depth_km)
cursor.execute(""" SELECT place,mag,depth_km
              FROM earthquake_data
              ORDER BY depth_km DESC
              LIMIT 10; """ )
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)              

# %%
#3.Shallow earthquake <50 km and mag>7.5
cursor.execute(""" SELECT place, depth_km,mag,earthquake_flag 
              FROM earthquake_data
              WHERE depth_km<50 And mag>7.5""")
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)              

# %% [markdown]
# "4.Average depth per continent": 
#         "Answer Unavailable:'Continent column is not present in the dataset"

# %%
#5.Average magnitude per magnitude type(magType) 
cursor.execute("""SELECT magType,AVG(mag) AS AVERAGE_MAG
               FROM earthquake_data
               GROUP BY magType""")
              
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)

# %%
#TIME Analysis
#6.Year with most earthquakes.
cursor.execute("""SELECT year,count(*) AS total_earthquakes
               FROM earthquake_data
               GROUP BY year
               ORDER BY total_earthquakes DESC
               Limit 1;""" )
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)               

# %%
#7.Month with Highest number of earthquakes.
cursor.execute("""SELECT month, count(*) AS total_earthquakes
               FROM earthquake_data
               GROUP BY month
               ORDER BY total_earthquakes DESC
               LIMIT 1;""")

data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)               

# %%
#8.Day of week with most earthquakes
cursor.execute("""SELECT day_of_week, count(*) AS total_earthquakes
               FROM earthquake_data
               GROUP BY day_of_week
               ORDER BY total_earthquakes DESC
               LIMIT 1;""")
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)               

# %%
#9.Count of earthquakes per hour of day.
cursor.execute("""SELECT hour(time) AS hour_of_day, count(*) AS total_earthquakes
               FROM earthquake_data
               GROUP BY hour_of_day
               ORDER BY total_earthquakes DESC;""")
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)               

# %%
#10.Most active reporting network(net)
cursor.execute("""SELECT net, count(*) AS total_earthquakes
               FROM earthquake_data
               GROUP BY net
               ORDER BY total_earthquakes DESC
               LIMIT 1;""")
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)               

# %%
#Casualties & Economic Loss
#11.Top 5 places with highest Casualties. 
cursor.execute("""SELECT place, Max(felt) AS highest_casualties
               FROM earthquake_data
               GROUP BY place
               ORDER BY highest_casualties DESC
               LIMIT 5;""")
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)                              

# %% [markdown]
# 12.Total estimated economic loss per continent
#     Answer Unavailable:'Continent column is not present in the dataset.
# 

# %%
#13. Average economic loss by alert level
cursor.execute("""SELECT alert,Avg(mag) AS Average_eco_loss
               FROM earthquake_data
               GROUP BY alert;
               """)
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)                              

# %%
#Event Types & Quality Metrics
#14.Count of reviewed vs automatic earthquakes(status)
cursor.execute("""SELECT status,count(*) AS Total_Earthquakes
               FROM earthquake_data
               GROUP BY status;""")

data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)               

# %%
#15.Count by earthquake type(type)
cursor.execute("""SELECT type,count(*) AS Total_Earthquakes
               FROM earthquake_data
               GROUP BY type;""")
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)                              

# %%
#16.Number of earthquakes by data type(types).
cursor.execute("""SELECT types,count(*) AS Number_of_Earthquakes
               FROM earthquake_data
               GROUP BY types;""")
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)                              

# %% [markdown]
# 17. Average RMS and gap per continent.
#         Answer Unavailable:'Continent column is not present in the dataset

# %%
#18.Events with high station coverage(nst>thresold)
cursor.execute("""SELECT id,mag,mag_flag,nst
               FROM earthquake_data
               WHERE nst>mag
               ORDER BY nst DESC;""")
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)                              

# %%
#Tsunamis & Alerts
#19. Number of Tsunamis triggered per year
cursor.execute("""SELECT year,tsunami,count(*) AS Total_earthquakes
               FROM earthquake_data
               WHERE tsunami =1
               GROUP BY year
               ORDER BY Total_earthquakes DESC;""")
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)                   

# %%
#20.Count earthquakes by alert levels(red,Orange,etc)
cursor.execute("""SELECT alert,count(*) AS Total_earthquakes
               FROM earthquake_data
               GROUP BY alert
               ORDER BY Total_earthquakes DESC;""")
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)                   

# %%
#Seismic Pattern & Trends Analysis.
#21.Find the top 5 countries with the highest average magnitude of earthquakes in the past 5 years
cursor.execute("""SELECT place,AVG(mag) AS Avarage_magnitude
               FROM earthquake_data
               GROUP BY place
               ORDER BY Avarage_magnitude DESC
               LIMIT 5;""")
               
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)                                  
               

# %%
#22.Find countries that have experienced both shallow and deep earthquakes within the same month
cursor.execute("""SELECT place
               FROM earthquake_data
               GROUP BY place, month
               HAVING SUM(CASE WHEN earthquake_flag = "shallow" THEN 1 ELSE 0 END)>0 
               AND SUM(CASE WHEN earthquake_flag = "deep" THEN 1 ELSE 0 END)>0;
               """)
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)                                  

# %%
#23.Compute the year-over-year growth rate in the total number of earthquakes globally.
cursor.execute(""" SELECT
               year,
               total_earthquake,

               LAG(total_earthquake) OVER (ORDER BY year) AS prev_year_earthquake,
               ROUND(
               (
               (total_earthquake-LAG(total_earthquake) OVER (ORDER BY year))*100.0 /
               LAG(total_earthquake) OVER(ORDER BY year)
               ),
               2 ) AS yoy_growth_rate

               FROM (SELECT year,
               COUNT(*) AS total_earthquake
               FROM earthquake_data
               GROUP BY year) AS yearly;
               """
               )
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)                                  

# %%
#24.List the 3 most seismically active regions by combining both frequency and average magnitude.
cursor.execute("""SELECT place,
               COUNT(*) AS frequency,
               AVG(mag) AS Avg_magnitude
               FROM earthquake_data
               GROUP BY place
               ORDER BY frequency DESC ,Avg_magnitude DESC
               LIMIT 3;""")
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)                                  

# %%
#25.For each country, calculate the average depth of earthquakes within ±5° latitude range of the equator.
cursor.execute("""SELECT place, AVG(depth_km) AS Avg_depth_km
               FROM earthquake_data
               WHERE latitude  between -5 and +5
               GROUP BY place;
               """)
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)                   

# %%
#26.Identify countries having the highest ratio of shallow to deep earthquakes.
cursor.execute("""SELECT place,
               SUM(CASE WHEN earthquake_flag = "shallow" THEN 1 ELSE 0 END) AS shallow_count,
               SUM(CASE WHEN earthquake_flag = "deep"THEN 1 ELSE 0 END) AS deep_count,
               SUM(CASE WHEN earthquake_flag = "shallow" THEN 1 ELSE 0 END) *1.0 /
               NULLIF(SUM(CASE WHEN earthquake_flag = "deep"THEN 1 ELSE 0 END),0) AS ratio
               FROM earthquake_data
               GROUP BY place
               ORDER BY ratio DESC;""")               
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)                   

# %%
#27.Find the average magnitude difference between earthquakes with tsunami alerts and those without.
cursor.execute("""SELECT
               AVG(CASE WHEN tsunami = 1 THEN mag END) -
               AVG(CASE WHEN tsunami = 0 THEN mag END) AS avg_magnitude_difference
               FROM earthquake_data;""")
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)                                

# %%
#28.Using the gap and rms columns, identify events with the lowest data reliability (highest average error margins). 
cursor.execute("""SELECT id,
               place,
               gap,
               rms
               FROM earthquake_data
               ORDER BY gap DESC,rms DESC
               LIMIT 1 ;
               """)
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)                             
                       

# %% [markdown]
#  29. Find pairs of consecutive earthquakes (by time) that occurred within 50 km of each other and within 1 hour.
#         Answer Unavailable

# %%
#30.Determine the regions with the highest frequency of deep-focus earthquakes (depth > 300 km).
cursor.execute("""SELECT place,count(*) AS frequency
               FROM earthquake_data
               WHERE depth_km>300
               GROUP BY place
               ORDER BY frequency DESC
               LIMIT 1;""")
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
df=pd.DataFrame(data, columns=columns)
print(df)                             
               



